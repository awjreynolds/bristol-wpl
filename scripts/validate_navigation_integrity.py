#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.validate_registers import check_no_authored_pdfs

SCAN_FILES = [
    "README.md",
    "docs/public/README.md",
    "docs/public/how-to-read-this-repo.md",
    "docs/public/what-this-repo-can-and-cannot-tell-you.md",
    "docs/public/source-link-and-freshness-status.md",
    "docs/officer/assurance-dashboard.md",
    "docs/officer/cabinet-and-officer-navigation-guide.md",
    "docs/officer/risk-gate-atlas.md",
    "docs/officer/document-map.md",
    "docs/officer/programme-risk-briefing.md",
    "docs/stages/README.md",
]

REQUIRED_NAV_REFERENCES = {
    "README.md": [
        "docs/public/how-to-read-this-repo.md",
        "docs/public/source-link-and-freshness-status.md",
        "docs/officer/cabinet-and-officer-navigation-guide.md",
        "docs/officer/risk-gate-atlas.md",
        "docs/visuals/visual-accessibility-qa-register.csv",
        "scripts/validate_external_liveness.py",
        "scripts/validate_navigation_integrity.py",
        "scripts/validate_register_references.py",
        "scripts/validate_dashboard_consistency.py",
        "scripts/validate_stage_gate_reports.py",
        "scripts/validate_validation_evidence_log.py",
        "scripts/validate_validation_coverage.py",
        "scripts/validate_bristol_public_sources.py",
        "scripts/validate_subagent_context_control.py",
        "evidence/validation/README.md",
        "docs/public/bristol-live-public-source-status.md",
        "docs/agents/subagent-stage-packet-template.md",
        "review/stage_gate_reports/stage-28a-bristol-live-public-source-coverage-report.md",
        "review/stage_gate_reports/stage-29a-subagent-context-control-hardening-report.md",
        "review/stage_gate_reports/stage-30a-validation-coverage-for-stage-29a-report.md",
    ],
    "docs/public/README.md": [
        "docs/public/how-to-read-this-repo.md",
        "docs/public/what-this-repo-can-and-cannot-tell-you.md",
        "docs/public/source-link-and-freshness-status.md",
        "docs/officer/cabinet-and-officer-navigation-guide.md",
        "docs/visuals/visual-accessibility-qa-register.csv",
        "scripts/validate_external_liveness.py",
        "scripts/validate_navigation_integrity.py",
        "scripts/validate_register_references.py",
        "scripts/validate_dashboard_consistency.py",
        "scripts/validate_stage_gate_reports.py",
        "scripts/validate_validation_evidence_log.py",
        "scripts/validate_validation_coverage.py",
        "scripts/validate_bristol_public_sources.py",
        "scripts/validate_subagent_context_control.py",
        "evidence/validation/README.md",
        "docs/public/bristol-live-public-source-status.md",
        "docs/agents/subagent-stage-packet-template.md",
    ],
    "docs/officer/document-map.md": [
        "docs/public/source-link-and-freshness-status.md",
        "scripts/validate_register_references.py",
        "scripts/validate_dashboard_consistency.py",
        "scripts/validate_stage_gate_reports.py",
        "scripts/validate_validation_evidence_log.py",
        "scripts/validate_validation_coverage.py",
        "scripts/validate_bristol_public_sources.py",
        "scripts/validate_subagent_context_control.py",
        "evidence/validation/README.md",
        "docs/public/bristol-live-public-source-status.md",
        "docs/agents/subagent-stage-packet-template.md",
        "docs/officer/risk-control-crosswalk.csv",
        "docs/visuals/visual-accessibility-qa-register.csv",
    ],
    "docs/stages/README.md": [
        "stage-29a-subagent-context-control-hardening.md",
        "review/stage_gate_reports/stage-29a-subagent-context-control-hardening-report.md",
        "stage-30a-validation-coverage-for-stage-29a.md",
        "review/stage_gate_reports/stage-30a-validation-coverage-for-stage-29a-report.md",
    ],
}

