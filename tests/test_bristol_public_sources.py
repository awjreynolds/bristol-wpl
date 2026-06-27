from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]


class BristolPublicSourcesTest(unittest.TestCase):
    def test_bristol_public_source_validator_passes(self):
        result = subprocess.run(
            [sys.executable, "scripts/validate_bristol_public_sources.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Bristol public source coverage QA passed", result.stdout)
        self.assertIn("not source truth, currentness or WPL readiness", result.stdout)


if __name__ == "__main__":
    unittest.main()
