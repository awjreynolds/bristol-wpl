import subprocess
import sys
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class GovukStyleSkillTest(unittest.TestCase):
    def test_govuk_style_skill_validator_passes(self):
        result = subprocess.run(
            [sys.executable, "scripts/validate_govuk_style_skill.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("GOV.UK style skill QA passed", result.stdout)

    def test_repo_local_skill_is_present_and_bounded(self):
        skill = ROOT / "skills/govuk-style/SKILL.md"
        self.assertTrue(skill.exists())
        text = skill.read_text(encoding="utf-8")
        self.assertIn("name: govuk-style", text)
        self.assertIn("https://gist.github.com/fofr/505e225f9bf5e839d30c12ba6bfa0be2", text)
        self.assertIn("https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/", text)
        self.assertIn("Do not simplify away legal, statutory, financial, evidence or no-go meaning.", text)

    def test_stage34a_application_record_exists(self):
        record = ROOT / "analysis/content/stage-34a-govuk-style-application.md"
        self.assertTrue(record.exists())
        text = record.read_text(encoding="utf-8")
        self.assertIn("Stage 34A", text)
        self.assertIn("business_case/obc/simulation-release/bristol-wpl-outline-business-case-simulation-release.md", text)
        self.assertIn("docs/public/how-to-read-this-repo.md", text)
