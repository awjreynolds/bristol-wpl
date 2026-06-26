#!/usr/bin/env python3
"""Refresh a live URL-status snapshot for source-register entries.

This script uses network access and is intentionally kept out of the default
offline validation path. It records HTTP reachability metadata only; it does
not download source bodies, verify content truth or prove source currentness.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import socket
import ssl
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_REGISTER = ROOT / "evidence/source_register.csv"
OUTPUT_REGISTER = ROOT / "evidence/external_source_liveness_register.csv"

OUTPUT_COLUMNS = [
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

USER_AGENT = "bristol-wpl-source-liveness-control/1.0"


@dataclass
class ProbeResult:
    method: str
    status: str
    final_url: str
    content_type: str
    last_modified: str
    etag: str
    error: str = ""


def read_sources(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def build_request(url: str, method: str) -> urllib.request.Request:
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "*/*",
    }
    if method == "GET":
        headers["Range"] = "bytes=0-0"
    return urllib.request.Request(url, headers=headers, method=method)


def probe(url: str, method: str, timeout: float) -> ProbeResult:
    request = build_request(url, method)
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return ProbeResult(
                method=method,
                status=str(response.status),
                final_url=response.geturl(),
                content_type=response.headers.get("Content-Type", ""),
                last_modified=response.headers.get("Last-Modified", ""),
                etag=response.headers.get("ETag", ""),
            )
    except urllib.error.HTTPError as exc:
        return ProbeResult(
            method=method,
            status=str(exc.code),
            final_url=exc.geturl(),
            content_type=exc.headers.get("Content-Type", ""),
            last_modified=exc.headers.get("Last-Modified", ""),
            etag=exc.headers.get("ETag", ""),
            error=str(exc.reason),
        )
    except (urllib.error.URLError, socket.timeout, TimeoutError, ssl.SSLError) as exc:
        return ProbeResult(
            method=method,
            status="",
            final_url=url,
            content_type="",
            last_modified="",
            etag="",
            error=str(getattr(exc, "reason", exc)),
        )


def classify(row: dict[str, str], result: ProbeResult) -> tuple[str, str]:
    if not row.get("url"):
        return "not_checked_no_url", "Source register row has no URL."
    if not result.status:
        return "network_error", f"Network probe failed: {result.error}"
    try:
        status = int(result.status)
    except ValueError:
        return "network_error", f"Unexpected HTTP status: {result.status}"
    if 200 <= status < 400:
        if result.final_url and result.final_url != row["url"]:
            return "redirected_reachable", "HTTP status was reachable but URL resolves via redirect."
        return "reachable_http_ok", "HTTP status indicates the endpoint was reachable."
    if status in {401, 403, 429}:
        return "manual_review_required", "Endpoint responded but access/rate policy prevents liveness certainty."
    return "http_error", f"Endpoint returned HTTP {status}; source may need reacquisition or replacement."


def check_url(url: str, timeout: float) -> ProbeResult:
    head = probe(url, "HEAD", timeout)
    if head.status:
        try:
            if 200 <= int(head.status) < 400:
                return head
        except ValueError:
            pass
    get = probe(url, "GET", timeout)
    if get.status or not head.status:
        return get
    return head


def make_output_row(row: dict[str, str], checked_at: str, result: ProbeResult) -> dict[str, str]:
    outcome, notes = classify(row, result)
    return {
        "source_id": row.get("source_id", ""),
        "priority": row.get("priority", ""),
        "source_body": row.get("source_body", ""),
        "title": row.get("title", ""),
        "source_status": row.get("status", ""),
        "url": row.get("url", ""),
        "checked_at_utc": checked_at,
        "check_method": result.method,
        "http_status": result.status,
        "outcome": outcome,
        "final_url": result.final_url,
        "content_type": result.content_type,
        "last_modified": result.last_modified,
        "etag": result.etag,
        "notes": notes,
    }


def write_rows(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-register", default=SOURCE_REGISTER)
    parser.add_argument("--output", default=OUTPUT_REGISTER)
    parser.add_argument("--priority", action="append", default=["1_must"])
    parser.add_argument("--timeout", type=float, default=12.0)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    source_path = Path(args.source_register)
    output_path = Path(args.output)
    priorities = set(args.priority)
    sources = [row for row in read_sources(source_path) if row.get("priority") in priorities and row.get("url")]
    if args.limit is not None:
        sources = sources[: args.limit]

    checked_at = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    rows = []
    for row in sources:
        result = check_url(row["url"], args.timeout)
        rows.append(make_output_row(row, checked_at, result))

    if args.write:
        write_rows(output_path, rows)

    counts: dict[str, int] = {}
    for row in rows:
        counts[row["outcome"]] = counts.get(row["outcome"], 0) + 1
    print(f"Checked {len(rows)} source URLs")
    for outcome in sorted(counts):
        print(f"{outcome}: {counts[outcome]}")
    if not args.write:
        print("Dry run only; pass --write to update evidence/external_source_liveness_register.csv")
    print("HTTP reachability only; content truth, legal correctness and WPL readiness not checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
