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

STAGE_15A_SOURCE_IDS = {
    "SRC-BCC-0005",
    "SRC-BCC-0008",
    "SRC-BCC-0009",
    "SRC-BCC-0010",
    "SRC-BCC-0011",
    "SRC-BCC-0015",
    "SRC-BCC-0016",
    "SRC-BCC-0017",
    "SRC-BCC-0022",
    "SRC-BCC-0023",
    "SRC-BCC-0024",
    "SRC-BCC-0025",
    "SRC-BCC-0026",
    "SRC-BCC-0027",
    "SRC-BCC-0028",
    "SRC-BCC-0029",
    "SRC-BCC-0030",
    "SRC-BCC-0031",
    "SRC-BCC-0032",
    "SRC-BCC-0033",
    "SRC-BCC-0034",
    "SRC-BCC-0035",
    "SRC-BCC-0036",
    "SRC-LEG-0001",
    "SRC-LEG-0003",
    "SRC-LEG-0004",
    "SRC-LEG-0005",
    "SRC-LEG-0006",
    "SRC-LEG-0007",
    "SRC-LEG-0008",
    "SRC-LEG-0011",
    "SRC-LEG-0012",
    "SRC-LEG-0013",
    "SRC-LEG-0017",
    "SRC-LEG-0018",
    "SRC-LEG-0019",
    "SRC-LEG-0020",
    "SRC-LEG-0021",
    "SRC-LEG-0024",
    "SRC-LEG-0025",
    "SRC-LEG-0026",
    "SRC-LEG-0027",
}

STAGE_15B_SOURCE_IDS = {
    "SRC-WECA-0001",
    "SRC-WECA-0003",
    "SRC-WECA-0004",
    "SRC-WECA-0006",
    "SRC-ACADEMIC-0002",
    "SRC-TFL-0001",
    "SRC-UK-0003",
    "SRC-LEG-0009",
    "SRC-LEG-0010",
    "SRC-HMT-0002",
    "SRC-HMT-0003",
    "SRC-HMT-0004",
    "SRC-DFT-0002",
    "SRC-WECA-0011",
    "SRC-WECA-0012",
    "SRC-WECA-0013",
    "SRC-LEG-0014",
    "SRC-LEG-0015",
    "SRC-LEG-0016",
    "SRC-LEG-0022",
    "SRC-LEG-0023",
    "SRC-WECA-0017",
    "SRC-WECA-0018",
    "SRC-WECA-0019",
    "SRC-WECA-0020",
    "SRC-WECA-0021",
    "SRC-WECA-0022",
    "SRC-WECA-0023",
    "SRC-WECA-0024",
    "SRC-WECA-0025",
    "SRC-WECA-0026",
    "SRC-WECA-0027",
    "SRC-WECA-0028",
    "SRC-WECA-0029",
    "SRC-DFT-0003",
    "SRC-DFT-0004",
}

