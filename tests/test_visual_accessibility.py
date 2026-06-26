from pathlib import Path
import csv
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]


class VisualAccessibilityTest(unittest.TestCase):
    def test_visual_accessibility_validator_passes(self):
        result = subprocess.run(
            [sys.executable, "scripts/validate_visual_accessibility.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("repo-level control QA passed", result.stdout)
        self.assertIn("no real user/accessibility assurance", result.stdout)

    def test_eg0047_remains_open(self):
        with (ROOT / "evidence/evidence_gap_register.csv").open(newline="", encoding="utf-8") as handle:
            rows = {row["gap_id"]: row for row in csv.DictReader(handle)}
        self.assertEqual(rows["EG-0047"]["status"], "open")

    def test_visuals_have_no_go_caption_and_legend(self):
        for rel in ["docs/visuals/stage-gate-map.mmd", "docs/visuals/risk-control-atlas.mmd"]:
            text = (ROOT / rel).read_text(encoding="utf-8")
            self.assertIn("Simulation control map only", text)
            self.assertIn("No WPL readiness gate closes", text)
            self.assertIn("Legend", text)
            self.assertNotIn("Complete", text)


if __name__ == "__main__":
    unittest.main()
