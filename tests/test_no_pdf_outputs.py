from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class NoPdfOutputsTest(unittest.TestCase):
    def test_pdfs_only_under_raw_evidence(self):
        offenders = []
        for path in ROOT.rglob("*"):
            if not path.is_file():
                continue
            rel = path.relative_to(ROOT).as_posix()
            if rel.startswith("evidence/raw/"):
                continue
            has_pdf_extension = path.suffix.lower() == ".pdf"
            has_pdf_magic = path.read_bytes()[:4] == b"%PDF"
            if has_pdf_extension or has_pdf_magic:
                offenders.append(rel)
        self.assertEqual(offenders, [])
