import csv
import subprocess
import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class HandoverControlTest(unittest.TestCase):
    def test_handover_validator_passes(self):
        result = subprocess.run(
            [sys.executable, "scripts/validate_handover.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Handover QA passed", result.stdout)
        self.assertIn("no WPL gate is closed", result.stdout)

    def test_critical_path_work_packages_cover_open_blocker_domains(self):
        with (ROOT / "handover/controls/critical-path-work-package-register.csv").open(
            newline="",
            encoding="utf-8",
        ) as handle:
            rows = list(csv.DictReader(handle))

        self.assertEqual(
            {
                "WP-LEGAL-ROUTE",
                "WP-WECA-MCA",
                "WP-DFT-PROCESS",
                "WP-BOUNDARY-INVENTORY",
                "WP-DISPLACEMENT",
                "WP-APPRAISAL-MODEL",
                "WP-CONSULTATION",
                "WP-FINANCE-S151",
                "WP-OPERATIONS-DATA",
                "WP-OBC-FBC-EVIDENCE",
                "WP-PUBLIC-GOVERNANCE",
            },
            {row["work_package_id"] for row in rows},
        )
        self.assertTrue(all(row["current_status"] == "blocked_work_package" for row in rows))

    def test_blocker_map_links_key_issues_to_work_packages(self):
        with (ROOT / "handover/controls/blocker-to-workstream-map.csv").open(
            newline="",
            encoding="utf-8",
        ) as handle:
            rows = list(csv.DictReader(handle))

        covered = {row["blocker_id"] for row in rows}
        for blocker_id in {
            "ISS-0001",
            "ISS-0002",
            "ISS-0003",
            "ISS-0004",
            "ISS-0008",
            "ISS-0011",
            "ISS-0012",
            "ISS-0015",
            "ISS-0016",
            "ISS-0017",
        }:
            self.assertIn(blocker_id, covered)
        self.assertTrue(all(row["gate_effect"] in {"P0_blocks", "P1_blocks", "control_only"} for row in rows))

    def test_blocker_map_is_exhaustive_against_work_package_linked_blockers(self):
        with (ROOT / "handover/controls/critical-path-work-package-register.csv").open(
            newline="",
            encoding="utf-8",
        ) as handle:
            work_packages = list(csv.DictReader(handle))
        with (ROOT / "handover/controls/blocker-to-workstream-map.csv").open(
            newline="",
            encoding="utf-8",
        ) as handle:
            blocker_map = list(csv.DictReader(handle))

        expected_pairs = {
            (blocker_id, row["work_package_id"])
            for row in work_packages
            for blocker_id in row["linked_blockers"].split(";")
            if blocker_id
        }
        actual_pairs = {(row["blocker_id"], row["work_package_id"]) for row in blocker_map}
        self.assertFalse(expected_pairs - actual_pairs)

    def test_work_package_reviews_are_marked_simulation_only(self):
        with (ROOT / "handover/controls/critical-path-work-package-register.csv").open(
            newline="",
            encoding="utf-8",
        ) as handle:
            rows = list(csv.DictReader(handle))

        self.assertTrue(all("simulation-only" in row["no_go_note"] for row in rows))
        self.assertTrue(all("real officer professional replacement" in row["no_go_note"] for row in rows))

    def test_next_90_day_plan_is_control_only(self):
        with (ROOT / "handover/controls/next-90-day-plan.csv").open(
            newline="",
            encoding="utf-8",
        ) as handle:
            rows = list(csv.DictReader(handle))

        self.assertEqual({"days_0_30", "days_31_60", "days_61_90"}, {row["phase_id"] for row in rows})
        self.assertTrue(all(row["current_status"] == "planning_control_only" for row in rows))
        self.assertTrue(all("does not authorise spend" in row["no_go_note"] for row in rows))

    def test_handover_no_go_claims_block_backlog_overclaims(self):
        with (ROOT / "handover/controls/handover-no-go-register.csv").open(
            newline="",
            encoding="utf-8",
        ) as handle:
            rows = list(csv.DictReader(handle))

        claims = {row["prohibited_claim"] for row in rows}
        self.assertIn("critical path is an approved programme", claims)
        self.assertIn("work packages close blockers", claims)
        self.assertIn("90 day plan authorises spend or procurement", claims)
        self.assertIn("handover replaces officer decisions", claims)
        self.assertIn("handover means gates can pass", claims)
        self.assertTrue(all(row["current_status"] == "blocked" for row in rows))

    def test_readme_points_to_next_steps_critical_path(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("Stage 13A", text)
        self.assertIn("docs/officer/next-steps-critical-path.md", text)
        self.assertIn("critical path is not approval", text)

    def test_public_and_gate_docs_surface_stage_13a_handover(self):
        public_text = (ROOT / "docs/public/README.md").read_text(encoding="utf-8")
        self.assertIn("docs/officer/next-steps-critical-path.md", public_text)
        self.assertIn("critical path is not approval", public_text)

        gate_text = (ROOT / "governance/stage-gate-plan.md").read_text(encoding="utf-8")
        self.assertIn("Stage 13A", gate_text)
        self.assertIn("handover-control", gate_text)


if __name__ == "__main__":
    unittest.main()
