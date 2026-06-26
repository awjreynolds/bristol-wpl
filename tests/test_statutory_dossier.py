import csv
import subprocess
import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts import validate_statutory_dossier


class StatutoryDossierControlTest(unittest.TestCase):
    def test_statutory_dossier_validator_passes(self):
        result = subprocess.run(
            [sys.executable, "scripts/validate_statutory_dossier.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Statutory dossier QA passed", result.stdout)
        self.assertIn("Stage 10 statutory submission remains blocked", result.stdout)

    def test_component_register_covers_master_prompt_components(self):
        with (ROOT / "statutory_dossier/controls/dossier-component-register.csv").open(
            newline="",
            encoding="utf-8",
        ) as handle:
            rows = list(csv.DictReader(handle))

        self.assertEqual(23, len(rows))
        self.assertEqual({str(i).zfill(2) for i in range(1, 24)}, {row["component_number"] for row in rows})
        self.assertTrue(all(row["current_status"] == "blocked_control_only" for row in rows))

    def test_component_register_required_documents_resolve(self):
        with (ROOT / "statutory_dossier/controls/dossier-component-register.csv").open(
            newline="",
            encoding="utf-8",
        ) as handle:
            rows = list(csv.DictReader(handle))

        missing = [
            row["required_document"]
            for row in rows
            if row["required_document"] and not (ROOT / row["required_document"]).exists()
        ]
        self.assertEqual([], missing)

    def test_component_register_records_post_confirmation_certified_order_control(self):
        with (ROOT / "statutory_dossier/controls/dossier-component-register.csv").open(
            newline="",
            encoding="utf-8",
        ) as handle:
            rows = list(csv.DictReader(handle))

        component_22 = next(row for row in rows if row["component_number"] == "22")
        evidence = component_22["minimum_evidence"].lower()
        self.assertIn("post-confirmation certified order", evidence)

    def test_no_go_register_blocks_submission_overclaims(self):
        with (ROOT / "statutory_dossier/controls/submission-no-go-register.csv").open(
            newline="",
            encoding="utf-8",
        ) as handle:
            rows = list(csv.DictReader(handle))

        claims = {row["prohibited_claim"] for row in rows}
        self.assertIn("statutory submission is ready", claims)
        self.assertIn("scheme order is certified", claims)
        self.assertIn("DfT has accepted the dossier", claims)
        self.assertIn("FBC is ready for submission", claims)
        self.assertTrue(all(row["current_status"] == "blocked_control_only" for row in rows))

    def test_validator_requires_fbc_no_go_claim(self):
        self.assertIn("FBC is ready for submission", validate_statutory_dossier.REQUIRED_NO_GO_CLAIMS)

    def test_statutory_submission_blockers_include_stage_10a_controls(self):
        blockers = validate_statutory_dossier.collect_statutory_submission_blockers()
        joined = "\n".join(blockers)

        self.assertIn("dossier-readiness-gate.csv", joined)
        self.assertIn("submission-no-go-register.csv", joined)
        self.assertIn("EG-0034", joined)
        self.assertNotIn("OBC assembly", joined)

    def test_clause_matrix_is_control_only(self):
        with (ROOT / "statutory_dossier/draft_scheme_order/clause-by-clause-powers-matrix.csv").open(
            newline="",
            encoding="utf-8",
        ) as handle:
            rows = list(csv.DictReader(handle))

        self.assertGreaterEqual(len(rows), 8)
        self.assertTrue(all(row["current_status"] == "blocked_control_only" for row in rows))

    def test_submission_gate_fails_with_live_blockers(self):
        result = subprocess.run(
            [sys.executable, "scripts/validate_statutory_dossier.py", "--gate"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Stage 10 statutory submission blocked", result.stderr)
        self.assertIn("open P0", result.stderr)
        self.assertIn("dossier-readiness-gate.csv", result.stderr)
        self.assertIn("submission-no-go-register.csv", result.stderr)
        self.assertNotIn("OBC assembly", result.stderr)


if __name__ == "__main__":
    unittest.main()
