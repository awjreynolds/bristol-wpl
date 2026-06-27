#!/usr/bin/env python3
from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.validate_registers import check_no_authored_pdfs

REGISTER = "evidence/validation/validation-run-register.csv"
LOG = "evidence/validation/stage-25a-validation-run-log.md"

REQUIRED_COLUMNS = [
    "validation_id",
    "stage",
    "run_date",
    "commit_ref",
    "working_directory",
    "command",
    "exit_code",
    "outcome",
    "evidence_file",
    "output_summary",
    "scope_limit",
    "related_issue_ids",
    "related_gap_ids",
    "recorded_by",
]

REQUIRED_COMMANDS = {
    "python3 scripts/validate_stage_gate_reports.py",
    "python3 -m unittest tests.test_stage_gate_reports",
    "python3 scripts/validate_navigation_integrity.py",
    "python3 scripts/validate_dashboard_consistency.py",
    "python3 scripts/validate_public_cabinet_comprehension.py",
    "python3 scripts/validate_visual_accessibility.py",
    "python3 scripts/validate_register_references.py",
    "python3 -m unittest tests.test_navigation_integrity tests.test_register_references tests.test_dashboard_consistency",
    "python3 scripts/build_register_workbooks.py",
    "make validate",
    "git diff --check",
    "python3 scripts/scan_secrets.py --all-history",
}

REQUIRED_LIMIT_TERMS = [
    "does not prove",
    "evidence truth",
    "professional assurance",
    "WPL readiness",
]

STAGE_LINKS = {
    "Stage 25A": ("ISS-0035", "EG-0053"),
    "Stage 26A": ("ISS-0036", "EG-0054"),
    "Stage 29A": ("ISS-0039", "EG-0057"),
}


def read_rows(rel: str) -> list[dict[str, str]]:
    with (ROOT / rel).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def check_register() -> list[str]:
    path = ROOT / REGISTER
    if not path.exists():
        return [f"missing validation evidence register: {REGISTER}"]
    errors: list[str] = []
    with path.open(newline="", encoding="utf-8") as handle:
        header = next(csv.reader(handle))
    for column in REQUIRED_COLUMNS:
        if column not in header:
            errors.append(f"{REGISTER} missing column {column}")
    rows = read_rows(REGISTER)
    if not rows:
        errors.append(f"{REGISTER} must contain validation rows")
        return errors
    commands = {row.get("command", "") for row in rows}
    for command in sorted(REQUIRED_COMMANDS - commands):
        errors.append(f"{REGISTER} missing required command row: {command}")
    seen_ids: set[str] = set()
    for row_number, row in enumerate(rows, start=2):
        row_id = row.get("validation_id", "")
        if not row_id:
            errors.append(f"{REGISTER}:{row_number} missing validation_id")
        elif row_id in seen_ids:
            errors.append(f"{REGISTER}:{row_number} duplicate validation_id {row_id}")
        seen_ids.add(row_id)
        if row.get("outcome") != "passed":
            errors.append(f"{REGISTER}:{row_number} {row_id} outcome must be passed for accepted evidence rows")
        if row.get("exit_code") != "0":
            errors.append(f"{REGISTER}:{row_number} {row_id} exit_code must be 0 for accepted evidence rows")
        if row.get("working_directory") != "repository root":
            errors.append(f"{REGISTER}:{row_number} {row_id} working_directory must be repository root")
        evidence_file = row.get("evidence_file", "")
        if not evidence_file or not (ROOT / evidence_file).exists():
            errors.append(f"{REGISTER}:{row_number} {row_id} evidence_file missing or unresolved")
        scope_limit = row.get("scope_limit", "")
        for term in REQUIRED_LIMIT_TERMS:
            if term.lower() not in scope_limit.lower():
                errors.append(f"{REGISTER}:{row_number} {row_id} scope_limit missing {term}")
        stage = row.get("stage", "")
        if stage not in STAGE_LINKS:
            errors.append(f"{REGISTER}:{row_number} {row_id} has unsupported validation evidence stage {stage}")
        else:
            expected_issue, expected_gap = STAGE_LINKS[stage]
            if expected_issue not in row.get("related_issue_ids", ""):
                errors.append(f"{REGISTER}:{row_number} {row_id} missing related issue {expected_issue}")
            if expected_gap not in row.get("related_gap_ids", ""):
                errors.append(f"{REGISTER}:{row_number} {row_id} missing related gap {expected_gap}")
    return errors


def check_log() -> list[str]:
    path = ROOT / LOG
    if not path.exists():
        return [f"missing validation run log: {LOG}"]
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    for command in REQUIRED_COMMANDS:
        if command not in text:
            errors.append(f"{LOG} missing command evidence: {command}")
    for phrase in [
        "Exit",
        "118 unit tests passed",
        "does not prove evidence truth",
        "source currentness",
        "professional assurance",
        "WPL readiness",
    ]:
        if phrase not in text:
            errors.append(f"{LOG} missing phrase: {phrase}")
    return errors


def check_makefile_integration() -> list[str]:
    makefile = ROOT / "Makefile"
    if not makefile.exists():
        return ["missing Makefile"]
    text = makefile.read_text(encoding="utf-8")
    errors: list[str] = []
    for phrase in [
        "scripts/validate_validation_evidence_log.py",
        "validation-evidence-qa",
    ]:
        if phrase not in text:
            errors.append(f"Makefile missing validation evidence integration: {phrase}")
    return errors


def collect_errors() -> list[str]:
    errors: list[str] = []
    errors.extend(check_register())
    errors.extend(check_log())
    errors.extend(check_makefile_integration())
    errors.extend(check_no_authored_pdfs(ROOT))
    return errors


def main() -> int:
    errors = collect_errors()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Validation evidence log QA passed; command-run record only, not evidence truth or WPL readiness")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
