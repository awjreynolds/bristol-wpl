import csv
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class SourceSeedTest(unittest.TestCase):
    def test_input_seed_has_required_columns(self):
        path = ROOT / "inputs/bristol_wpl_codex_sources.csv"
        with path.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            self.assertIn("doc_id", reader.fieldnames)
            self.assertIn("url", reader.fieldnames)
            rows = list(reader)
        self.assertEqual(sum(1 for row in rows if not row["url"]), 0)
