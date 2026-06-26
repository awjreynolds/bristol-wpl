#!/usr/bin/env python3
from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REGISTER = "analysis/economic/nottingham_lessons_register.csv"
REQUIRED_HEADERS = [
    "lesson_id",
    "lesson_theme",
    "nottingham_or_comparator_evidence",
    "bristol_relevance",
    "evidence_strength",
    "transfer_condition",
    "prohibited_overclaim",
    "required_bristol_evidence",
    "current_status",
    "owner",
]

REQUIRED_THEMES = {
    "displaced_parking_cpz",
    "public_transport_package",
    "no_charge_transfer",
    "no_elasticity_transfer",
    "evidence_caution",
    "employer_support_shadow_year",
}

FORBIDDEN_DOC_PHRASES = [
    "Nottingham proves Bristol",
    "Nottingham guarantees",
    "Bristol will achieve Nottingham",
]


def read_rows(rel: str) -> list[dict[str, str]]:
    with (ROOT / rel).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def read_header(rel: str) -> list[str]:
    with (ROOT / rel).open(newline="", encoding="utf-8") as handle:
        return next(csv.reader(handle))


def collect_errors() -> list[str]:
    path = ROOT / REGISTER
    if not path.exists():
        return [f"missing Nottingham lessons register: {REGISTER}"]
    errors = []
    header = read_header(REGISTER)
    for column in REQUIRED_HEADERS:
        if column not in header:
            errors.append(f"{REGISTER} missing column {column}")
    rows = read_rows(REGISTER)
    themes = {row.get("lesson_theme", "") for row in rows}
    for theme in sorted(REQUIRED_THEMES - themes):
        errors.append(f"{REGISTER} missing required lesson theme: {theme}")
    for row in rows:
        lesson_id = row.get("lesson_id", "<unknown>")
        if row.get("current_status") not in {"blocked", "controlled_open"}:
            errors.append(f"{REGISTER} {lesson_id} must remain blocked or controlled_open")
        if not row.get("prohibited_overclaim"):
            errors.append(f"{REGISTER} {lesson_id} missing prohibited overclaim")
        if not row.get("required_bristol_evidence"):
            errors.append(f"{REGISTER} {lesson_id} missing required Bristol evidence")
    briefing = ROOT / "docs/officer/nottingham-and-comparator-lessons.md"
    if not briefing.exists():
        errors.append("missing docs/officer/nottingham-and-comparator-lessons.md")
    else:
        text = briefing.read_text(encoding="utf-8")
        for phrase in [
            "lessons only",
            "does not claim that Nottingham outcomes will happen in Bristol",
            "Residential spillover",
            "CPZ/RPZ mitigation",
        ]:
            if phrase not in text:
                errors.append(f"docs/officer/nottingham-and-comparator-lessons.md missing phrase: {phrase}")
        for phrase in FORBIDDEN_DOC_PHRASES:
            if phrase in text:
                errors.append(f"docs/officer/nottingham-and-comparator-lessons.md contains forbidden phrase: {phrase}")
    return errors


def main() -> int:
    errors = collect_errors()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Nottingham transferability QA passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
