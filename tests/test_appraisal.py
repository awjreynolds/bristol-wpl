import subprocess
import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class AppraisalControlTest(unittest.TestCase):
    def test_stage5a_appraisal_qa_passes(self):
        result = subprocess.run(
            [sys.executable, "scripts/validate_appraisal.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Stage 5 gate remains blocked", result.stdout)

    def test_model_run_manifest_template_is_not_output(self):
        text = (ROOT / "models/outputs/model-run-manifest-template.json").read_text(encoding="utf-8")
        self.assertIn('"status": "template_only"', text)
