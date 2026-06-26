#!/usr/bin/env python3
from __future__ import annotations

import csv
import sys
from pathlib import Path

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

REQUIRED_SOURCE_IDS = CORE_SOURCE_IDS | STAGE_15A_SOURCE_IDS | STAGE_15B_SOURCE_IDS

REQUIRED_FILES = [
    "analysis/evidence/stage-14a-source-note-control-package.md",
    "analysis/evidence/stage-15a-source-note-expansion-control-package.md",
    "analysis/evidence/stage-15b-source-note-completion-control-package.md",
    "evidence/source_notes/README.md",
    "evidence/source_notes/source-note-coverage-register.csv",
    "evidence/source_notes/source-note-no-go-register.csv",
    "docs/stages/stage-14a-source-notes.md",
    "docs/stages/stage-15a-source-note-expansion.md",
    "docs/stages/stage-15b-source-note-completion.md",
    "review/peer_review/stage-14a-source-note-review.md",
    "review/peer_review/stage-15a-source-note-expansion-review.md",
    "review/peer_review/stage-15b-source-note-completion-review.md",
    "review/stage_gate_reports/stage-14a-source-note-control-report.md",
    "review/stage_gate_reports/stage-15a-source-note-expansion-report.md",
    "review/stage_gate_reports/stage-15b-source-note-completion-report.md",
]

CSV_HEADERS = {
    "evidence/source_notes/source-note-coverage-register.csv": [
        "source_id",
        "coverage_stage",
        "workstream",
        "source_title",
        "note_path",
        "note_status",
        "claim_status",
        "review_required",
        "no_go_note",
    ],
    "evidence/source_notes/source-note-no-go-register.csv": [
        "claim_id",
        "prohibited_claim",
        "allowed_wording",
        "current_status",
        "gate_effect",
    ],
}

REQUIRED_NO_GO_CLAIMS = {
    "source note means claim is verified",
    "source note means OBC or FBC evidence is complete",
    "source note replaces legal advice",
    "source note closes ISS-0007",
    "source note means source is current",
}

REQUIRED_NOTE_PHRASES = [
    "Simulation-only source note",
    "What This Source Can Support",
    "What This Source Must Not Be Used To Claim",
    "Does not close ISS-0007",
]

WECA_CONTROL_SOURCE_IDS = {
    source_id
    for source_id in STAGE_15B_SOURCE_IDS
    if source_id.startswith("SRC-WECA-")
} | {
    "SRC-LEG-0009",
    "SRC-LEG-0010",
    "SRC-LEG-0014",
    "SRC-LEG-0015",
    "SRC-LEG-0016",
    "SRC-LEG-0022",
    "SRC-LEG-0023",
}

METHOD_GUIDANCE_SOURCE_IDS = {
    "SRC-HMT-0002",
    "SRC-HMT-0003",
    "SRC-HMT-0004",
    "SRC-DFT-0002",
    "SRC-DFT-0003",
    "SRC-DFT-0004",
}

DFT_SEARCH_CONTROL_SOURCE_IDS = {
    "SRC-DFT-0003",
    "SRC-DFT-0004",
}

COMPARATOR_TRANSFER_SOURCE_IDS = {
    "SRC-ACADEMIC-0002",
    "SRC-TFL-0001",
    "SRC-UK-0003",
}

SOURCE_SPECIFIC_NOTE_PHRASES = {
    **{
        source_id: [
            "Absence of WPL material in this source is not proof that no WECA record exists elsewhere",
        ]
        for source_id in WECA_CONTROL_SOURCE_IDS
    },
    **{
        source_id: [
            "Guidance/source-control note only",
            "no Green Book or TAG compliance",
            "no VFM conclusion",
        ]
        for source_id in METHOD_GUIDANCE_SOURCE_IDS
    },
    **{
        source_id: [
            "not proof that no guidance, approval route or DfT process exists",
        ]
        for source_id in DFT_SEARCH_CONTROL_SOURCE_IDS
    },
    **{
        source_id: [
            "without Bristol-specific transferability evidence",
            "mode-share, elasticity, congestion, revenue, charge level",
        ]
        for source_id in COMPARATOR_TRANSFER_SOURCE_IDS
    },
}

