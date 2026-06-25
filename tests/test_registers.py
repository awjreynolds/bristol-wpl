import csv
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class RegisterTest(unittest.TestCase):
    def header(self, rel):
        with (ROOT / rel).open(newline="", encoding="utf-8") as handle:
            return next(csv.reader(handle))

    def test_simulation_signoff_register_exists(self):
        header = self.header("governance/simulation_signoff_register.csv")
        self.assertIn("agent_role", header)
        self.assertIn("decision", header)

    def test_source_register_seeded(self):
        with (ROOT / "evidence/source_register.csv").open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
        self.assertGreaterEqual(len(rows), 40)
