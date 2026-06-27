#!/usr/bin/env python3
from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.validate_registers import check_no_authored_pdfs

REGISTER = "evidence/bristol_public_source_status.csv"

EXPECTED_SOURCES = {
    "BPS-0001": {
        "source_id": "SRC-BCC-0001",
        "source_type": "official_project_page",
        "url": "https://www.bristol.gov.uk/residents/streets-travel/transport-plans-and-projects/workplace-parking-levy",
        "status_terms": ["downloaded", "browser-readable"],
        "must_not_terms": ["approval", "consultation readiness", "OBC", "FBC", "statutory readiness", "WPL readiness"],
    },
    "BPS-0002": {
        "source_id": "SRC-BCC-0002",
        "source_type": "official_news_release",
        "url": "https://news.bristol.gov.uk/press-releases/ba17de24-32b0-46ce-80b6-3d629d6eade1/further-information-bristol-workplace-parking-levy",
        "status_terms": ["script_hydrated_or_placeholder", "loading shell"],
        "must_not_terms": ["committee decision", "legal effect", "consultation launch", "WPL readiness"],
    },
    "BPS-0003": {
        "source_id": "SRC-BCC-0020",
        "source_type": "media_context",
        "url": "https://www.bristolpost.co.uk/news/bristol-news/bristol-workplace-parking-levy-could-11025667",
        "status_terms": ["seeded_not_downloaded", "402 Payment Required", "no source note"],
        "must_not_terms": ["official decision", "charge level", "media accuracy", "WPL readiness"],
    },
}

REQUIRED_COLUMNS = [
    "watch_id",
    "source_id",
    "source_type",
    "title",
    "url",
    "source_register_status",
    "liveness_or_access_status",
    "repository_content_status",
    "source_note_status",
    "claim_use_limit",
    "formal_decision_use",
    "related_issue_ids",
    "related_gap_ids",
    "next_action",
]

PUBLIC_FILES = [
    "README.md",
    "docs/public/README.md",
    "docs/public/source-link-and-freshness-status.md",
    "docs/public/bristol-live-public-source-status.md",
    "docs/officer/assurance-dashboard.md",
    "docs/officer/document-map.md",
    "docs/stages/README.md",
    "docs/stages/stage-28a-bristol-live-public-source-coverage.md",
    "docs/visuals/stage-gate-map.mmd",
    "docs/visuals/risk-control-atlas.mmd",
]


def read_rows(rel: str) -> list[dict[str, str]]:
    with (ROOT / rel).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def read_header(rel: str) -> list[str]:
    with (ROOT / rel).open(newline="", encoding="utf-8") as handle:
        return next(csv.reader(handle))


def text_for(row: dict[str, str]) -> str:
    return " ".join(row.values())


def check_register() -> list[str]:
    path = ROOT / REGISTER
    if not path.exists():
        return [f"missing Bristol public source status register: {REGISTER}"]
    errors: list[str] = []
    header = read_header(REGISTER)
    for column in REQUIRED_COLUMNS:
        if column not in header:
            errors.append(f"{REGISTER} missing column {column}")
    rows = {row.get("watch_id", ""): row for row in read_rows(REGISTER)}
    for watch_id, expected in EXPECTED_SOURCES.items():
        row = rows.get(watch_id)
        if row is None:
            errors.append(f"{REGISTER} missing row {watch_id}")
            continue
        for key in ["source_id", "source_type", "url"]:
            if row.get(key) != expected[key]:
                errors.append(f"{REGISTER} {watch_id} has wrong {key}: {row.get(key)}")
        if row.get("formal_decision_use") != "no":
            errors.append(f"{REGISTER} {watch_id} formal_decision_use must be no")
        if "ISS-0038" not in row.get("related_issue_ids", ""):
            errors.append(f"{REGISTER} {watch_id} missing ISS-0038")
        if "EG-0056" not in row.get("related_gap_ids", ""):
            errors.append(f"{REGISTER} {watch_id} missing EG-0056")
        combined = text_for(row)
        for term in expected["status_terms"]:
            if term not in combined:
                errors.append(f"{REGISTER} {watch_id} missing status term: {term}")
        claim_limit = row.get("claim_use_limit", "")
        for term in expected["must_not_terms"]:
            if term not in claim_limit:
                errors.append(f"{REGISTER} {watch_id} claim_use_limit missing: {term}")
    return errors


def check_source_register_alignment() -> list[str]:
    rows = {row["source_id"]: row for row in read_rows("evidence/source_register.csv")}
    errors: list[str] = []
    for expected in EXPECTED_SOURCES.values():
        row = rows.get(expected["source_id"])
        if row is None:
            errors.append(f"evidence/source_register.csv missing {expected['source_id']}")
            continue
        if row.get("url") != expected["url"]:
            errors.append(f"evidence/source_register.csv {expected['source_id']} wrong URL")
    if rows.get("SRC-BCC-0020", {}).get("status") != "seeded_not_downloaded":
        errors.append("SRC-BCC-0020 must remain seeded_not_downloaded until lawfully acquired")
    return errors


def check_public_docs() -> list[str]:
    errors: list[str] = []
    required_phrases = [
        "Stage 28A",
        "Bristol live public-source coverage",
        "SRC-BCC-0001",
        "SRC-BCC-0002",
        "SRC-BCC-0020",
        "does not prove",
        "WPL readiness",
        "media context",
    ]
    for rel in PUBLIC_FILES:
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing Bristol source public file: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        for phrase in required_phrases:
            if phrase not in text:
                errors.append(f"{rel} missing Bristol public source phrase: {phrase}")
    return errors


def check_register_rows() -> list[str]:
    expected = [
        ("governance/issues_register.csv", "issue_id", "ISS-0038"),
        ("governance/risk_register.csv", "risk_id", "RISK-0041"),
        ("governance/pitfalls_register.csv", "pitfall_id", "PIT-0035"),
        ("evidence/evidence_gap_register.csv", "gap_id", "EG-0056"),
        ("governance/requirements_register.csv", "requirement_id", "REQ-0049"),
        ("governance/checks_and_balances_register.csv", "control_id", "CB-0035"),
        ("governance/decision_log.csv", "decision_id", "DEC-0042"),
        ("governance/approvals_register.csv", "approval_id", "APP-0047"),
        ("governance/simulation_signoff_register.csv", "signoff_id", "SSO-0105"),
    ]
    errors: list[str] = []
    for rel, column, row_id in expected:
        rows = {row.get(column, "") for row in read_rows(rel)}
        if row_id not in rows:
            errors.append(f"{rel} missing Stage 28A row {row_id}")
    return errors


def collect_errors() -> list[str]:
    errors: list[str] = []
    errors.extend(check_register())
    errors.extend(check_source_register_alignment())
    errors.extend(check_public_docs())
    errors.extend(check_register_rows())
    errors.extend(check_no_authored_pdfs(ROOT))
    return errors


def main() -> int:
    errors = collect_errors()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Bristol public source coverage QA passed; source coverage only, not source truth, currentness or WPL readiness")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
