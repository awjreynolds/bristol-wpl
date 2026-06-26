import subprocess
import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class AuthoringGuardrailTest(unittest.TestCase):
    def test_authoring_guardrail_validator_passes(self):
        result = subprocess.run(
            [sys.executable, "scripts/validate_authoring_guardrails.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Authoring guardrails QA passed", result.stdout)

    def test_assembly_scripts_fail_closed(self):
        for script in ["scripts/assemble_obc.py", "scripts/assemble_fbc.py"]:
            result = subprocess.run(
                [sys.executable, script],
                cwd=ROOT,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Do not create", result.stdout + result.stderr)

    def test_no_case_insensitive_pdf_outputs_outside_raw(self):
        offenders = [
            path.relative_to(ROOT).as_posix()
            for path in ROOT.rglob("*")
            if path.is_file()
            and path.suffix.lower() == ".pdf"
            and not path.relative_to(ROOT).as_posix().startswith("evidence/raw/")
        ]
        self.assertEqual(offenders, [])


if __name__ == "__main__":
    unittest.main()
