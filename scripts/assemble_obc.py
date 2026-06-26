#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.validate_obc import collect_readiness_blockers

if __name__ == "__main__":
    blockers = collect_readiness_blockers()
    if blockers:
        print("Stage 6A assembly blocked: OBC/FBC and consultation readiness remain blocked by live readiness registers.")
        for blocker in blockers[:20]:
            print(f"- {blocker}")
        if len(blockers) > 20:
            print(f"- plus {len(blockers) - 20} additional blockers")
        print("Do not create business_case/obc/assembled/bristol-wpl-outline-business-case.md or officer-review DOCX output.")
        sys.exit(1)
    print("OBC readiness gate passed, but source-linked OBC assembly implementation is not yet available.")
    sys.exit(1)
