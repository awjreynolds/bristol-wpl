from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class NoPdfOutputsTest(unittest.TestCase):
    def test_pdfs_only_under_raw_evidence(self):
        offenders = [
            p.relative_to(ROOT).as_posix()
            for p in ROOT.rglob("*.pdf")
            if not p.relative_to(ROOT).as_posix().startswith("evidence/raw/")
        ]
        self.assertEqual(offenders, [])
