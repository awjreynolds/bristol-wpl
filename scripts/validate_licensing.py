#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.validate_registers import check_no_authored_pdfs

REQUIRED_FILE_PHRASES = {
    "LICENSE": [
        "MIT License",
        "Copyright (c) 2026 Adam Reynolds",
        "Permission is hereby granted, free of charge",
        'THE SOFTWARE IS PROVIDED "AS IS"',
    ],
    "THIRD_PARTY_NOTICES.md": [
        "This repository's original content is licensed under the MIT License.",
        "GOV.UK content and publishing guidance",
        "Open Government Licence v3.0",
        "Contains public sector information licensed under the Open Government Licence",
        "does not grant a right to use the information in a way that suggests official status or endorsement",
        "fofr GOV.UK style skill gist",
        "No explicit licence statement was observed",
        "not a verbatim copy of the gist",
    ],
    "README.md": [
        "[LICENSE](LICENSE)",
        "[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)",
        "Original repository content is MIT licensed.",
        "Third-party source material keeps its original licence or terms.",
    ],
    "skills/govuk-style/SKILL.md": [
        "See `skills/govuk-style/references/sources.md` and `THIRD_PARTY_NOTICES.md` for attribution and licensing notes.",
    ],
    "skills/govuk-style/references/sources.md": [
        "Open Government Licence v3.0",
        "Contains public sector information licensed under the Open Government Licence v3.0.",
        "No explicit licence statement was observed on the reviewed gist page.",
        "not a verbatim copy of the gist",
    ],
    "Makefile": [
        "license-qa:",
        "scripts/validate_licensing.py",
    ],
}


def check_required_phrases() -> list[str]:
    errors: list[str] = []
    for rel, phrases in REQUIRED_FILE_PHRASES.items():
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing licensing file: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in text:
                errors.append(f"{rel} missing licensing phrase: {phrase}")
    return errors


def collect_errors() -> list[str]:
    errors: list[str] = []
    errors.extend(check_required_phrases())
    errors.extend(check_no_authored_pdfs(ROOT))
    return errors


def main() -> int:
    errors = collect_errors()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Licensing QA passed; MIT repo licence and third-party attribution notices are present")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
