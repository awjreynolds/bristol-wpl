import csv
import subprocess
import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ObcAssuranceGateTest(unittest.TestCase):
    def test_stage7a_obc_assurance_validator_passes(self):
        result = subprocess.run(
            [sys.executable, "scripts/validate_obc_assurance.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("OBC assurance QA passed", result.stdout)
        self.assertIn("Stage 7 OBC gate remains blocked", result.stdout)

    def test_stage7_gate_checklist_covers_required_assurance_areas(self):
        with (ROOT / "business_case/obc/controls/stage-7-obc-gate-checklist.csv").open(
            newline="",
            encoding="utf-8",
        ) as handle:
            rows = list(csv.DictReader(handle))

        self.assertEqual(
            {
                "legal_governance",
                "strategic_case",
                "economic_appraisal",
                "spatial_parking",
                "financial_affordability",
                "commercial_operations",
                "management_delivery",
                "consultation_readiness",
                "equality_data_accessibility",
                "statutory_route",
                "red_team",
                "officer_editability",
            },
            {row["assurance_area"] for row in rows},
        )
        self.assertTrue(all(row["current_status"] == "blocked_control_only" for row in rows))

    def test_stage7_panel_register_requires_real_world_replacements(self):
        with (ROOT / "business_case/obc/controls/stage-7-assurance-panel-register.csv").open(
            newline="",
            encoding="utf-8",
        ) as handle:
            rows = list(csv.DictReader(handle))

        self.assertGreaterEqual(len(rows), 10)
        self.assertTrue(all(row["real_world_replacement"] for row in rows))
        self.assertIn("Monitoring Officer", " ".join(row["real_world_replacement"] for row in rows))

    def test_stage7_validator_reports_live_obc_gate_blockers(self):
        result = subprocess.run(
            [sys.executable, "scripts/validate_obc_assurance.py", "--gate"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("open P0", result.stderr)
        self.assertIn("Stage 7 OBC gate blocked", result.stderr)


if __name__ == "__main__":
    unittest.main()
