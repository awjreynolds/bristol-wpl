from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]


class NottinghamLessonsTest(unittest.TestCase):
    def test_nottingham_transferability_validator_passes(self):
        result = subprocess.run(
            [sys.executable, "scripts/validate_nottingham_transferability.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Nottingham transferability QA passed", result.stdout)


if __name__ == "__main__":
    unittest.main()
