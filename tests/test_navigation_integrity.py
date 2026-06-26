from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]


class NavigationIntegrityTest(unittest.TestCase):
    def test_navigation_integrity_validator_passes(self):
        result = subprocess.run(
            [sys.executable, "scripts/validate_navigation_integrity.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("repo-local QA passed", result.stdout)
        self.assertIn("external links and content truth not checked", result.stdout)

    def test_latest_stage_navigation_is_present(self):
        for rel in ["README.md", "docs/stages/README.md", "docs/visuals/stage-gate-map.mmd"]:
            self.assertIn("Stage 23A", (ROOT / rel).read_text(encoding="utf-8"))

    def test_recent_stage_reports_are_linked_from_readme(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        for report in [
            "review/stage_gate_reports/stage-18a-nottingham-displacement-transferability-report.md",
            "review/stage_gate_reports/stage-19a-public-cabinet-comprehension-report.md",
            "review/stage_gate_reports/stage-20a-visual-accessibility-qa-report.md",
            "review/stage_gate_reports/stage-21a-link-navigation-integrity-report.md",
            "review/stage_gate_reports/stage-22a-external-source-liveness-currentness-report.md",
            "review/stage_gate_reports/stage-23a-register-reference-integrity-report.md",
        ]:
            self.assertIn(report, readme)
            self.assertTrue((ROOT / report).exists())


if __name__ == "__main__":
    unittest.main()
