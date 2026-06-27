#!/usr/bin/env python3
from __future__ import annotations

import sys
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.validate_registers import check_no_authored_pdfs

REPORTS = {
    "review/stage_gate_reports/stage-22a-external-source-liveness-currentness-report.md": {
        "stage": "Stage 22A",
        "focused_commands": [
            "python3 scripts/validate_external_liveness.py",
            "python3 -m unittest tests.test_external_liveness",
        ],
        "extra_limit_terms": [],
    },
    "review/stage_gate_reports/stage-23a-register-reference-integrity-report.md": {
        "stage": "Stage 23A",
        "focused_commands": [
            "python3 scripts/validate_register_references.py",
            "python3 -m unittest tests.test_register_references",
        ],
        "extra_limit_terms": [],
    },
    "review/stage_gate_reports/stage-24a-dashboard-blocker-consistency-report.md": {
        "stage": "Stage 24A",
        "focused_commands": [
            "python3 scripts/validate_dashboard_consistency.py",
            "python3 -m unittest tests.test_dashboard_consistency",
        ],
        "extra_limit_terms": [],
    },
    "review/stage_gate_reports/stage-25a-stage-gate-report-evidence-consistency-report.md": {
        "stage": "Stage 25A",
        "focused_commands": [
            "python3 scripts/validate_stage_gate_reports.py",
            "python3 -m unittest tests.test_stage_gate_reports",
        ],
        "extra_limit_terms": [
            "command execution",
            "substantive gate",
        ],
    },
    "review/stage_gate_reports/stage-26a-validation-evidence-log-controls-report.md": {
        "stage": "Stage 26A",
        "focused_commands": [
            "python3 scripts/validate_validation_evidence_log.py",
            "python3 -m unittest tests.test_validation_evidence_log",
        ],
        "extra_limit_terms": [
            "source currentness",
            "substantive gate",
        ],
    },
    "review/stage_gate_reports/stage-27a-validation-evidence-coverage-report.md": {
        "stage": "Stage 27A",
        "focused_commands": [
            "python3 scripts/validate_validation_coverage.py",
            "python3 -m unittest tests.test_validation_coverage",
        ],
        "extra_limit_terms": [
            "command sufficiency",
            "source currentness",
            "substantive gate",
        ],
    },
    "review/stage_gate_reports/stage-28a-bristol-live-public-source-coverage-report.md": {
        "stage": "Stage 28A",
        "focused_commands": [
            "python3 scripts/validate_bristol_public_sources.py",
            "python3 -m unittest tests.test_bristol_public_sources",
        ],
        "extra_limit_terms": [
            "source currentness",
            "media accuracy",
            "formal decision",
        ],
    },
    "review/stage_gate_reports/stage-29a-subagent-context-control-hardening-report.md": {
        "stage": "Stage 29A",
        "focused_commands": [
            "python3 scripts/validate_subagent_context_control.py",
            "python3 -m unittest tests.test_subagent_context_control",
        ],
        "extra_limit_terms": [
            "future agents obey instructions",
            "legal correctness",
            "substantive gate correctness",
        ],
    },
    "review/stage_gate_reports/stage-30a-validation-coverage-for-stage-29a-report.md": {
        "stage": "Stage 30A",
        "focused_commands": [
            "python3 scripts/validate_validation_coverage.py",
            "python3 -m unittest tests.test_validation_coverage",
        ],
        "extra_limit_terms": [
            "command sufficiency",
            "command authenticity",
            "future agent compliance",
            "substantive gate correctness",
        ],
    },
}

COMMON_COMMANDS = [
    "make validate",
    "git diff --check",
    "python3 scripts/scan_secrets.py --all-history",
]

REQUIRED_SECTIONS = [
    "Validation",
    "## Remaining Blockers",
    "## Gate Decision",
]

NO_GO_TERMS = [
    "evidence truth",
    "professional assurance",
    "WPL readiness",
]

NEGATION_MARKERS = (
    "does not",
    "do not",
    "not ",
    "no ",
    "cannot",
    "must not",
    "blocked",
    "separate",
    "outside scope",
)

UNSAFE_OVERCLAIM_PATTERNS = [
    re.compile(r"\b(?:approved|certified|ready)\b", re.IGNORECASE),
    re.compile(r"\bproves?\s+evidence\s+truth\b", re.IGNORECASE),
    re.compile(r"\bprofessional\s+assurance\s+exists\b", re.IGNORECASE),
    re.compile(r"\bcommand[- ]execution\s+proof\b", re.IGNORECASE),
]


def markdown_sections(text: str) -> dict[str, str]:
    sections: dict[str, list[str]] = {}
    current = ""
    for line in text.splitlines():
        if line.startswith("## "):
            current = line[3:].strip()
            sections.setdefault(current, [])
            continue
        sections.setdefault(current, []).append(line)
    return {heading: "\n".join(lines).strip() for heading, lines in sections.items()}


def has_negation(line: str) -> bool:
    lowered = line.lower()
    return any(marker in lowered for marker in NEGATION_MARKERS)


def check_report(rel: str, config: dict[str, object]) -> list[str]:
    path = ROOT / rel
    if not path.exists():
        return [f"missing stage-gate report: {rel}"]
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    sections = markdown_sections(text)

    for section in REQUIRED_SECTIONS:
        section_name = section.removeprefix("## ")
        if section_name not in sections:
            errors.append(f"{rel} missing required section: ## {section_name}")

    validation = sections.get("Validation", "")
    if "Focused validation:" not in validation:
        errors.append(f"{rel} missing Focused validation block")
    if "Full validation before commit:" not in validation:
        errors.append(f"{rel} missing Full validation before commit block")

    for command in config["focused_commands"]:  # type: ignore[index]
        if str(command) not in validation:
            errors.append(f"{rel} missing focused validation command in Validation section: {command}")
    for command in COMMON_COMMANDS:
        if command not in validation:
            errors.append(f"{rel} missing full validation command in Validation section: {command}")

    makefile = (ROOT / "Makefile").read_text(encoding="utf-8")
    if "scripts/validate_stage_gate_reports.py" not in makefile:
        errors.append("Makefile missing validate_stage_gate_reports.py integration")
    if "stage-gate-reports-qa" not in makefile:
        errors.append("Makefile missing stage-gate-reports-qa target")

    lowered = text.lower()
    for term in NO_GO_TERMS + list(config["extra_limit_terms"]):  # type: ignore[index]
        if term.lower() not in lowered:
            errors.append(f"{rel} missing no-overclaim term: {term}")
    if "does not" not in lowered and "not prove" not in lowered:
        errors.append(f"{rel} missing explicit negative limitation wording")

    blockers_and_decision = "\n".join(
        [
            sections.get("Remaining Blockers", ""),
            sections.get("Gate Decision", ""),
        ]
    ).lower()
    for term in NO_GO_TERMS:
        if term.lower() not in blockers_and_decision:
            errors.append(f"{rel} missing {term} in Remaining Blockers or Gate Decision")

    for line_number, line in enumerate(text.splitlines(), start=1):
        for pattern in UNSAFE_OVERCLAIM_PATTERNS:
            if pattern.search(line) and not has_negation(line):
                errors.append(f"{rel}:{line_number} possible unnegated gate overclaim: {line.strip()}")
    return errors


def collect_errors() -> list[str]:
    errors: list[str] = []
    for rel, config in REPORTS.items():
        errors.extend(check_report(rel, config))
    errors.extend(check_no_authored_pdfs(ROOT))
    return errors


def main() -> int:
    errors = collect_errors()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Stage-gate report structure QA passed; bounded report set only, not command execution proof, evidence truth or WPL readiness")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
