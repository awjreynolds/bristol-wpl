import csv
import subprocess
import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PublicReleaseGateTest(unittest.TestCase):
    def test_public_release_validator_passes(self):
        result = subprocess.run(
            [sys.executable, "scripts/validate_public_release.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Public release QA passed", result.stdout)
        self.assertIn("WPL approval gates remain blocked", result.stdout)

    def test_publication_checklist_covers_release_controls(self):
        with (ROOT / "publication/controls/repository-publication-checklist.csv").open(
            newline="",
            encoding="utf-8",
        ) as handle:
            rows = list(csv.DictReader(handle))

        self.assertEqual(
            {
                "repo_visibility",
                "simulation_notice",
                "no_authored_pdfs",
                "restricted_data_paths",
                "officer_editable_formats",
                "readme_entrypoints",
                "gate_blockers_visible",
                "subagent_context_hygiene",
            },
            {row["control_id"] for row in rows},
        )
        visibility = next(row for row in rows if row["control_id"] == "repo_visibility")
        self.assertEqual("public_verified", visibility["current_status"])
        self.assertIn("gh repo view awjreynolds/bristol-wpl", visibility["evidence"])

    def test_public_release_no_go_claims_block_readiness_overclaims(self):
        with (ROOT / "publication/controls/public-release-no-go-register.csv").open(
            newline="",
            encoding="utf-8",
        ) as handle:
            rows = list(csv.DictReader(handle))

        claims = {row["prohibited_claim"] for row in rows}
        self.assertIn("public repository means council approval", claims)
        self.assertIn("public repository means legal advice", claims)
        self.assertIn("public repository means OBC or FBC ready", claims)
        self.assertIn("public repository means consultation can launch", claims)
        self.assertIn("public repository means statutory submission is ready", claims)
        self.assertIn("public repository means official council publication", claims)
        self.assertIn("agent sign-offs replace officers lawyers or consultants", claims)
        self.assertTrue(all(row["current_status"] == "blocked" for row in rows))

    def test_public_release_scan_register_records_distribution_controls(self):
        with (ROOT / "publication/controls/public-release-scan-register.csv").open(
            newline="",
            encoding="utf-8",
        ) as handle:
            rows = list(csv.DictReader(handle))

        checks = {row["scan_id"]: row for row in rows}
        self.assertEqual("pass", checks["PUB-SCAN-001"]["current_status"])
        self.assertEqual("pass", checks["PUB-SCAN-002"]["current_status"])
        self.assertEqual("pass", checks["PUB-SCAN-003"]["current_status"])
        self.assertIn("no authored PDFs outside evidence/raw", checks["PUB-SCAN-001"]["finding"])
        self.assertIn("restricted paths empty", checks["PUB-SCAN-002"]["finding"])

    def test_readme_states_public_repo_is_not_wpl_readiness(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("This repository is public", text)
        self.assertIn("public visibility is not approval", text)
        self.assertIn("not an official council publication", text)
        self.assertIn("Stage 12A", text)


if __name__ == "__main__":
    unittest.main()