STAGE_32A_SOURCE_IDS = {
    "SRC-WECA-0008",
    "SRC-WECA-0009",
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
        expanded_15a = {
            row["source_id"] for row in rows if row["note_status"] == "stage_15a_note_created"
        }
        expanded_15b = {
            row["source_id"] for row in rows if row["note_status"] == "stage_15b_note_created"
        }
        expanded_32a = {
            row["source_id"] for row in rows if row["note_status"] == "stage_32a_note_created"
        }
        self.assertTrue(STAGE_15A_SOURCE_IDS <= expanded_15a)
        self.assertTrue(STAGE_15B_SOURCE_IDS <= expanded_15b)
        self.assertTrue(STAGE_32A_SOURCE_IDS <= expanded_32a)
        for row in rows:
            if row["source_id"] in CORE_SOURCE_IDS:
                self.assertEqual(row["coverage_stage"], "Stage 14A")
                self.assertTrue(row["note_path"].startswith("evidence/source_notes/core/"))
            if row["source_id"] in STAGE_15A_SOURCE_IDS:
                self.assertEqual(row["coverage_stage"], "Stage 15A")
                self.assertTrue(row["note_path"].startswith("evidence/source_notes/expanded/"))
            if row["source_id"] in STAGE_15B_SOURCE_IDS:
                self.assertEqual(row["coverage_stage"], "Stage 15B")
                self.assertTrue(row["note_path"].startswith("evidence/source_notes/stage15b/"))
            if row["source_id"] in STAGE_32A_SOURCE_IDS:
                self.assertEqual(row["coverage_stage"], "Stage 32A")
                self.assertTrue(row["note_path"].startswith("evidence/source_notes/stage32a/"))

    def test_core_source_notes_are_editable_and_bound_claims(self):
        note_paths = [
            ROOT / "evidence/source_notes/core" / f"{source_id.lower()}.md"
            for source_id in CORE_SOURCE_IDS
        ]
        note_paths.extend(
            ROOT / "evidence/source_notes/expanded" / f"{source_id.lower()}.md"
            for source_id in STAGE_15A_SOURCE_IDS
        )
        note_paths.extend(
            ROOT / "evidence/source_notes/stage15b" / f"{source_id.lower()}.md"
            for source_id in STAGE_15B_SOURCE_IDS
        )
        note_paths.extend(
            ROOT / "evidence/source_notes/stage32a" / f"{source_id.lower()}.md"
            for source_id in STAGE_32A_SOURCE_IDS
        )
        for path in note_paths:
            text = path.read_text(encoding="utf-8")
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

    def test_source_note_completion_tracks_claim_summary_handoff(self):
        with (ROOT / "governance/issues_register.csv").open(newline="", encoding="utf-8") as handle:
            issues = {row["issue_id"]: row for row in csv.DictReader(handle)}
        with (ROOT / "evidence/evidence_gap_register.csv").open(
            newline="",
            encoding="utf-8",
        ) as handle:
            gaps = {row["gap_id"]: row for row in csv.DictReader(handle)}

        self.assertEqual(issues["ISS-0007"]["status"], "closed_stage_15b")
        self.assertEqual(gaps["EG-0024"]["status"], "partially_closed_stage_15b")
        self.assertEqual(gaps["EG-0038"]["status"], "closed_stage_15b")
        self.assertEqual(gaps["EG-0043"]["status"], "closed_stage_15b")
        self.assertEqual(gaps["EG-0044"]["status"], "partially_closed_stage_16a")
        self.assertEqual(gaps["EG-0045"]["status"], "open")

    def test_stage_15a_and_15b_sources_have_usable_extracted_text(self):
        with (ROOT / "evidence/extraction_manifest.csv").open(
            newline="",
            encoding="utf-8",
        ) as handle:
            manifest = {row["source_id"]: row for row in csv.DictReader(handle)}

        for source_id in STAGE_15A_SOURCE_IDS | STAGE_15B_SOURCE_IDS | STAGE_32A_SOURCE_IDS:
            self.assertIn(source_id, manifest)
            self.assertTrue(manifest[source_id]["status"].startswith("extracted"))
            self.assertEqual(manifest[source_id]["quality"], "usable")

    def test_downloaded_priority_sources_have_source_notes(self):
        with (ROOT / "evidence/source_notes/source-note-coverage-register.csv").open(
            newline="",
            encoding="utf-8",
        ) as handle:
            covered = {row["source_id"] for row in csv.DictReader(handle)}
        with (ROOT / "evidence/source_register.csv").open(newline="", encoding="utf-8") as handle:
            missing = [
                row["source_id"]
                for row in csv.DictReader(handle)
                if row["priority"] == "1_must"
                and row["status"].startswith("downloaded")
                and row["source_id"] not in covered
            ]
        self.assertEqual(missing, [])

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
        self.assertIn("Stage 15A", readme)
        self.assertIn("Stage 15B", readme)
        self.assertIn("evidence/source_notes/README.md", readme)
        self.assertIn("source-note backlog remains controlled", readme)

        stage_index = (ROOT / "docs/stages/README.md").read_text(encoding="utf-8")
        self.assertIn("Stage 14A", stage_index)
        self.assertIn("Stage 15A", stage_index)
        self.assertIn("Stage 15B", stage_index)
        self.assertIn("source-note control", stage_index)
        self.assertIn("source-note expansion", stage_index)
        self.assertIn("source-note completion", stage_index)


if __name__ == "__main__":
    unittest.main()
