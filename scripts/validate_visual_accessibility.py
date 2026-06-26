#!/usr/bin/env python3
from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.validate_registers import check_no_authored_pdfs

REGISTER = "docs/visuals/visual-accessibility-qa-register.csv"

REQUIRED_COLUMNS = [
    "visual_id",
    "file_path",
    "review_date",
    "reviewer_role",
    "render_check_status",
    "plain_language_status",
    "false_readiness_risk",
    "missing_no_go_wording",
    "colour_only_dependency",
    "legend_present",
    "reader_task",
    "observed_failure_mode",
    "required_change",
    "claim_limit_wording",
    "related_issue_ids",
    "related_risk_ids",
    "residual_status",
    "next_real_world_proof",
    "validator",
]

REQUIRED_VISUALS = {
    "VQA-001": "docs/visuals/stage-gate-map.mmd",
    "VQA-002": "docs/visuals/risk-control-atlas.mmd",
    "VQA-003": "README.md",
}

REQUIRED_TEXT_FALLBACK_PHRASES = {
    "docs/officer/risk-gate-atlas.md": [
        "text fallback",
        "docs/officer/risk-control-crosswalk.csv",
    ],
    "docs/officer/document-map.md": [
        "visual fallback",
        "docs/visuals/visual-accessibility-qa-register.csv",
    ],
}

REQUIRED_MERMAID_PHRASES = {
    "docs/visuals/stage-gate-map.mmd": [
        "flowchart",
        "Simulation control map only",
        "No WPL readiness gate closes",
        "Legend",
        "dashed arrow",
        "Stage 20A",
        "Static source checks only",
        "Stage 21A",
        "Stage 22A",
        "Stage 23A",
        "Stage 24A",
    ],
    "docs/visuals/risk-control-atlas.mmd": [
        "flowchart",
        "Simulation control map only",
        "No-go for approval",
        "Future real-world proof",
        "Public/cabinet comprehension",
        "Visual/accessibility QA",
        "Source-link/freshness status",
        "Register reference integrity",
        "Dashboard blocker consistency",
        "Legend",
    ],
}


def read_rows(rel: str) -> list[dict[str, str]]:
    with (ROOT / rel).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def read_header(rel: str) -> list[str]:
    with (ROOT / rel).open(newline="", encoding="utf-8") as handle:
        return next(csv.reader(handle))


def check_register() -> list[str]:
    path = ROOT / REGISTER
    if not path.exists():
        return [f"missing visual QA register: {REGISTER}"]
    errors = []
    header = read_header(REGISTER)
    for column in REQUIRED_COLUMNS:
        if column not in header:
            errors.append(f"{REGISTER} missing column {column}")
    rows = read_rows(REGISTER)
    by_id = {row.get("visual_id", ""): row for row in rows}
    for visual_id, artifact in REQUIRED_VISUALS.items():
        row = by_id.get(visual_id)
        if row is None:
            errors.append(f"{REGISTER} missing row {visual_id}")
            continue
        if row.get("file_path") != artifact:
            errors.append(f"{REGISTER} {visual_id} must point to {artifact}")
        if row.get("render_check_status") != "static_source_check_only":
            errors.append(f"{REGISTER} {visual_id} render_check_status must remain static_source_check_only")
        if row.get("plain_language_status") != "control_only":
            errors.append(f"{REGISTER} {visual_id} plain_language_status must remain control_only")
        if row.get("missing_no_go_wording") != "no":
            errors.append(f"{REGISTER} {visual_id} missing_no_go_wording must be no")
        if row.get("colour_only_dependency") != "no":
            errors.append(f"{REGISTER} {visual_id} colour_only_dependency must be no")
        if row.get("legend_present") != "yes":
            errors.append(f"{REGISTER} {visual_id} legend_present must be yes")
        if row.get("residual_status") != "controlled_open":
            errors.append(f"{REGISTER} {visual_id} residual_status must remain controlled_open")
        for column in ["reader_task", "observed_failure_mode", "required_change", "claim_limit_wording", "next_real_world_proof", "validator"]:
            if not row.get(column):
                errors.append(f"{REGISTER} {visual_id} missing {column}")
        if "certification" in " ".join(row.values()).lower():
            errors.append(f"{REGISTER} {visual_id} must not claim certification")
        if "no WPL readiness gate closes" not in row.get("claim_limit_wording", ""):
            errors.append(f"{REGISTER} {visual_id} claim_limit_wording must preserve no readiness gate wording")
    return errors


def check_mermaid_sources() -> list[str]:
    errors = []
    for rel, phrases in REQUIRED_MERMAID_PHRASES.items():
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing Mermaid source: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        if "Complete" in text:
            errors.append(f"{rel} must not use standalone Complete labels")
        if "WCAG" in text or "certified" in text.lower():
            errors.append(f"{rel} must not claim accessibility certification")
        for phrase in phrases:
            if phrase not in text:
                errors.append(f"{rel} missing phrase: {phrase}")
    return errors


def check_text_fallbacks() -> list[str]:
    errors = []
    for rel, phrases in REQUIRED_TEXT_FALLBACK_PHRASES.items():
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing visual fallback file: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in text:
                errors.append(f"{rel} missing visual fallback phrase: {phrase}")
    return errors


def check_eg0047_open() -> list[str]:
    rows = read_rows("evidence/evidence_gap_register.csv")
    for row in rows:
        if row.get("gap_id") == "EG-0047":
            if row.get("status") != "open":
                return ["evidence/evidence_gap_register.csv EG-0047 must remain open"]
            return []
    return ["evidence/evidence_gap_register.csv missing EG-0047"]


def collect_errors() -> list[str]:
    errors = []
    errors.extend(check_register())
    errors.extend(check_mermaid_sources())
    errors.extend(check_text_fallbacks())
    errors.extend(check_eg0047_open())
    errors.extend(check_no_authored_pdfs(ROOT))
    return errors


def main() -> int:
    errors = collect_errors()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Visual/accessibility repo-level control QA passed; no real user/accessibility assurance")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
