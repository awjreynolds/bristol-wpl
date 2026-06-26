#!/usr/bin/env python3
from __future__ import annotations

import csv
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "analysis/context/stage-17a-editable-document-assembly-context.md",
    "docs/authoring/README.md",
    "docs/authoring/document-assembly-control-register.csv",
    "docs/visuals/authoring-control-flow.mmd",
    "docs/stages/stage-17a-editable-document-assembly.md",
    "review/peer_review/stage-17a-editable-document-assembly-review.md",
    "review/stage_gate_reports/stage-17a-editable-document-assembly-report.md",
]

REGISTER_COLUMNS = [
    "output_id",
    "output_name",
    "target_path",
    "editable_format",
    "current_status",
    "assembly_gate",
    "required_before_release",
    "no_go_note",
]

REQUIRED_OUTPUT_IDS = {f"OUT-{number:03d}" for number in range(1, 11)}

REQUIRED_CONTROL_PHRASES = {
    "docs/authoring/README.md": [
        "Editable authoring outputs are working files only",
        "They are not PDFs",
        "not an assembled OBC or FBC",
        "not a statutory submission",
        "not consultation material",
        "not approval by Bristol City Council, WECA/MCA, DfT or any statutory decision-maker",
        "No authored officer-distribution PDF",
    ],
    "README.md": [
        "Stage 17A",
        "Editable authoring outputs are working files only",
        "No authored officer-distribution PDFs",
    ],
    "docs/public/README.md": [
        "drafting scaffolds",
        "not finished documents",
    ],
    "docs/officer/assurance-dashboard.md": [
        "Editable outputs",
        "controlled inputs for future assurance",
    ],
    "docs/officer/document-map.md": [
        "editable control/drafting areas",
        "not approved/not assembled/not PDF",
        "Authored PDFs are prohibited",
    ],
    "review/stage_gate_reports/stage-17a-editable-document-assembly-report.md": [
        "Accepted for Stage 17A editable authoring-control purposes only",
        "does not assemble, approve or certify an OBC, FBC, statutory dossier, consultation pack, officer-review DOCX, public pack, scheme order or statutory submission",
    ],
}

PROHIBITED_OUTPUT_PATHS = [
    "business_case/obc/assembled/bristol-wpl-outline-business-case.md",
    "business_case/fbc/assembled/bristol-wpl-full-business-case.md",
    "business_case/obc/assembled/bristol-wpl-outline-business-case.docx",
    "business_case/fbc/assembled/bristol-wpl-full-business-case.docx",
    "consultation/assembled/consultation-launch-pack.md",
    "docs/officer/assembled/officer-review-pack.docx",
    "docs/public/assembled/public-pack.html",
]

ASSEMBLY_DIRS = [
    "business_case/obc/assembled",
    "business_case/fbc/assembled",
]


def read_rows(rel: str) -> list[dict[str, str]]:
    with (ROOT / rel).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def read_header(rel: str) -> list[str]:
    with (ROOT / rel).open(newline="", encoding="utf-8") as handle:
        return next(csv.reader(handle))


def check_required_files() -> list[str]:
    return [f"missing Stage 17A file: {rel}" for rel in REQUIRED_FILES if not (ROOT / rel).exists()]


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


def check_output_register() -> list[str]:
    rel = "docs/authoring/document-assembly-control-register.csv"
    errors = []
    if not (ROOT / rel).exists():
        return [f"missing authoring output register: {rel}"]
    header = read_header(rel)
    for column in REGISTER_COLUMNS:
        if column not in header:
            errors.append(f"{rel} missing column {column}")
    errors.extend(check_csv_widths(rel))
    rows = read_rows(rel)
    ids = {row["output_id"] for row in rows}
    if ids != REQUIRED_OUTPUT_IDS:
        for output_id in sorted(REQUIRED_OUTPUT_IDS - ids):
            errors.append(f"{rel} missing output_id {output_id}")
        for output_id in sorted(ids - REQUIRED_OUTPUT_IDS):
            errors.append(f"{rel} has unexpected output_id {output_id}")
    for row in rows:
        text = " ".join(row.values())
        if row["output_id"] in {"OUT-004", "OUT-005", "OUT-010"} and row["current_status"] not in {"blocked", "prohibited"}:
            errors.append(f"{rel} {row['output_id']} must be blocked or prohibited")
        if "not" not in row.get("no_go_note", "").lower() and "Do not" not in row.get("no_go_note", ""):
            errors.append(f"{rel} {row['output_id']} missing no-go wording")
        if row["output_id"] == "OUT-010" and "PDFs are allowed only as downloaded raw evidence under evidence/raw/" not in text:
            errors.append(f"{rel} OUT-010 missing raw-evidence-only PDF rule")
    return errors


