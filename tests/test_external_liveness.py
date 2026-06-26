from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ExternalLivenessTest(unittest.TestCase):
    def test_external_liveness_validator_passes_offline(self):
        result = subprocess.run(
            [sys.executable, "scripts/validate_external_liveness.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("External-source liveness/currentness metadata QA passed", result.stdout)
        self.assertIn("Evidence truth, legal correctness", result.stdout)

    def test_live_checker_has_dry_run_mode(self):
        result = subprocess.run(
            [
                sys.executable,
                "scripts/check_external_source_liveness.py",
                "--limit",
                "0",
            ],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Dry run only", result.stdout)
        self.assertIn("HTTP reachability only", result.stdout)


if __name__ == "__main__":
    unittest.main()
