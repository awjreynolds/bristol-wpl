#!/usr/bin/env python3
from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.validate_registers import check_no_authored_pdfs

REQUIRED_FILES = [
    "CODEX_MASTER_PROMPT.md",
    "instructions/20-stage-continuation-and-context-control.md",
    "docs/agents/README.md",
    "docs/agents/subagent-stage-packet-template.md",
    "analysis/context/stage-29a-subagent-context-control-hardening-context.md",
    "docs/stages/stage-29a-subagent-context-control-hardening.md",
    "review/peer_review/stage-29a-subagent-context-control-hardening-review.md",
    "review/stage_gate_reports/stage-29a-subagent-context-control-hardening-report.md",
]

REQUIRED_PHRASES = {
    "CODEX_MASTER_PROMPT.md": [
        "docs/agents/subagent-stage-packet-template.md",
        "bounded task packets",
        "fork_context=false",
        "domain, evidence/citation, public/officer readability and red-team review lanes",
        "does not prove future agents obeyed the instruction",
        "does not prove evidence truth",
        "WPL readiness",
        "scoped simulation review decision",
    ],
    "instructions/20-stage-continuation-and-context-control.md": [
        "This instruction applies to every future stage and continuation stage",
        "subagents must receive bounded task packets",
        "maximum 8-12 first-read files unless the task justifies more",
        "allowed write paths, or `read-only`",
        "context budget and stopping rule",
        "record unknowns as gaps rather than infer",
        "P0/P1/P2/P3 severity rules",
        "Durable Packet And Handover Storage",
        "does not prove future agents obeyed the instruction",
        "does not prove evidence truth",
        "does not prove legal correctness",
        "does not prove professional assurance",
        "does not prove WPL readiness",
    ],
    "docs/agents/subagent-stage-packet-template.md": [
        "Exact Question",
        "Allowed Context",
        "Out Of Scope",
        "No-Go Claims",
        "Review Criteria",
        "Severity Rules",
        "Context Budget",
        "Required Output",
        "record unknowns as gaps rather than infer",
        "allowed write paths",
        "read-only",
        "does not prove evidence truth",
        "professional assurance",
        "WPL readiness",
    ],
    "docs/agents/README.md": [
        "bounded subagent work",
        "subagent-stage-packet-template.md",
        "does not prove future agents obeyed the instruction",
        "WPL readiness",
    ],
    "docs/stages/stage-29a-subagent-context-control-hardening.md": [
        "Stage 29A",
        "instruction/template presence control only",
        "does not prove future agents obey instructions",
        "does not prove evidence truth",
        "does not prove legal correctness",
        "does not prove professional assurance",
        "does not prove substantive gate correctness",
        "WPL readiness",
    ],
    "review/stage_gate_reports/stage-29a-subagent-context-control-hardening-report.md": [
        "instruction/template presence",
        "python3 scripts/validate_subagent_context_control.py",
        "python3 -m unittest tests.test_subagent_context_control",
        "make validate",
        "git diff --check",
        "python3 scripts/scan_secrets.py --all-history",
        "does not prove future agents obey instructions",
        "evidence truth",
        "legal correctness",
        "professional assurance",
        "substantive gate correctness",
        "WPL readiness",
    ],
}

EXPECTED_REGISTER_ROWS = [
    ("governance/issues_register.csv", "issue_id", "ISS-0039"),
    ("governance/risk_register.csv", "risk_id", "RISK-0042"),
    ("governance/pitfalls_register.csv", "pitfall_id", "PIT-0036"),
    ("evidence/evidence_gap_register.csv", "gap_id", "EG-0057"),
    ("governance/requirements_register.csv", "requirement_id", "REQ-0050"),
    ("governance/checks_and_balances_register.csv", "control_id", "CB-0036"),
    ("governance/decision_log.csv", "decision_id", "DEC-0043"),
    ("governance/approvals_register.csv", "approval_id", "APP-0048"),
    ("governance/simulation_signoff_register.csv", "signoff_id", "SSO-0107"),
]


def read_rows(rel: str) -> list[dict[str, str]]:
    with (ROOT / rel).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def check_required_files() -> list[str]:
    return [f"missing Stage 29A context-control file: {rel}" for rel in REQUIRED_FILES if not (ROOT / rel).exists()]


def check_required_phrases() -> list[str]:
    errors: list[str] = []
    for rel, phrases in REQUIRED_PHRASES.items():
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing Stage 29A phrase file: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in text:
                errors.append(f"{rel} missing required context-control phrase: {phrase}")
    return errors


def check_register_rows() -> list[str]:
    errors: list[str] = []
    for rel, column, row_id in EXPECTED_REGISTER_ROWS:
        rows = {row.get(column, "") for row in read_rows(rel)}
        if row_id not in rows:
            errors.append(f"{rel} missing Stage 29A row {row_id}")
    return errors


def check_makefile() -> list[str]:
    path = ROOT / "Makefile"
    if not path.exists():
        return ["missing Makefile"]
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    for phrase in [
        "subagent-context-control-qa",
        "scripts/validate_subagent_context_control.py",
    ]:
        if phrase not in text:
            errors.append(f"Makefile missing subagent context-control integration: {phrase}")
    return errors


def collect_errors() -> list[str]:
    errors: list[str] = []
    errors.extend(check_required_files())
    errors.extend(check_required_phrases())
    errors.extend(check_register_rows())
    errors.extend(check_makefile())
    errors.extend(check_no_authored_pdfs(ROOT))
    return errors


def main() -> int:
    errors = collect_errors()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Subagent/context-control QA passed for Stage 29A instruction/template presence and no-overclaim wording only; does not prove future agents obey instructions, evidence truth, legal correctness, professional assurance, substantive gate correctness or WPL readiness")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
