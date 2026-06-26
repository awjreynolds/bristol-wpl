from pathlib import Path
import csv
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PublicCabinetComprehensionTest(unittest.TestCase):
    def test_public_cabinet_comprehension_validator_passes(self):
        result = subprocess.run(
            [sys.executable, "scripts/validate_public_cabinet_comprehension.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Public/cabinet comprehension QA passed", result.stdout)

    def test_stage_19a_crosswalk_has_residual_blockers(self):
        with (ROOT / "docs/officer/risk-control-crosswalk.csv").open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
        self.assertTrue(any(row["stage"] == "Stage 19A" for row in rows))
        for row in rows:
            self.assertTrue(row["residual_blocker"], row)
            self.assertIn("Block", row["gate_effect"], row)

    def test_visual_stage_map_avoids_complete_label(self):
        text = (ROOT / "docs/visuals/stage-gate-map.mmd").read_text(encoding="utf-8")
        self.assertNotIn("Complete", text)
        self.assertIn("Stage 19A", text)
        self.assertIn("Navigation only; no readiness gate closes", text)


if __name__ == "__main__":
    unittest.main()
