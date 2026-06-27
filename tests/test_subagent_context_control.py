from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]


class SubagentContextControlTest(unittest.TestCase):
    def test_subagent_context_control_validator_passes(self):
        result = subprocess.run(
            [sys.executable, "scripts/validate_subagent_context_control.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Subagent/context-control QA passed", result.stdout)
        self.assertIn("does not prove future agents obey instructions", result.stdout)


if __name__ == "__main__":
    unittest.main()
