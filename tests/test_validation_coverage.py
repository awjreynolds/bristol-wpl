from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ValidationCoverageTest(unittest.TestCase):
    def test_validation_coverage_validator_passes(self):
        result = subprocess.run(
            [sys.executable, "scripts/validate_validation_coverage.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Validation coverage QA passed", result.stdout)
        self.assertIn("not command sufficiency or WPL readiness", result.stdout)


if __name__ == "__main__":
    unittest.main()

