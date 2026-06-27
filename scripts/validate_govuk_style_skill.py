#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "skills/govuk-style/SKILL.md",
    "skills/govuk-style/references/sources.md",
    "analysis/content/stage-34a-govuk-style-application.md",
    "docs/stages/stage-34a-govuk-style-skill-adoption.md",
    "review/stage_gate_reports/stage-34a-govuk-style-skill-adoption-report.md",
]

REQUIRED_SKILL_PHRASES = [
    "name: govuk-style",
    "Use when writing or editing public, officer, cabinet, README, guidance, summary, report or review prose",
    "This is not GOV.UK/GDS-owned or endorsed.",
    "Using this guidance does not make repo content official GOV.UK content or certified GOV.UK/GDS-compliant.",
    "https://gist.github.com/fofr/505e225f9bf5e839d30c12ba6bfa0be2",
    "https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/",
    "https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/style-guides/a-to-z-style-guide/",
    "Do not simplify away legal, statutory, financial, evidence or no-go meaning.",
    "no-go wording about approval, officer advice, procurement authority, consultation readiness, statutory readiness, professional assurance and WPL readiness",
]

REQUIRED_APPLICATION_PHRASES = [
    "Stage 34A",
    "relevant to this simulation",
    "business_case/obc/simulation-release/bristol-wpl-outline-business-case-simulation-release.md",
    "docs/public/how-to-read-this-repo.md",
    "not an approved OBC",
    "does not change the no-go position",
]

REQUIRED_SOURCE_PHRASES = [
    "This repo-local skill is an adapted implementation.",
    "Open Government Licence v3.0",
    "Contains public sector information licensed under the Open Government Licence v3.0.",
    "No explicit licence statement was observed on the reviewed gist page.",
    "THIRD_PARTY_NOTICES.md",
    "Neither source makes this repo official GOV.UK content, GOV.UK/GDS endorsed, legally assured, accessibility certified or WPL-ready.",
]

REQUIRED_PUBLIC_PHRASES = {
    "docs/public/how-to-read-this-repo.md": [
        "It includes an editable simulated OBC release.",
        "It is not an approved Outline Business Case, Full Business Case or statutory submission.",
        "How to look in detail",
    ],
    "README.md": [
        "Stage 34A",
        "GOV.UK style skill",
        "skills/govuk-style/SKILL.md",
    ],
    "docs/stages/README.md": [
        "Stage 34A",
        "GOV.UK style skill adoption",
    ],
}


def check_required_files() -> list[str]:
    return [f"missing GOV.UK style skill file: {rel}" for rel in REQUIRED_FILES if not (ROOT / rel).exists()]


def check_phrases(rel: str, phrases: list[str]) -> list[str]:
    path = ROOT / rel
    if not path.exists():
        return [f"missing phrase file: {rel}"]
    text = path.read_text(encoding="utf-8")
    return [f"{rel} missing phrase: {phrase}" for phrase in phrases if phrase not in text]


def collect_errors() -> list[str]:
    errors: list[str] = []
    errors.extend(check_required_files())
    errors.extend(check_phrases("skills/govuk-style/SKILL.md", REQUIRED_SKILL_PHRASES))
    errors.extend(check_phrases("skills/govuk-style/references/sources.md", REQUIRED_SOURCE_PHRASES))
    errors.extend(check_phrases("analysis/content/stage-34a-govuk-style-application.md", REQUIRED_APPLICATION_PHRASES))
    for rel, phrases in REQUIRED_PUBLIC_PHRASES.items():
        errors.extend(check_phrases(rel, phrases))
    return errors


def main() -> int:
    errors = collect_errors()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("GOV.UK style skill QA passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