REQUIRED_NAV_PHRASES = {
    "README.md": [
        "Stage 14A",
        "Stage 15A",
        "Stage 15B",
        "evidence/source_notes/README.md",
        "source-note backlog remains controlled",
    ],
    "docs/stages/README.md": [
        "Stage 14A",
        "Stage 15A",
        "Stage 15B",
        "source-note control",
        "source-note expansion",
        "source-note completion",
    ],
    "evidence/source_notes/README.md": [
        "Simulation-only source notes",
        "Stage 15A",
        "Stage 15B",
        "source-note backlog remains controlled",
        "Does not close ISS-0007",
    ],
    "review/stage_gate_reports/stage-14a-source-note-control-report.md": [
        "Accepted for source-note control purposes only",
        "source-note backlog remains controlled",
    ],
    "review/stage_gate_reports/stage-15a-source-note-expansion-report.md": [
        "Accepted for expanded source-note control purposes only",
        "source-note backlog remains controlled",
    ],
    "review/stage_gate_reports/stage-15b-source-note-completion-report.md": [
        "Accepted for acquired-priority source-note completion purposes only",
        "claim-level source summaries remain open",
    ],
}


def expected_status(source_id: str) -> str | None:
    if source_id in CORE_SOURCE_IDS:
        return "pilot_note_created"
    if source_id in STAGE_15A_SOURCE_IDS:
        return "stage_15a_note_created"
    if source_id in STAGE_15B_SOURCE_IDS:
        return "stage_15b_note_created"
    return None


def expected_stage(source_id: str) -> str | None:
    if source_id in CORE_SOURCE_IDS:
        return "Stage 14A"
    if source_id in STAGE_15A_SOURCE_IDS:
        return "Stage 15A"
    if source_id in STAGE_15B_SOURCE_IDS:
        return "Stage 15B"
    return None


def expected_note_dir(source_id: str) -> str | None:
    if source_id in CORE_SOURCE_IDS:
        return "evidence/source_notes/core/"
    if source_id in STAGE_15A_SOURCE_IDS:
        return "evidence/source_notes/expanded/"
    if source_id in STAGE_15B_SOURCE_IDS:
        return "evidence/source_notes/stage15b/"
    return None


def read_rows(rel: str) -> list[dict[str, str]]:
    with (ROOT / rel).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def read_header(rel: str) -> list[str]:
    with (ROOT / rel).open(newline="", encoding="utf-8") as handle:
        return next(csv.reader(handle))


def check_csv_widths(rel: str) -> list[str]:
    errors = []
    with (ROOT / rel).open(newline="", encoding="utf-8") as handle:
        reader = csv.reader(handle)
        try:
            header = next(reader)
        except StopIteration:
            return [f"{rel} is empty"]
        expected = len(header)
        for line_number, row in enumerate(reader, start=2):
            if len(row) != expected:
                errors.append(f"{rel}:{line_number} has {len(row)} fields; expected {expected}")
    return errors


def source_register_ids() -> set[str]:
    return {row["source_id"] for row in read_rows("evidence/source_register.csv")}


def source_register_rows() -> dict[str, dict[str, str]]:
    return {row["source_id"]: row for row in read_rows("evidence/source_register.csv")}


def extraction_manifest_rows() -> dict[str, dict[str, str]]:
    return {row["source_id"]: row for row in read_rows("evidence/extraction_manifest.csv")}


def check_required_files() -> list[str]:
    return [f"missing source-note file: {rel}" for rel in REQUIRED_FILES if not (ROOT / rel).exists()]


