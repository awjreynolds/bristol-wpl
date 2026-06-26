import csv
import subprocess
import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts import validate_fbc_statutory_gate


class FbcStatutoryGateControlTest(unittest.TestCase):
    def test_stage11a_validator_passes(self):
        result = subprocess.run(
            [sys.executable, "scripts/validate_fbc_statutory_gate.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("FBC/statutory gate QA passed", result.stdout)
        self.assertIn("Stage 11 FBC/statutory gate remains blocked", result.stdout)

    def test_stage11_checklist_covers_master_prompt_gate_conditions(self):
        with (ROOT / "business_case/fbc/controls/stage-11-fbc-statutory-gate-checklist.csv").open(
            newline="",
            encoding="utf-8",
        ) as handle:
            rows = list(csv.DictReader(handle))

        self.assertEqual(
            {
                "scheme_order_boundary_legal",
                "consultation_reconsultation",
                "statutory_confirmation",
                "finance_s151_affordability",
                "procurement_commercial",
                "data_cyber",
                "operations_enforcement",
                "charge_base_revenue_models",
                "investment_programme",
                "equality_mitigation",
                "dft_engagement",
                "weca_mca_dependencies",
                "residual_risk_decision_pack",
            },
            {row["assurance_area"] for row in rows},
        )
        self.assertTrue(all(row["current_status"] == "blocked_control_only" for row in rows))
        residual = next(row for row in rows if row["assurance_area"] == "residual_risk_decision_pack")
        self.assertIn("no P0 findings remain", residual["pass_condition"])

    def test_stage11_panel_register_requires_real_world_replacements(self):
        with (ROOT / "business_case/fbc/controls/stage-11-assurance-panel-register.csv").open(
            newline="",
            encoding="utf-8",
        ) as handle:
            rows = list(csv.DictReader(handle))

        self.assertGreaterEqual(len(rows), 10)
        replacements = " ".join(row["real_world_replacement"] for row in rows)
        self.assertIn("Section 151", replacements)
        self.assertIn("Monitoring Officer", replacements)
        self.assertTrue(all(row["current_status"] == "blocked_control_only" for row in rows))

    def test_stage11_panel_register_covers_every_named_reviewer(self):
        with (ROOT / "business_case/fbc/controls/stage-11-fbc-statutory-gate-checklist.csv").open(
            newline="",
            encoding="utf-8",
        ) as handle:
            checklist_rows = list(csv.DictReader(handle))
        with (ROOT / "business_case/fbc/controls/stage-11-assurance-panel-register.csv").open(
            newline="",
            encoding="utf-8",
        ) as handle:
            panel_rows = list(csv.DictReader(handle))

        reviewer_text = " ".join(row["review_role"] for row in panel_rows)
        for row in checklist_rows:
            for reviewer in row["required_reviewer"].split(" and "):
                self.assertIn(reviewer, reviewer_text)

    def test_stage11_no_go_claims_include_submission_and_implementation(self):
        with (ROOT / "business_case/fbc/controls/stage-11-no-go-claim-register.csv").open(
            newline="",
            encoding="utf-8",
        ) as handle:
            rows = list(csv.DictReader(handle))

        claims = {row["prohibited_claim"] for row in rows}
        self.assertIn("recommend submit and implement", claims)
        self.assertIn("FBC is ready for approval", claims)
        self.assertIn("scheme order and boundary have legal sign-off", claims)
        self.assertIn("Section 151 affordability review is complete", claims)
        self.assertIn("reconsultation assessment is complete", claims)
        self.assertIn("current statutory confirmation requirements are satisfied", claims)
        self.assertIn("data protection and cyber controls are ready", claims)
        self.assertIn("investment programme is deliverable", claims)
        self.assertIn("equality mitigations are funded and owned", claims)
        self.assertIn("no P0 findings remain", claims)
        self.assertTrue(all(row["current_status"] == "blocked_control_only" for row in rows))

    def test_gate_blocker_status_logic_catches_open_rows(self):
        self.assertTrue(validate_fbc_statutory_gate.is_active_blocker("open"))
        self.assertTrue(validate_fbc_statutory_gate.is_active_blocker("controlled_open"))
        self.assertTrue(validate_fbc_statutory_gate.is_active_blocker("working"))
        self.assertTrue(validate_fbc_statutory_gate.is_active_blocker("blocked_control_only"))
        self.assertFalse(validate_fbc_statutory_gate.is_active_blocker("closed"))

    def test_stage11_gate_fails_with_integrated_blockers(self):
        result = subprocess.run(
            [sys.executable, "scripts/validate_fbc_statutory_gate.py", "--gate"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Stage 11 FBC/statutory gate blocked", result.stderr)
        self.assertIn("open P0", result.stderr)
        self.assertIn("stage-11-fbc-statutory-gate-checklist.csv", result.stderr)
        self.assertIn("stage-11-no-go-claim-register.csv", result.stderr)


if __name__ == "__main__":
    unittest.main()
