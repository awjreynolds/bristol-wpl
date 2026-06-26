from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]


class RegisterReferencesTest(unittest.TestCase):
    def test_register_references_validator_passes(self):
        result = subprocess.run(
            [sys.executable, "scripts/validate_register_references.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Register reference integrity QA passed", result.stdout)
        self.assertIn("not evidence truth or readiness", result.stdout)


if __name__ == "__main__":
    unittest.main()
