from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]


class StageGateReportsTest(unittest.TestCase):
    def test_stage_gate_report_validator_passes(self):
        result = subprocess.run(
            [sys.executable, "scripts/validate_stage_gate_reports.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Stage-gate report structure QA passed", result.stdout)
        self.assertIn("not command execution proof, evidence truth or WPL readiness", result.stdout)


if __name__ == "__main__":
    unittest.main()