def check_csv_headers() -> list[str]:
    errors = []
    for rel, columns in CSV_HEADERS.items():
        if not (ROOT / rel).exists():
            errors.append(f"missing source-note CSV: {rel}")
            continue
        header = read_header(rel)
        for column in columns:
            if column not in header:
                errors.append(f"{rel} missing column {column}")
        errors.extend(check_csv_widths(rel))
    return errors


def check_coverage_register() -> list[str]:
    rel = "evidence/source_notes/source-note-coverage-register.csv"
    if not (ROOT / rel).exists():
        return [f"missing source-note coverage register: {rel}"]
    errors = []
    rows = read_rows(rel)
    by_source = {row["source_id"]: row for row in rows}
    register_rows = source_register_rows()
    manifest_rows = extraction_manifest_rows()
    register_ids = set(register_rows)

    for source_id in sorted(REQUIRED_SOURCE_IDS - set(by_source)):
        errors.append(f"{rel} missing required source_id {source_id}")
    for source_id in sorted(REQUIRED_SOURCE_IDS - register_ids):
        errors.append(f"{rel} required source_id {source_id} is absent from source_register.csv")

    for row in rows:
        source_id = row.get("source_id", "")
        registered = register_rows.get(source_id)
        if not registered:
            errors.append(f"{rel} {source_id} is absent from source_register.csv")
            continue
        status = expected_status(source_id)
        stage = expected_stage(source_id)
        note_dir = expected_note_dir(source_id)
        if not status or not stage or not note_dir:
            errors.append(f"{rel} {source_id} is not in a controlled source-note cohort")
            continue
        if row.get("coverage_stage") != stage:
            errors.append(f"{rel} {source_id} must have coverage_stage {stage}")
        if row.get("note_status") != status:
            errors.append(f"{rel} {source_id} must be {status}")
        if row.get("claim_status") != "source_note_control_only":
            errors.append(f"{rel} {source_id} has unsafe claim_status {row.get('claim_status')}")
        if row.get("source_title") != registered.get("title"):
            errors.append(f"{rel} {source_id} title does not match source_register.csv")
        if "Does not close ISS-0007" not in row.get("no_go_note", ""):
            errors.append(f"{rel} {source_id} missing ISS-0007 no-go note")
        note_path = row.get("note_path", "")
        if not note_path.startswith(note_dir):
            errors.append(f"{rel} {source_id} note_path must stay under {note_dir}")
        elif not note_path.endswith(f"{source_id.lower()}.md"):
            errors.append(f"{rel} {source_id} note_path must end with {source_id.lower()}.md")
        elif not (ROOT / note_path).exists():
            errors.append(f"{rel} {source_id} note does not exist: {note_path}")
        else:
            note_text = (ROOT / note_path).read_text(encoding="utf-8")
            if registered.get("local_path") not in note_text:
                errors.append(f"{note_path} missing registered local_path {registered.get('local_path')}")
            if registered.get("status") == "downloaded_raw_omitted_from_public_repo":
                required = "raw PDF is deliberately omitted from the public repository"
                if required not in note_text:
                    errors.append(f"{note_path} missing raw-omitted public repo control wording")
        if source_id in STAGE_15A_SOURCE_IDS | STAGE_15B_SOURCE_IDS:
            manifest = manifest_rows.get(source_id)
            if not manifest:
                errors.append(f"evidence/extraction_manifest.csv missing {source_id}")
            elif not manifest.get("status", "").startswith("extracted"):
                errors.append(f"evidence/extraction_manifest.csv {source_id} is not extracted")
            elif manifest.get("quality") != "usable":
                errors.append(f"evidence/extraction_manifest.csv {source_id} is not usable")
    return errors


