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

REQUIRED_FILES = [
    "analysis/context/stage-19a-public-cabinet-comprehension-context.md",
    "docs/public/how-to-read-this-repo.md",
    "docs/public/what-this-repo-can-and-cannot-tell-you.md",
    "docs/officer/cabinet-and-officer-navigation-guide.md",
    "docs/officer/risk-gate-atlas.md",
    "docs/officer/risk-control-crosswalk.csv",
    "docs/visuals/risk-control-atlas.mmd",
    "docs/stages/stage-19a-public-cabinet-comprehension.md",
    "review/peer_review/stage-19a-public-cabinet-comprehension-review.md",
    "review/stage_gate_reports/stage-19a-public-cabinet-comprehension-report.md",
]

REQUIRED_PHRASES = {
    "README.md": [
        "Current Reader Answer",
        "Stage 19A",
        "public and cabinet comprehension controls",
        "It does not approve, launch, fund, procure or submit a Bristol Workplace Parking Levy.",
        "docs/public/how-to-read-this-repo.md",
        "docs/officer/risk-gate-atlas.md",
        "docs/visuals/risk-control-atlas.mmd",
    ],
    "docs/public/README.md": [
        "Common Terms",
        "Green control",
        "docs/public/how-to-read-this-repo.md",
        "docs/public/what-this-repo-can-and-cannot-tell-you.md",
        "docs/officer/cabinet-and-officer-navigation-guide.md",
    ],
    "docs/officer/assurance-dashboard.md": [
        "Simulation Control Dashboard",
        "RAG colours describe repository control status, not real-world WPL readiness.",
        "`GREEN` means a control exists for the stated limited purpose only.",
        "Stage 19A records public and cabinet comprehension controls.",
    ],
    "docs/stages/README.md": [
        "Gate Taxonomy",
        "Stage 19A",
        "not evidence that readers understand the repo",
        "does not pass a readiness gate",
    ],
    "docs/public/how-to-read-this-repo.md": [
        "What Green Means",
        "Green means a control exists. It does not mean the WPL is approved or ready.",
        "Simulation Sign-Off",
    ],
    "docs/public/what-this-repo-can-and-cannot-tell-you.md": [
        "Known",
        "Simulation Assumption",
        "Gap",
        "Do Not Claim",
        "CPZ/RPZ mitigation is selected, costed, consulted on or ready.",
    ],
    "docs/officer/cabinet-and-officer-navigation-guide.md": [
        "Thirty-Second Status",
        "Gate Taxonomy",
        "Current Gate Board",
        "Simulation Sign-Off Rule",
    ],
    "docs/officer/risk-gate-atlas.md": [
        "This atlas explains where the main risks sit",
        "It does not accept residual risk.",
        "docs/visuals/risk-control-atlas.mmd",
    ],
    "docs/officer/programme-risk-briefing.md": [
        "Risk-Control Crosswalk",
        "docs/officer/risk-control-crosswalk.csv",
        "It does not mean mitigations are complete",
    ],
}

CROSSWALK = "docs/officer/risk-control-crosswalk.csv"
CROSSWALK_COLUMNS = [
    "stage",
    "blocker",
    "issue_id",
    "risk_id",
    "pitfall_id",
    "evidence_gap_id",
    "current_control",
    "residual_blocker",
    "gate_effect",
    "owner",
    "next_evidence_or_decision",
    "validator",
]

REQUIRED_CROSSWALK_STAGES = {
    "Stage 2",
    "Stage 4",
    "Stage 5",
    "Stage 8",
    "Stage 17A",
    "Stage 18A",
    "Stage 19A",
}

REQUIRED_REGISTER_ROWS = [
    ("governance/issues_register.csv", "issue_id", "ISS-0029"),
    ("governance/risk_register.csv", "risk_id", "RISK-0032"),
    ("governance/pitfalls_register.csv", "pitfall_id", "PIT-0026"),
    ("evidence/evidence_gap_register.csv", "gap_id", "EG-0047"),
    ("governance/requirements_register.csv", "requirement_id", "REQ-0040"),
    ("governance/checks_and_balances_register.csv", "control_id", "CB-0026"),
    ("governance/decision_log.csv", "decision_id", "DEC-0033"),
    ("governance/approvals_register.csv", "approval_id", "APP-0038"),
    ("governance/simulation_signoff_register.csv", "signoff_id", "SSO-0087"),
]

PUBLIC_OFFICER_FILES = [
    "README.md",
    "docs/public/README.md",
    "docs/public/how-to-read-this-repo.md",
    "docs/public/what-this-repo-can-and-cannot-tell-you.md",
    "docs/public/evidence-and-assumptions-summary.md",
    "docs/officer/assurance-dashboard.md",
    "docs/officer/cabinet-and-officer-navigation-guide.md",
    "docs/officer/risk-gate-atlas.md",
    "docs/officer/programme-risk-briefing.md",
    "docs/officer/checks-and-balances-map.md",
    "docs/officer/document-map.md",
    "docs/visuals/stage-gate-map.mmd",
    "docs/visuals/risk-control-atlas.mmd",
]

UNSAFE_POSITIVE_PATTERNS = [
    re.compile(r"\b(?:scheme|wpl|consultation|obc|fbc|statutory submission)\s+(?:is\s+)?(?:approved|ready|endorsed|cleared)\b", re.IGNORECASE),
    re.compile(r"\b(?:green|complete)\b.{0,80}\b(?:ready|approved|endorsed|cleared)\b", re.IGNORECASE),
    re.compile(r"\bagent sign-?offs? replace\b", re.IGNORECASE),
]

