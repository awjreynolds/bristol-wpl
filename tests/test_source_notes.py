import csv
import subprocess
import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

CORE_SOURCE_IDS = {
    "SRC-BCC-0001",
    "SRC-BCC-0002",
    "SRC-BCC-0003",
    "SRC-BCC-0004",
    "SRC-BCC-0006",
    "SRC-BCC-0007",
    "SRC-BCC-0014",
    "SRC-DFT-0001",
    "SRC-HMT-0001",
    "SRC-LEG-0002",
    "SRC-WECA-0007",
    "SRC-NOTT-0001",
    "SRC-NOTT-0002",
}


class SourceNoteControlTest(unittest.TestCase):
    def test_source_note_validator_passes(self):
        result = subprocess.run(
            [sys.executable, "scripts/validate_source_notes.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Source notes QA passed", result.stdout)
        self.assertIn("source-note backlog remains controlled", result.stdout)

    def test_core_source_note_coverage_register_has_required_sources(self):
        with (ROOT / "evidence/source_notes/source-note-coverage-register.csv").open(
            newline="",
            encoding="utf-8",
        ) as handle:
            rows = list(csv.DictReader(handle))

        covered = {row["source_id"] for row in rows if row["note_status"] == "pilot_note_created"}
        self.assertTrue(CORE_SOURCE_IDS <= covered)
        self.assertTrue(all(row["note_path"].startswith("evidence/source_notes/core/") for row in rows))

    def test_core_source_notes_are_editable_and_bound_claims(self):
        for source_id in CORE_SOURCE_IDS:
            path = ROOT / "evidence/source_notes/core" / f"{source_id.lower()}.md"
            text = path.read_text(encoding="utf-8")
            self.assertIn(source_id, text)
            self.assertIn("Simulation-only source note", text)
            self.assertIn("What This Source Can Support", text)
            self.assertIn("What This Source Must Not Be Used To Claim", text)
            self.assertIn("Does not close ISS-0007", text)

    def test_source_note_no_go_claims_block_overclaims(self):
        with (ROOT / "evidence/source_notes/source-note-no-go-register.csv").open(
            newline="",
            encoding="utf-8",
        ) as handle:
            rows = list(csv.DictReader(handle))

        claims = {row["prohibited_claim"] for row in rows}
        self.assertIn("source note means claim is verified", claims)
        self.assertIn("source note means OBC or FBC evidence is complete", claims)
        self.assertIn("source note replaces legal advice", claims)
        self.assertIn("source note closes ISS-0007", claims)
        self.assertIn("source note means source is current", claims)
        self.assertTrue(all(row["current_status"] == "blocked" for row in rows))

    def test_coverage_register_rows_align_to_source_register_and_note_paths(self):
        with (ROOT / "evidence/source_register.csv").open(newline="", encoding="utf-8") as handle:
            source_register = {row["source_id"]: row for row in csv.DictReader(handle)}
        with (ROOT / "evidence/source_notes/source-note-coverage-register.csv").open(
            newline="",
            encoding="utf-8",
        ) as handle:
            rows = list(csv.DictReader(handle))

        for row in rows:
            source_id = row["source_id"]
            self.assertIn(source_id, source_register)
            self.assertTrue(row["note_path"].endswith(f"{source_id.lower()}.md"))
            note_text = (ROOT / row["note_path"]).read_text(encoding="utf-8")
            self.assertIn(source_register[source_id]["local_path"], note_text)
            self.assertEqual(row["source_title"], source_register[source_id]["title"])

    def test_readme_and_stage_index_surface_stage_14a_source_notes(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("Stage 14A", readme)
        self.assertIn("evidence/source_notes/README.md", readme)
        self.assertIn("source-note backlog remains controlled", readme)

        stage_index = (ROOT / "docs/stages/README.md").read_text(encoding="utf-8")
        self.assertIn("Stage 14A", stage_index)
        self.assertIn("source-note control", stage_index)


if __name__ == "__main__":
    unittest.main()
