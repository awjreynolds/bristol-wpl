from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]


class OfficerPackTest(unittest.TestCase):
    def run_command(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, *args],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_officer_pack_validator_passes(self):
        result = self.run_command("scripts/validate_officer_pack.py")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Officer pack QA passed", result.stdout)

    def test_obc_gate_fails_with_open_p0(self):
        result = self.run_command("scripts/stage_gate_check.py", "--gate", "obc")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("open P0", result.stderr)

    def test_fbc_gate_fails_with_open_p0(self):
        result = self.run_command("scripts/stage_gate_check.py", "--gate", "fbc")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("open P0", result.stderr)

    def test_red_team_target_remains_bounded_review_not_gate_pass(self):
        result = self.run_command("scripts/stage_gate_check.py", "--red-team")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("bounded red-team packet", result.stdout)


if __name__ == "__main__":
    unittest.main()
