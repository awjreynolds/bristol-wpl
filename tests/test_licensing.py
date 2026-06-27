import subprocess
import sys
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class LicensingTest(unittest.TestCase):
    def test_licensing_validator_passes(self):
        result = subprocess.run(
            [sys.executable, "scripts/validate_licensing.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Licensing QA passed", result.stdout)


if __name__ == "__main__":
    unittest.main()