def check_source_notes() -> list[str]:
    errors = []
    for source_id in sorted(REQUIRED_SOURCE_IDS):
        note_dir = expected_note_dir(source_id)
        assert note_dir is not None
        path = ROOT / note_dir / f"{source_id.lower()}.md"
        if not path.exists():
            errors.append(f"missing source note: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        for phrase in REQUIRED_NOTE_PHRASES:
            if phrase not in text:
                errors.append(f"{path.relative_to(ROOT)} missing required phrase: {phrase}")
        for phrase in SOURCE_SPECIFIC_NOTE_PHRASES.get(source_id, []):
            if phrase not in text:
                errors.append(f"{path.relative_to(ROOT)} missing source-specific phrase: {phrase}")
        if source_id not in text:
            errors.append(f"{path.relative_to(ROOT)} missing source id {source_id}")
    return errors


def check_no_go_register() -> list[str]:
    rel = "evidence/source_notes/source-note-no-go-register.csv"
    if not (ROOT / rel).exists():
        return [f"missing source-note no-go register: {rel}"]
    errors = []
    rows = read_rows(rel)
    claims = {row["prohibited_claim"] for row in rows}
    for claim in sorted(REQUIRED_NO_GO_CLAIMS - claims):
        errors.append(f"{rel} missing prohibited claim: {claim}")
    for row in rows:
        claim_id = row.get("claim_id", "<unknown>")
        if row.get("current_status") != "blocked":
            errors.append(f"{rel} {claim_id} must remain blocked")
        if claim_id == "SN-NG-004" and "Stage 15B closes only acquired-priority" not in row.get(
            "allowed_wording",
            "",
        ):
            errors.append(f"{rel} SN-NG-004 must qualify the Stage 15B ISS-0007 closure")
    return errors


def check_required_phrases() -> list[str]:
    errors = []
    for rel, phrases in REQUIRED_NAV_PHRASES.items():
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing phrase-check file: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in text:
                errors.append(f"{rel} missing required phrase: {phrase}")
    return errors


def check_downloaded_priority_sources_are_noted() -> list[str]:
    errors = []
    coverage = {row["source_id"] for row in read_rows("evidence/source_notes/source-note-coverage-register.csv")}
    for row in source_register_rows().values():
        if row.get("priority") == "1_must" and row.get("status", "").startswith("downloaded"):
            if row["source_id"] not in coverage:
                errors.append(f"missing source note coverage for downloaded priority source {row['source_id']}")
    return errors


def check_backlog_status_controlled() -> list[str]:
    errors = []
    issue_rows = {row["issue_id"]: row for row in read_rows("governance/issues_register.csv")}
    gap_rows = {row["gap_id"]: row for row in read_rows("evidence/evidence_gap_register.csv")}
    if issue_rows.get("ISS-0007", {}).get("status") != "closed_stage_15b":
        errors.append("ISS-0007 must be closed_stage_15b after acquired-priority source notes are complete")
    if gap_rows.get("EG-0024", {}).get("status") != "partially_closed_stage_15b":
        errors.append("EG-0024 must remain partially_closed_stage_15b because claim-level summaries remain open")
    if gap_rows.get("EG-0038", {}).get("status") != "closed_stage_15b":
        errors.append("EG-0038 must be closed_stage_15b after Stage 15B source-note completion")
    if gap_rows.get("EG-0043", {}).get("status") != "closed_stage_15b":
        errors.append("EG-0043 must be closed_stage_15b after Stage 15B source-note completion")
    if gap_rows.get("EG-0044", {}).get("status") != "open":
        errors.append("EG-0044 must remain open for claim-level source summaries")
    return errors


def collect_errors() -> list[str]:
    errors = []
    errors.extend(check_required_files())
    errors.extend(check_csv_headers())
    errors.extend(check_coverage_register())
    errors.extend(check_source_notes())
    errors.extend(check_no_go_register())
    errors.extend(check_required_phrases())
    errors.extend(check_downloaded_priority_sources_are_noted())
    errors.extend(check_backlog_status_controlled())
    return errors


def main() -> int:
    errors = collect_errors()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Source notes QA passed; source-note backlog remains controlled")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