def check_no_authored_pdfs() -> list[str]:
    errors = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT).as_posix()
        if ".git/" in rel:
            continue
        is_pdf_ext = path.suffix.lower() == ".pdf"
        is_pdf_magic = False
        try:
            is_pdf_magic = path.read_bytes()[:4] == b"%PDF"
        except OSError:
            pass
        if (is_pdf_ext or is_pdf_magic) and not rel.startswith("evidence/raw/"):
            errors.append(f"authored/non-raw PDF is prohibited: {rel}")
    return errors


def check_blocked_outputs_absent() -> list[str]:
    errors = []
    for rel in PROHIBITED_OUTPUT_PATHS:
        if (ROOT / rel).exists():
            errors.append(f"blocked assembled/distribution output exists: {rel}")
    for rel in ASSEMBLY_DIRS:
        path = ROOT / rel
        if not path.exists():
            continue
        for child in path.iterdir():
            if child.name != ".gitkeep":
                errors.append(f"blocked assembly directory contains output: {child.relative_to(ROOT)}")
    return errors


def check_assembly_scripts_fail_closed() -> list[str]:
    errors = []
    commands = [
        ("scripts/assemble_obc.py", "OBC/FBC and consultation readiness remain blocked"),
        ("scripts/assemble_fbc.py", "FBC/statutory readiness remains blocked"),
    ]
    for script, required in commands:
        result = subprocess.run(
            [sys.executable, script],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        output = result.stdout + result.stderr
        if result.returncode == 0:
            errors.append(f"{script} must fail closed while readiness blockers remain")
        if required not in output:
            errors.append(f"{script} missing blocked-output wording: {required}")
        if "Do not create" not in output:
            errors.append(f"{script} missing 'Do not create' output warning")
    return errors


def check_statutory_rows_remain_blocked() -> list[str]:
    errors = []
    for rel, key in [
        ("statutory_dossier/controls/submission-no-go-register.csv", "claim_id"),
        ("statutory_dossier/controls/dossier-readiness-gate.csv", "gate_item_id"),
    ]:
        for row in read_rows(rel):
            if row.get("current_status") != "blocked_control_only":
                errors.append(f"{rel} {row.get(key)} must remain blocked_control_only")
    return errors


def check_issue_statuses() -> list[str]:
    errors = []
    issues = {row["issue_id"]: row for row in read_rows("governance/issues_register.csv")}
    for issue_id in ["ISS-0001", "ISS-0002", "ISS-0008"]:
        if issues.get(issue_id, {}).get("status") != "narrowed_open":
            errors.append(f"{issue_id} must remain narrowed_open")
    for issue_id in ["ISS-0011", "ISS-0012", "ISS-0015", "ISS-0016", "ISS-0025", "ISS-0026"]:
        if issues.get(issue_id, {}).get("status") != "controlled_open":
            errors.append(f"{issue_id} must remain controlled_open")
    if issues.get("ISS-0027", {}).get("status") != "controlled_open":
        errors.append("ISS-0027 must remain controlled_open")
    return errors


def check_navigation_phrases() -> list[str]:
    errors = []
    for rel, phrases in REQUIRED_CONTROL_PHRASES.items():
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing navigation/control file: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in text:
                errors.append(f"{rel} missing required phrase: {phrase}")
    return errors


def collect_errors() -> list[str]:
    errors = []
    errors.extend(check_required_files())
    if errors:
        return errors
    errors.extend(check_output_register())
    errors.extend(check_no_authored_pdfs())
    errors.extend(check_blocked_outputs_absent())
    errors.extend(check_assembly_scripts_fail_closed())
    errors.extend(check_statutory_rows_remain_blocked())
    errors.extend(check_issue_statuses())
    errors.extend(check_navigation_phrases())
    return errors


def main() -> int:
    errors = collect_errors()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Authoring guardrails QA passed; editable outputs remain control-only")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
