#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = {
    "governance/skills_gap_register.csv": ["gap_id", "required_profession_or_agent", "simulation_role"],
    "governance/simulation_signoff_register.csv": ["signoff_id", "agent_role", "decision", "statement"],
    "evidence/source_register.csv": ["source_id", "seed_doc_id", "url", "status"],
    "evidence/claim_evidence_matrix.csv": ["claim_id", "document_id", "claim_text", "source_ids"],
    "statutory_dossier/legal_compliance_matrix.csv": ["requirement_id", "legal_source", "operative_requirement"],
    "governance/pitfalls_register.csv": ["pitfall_id", "stage", "pitfall", "mitigation"],
    "governance/stage_risk_matrix.csv": ["stage", "blocker", "mitigation", "gate_effect"],
    "governance/checks_and_balances_register.csv": ["control_id", "claim_type", "required_evidence", "validator_or_gate"],
    "governance/real_world_adoption_checklist.csv": ["adoption_id", "simulation_control", "required_real_world_replacement"],
    "statutory_dossier/controls/dossier-component-register.csv": ["component_number", "component_name", "current_status"],
    "statutory_dossier/controls/submission-no-go-register.csv": ["claim_id", "prohibited_claim", "current_status"],
    "business_case/fbc/controls/stage-11-fbc-statutory-gate-checklist.csv": ["gate_item_id", "assurance_area", "current_status"],
    "business_case/fbc/controls/stage-11-no-go-claim-register.csv": ["claim_id", "prohibited_claim", "current_status"],
}

def read_header(path: Path) -> list[str]:
    with path.open(newline="", encoding="utf-8") as handle:
        return next(csv.reader(handle))

def check_registers() -> list[str]:
    errors = []
    for rel, columns in REQUIRED.items():
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing required register: {rel}")
            continue
        header = read_header(path)
        for col in columns:
            if col not in header:
                errors.append(f"{rel} missing column {col}")
    return errors

def check_csv_row_widths(root: Path = ROOT) -> list[str]:
    errors = []
    for path in root.rglob("*.csv"):
        if ".git" in path.parts:
            continue
        rel = path.relative_to(root).as_posix()
        with path.open(newline="", encoding="utf-8") as handle:
            reader = csv.reader(handle)
            try:
                header = next(reader)
            except StopIteration:
                continue
            expected = len(header)
            for line_number, row in enumerate(reader, start=2):
                if len(row) != expected:
                    errors.append(
                        f"{rel}:{line_number} has {len(row)} fields; expected {expected}"
                    )
    return errors

def check_no_authored_pdfs() -> list[str]:
    errors = []
    for path in ROOT.rglob("*.pdf"):
        rel = path.relative_to(ROOT).as_posix()
        if not rel.startswith("evidence/raw/"):
            errors.append(f"authored or misplaced PDF is not allowed: {rel}")
    return errors

def check_sensitive_paths() -> list[str]:
    errors = []
    forbidden_parts = [
        "data/restricted/",
        "consultation/response_data/raw/",
        "consultation/response_data/personal/",
    ]
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT).as_posix()
        if any(rel.startswith(part) for part in forbidden_parts) and path.name != ".gitkeep":
            errors.append(f"restricted file present in normal repo path: {rel}")
    return errors

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", action="store_true")
    parser.parse_args()
    errors = []
    errors.extend(check_registers())
    errors.extend(check_csv_row_widths())
    errors.extend(check_no_authored_pdfs())
    errors.extend(check_sensitive_paths())
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Validation passed")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
