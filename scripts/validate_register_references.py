#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.validate_registers import check_no_authored_pdfs

REGISTER_IDS = {
    "ISS": ("governance/issues_register.csv", "issue_id"),
    "RISK": ("governance/risk_register.csv", "risk_id"),
    "PIT": ("governance/pitfalls_register.csv", "pitfall_id"),
    "EG": ("evidence/evidence_gap_register.csv", "gap_id"),
    "REQ": ("governance/requirements_register.csv", "requirement_id"),
    "CB": ("governance/checks_and_balances_register.csv", "control_id"),
    "DEC": ("governance/decision_log.csv", "decision_id"),
    "APP": ("governance/approvals_register.csv", "approval_id"),
    "SSO": ("governance/simulation_signoff_register.csv", "signoff_id"),
}

ID_PATTERN = re.compile(r"\b(ISS|RISK|PIT|EG|REQ|CB|DEC|APP|SSO)-\d{4}\b")

PATH_COLUMNS = [
    ("governance/decision_log.csv", "evidence"),
    ("governance/requirements_register.csv", "evidence"),
    ("governance/checks_and_balances_register.csv", "validator_or_gate"),
    ("governance/pitfalls_register.csv", "evidence_or_control_refs"),
    ("governance/approvals_register.csv", "artefact"),
    ("governance/simulation_signoff_register.csv", "artefact"),
    ("docs/officer/risk-control-crosswalk.csv", "validator"),
]

ID_COLUMNS = [
    ("docs/officer/risk-control-crosswalk.csv", "issue_id"),
    ("docs/officer/risk-control-crosswalk.csv", "risk_id"),
    ("docs/officer/risk-control-crosswalk.csv", "pitfall_id"),
    ("docs/officer/risk-control-crosswalk.csv", "evidence_gap_id"),
    ("governance/pitfalls_register.csv", "linked_issue_ids"),
    ("governance/pitfalls_register.csv", "linked_risk_ids"),
    ("governance/approvals_register.csv", "evidence"),
    ("governance/simulation_signoff_register.csv", "unresolved_risks"),
]


def read_rows(rel: str) -> list[dict[str, str]]:
    with (ROOT / rel).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def collect_known_ids() -> dict[str, set[str]]:
    known: dict[str, set[str]] = {}
    for prefix, (rel, column) in REGISTER_IDS.items():
        rows = read_rows(rel)
        known[prefix] = {row.get(column, "") for row in rows if row.get(column)}
    return known


def check_primary_key_uniqueness() -> list[str]:
    errors: list[str] = []
    for _prefix, (rel, column) in REGISTER_IDS.items():
        seen: dict[str, int] = {}
        for row_number, row in enumerate(read_rows(rel), start=2):
            row_id = row.get(column, "")
            if not row_id:
                errors.append(f"{rel}:{row_number} missing primary key {column}")
                continue
            if row_id in seen:
                errors.append(f"{rel}:{row_number} duplicate primary key {row_id}; first seen line {seen[row_id]}")
            else:
                seen[row_id] = row_number
    return errors


def split_multi_value(value: str) -> list[str]:
    if not value:
        return []
    parts = []
    for chunk in re.split(r"[;\n]", value):
        clean = chunk.strip()
        if clean:
            parts.append(clean)
    return parts


def extract_ids(value: str) -> list[str]:
    return [match.group(0) for match in ID_PATTERN.finditer(value or "")]


def check_ids_resolve(known: dict[str, set[str]]) -> list[str]:
    errors: list[str] = []
    for rel, column in ID_COLUMNS:
        for row_number, row in enumerate(read_rows(rel), start=2):
            for found_id in extract_ids(row.get(column, "")):
                prefix = found_id.split("-", 1)[0]
                if found_id not in known.get(prefix, set()):
                    errors.append(f"{rel}:{row_number} {column} references unknown id {found_id}")
    return errors


def looks_like_repo_path(value: str) -> bool:
    if not value or " " in value:
        return False
    if value.startswith(("http://", "https://", "python3 ", "make ")):
        return False
    return "/" in value and not value.startswith("#")


def check_paths_resolve() -> list[str]:
    errors: list[str] = []
    for rel, column in PATH_COLUMNS:
        for row_number, row in enumerate(read_rows(rel), start=2):
            for value in split_multi_value(row.get(column, "")):
                if not looks_like_repo_path(value):
                    continue
                path = ROOT / value
                if not path.exists():
                    errors.append(f"{rel}:{row_number} {column} references missing path {value}")
    return errors


def check_latest_stage_register_rows(known: dict[str, set[str]]) -> list[str]:
    required = {
        "ISS-0032",
        "RISK-0035",
        "PIT-0029",
        "EG-0050",
        "REQ-0043",
        "CB-0029",
        "DEC-0036",
        "APP-0041",
        "SSO-0093",
        "ISS-0033",
        "RISK-0036",
        "PIT-0030",
        "EG-0051",
        "REQ-0044",
        "CB-0030",
        "DEC-0037",
        "APP-0042",
        "SSO-0095",
        "ISS-0034",
        "RISK-0037",
        "PIT-0031",
        "EG-0052",
        "REQ-0045",
        "CB-0031",
        "DEC-0038",
        "APP-0043",
        "SSO-0097",
        "ISS-0035",
        "RISK-0038",
        "PIT-0032",
        "EG-0053",
        "REQ-0046",
        "CB-0032",
        "DEC-0039",
        "APP-0044",
        "SSO-0099",
        "ISS-0036",
        "RISK-0039",
        "PIT-0033",
        "EG-0054",
        "REQ-0047",
        "CB-0033",
        "DEC-0040",
        "APP-0045",
        "SSO-0101",
        "ISS-0037",
        "RISK-0040",
        "PIT-0034",
        "EG-0055",
        "REQ-0048",
        "CB-0034",
        "DEC-0041",
        "APP-0046",
        "SSO-0103",
    }
    errors = []
    flat_known = set().union(*known.values())
    for row_id in sorted(required - flat_known):
        errors.append(f"missing recent-stage baseline register row: {row_id}")
    return errors


def collect_errors() -> list[str]:
    known = collect_known_ids()
    errors: list[str] = []
    errors.extend(check_primary_key_uniqueness())
    errors.extend(check_ids_resolve(known))
    errors.extend(check_paths_resolve())
    errors.extend(check_latest_stage_register_rows(known))
    errors.extend(check_no_authored_pdfs(ROOT))
    return errors


def main() -> int:
    errors = collect_errors()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Register reference integrity QA passed; linkage integrity only, not evidence truth or readiness")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
