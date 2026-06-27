import subprocess
import sys
import zipfile
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PACK_DIR = ROOT / "business_case" / "obc" / "docx-pack"


class ObcDocxPackTest(unittest.TestCase):
    def test_obc_docx_pack_validator_passes(self):
        result = subprocess.run(
            [sys.executable, "scripts/validate_obc_docx_pack.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("OBC DOCX pack QA passed", result.stdout)

    def test_zip_is_officer_facing_docx_pack(self):
        zip_path = PACK_DIR / "bristol-wpl-obc-document-pack.zip"
        self.assertTrue(zip_path.exists())
        with zipfile.ZipFile(zip_path) as archive:
            names = set(archive.namelist())
        self.assertEqual(
            names,
            {
                "bristol-wpl-obc-simulation-release.docx",
                "bristol-wpl-obc-reader-support-guide.docx",
                "bristol-wpl-obc-risk-process-control-summary.docx",
                "PACK-MANIFEST.txt",
            },
        )
        self.assertFalse(any(name.lower().endswith((".md", ".pdf")) for name in names))


if __name__ == "__main__":
    unittest.main()
