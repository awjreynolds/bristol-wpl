from pathlib import Path
import csv
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import scripts.validate_nottingham_transferability as validator


class NottinghamLessonsTest(unittest.TestCase):
    def test_nottingham_transferability_validator_passes(self):
        result = subprocess.run(
            [sys.executable, "scripts/validate_nottingham_transferability.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Nottingham transferability QA passed", result.stdout)

    def test_stage_18a_required_rows_are_present(self):
        with (ROOT / "analysis/economic/nottingham_lessons_register.csv").open(newline="", encoding="utf-8") as handle:
            lesson_rows = list(csv.DictReader(handle))
        lesson_ids = {row["lesson_id"] for row in lesson_rows}
        self.assertTrue(set(validator.REQUIRED_LESSONS).issubset(lesson_ids))

        with (ROOT / "analysis/economic/nottingham-transferability-matrix.csv").open(newline="", encoding="utf-8") as handle:
            matrix_rows = list(csv.DictReader(handle))
        matrix_topics = {row["nottingham_assumption_or_evidence"] for row in matrix_rows}
        self.assertTrue(validator.REQUIRED_TRANSFERABILITY_TOPICS.issubset(matrix_topics))

    def test_validator_fails_when_stage_18a_lesson_rows_are_removed(self):
        with tempfile.TemporaryDirectory() as directory:
            temp_root = Path(directory)
            self._copy_validation_fixture(temp_root)
            register = temp_root / validator.REGISTER
            with register.open(newline="", encoding="utf-8") as handle:
                reader = csv.DictReader(handle)
                rows = [row for row in reader if row["lesson_id"] != "NLR-0007"]
                fieldnames = reader.fieldnames
            with register.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)

            with patch.object(validator, "ROOT", temp_root):
                errors = validator.collect_errors()
            self.assertTrue(any("NLR-0007" in error for error in errors), errors)

    def test_validator_fails_when_cross_register_blocker_is_softened(self):
        with tempfile.TemporaryDirectory() as directory:
            temp_root = Path(directory)
            self._copy_validation_fixture(temp_root)
            risk_register = temp_root / "governance/risk_register.csv"
            with risk_register.open(newline="", encoding="utf-8") as handle:
                reader = csv.DictReader(handle)
                rows = list(reader)
                fieldnames = reader.fieldnames
            for row in rows:
                if row["risk_id"] == "RISK-0009":
                    row["status"] = "controlled_open"
            with risk_register.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)

            with patch.object(validator, "ROOT", temp_root):
                errors = validator.collect_errors()
            self.assertTrue(any("RISK-0009" in error for error in errors), errors)

    def _copy_validation_fixture(self, temp_root: Path):
        files = [
            validator.REGISTER,
            validator.TRANSFERABILITY_MATRIX,
            validator.DISPLACEMENT_CHECKLIST,
            "docs/officer/nottingham-and-comparator-lessons.md",
            "docs/officer/assurance-dashboard.md",
            "docs/public/README.md",
            "README.md",
            "governance/issues_register.csv",
            "governance/risk_register.csv",
            "governance/pitfalls_register.csv",
            "evidence/evidence_gap_register.csv",
        ]
        for rel in files:
            destination = temp_root / rel
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / rel, destination)


if __name__ == "__main__":
    unittest.main()
