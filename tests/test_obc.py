import subprocess
import sys
from pathlib import Path
import unittest
import csv

from scripts.validate_obc import (
    OBC_SECTION_FILES,
    check_positive_claims,
    check_obc_output_roots_empty,
    collect_readiness_blockers,
    issue_readiness_error,
    line_has_positive_claim,
)

ROOT = Path(__file__).resolve().parents[1]


class ObcControlTest(unittest.TestCase):
    def test_stage6a_obc_qa_passes(self):
        result = subprocess.run(
            [sys.executable, "scripts/validate_obc.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("OBC assembly remains blocked", result.stdout)

    def test_assemble_obc_blocks_output(self):
        result = subprocess.run(
            [sys.executable, "scripts/assemble_obc.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Stage 6A assembly blocked", result.stdout)
        self.assertIn("open P0", result.stdout)

    def test_no_assembled_obc_outputs_exist(self):
        self.assertEqual(check_obc_output_roots_empty(), [])

    def test_claim_dependency_register_covers_main_sections(self):
        with (ROOT / "business_case/obc/controls/section-claim-dependency-register.csv").open(
            newline="",
            encoding="utf-8",
        ) as handle:
            rows = list(csv.DictReader(handle))

        self.assertEqual(
            {
                "executive_summary",
                "strategic_case",
                "economic_case",
                "commercial_case",
                "financial_case",
                "management_case",
                "conclusions_and_decisions",
            },
            {row["section"] for row in rows},
        )
        self.assertTrue(all(row["dependency_status"] == "blocked_control_only" for row in rows))

    def test_readiness_gate_blocks_live_open_p0(self):
        blockers = collect_readiness_blockers()
        self.assertTrue(any("open P0" in blocker for blocker in blockers))

    def test_p1_without_accepted_condition_blocks(self):
        error = issue_readiness_error(
            {
                "issue_id": "ISS-TEST",
                "severity": "P1",
                "status": "controlled_open",
                "owner": "Owner",
                "due_date": "",
                "notes": "No residual risk decision.",
            }
        )
        self.assertEqual(
            error,
            "ISS-TEST is controlled_open; P1 issue lacks Simulation Gate Authority condition with owner deadline and residual risk",
        )

    def test_stage6a_forbids_authored_obc_outputs_even_if_suffix_is_future_allowed(self):
        temp_output = ROOT / "business_case/obc/assembled/example.md"
        try:
            temp_output.write_text("# Example\n", encoding="utf-8")
            self.assertEqual(
                check_obc_output_roots_empty(),
                ["Stage 6A forbids authored OBC output while assembly is blocked: business_case/obc/assembled/example.md"],
            )
        finally:
            temp_output.unlink(missing_ok=True)

    def test_section_matrix_covers_each_obc_section_path(self):
        with (ROOT / "business_case/obc/controls/section-dependency-matrix.csv").open(
            newline="",
            encoding="utf-8",
        ) as handle:
            rows = list(csv.DictReader(handle))

        self.assertEqual(set(OBC_SECTION_FILES), {row["section_path"] for row in rows})

    def test_banned_claim_lists_are_not_scanned_as_positive_claims(self):
        errors = check_positive_claims()
        self.assertEqual(errors, [])

    def test_positive_readiness_variants_are_caught(self):
        samples = {
            "An assembled OBC has been created": "assembled OBC output",
            "The officer-review DOCX has been created": "officer-review DOCX output",
            "BCR is decision-grade": "BCR decision-grade claim",
            "VFM is decision grade": "VFM decision-grade claim",
            "benefits are decision grade": "benefits decision-grade claim",
            "boundary is decision grade": "boundary decision-grade claim",
            "charge-base is decision-grade": "charge-base decision-grade claim",
            "revenue is decision grade": "revenue decision-grade claim",
        }
        for text, expected in samples.items():
            with self.subTest(text=text):
                self.assertEqual(line_has_positive_claim(text), expected)
