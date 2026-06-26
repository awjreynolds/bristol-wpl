#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv
import sys

ROOT = Path(__file__).resolve().parents[1]

CONTROLLED_EMPTY_SOURCE_TYPES = {
    "strategic_control",
    "obc_control",
    "consultation_control",
}


def read_rows(rel: str) -> list[dict[str, str]]:
    with (ROOT / rel).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def collect_errors() -> list[str]:
    errors = []
    for row in read_rows("evidence/claim_evidence_matrix.csv"):
        claim_id = row.get("claim_id", "<unknown>")
        for column in ["document_id", "section", "claim_text", "materiality", "claim_type", "reviewer", "review_status"]:
            if not row.get(column):
                errors.append(f"{claim_id} missing {column}")
        source_ids = row.get("source_ids", "")
        assumption_id = row.get("assumption_id", "")
        notes = row.get("notes", "").lower()
        claim_type = row.get("claim_type", "")
        if not source_ids and not assumption_id and claim_type not in CONTROLLED_EMPTY_SOURCE_TYPES and "repo absence confirmed" not in notes:
            errors.append(f"{claim_id} has no source_ids assumption_id or explicit control/absence note")
        if row.get("review_status") not in {"verified_simulation", "verified_simulation_synthesis"}:
            errors.append(f"{claim_id} has unsupported review_status {row.get('review_status', '')}")
    return errors


if __name__ == "__main__":
    found = collect_errors()
    if found:
        for error in found:
            print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(1)
    print("Claims QA passed")
