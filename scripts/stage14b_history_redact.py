#!/usr/bin/env python3
"""Tree-filter helper for the Stage 14B history-cleanup dry run.

This script is intended to be called by `git filter-branch --tree-filter` in a
temporary mirror clone. It removes the three raw public PDFs that triggered the
hosted detector collision and redacts the extracted-text collision pattern.
"""

from __future__ import annotations

import re
from pathlib import Path

RAW_PDF_PATHS = [
    "evidence/raw/bristol-city-council/src-bcc-0005_public-reports-pack-transport-connectivity-policy-committee-2024-09-12.pdf",
    "evidence/raw/bristol-city-council/src-bcc-0011_public-reports-pack-transport-connectivity-policy-committee-2025-10-23.pdf",
    "evidence/raw/bristol-city-council/src-bcc-0015_public-reports-pack-transport-connectivity-policy-committee-2026-03-19.pdf",
]

COLLISION_PATTERN = re.compile(r"eyJrIjoi[A-Za-z0-9_./+=-]{20,}")
REDACTION = "[REDACTED_POWERBI_REPORT_ID]"


def main() -> int:
    for rel in RAW_PDF_PATHS:
        path = Path(rel)
        if path.exists():
            path.unlink()

    text_path = Path("evidence/processed/text/SRC-BCC-0011.txt")
    if text_path.exists():
        text = text_path.read_text(encoding="utf-8", errors="ignore")
        text_path.write_text(COLLISION_PATTERN.sub(REDACTION, text), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
