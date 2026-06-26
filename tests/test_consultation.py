import csv
from pathlib import Path
import subprocess
import sys
import unittest

from scripts.validate_consultation import (
    REQUIRED_STAKEHOLDER_GROUPS,
    check_output_roots_empty,
    check_response_schema,
    collect_launch_blockers,
    line_has_positive_claim,
)

ROOT = Path(__file__).resolve().parents[1]


class ConsultationControlTest(unittest.TestCase):
    def test_stage8a_consultation_qa_passes(self):
        result = subprocess.run(
            [sys.executable, "scripts/validate_consultation.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("consultation launch remains blocked", result.stdout)

    def test_launch_gate_blocks_live_open_p0(self):
        result = subprocess.run(
            [sys.executable, "scripts/validate_consultation.py", "--launch-gate"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("open P0", result.stderr)
        self.assertTrue(any("open P0" in blocker for blocker in collect_launch_blockers()))

    def test_no_consultation_outputs_or_response_data_exist_beyond_control_files(self):
        self.assertEqual(check_output_roots_empty(), [])

    def test_processed_response_schema_excludes_direct_identifiers(self):
        self.assertEqual(check_response_schema(), [])

    def test_stage8a_forbids_authored_consultation_outputs(self):
        temp_output = ROOT / "consultation/materials/example.docx"
        try:
            temp_output.write_text("placeholder", encoding="utf-8")
            self.assertEqual(
                check_output_roots_empty(),
                ["Stage 8A forbids authored consultation output or response data while launch is blocked: consultation/materials/example.docx"],
            )
        finally:
            temp_output.unlink(missing_ok=True)

    def test_stakeholder_register_covers_required_groups(self):
        with (ROOT / "consultation/controls/stakeholder-coverage-register.csv").open(
            newline="",
            encoding="utf-8",
        ) as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(REQUIRED_STAKEHOLDER_GROUPS, {row["stakeholder_group"] for row in rows})
        self.assertTrue(all(row["coverage_status"] == "control_placeholder" for row in rows))

    def test_positive_consultation_readiness_variants_are_caught(self):
        samples = {
            "consultation is ready to launch": "consultation is ready to launch",
            "consultation has launched": "consultation has launched",
            "consultation launch-ready": "consultation launch readiness",
            "materials are complete": "materials are complete",
            "questionnaire is ready": "questionnaire is ready",
            "authority to consult is evidenced": "authority to consult",
        }
        for text, expected in samples.items():
            with self.subTest(text=text):
                self.assertEqual(line_has_positive_claim(text), expected)
