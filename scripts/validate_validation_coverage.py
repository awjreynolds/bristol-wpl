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

STAGE_REQUIREMENTS = {
    "Stage 26A": {
        "commit": "2fe88f5",
        "log": "evidence/validation/stage-26a-validation-run-log.md",
        "issue": "ISS-0036",
        "gap": "EG-0054",
        "commands": {
            "python3 scripts/validate_validation_evidence_log.py",
            "python3 -m unittest tests.test_validation_evidence_log",
            "make validate",
            "git diff --check",
            "python3 scripts/scan_secrets.py --all-history",
        },
    },
}

REQUIRED_LIMIT_PHRASES = [
    "does not prove",
    "evidence truth",
    "legal correctness",
    "source currentness",
    "substantive gate correctness",
    "professional assurance",
    "WPL readiness",
]


def read_rows(rel: str) -> list[dict[str, str]]:
    with (ROOT / rel).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def check_stage_rows() -> list[str]:
    rows = read_rows(REGISTER)
    errors: list[str] = []
    for stage, requirement in STAGE_REQUIREMENTS.items():
        stage_rows = [row for row in rows if row.get("stage") == stage]
        if not stage_rows:
            errors.append(f"{REGISTER} missing validation evidence rows for {stage}")
            continue
        commands = {row.get("command", "") for row in stage_rows}
        for command in sorted(requirement["commands"] - commands):
            errors.append(f"{REGISTER} {stage} missing required command row: {command}")
        for row_number, row in enumerate(rows, start=2):
            if row.get("stage") != stage:
                continue
            row_id = row.get("validation_id", f"row {row_number}")
            if row.get("commit_ref") != requirement["commit"]:
                errors.append(f"{REGISTER}:{row_number} {row_id} wrong commit_ref for {stage}")
            if row.get("evidence_file") != requirement["log"]:
                errors.append(f"{REGISTER}:{row_number} {row_id} wrong evidence_file for {stage}")
            if row.get("exit_code") != "0" or row.get("outcome") != "passed":
                errors.append(f"{REGISTER}:{row_number} {row_id} must be a passing command row")
            if row.get("working_directory") != "repository root":
                errors.append(f"{REGISTER}:{row_number} {row_id} missing repository-root working directory")
            if requirement["issue"] not in row.get("related_issue_ids", ""):
                errors.append(f"{REGISTER}:{row_number} {row_id} missing related issue {requirement['issue']}")
            if requirement["gap"] not in row.get("related_gap_ids", ""):
                errors.append(f"{REGISTER}:{row_number} {row_id} missing related gap {requirement['gap']}")
            scope_limit = row.get("scope_limit", "").lower()
            for phrase in REQUIRED_LIMIT_PHRASES:
                if phrase.lower() not in scope_limit:
                    errors.append(f"{REGISTER}:{row_number} {row_id} scope_limit missing {phrase}")
    return errors


def check_stage_logs() -> list[str]:
    errors: list[str] = []
    for stage, requirement in STAGE_REQUIREMENTS.items():
        path = ROOT / requirement["log"]
        if not path.exists():
            errors.append(f"missing validation log for {stage}: {requirement['log']}")
            continue
        text = path.read_text(encoding="utf-8")
        for phrase in [
            "not a raw terminal transcript",
            "does not prove evidence truth",
            "source currentness",
            "professional assurance",
            "WPL readiness",
            requirement["commit"],
            "Working directory: repository root",
        ]:
            if phrase not in text:
                errors.append(f"{requirement['log']} missing phrase: {phrase}")
        for command in requirement["commands"]:
            if command not in text:
                errors.append(f"{requirement['log']} missing command: {command}")
    return errors


def collect_errors() -> list[str]:
    errors: list[str] = []
    errors.extend(check_stage_rows())
    errors.extend(check_stage_logs())
    errors.extend(check_no_authored_pdfs(ROOT))
    return errors


def main() -> int:
    errors = collect_errors()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Validation coverage QA passed for Stage 26A lag-one coverage only; not command sufficiency or WPL readiness")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
