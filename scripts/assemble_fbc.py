#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.validate_fbc_statutory_gate import collect_fbc_statutory_gate_blockers

if __name__ == "__main__":
    blockers = collect_fbc_statutory_gate_blockers()
    if blockers:
        print("Stage 11 assembly blocked: FBC/statutory readiness remains blocked by live readiness registers.")
        for blocker in blockers[:20]:
            print(f"- {blocker}")
        if len(blockers) > 20:
            print(f"- plus {len(blockers) - 20} additional blockers")
        print("Do not create business_case/fbc/assembled/bristol-wpl-full-business-case.md or officer-review DOCX output.")
        sys.exit(1)
    print("FBC/statutory readiness gate passed, but source-linked FBC assembly implementation is not yet available.")
    sys.exit(1)
