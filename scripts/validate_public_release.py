#!/usr/bin/env python3
from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.validate_registers import check_no_authored_pdfs, check_sensitive_paths

REQUIRED_FILES = [
    "analysis/publication/stage-12a-public-release-control-package.md",
    "publication/controls/repository-publication-checklist.csv",
    "publication/controls/public-release-no-go-register.csv",
    "publication/controls/public-release-scan-register.csv",
    "review/peer_review/stage-12a-public-release-review.md",
    "review/stage_gate_reports/stage-12a-public-release-gate-report.md",
    "docs/stages/stage-12a-public-release.md",
]

CSV_HEADERS = {
    "publication/controls/repository-publication-checklist.csv": [
        "control_id",
        "control_area",
        "requirement",
        "evidence",
        "current_status",
        "gate_effect",
        "next_check",
    ],
    "publication/controls/public-release-no-go-register.csv": [
        "claim_id",
        "prohibited_claim",
        "allowed_wording",
        "current_status",
        "gate_effect",
    ],
    "publication/controls/public-release-scan-register.csv": [
        "scan_id",
        "scan_name",
        "method",
        "finding",
        "current_status",
        "owner",
    ],
}

REQUIRED_CONTROL_IDS = {
    "repo_visibility",
    "simulation_notice",
    "no_authored_pdfs",
    "restricted_data_paths",
    "officer_editable_formats",
    "readme_entrypoints",
    "gate_blockers_visible",
    "subagent_context_hygiene",
}

REQUIRED_NO_GO_CLAIMS = {
    "public repository means council approval",
    "public repository means legal advice",
    "public repository means OBC or FBC ready",
    "public repository means consultation can launch",
    "public repository means statutory submission is ready",
    "public repository means official council publication",
    "agent sign-offs replace officers lawyers or consultants",
}

REQUIRED_PHRASES = {
    "README.md": [
        "This repository is public",
        "public visibility is not approval",
        "not an official council publication",
        "Stage 12A",
    ],
    "analysis/publication/stage-12a-public-release-control-package.md": [
        "public visibility is not approval",
        "does not close any WPL gate",
        "no authored PDFs",
    ],
    "review/stage_gate_reports/stage-12a-public-release-gate-report.md": [
        "Accepted for public-release control purposes only",
        "WPL approval gates remain blocked",
        "PUBLIC",
    ],
}


UNSAFE_PUBLIC_RELEASE_TERMS = {
    "approval",
    "approved",
    "ready",
    "readiness",
    "launch",
    "submit",
    "submission",
    "sign-off",
    "signoff",
    "official council publication",
}

SAFE_GATE_EFFECTS = {"publication_control", "P0"}

SAFE_ALLOWED_WORDING_PHRASES = {
    "consultation launch remains blocked",
    "no consultation material has been approved",
    "statutory submission remains blocked",
    "not an official council publication",
    "agent sign-offs are simulation controls",
}


def unsafe_allowed_wording_terms(value: str) -> list[str]:
    remaining = value.lower()
    for safe_phrase in SAFE_ALLOWED_WORDING_PHRASES:
        remaining = remaining.replace(safe_phrase, "")
    return [term for term in sorted(UNSAFE_PUBLIC_RELEASE_TERMS) if term in remaining]


def read_rows(rel: str, root: Path = ROOT) -> list[dict[str, str]]:
    with (root / rel).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def read_header(rel: str, root: Path = ROOT) -> list[str]:
    with (root / rel).open(newline="", encoding="utf-8") as handle:
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


def check_required_files(root: Path = ROOT) -> list[str]:
    return [f"missing public-release file: {rel}" for rel in REQUIRED_FILES if not (root / rel).exists()]


def check_csv_headers(root: Path = ROOT) -> list[str]:
    errors = []
    for rel, columns in CSV_HEADERS.items():
        if not (root / rel).exists():
            errors.append(f"missing public-release CSV: {rel}")
            continue
        header = read_header(rel, root)
        for column in columns:
            if column not in header:
                errors.append(f"{rel} missing column {column}")
        errors.extend(check_csv_widths(rel))
    return errors


def check_required_phrases(root: Path = ROOT) -> list[str]:
    errors = []
    for rel, phrases in REQUIRED_PHRASES.items():
        path = root / rel
        if not path.exists():
            errors.append(f"missing phrase-check file: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in text:
                errors.append(f"{rel} missing required phrase: {phrase}")
    return errors


def check_publication_checklist(root: Path = ROOT) -> list[str]:
    rel = "publication/controls/repository-publication-checklist.csv"
    if not (root / rel).exists():
        return [f"missing publication checklist: {rel}"]
    errors = []
    rows = read_rows(rel, root)
    control_ids = {row.get("control_id", "") for row in rows}
    for missing in sorted(REQUIRED_CONTROL_IDS - control_ids):
        errors.append(f"{rel} missing control_id {missing}")
    for row in rows:
        control_id = row.get("control_id", "<unknown>")
        if not row.get("evidence"):
            errors.append(f"{rel} {control_id} missing evidence")
        if row.get("current_status") not in {"pass", "public_verified", "controlled"}:
            errors.append(f"{rel} {control_id} has invalid current_status {row.get('current_status')}")
        gate_effect = row.get("gate_effect", "")
        if gate_effect not in SAFE_GATE_EFFECTS:
            errors.append(f"{rel} {control_id} has unsafe gate_effect {gate_effect}")
    return errors


def check_no_go_register(root: Path = ROOT) -> list[str]:
    rel = "publication/controls/public-release-no-go-register.csv"
    if not (root / rel).exists():
        return [f"missing public-release no-go register: {rel}"]
    errors = []
    rows = read_rows(rel, root)
    claims = {row.get("prohibited_claim", "") for row in rows}
    for missing in sorted(REQUIRED_NO_GO_CLAIMS - claims):
        errors.append(f"{rel} missing prohibited claim: {missing}")
    for row in rows:
        claim_id = row.get("claim_id", "<unknown>")
        if row.get("current_status") != "blocked":
            errors.append(f"{rel} {claim_id} must remain blocked")
        for unsafe_term in unsafe_allowed_wording_terms(row.get("allowed_wording", "")):
            errors.append(f"{rel} {claim_id} allowed_wording contains unsafe term: {unsafe_term}")
    return errors


def check_scan_register() -> list[str]:
    rel = "publication/controls/public-release-scan-register.csv"
    if not (ROOT / rel).exists():
        return [f"missing public-release scan register: {rel}"]
    errors = []
    rows = read_rows(rel)
    if {row.get("scan_id", "") for row in rows} != {"PUB-SCAN-001", "PUB-SCAN-002", "PUB-SCAN-003"}:
        errors.append(f"{rel} must include PUB-SCAN-001 to PUB-SCAN-003")
    for row in rows:
        scan_id = row.get("scan_id", "<unknown>")
        if row.get("current_status") != "pass":
            errors.append(f"{rel} {scan_id} must be pass")
    return errors


def collect_errors() -> list[str]:
    errors = []
    errors.extend(check_required_files())
    errors.extend(check_csv_headers())
    errors.extend(check_required_phrases())
    errors.extend(check_publication_checklist())
    errors.extend(check_no_go_register())
    errors.extend(check_scan_register())
    errors.extend(check_no_authored_pdfs())
    errors.extend(check_sensitive_paths())
    return errors


def main() -> int:
    errors = collect_errors()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Public release QA passed; WPL approval gates remain blocked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
