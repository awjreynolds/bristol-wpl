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

REQUIRED_FILES = [
    "analysis/evidence/stage-14a-source-note-control-package.md",
    "evidence/source_notes/README.md",
    "evidence/source_notes/source-note-coverage-register.csv",
    "evidence/source_notes/source-note-no-go-register.csv",
    "docs/stages/stage-14a-source-notes.md",
    "review/peer_review/stage-14a-source-note-review.md",
    "review/stage_gate_reports/stage-14a-source-note-control-report.md",
]

CSV_HEADERS = {
    "evidence/source_notes/source-note-coverage-register.csv": [
        "source_id",
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

REQUIRED_NAV_PHRASES = {
    "README.md": [
        "Stage 14A",
        "evidence/source_notes/README.md",
        "source-note backlog remains controlled",
    ],
    "docs/stages/README.md": [
        "Stage 14A",
        "source-note control",
    ],
    "evidence/source_notes/README.md": [
        "Simulation-only source notes",
        "source-note backlog remains controlled",
        "Does not close ISS-0007",
    ],
    "review/stage_gate_reports/stage-14a-source-note-control-report.md": [
        "Accepted for source-note control purposes only",
        "source-note backlog remains controlled",
    ],
}


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
    register_ids = set(register_rows)

    for source_id in sorted(CORE_SOURCE_IDS - set(by_source)):
        errors.append(f"{rel} missing core source_id {source_id}")
    for source_id in sorted(CORE_SOURCE_IDS - register_ids):
        errors.append(f"{rel} core source_id {source_id} is absent from source_register.csv")

    for row in rows:
        source_id = row.get("source_id", "")
        registered = register_rows.get(source_id)
        if not registered:
            errors.append(f"{rel} {source_id} is absent from source_register.csv")
            continue
        if row.get("note_status") != "pilot_note_created":
            errors.append(f"{rel} {source_id} must be pilot_note_created")
        if row.get("claim_status") != "source_note_control_only":
            errors.append(f"{rel} {source_id} has unsafe claim_status {row.get('claim_status')}")
        if row.get("source_title") != registered.get("title"):
            errors.append(f"{rel} {source_id} title does not match source_register.csv")
        if "Does not close ISS-0007" not in row.get("no_go_note", ""):
            errors.append(f"{rel} {source_id} missing ISS-0007 no-go note")
        note_path = row.get("note_path", "")
        if not note_path.startswith("evidence/source_notes/core/"):
            errors.append(f"{rel} {source_id} note_path must stay under evidence/source_notes/core")
        elif not note_path.endswith(f"{source_id.lower()}.md"):
            errors.append(f"{rel} {source_id} note_path must end with {source_id.lower()}.md")
        elif not (ROOT / note_path).exists():
            errors.append(f"{rel} {source_id} note does not exist: {note_path}")
        else:
            note_text = (ROOT / note_path).read_text(encoding="utf-8")
            if registered.get("local_path") not in note_text:
                errors.append(f"{note_path} missing registered local_path {registered.get('local_path')}")
    return errors


def check_source_notes() -> list[str]:
    errors = []
    for source_id in sorted(CORE_SOURCE_IDS):
        path = ROOT / "evidence/source_notes/core" / f"{source_id.lower()}.md"
        if not path.exists():
            errors.append(f"missing source note: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        for phrase in REQUIRED_NOTE_PHRASES:
            if phrase not in text:
                errors.append(f"{path.relative_to(ROOT)} missing required phrase: {phrase}")
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


def collect_errors() -> list[str]:
    errors = []
    errors.extend(check_required_files())
    errors.extend(check_csv_headers())
    errors.extend(check_coverage_register())
    errors.extend(check_source_notes())
    errors.extend(check_no_go_register())
    errors.extend(check_required_phrases())
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