SAFE_NEGATIONS = (
    "not ",
    "no ",
    "does not",
    "do not",
    "cannot",
    "must not",
    "blocked",
    "prohibited",
    "without",
)


def read_rows(rel: str) -> list[dict[str, str]]:
    with (ROOT / rel).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def read_header(rel: str) -> list[str]:
    with (ROOT / rel).open(newline="", encoding="utf-8") as handle:
        return next(csv.reader(handle))


def has_safe_negation(text: str) -> bool:
    lowered = text.lower()
    return any(term in lowered for term in SAFE_NEGATIONS)


def check_required_files() -> list[str]:
    return [f"missing Stage 19A file: {rel}" for rel in REQUIRED_FILES if not (ROOT / rel).exists()]


def check_required_phrases() -> list[str]:
    errors = []
    for rel, phrases in REQUIRED_PHRASES.items():
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing Stage 19A phrase file: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in text:
                errors.append(f"{rel} missing required phrase: {phrase}")
    return errors


def check_dashboard_green_rows() -> list[str]:
    dashboard = ROOT / "docs/officer/assurance-dashboard.md"
    if not dashboard.exists():
        return ["missing docs/officer/assurance-dashboard.md"]
    errors = []
    in_table = False
    for line_number, line in enumerate(dashboard.read_text(encoding="utf-8").splitlines(), start=1):
        if line.startswith("| Decision area "):
            in_table = True
            continue
        if in_table and not line.startswith("|"):
            in_table = False
        if in_table and "GREEN" in line and "control" not in line.lower():
            errors.append(f"docs/officer/assurance-dashboard.md:{line_number} GREEN row must say control-only")
    return errors


def check_crosswalk() -> list[str]:
    path = ROOT / CROSSWALK
    if not path.exists():
        return [f"missing Stage 19A crosswalk: {CROSSWALK}"]
    errors = []
    header = read_header(CROSSWALK)
    for column in CROSSWALK_COLUMNS:
        if column not in header:
            errors.append(f"{CROSSWALK} missing column {column}")
    rows = read_rows(CROSSWALK)
    stages = {row.get("stage", "") for row in rows}
    for stage in sorted(REQUIRED_CROSSWALK_STAGES - stages):
        errors.append(f"{CROSSWALK} missing stage coverage: {stage}")
    for row_number, row in enumerate(rows, start=2):
        row_id = row.get("stage", f"row {row_number}")
        for column in ["blocker", "current_control", "residual_blocker", "gate_effect", "owner", "next_evidence_or_decision", "validator"]:
            if not row.get(column):
                errors.append(f"{CROSSWALK}:{row_number} {row_id} missing {column}")
        if "block" not in row.get("gate_effect", "").lower():
            errors.append(f"{CROSSWALK}:{row_number} {row_id} gate_effect must preserve blocked/no-go wording")
    return errors


def check_register_rows() -> list[str]:
    errors = []
    for rel, id_column, row_id in REQUIRED_REGISTER_ROWS:
        if not (ROOT / rel).exists():
            errors.append(f"missing Stage 19A register file: {rel}")
            continue
        rows = {row.get(id_column, "") for row in read_rows(rel)}
        if row_id not in rows:
            errors.append(f"{rel} missing Stage 19A row {row_id}")
    return errors


def check_visual_language() -> list[str]:
    errors = []
    stage_map = ROOT / "docs/visuals/stage-gate-map.mmd"
    if not stage_map.exists():
        errors.append("missing docs/visuals/stage-gate-map.mmd")
    else:
        text = stage_map.read_text(encoding="utf-8")
        if "Complete" in text:
            errors.append("docs/visuals/stage-gate-map.mmd must not use standalone Complete labels")
        for phrase in ["Stage 19A", "Navigation only; no readiness gate closes"]:
            if phrase not in text:
                errors.append(f"docs/visuals/stage-gate-map.mmd missing phrase: {phrase}")
    risk_map = ROOT / "docs/visuals/risk-control-atlas.mmd"
    if not risk_map.exists():
        errors.append("missing docs/visuals/risk-control-atlas.mmd")
    else:
        text = risk_map.read_text(encoding="utf-8")
        for phrase in ["No-go for approval", "Future real-world proof", "Public/cabinet comprehension"]:
            if phrase not in text:
                errors.append(f"docs/visuals/risk-control-atlas.mmd missing phrase: {phrase}")
    return errors


def check_unsafe_positive_language() -> list[str]:
    errors = []
    for rel in PUBLIC_OFFICER_FILES:
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing public/officer scan file: {rel}")
            continue
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            for pattern in UNSAFE_POSITIVE_PATTERNS:
                if pattern.search(line) and not has_safe_negation(line):
                    errors.append(f"{rel}:{line_number} contains unsafe positive readiness language")
            if "sign-off" in line.lower() and not has_safe_negation(line) and "simulation" not in line.lower():
                errors.append(f"{rel}:{line_number} sign-off wording must be simulation-limited or negated")
    return errors


def collect_errors() -> list[str]:
    errors = []
    errors.extend(check_required_files())
    errors.extend(check_required_phrases())
    errors.extend(check_dashboard_green_rows())
    errors.extend(check_crosswalk())
    errors.extend(check_register_rows())
    errors.extend(check_visual_language())
    errors.extend(check_unsafe_positive_language())
    errors.extend(check_no_authored_pdfs(ROOT))
    return errors


def main() -> int:
    errors = collect_errors()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Public/cabinet comprehension QA passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