REQUIRED_STAGE_REPORTS = [
    "review/stage_gate_reports/stage-18a-nottingham-displacement-transferability-report.md",
    "review/stage_gate_reports/stage-19a-public-cabinet-comprehension-report.md",
    "review/stage_gate_reports/stage-20a-visual-accessibility-qa-report.md",
    "review/stage_gate_reports/stage-21a-link-navigation-integrity-report.md",
    "review/stage_gate_reports/stage-22a-external-source-liveness-currentness-report.md",
    "review/stage_gate_reports/stage-23a-register-reference-integrity-report.md",
    "review/stage_gate_reports/stage-24a-dashboard-blocker-consistency-report.md",
    "review/stage_gate_reports/stage-25a-stage-gate-report-evidence-consistency-report.md",
    "review/stage_gate_reports/stage-26a-validation-evidence-log-controls-report.md",
    "review/stage_gate_reports/stage-27a-validation-evidence-coverage-report.md",
    "review/stage_gate_reports/stage-28a-bristol-live-public-source-coverage-report.md",
    "review/stage_gate_reports/stage-29a-subagent-context-control-hardening-report.md",
    "review/stage_gate_reports/stage-30a-validation-coverage-for-stage-29a-report.md",
]

LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
INLINE_PATH_PATTERN = re.compile(
    r"`((?:docs|analysis|review|governance|evidence|scripts|tests|models|spatial|business_case|statutory_dossier|consultation|publication)/[^`]+)`"
)


def is_external(target: str) -> bool:
    return target.startswith(("http://", "https://", "mailto:", "#"))


def clean_target(target: str) -> str:
    target = target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    if "#" in target:
        target = target.split("#", 1)[0]
    return target


def resolve_markdown_link(base_file: Path, target: str) -> Path:
    clean = clean_target(target)
    if not clean:
        return ROOT
    if clean.startswith("/"):
        return Path(clean)
    return (base_file.parent / clean).resolve()


def resolve_repo_path(target: str) -> Path:
    clean = clean_target(target)
    if clean.startswith("/"):
        return Path(clean)
    return (ROOT / clean).resolve()


def check_markdown_links() -> list[str]:
    errors = []
    for rel in SCAN_FILES:
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing navigation scan file: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        for line_number, line in enumerate(text.splitlines(), start=1):
            for match in LINK_PATTERN.finditer(line):
                target = clean_target(match.group(1))
                if not target or is_external(target):
                    continue
                resolved = resolve_markdown_link(path, target)
                if not resolved.exists():
                    errors.append(f"{rel}:{line_number} missing linked file: {target}")
            for match in INLINE_PATH_PATTERN.finditer(line):
                target = clean_target(match.group(1))
                # Register IDs and glob-like examples are intentionally ignored.
                if "*" in target or target.endswith("/"):
                    continue
                resolved = resolve_repo_path(target)
                if not resolved.exists():
                    errors.append(f"{rel}:{line_number} missing inline path: {target}")
    return errors


def check_required_nav_references() -> list[str]:
    errors = []
    for rel, required_targets in REQUIRED_NAV_REFERENCES.items():
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing navigation file: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        for target in required_targets:
            if target not in text:
                errors.append(f"{rel} missing navigation reference: {target}")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for report in REQUIRED_STAGE_REPORTS:
        if report not in readme:
            errors.append(f"README.md missing stage report reference: {report}")
        if not (ROOT / report).exists():
            errors.append(f"missing stage report file: {report}")
    return errors


def check_latest_stage_alignment() -> list[str]:
    errors = []
    expectations = {
        "README.md": "Stage 30A",
        "docs/stages/README.md": "Stage 30A",
        "docs/visuals/stage-gate-map.mmd": "Stage 30A",
        "docs/visuals/risk-control-atlas.mmd": "Stage 29A validation coverage",
    }
    for rel, phrase in expectations.items():
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing latest-stage file: {rel}")
            continue
        if phrase not in path.read_text(encoding="utf-8"):
            errors.append(f"{rel} missing latest-stage phrase: {phrase}")
    return errors


def collect_errors() -> list[str]:
    errors = []
    errors.extend(check_markdown_links())
    errors.extend(check_required_nav_references())
    errors.extend(check_latest_stage_alignment())
    errors.extend(check_no_authored_pdfs(ROOT))
    return errors


def main() -> int:
    errors = collect_errors()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Navigation integrity repo-local QA passed; external links and content truth not checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
