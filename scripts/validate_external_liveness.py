#!/usr/bin/env python3
from __future__ import annotations

import csv
import datetime as dt
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_REGISTER = ROOT / "evidence/source_register.csv"
LIVENESS_REGISTER = ROOT / "evidence/external_source_liveness_register.csv"

REQUIRED_COLUMNS = [
    "source_id",
    "priority",
    "source_body",
    "title",
    "source_status",
    "url",
    "checked_at_utc",
    "check_method",
    "http_status",
    "outcome",
    "final_url",
    "content_type",
    "last_modified",
    "etag",
    "notes",
]

ALLOWED_OUTCOMES = {
    "reachable_http_ok",
    "redirected_reachable",
    "manual_review_required",
    "http_error",
    "network_error",
    "not_checked_no_url",
}

MAX_SNAPSHOT_AGE_DAYS = 60


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def read_header(path: Path) -> list[str]:
    with path.open(newline="", encoding="utf-8") as handle:
        return next(csv.reader(handle))


def parse_checked_date(value: str) -> dt.datetime | None:
    try:
        parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=dt.timezone.utc)
    return parsed.astimezone(dt.timezone.utc)


def priority_one_url_sources() -> dict[str, dict[str, str]]:
    return {
        row["source_id"]: row
        for row in read_csv(SOURCE_REGISTER)
        if row.get("priority") == "1_must" and row.get("url")
    }


def collect_errors() -> list[str]:
    errors: list[str] = []
    if not LIVENESS_REGISTER.exists():
        return ["missing evidence/external_source_liveness_register.csv"]

    header = read_header(LIVENESS_REGISTER)
    for column in REQUIRED_COLUMNS:
        if column not in header:
            errors.append(f"liveness register missing column: {column}")

    source_rows = priority_one_url_sources()
    liveness_rows = read_csv(LIVENESS_REGISTER)
    seen: dict[str, int] = {}
    now = dt.datetime.now(dt.timezone.utc)

    for line_number, row in enumerate(liveness_rows, start=2):
        source_id = row.get("source_id", "")
        seen[source_id] = seen.get(source_id, 0) + 1
        if source_id not in source_rows:
            errors.append(f"line {line_number}: unknown or non-priority source_id {source_id}")
        if row.get("outcome") not in ALLOWED_OUTCOMES:
            errors.append(f"line {line_number}: unsupported outcome {row.get('outcome')}")
        if not row.get("url"):
            errors.append(f"line {line_number}: missing URL")
        if row.get("url") and source_id in source_rows and row["url"] != source_rows[source_id]["url"]:
            errors.append(f"line {line_number}: URL drift for {source_id}")
        checked = parse_checked_date(row.get("checked_at_utc", ""))
        if checked is None:
            errors.append(f"line {line_number}: invalid checked_at_utc")
        elif now - checked > dt.timedelta(days=MAX_SNAPSHOT_AGE_DAYS):
            errors.append(f"line {line_number}: liveness snapshot older than {MAX_SNAPSHOT_AGE_DAYS} days")
        if row.get("outcome") in {"manual_review_required", "http_error", "network_error"} and not row.get("notes"):
            errors.append(f"line {line_number}: non-live outcome needs notes")
        if row.get("outcome") in {"reachable_http_ok", "redirected_reachable"} and not row.get("http_status"):
            errors.append(f"line {line_number}: reachable outcome missing HTTP status")

    for source_id in sorted(source_rows):
        if seen.get(source_id, 0) == 0:
            errors.append(f"missing liveness snapshot row for priority source: {source_id}")
        elif seen[source_id] > 1:
            errors.append(f"duplicate liveness snapshot rows for priority source: {source_id}")

    return errors


def main() -> int:
    errors = collect_errors()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    rows = read_csv(LIVENESS_REGISTER)
    counts: dict[str, int] = {}
    for row in rows:
        counts[row["outcome"]] = counts.get(row["outcome"], 0) + 1
    summary = ", ".join(f"{key}={counts[key]}" for key in sorted(counts))
    print(
        "External-source liveness/currentness metadata QA passed; "
        f"URL responses and refresh metadata are recorded only ({summary}). "
        "Evidence truth, legal correctness, source authority, content completeness, and WPL readiness are not checked."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
