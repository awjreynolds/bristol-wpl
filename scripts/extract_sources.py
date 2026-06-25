#!/usr/bin/env python3
"""Extract text from acquired source files.

The extractor is deliberately conservative. It records failures in an
extraction log and never fabricates source text. PDF extraction uses the local
pdftotext binary when available; HTML extraction uses only standard-library
parsing suitable for evidence triage, not final legal quotation.
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import re
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TODAY = date.today().isoformat()

SOURCE_REGISTER = ROOT / "evidence/source_register.csv"
TEXT_DIR = ROOT / "evidence/processed/text"
METADATA_DIR = ROOT / "evidence/processed/metadata"
LOG_PATH = ROOT / "evidence/extraction_log.csv"
MANIFEST_PATH = ROOT / "evidence/extraction_manifest.csv"

LOG_COLUMNS = [
    "source_id",
    "date",
    "source_path",
    "output_path",
    "status",
    "quality",
    "method",
    "characters",
    "message",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, columns: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        for row in rows:
            writer.writerow({column: row.get(column, "") for column in columns})


def clean_text(text: str) -> str:
    text = text.replace("\x00", " ")
    text = re.sub(r"[ \t\r\f\v]+", " ", text)
    text = re.sub(r"\n[ \t]+", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + ("\n" if text.strip() else "")


def decode_bytes(data: bytes) -> str:
    for encoding in ("utf-8", "utf-8-sig", "cp1252", "latin-1"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            continue
    return data.decode("utf-8", errors="replace")


def html_to_text(path: Path) -> str:
    raw = decode_bytes(path.read_bytes())
    raw = re.sub(r"(?is)<script\b.*?</script>", " ", raw)
    raw = re.sub(r"(?is)<style\b.*?</style>", " ", raw)
    raw = re.sub(r"(?is)<noscript\b.*?</noscript>", " ", raw)
    raw = re.sub(r"(?i)<br\s*/?>", "\n", raw)
    raw = re.sub(r"(?i)</(p|div|section|article|header|footer|li|tr|h[1-6])>", "\n", raw)
    raw = re.sub(r"(?s)<[^>]+>", " ", raw)
    return clean_text(html.unescape(raw))


def plain_text(path: Path) -> str:
    return clean_text(decode_bytes(path.read_bytes()))


def assess_quality(text: str) -> str:
    stripped = text.strip()
    lowered = stripped.lower()
    if lowered in {"loading", "loading..."} or lowered.endswith("\nloading"):
        return "script_hydrated_or_placeholder"
    if len(stripped) < 200:
        return "low_content"
    words = re.findall(r"[A-Za-z]{2,}", stripped)
    if len(words) < 50:
        return "low_content"
    return "usable"


def sniff_file(path: Path) -> str:
    prefix = path.read_bytes()[:512].lstrip().lower()
    if prefix.startswith(b"%pdf"):
        return "pdf"
    if prefix.startswith((b"<!doctype html", b"<html")) or b"<html" in prefix[:200]:
        return "html"
    return "unknown"


def pdf_to_text(path: Path) -> tuple[str, str]:
    pdftotext = shutil.which("pdftotext")
    if not pdftotext:
        raise RuntimeError("pdftotext is not available")
    result = subprocess.run(
        [pdftotext, "-layout", "-enc", "UTF-8", str(path), "-"],
        check=False,
        capture_output=True,
        text=True,
        timeout=180,
    )
    if result.returncode != 0:
        message = (result.stderr or result.stdout or "pdftotext failed").strip()
        raise RuntimeError(message[:500])
    return clean_text(result.stdout), "pdftotext-layout"


def extract_one(row: dict[str, str]) -> dict[str, str]:
    source_id = row.get("source_id", "")
    local_path = row.get("local_path", "")
    source_path = ROOT / local_path if local_path else Path()
    output_path = TEXT_DIR / f"{source_id}.txt"
    metadata_path = METADATA_DIR / f"{source_id}.json"

    log_row = {
        "source_id": source_id,
        "date": TODAY,
        "source_path": local_path,
        "output_path": output_path.relative_to(ROOT).as_posix(),
        "status": "",
        "quality": "",
        "method": "",
        "characters": "0",
        "message": "",
    }

    if row.get("status") != "downloaded":
        log_row["status"] = "skipped_download_failed" if row.get("status") == "download_failed" else "skipped_not_downloaded"
        log_row["quality"] = "not_assessed"
        log_row["message"] = f"source status is {row.get('status', '')}"
        return log_row
    if not local_path or not source_path.exists():
        log_row["status"] = "missing_source_file"
        log_row["quality"] = "not_assessed"
        log_row["message"] = "local_path missing or file does not exist"
        return log_row

    try:
        suffix = source_path.suffix.lower()
        sniffed_type = sniff_file(source_path)
        if suffix == ".pdf" and sniffed_type == "html":
            text, method = html_to_text(source_path), "html-sniffed-from-pdf-extension"
        elif suffix == ".pdf":
            text, method = pdf_to_text(source_path)
        elif suffix in {".html", ".htm"}:
            text, method = html_to_text(source_path), "html-standard-library"
        elif suffix in {".txt", ".csv", ".json", ".xml"}:
            text, method = plain_text(source_path), "plain-text"
        else:
            log_row["status"] = "skipped_unsupported_type"
            log_row["quality"] = "not_assessed"
            log_row["message"] = f"unsupported suffix {suffix or '(none)'}"
            return log_row

        TEXT_DIR.mkdir(parents=True, exist_ok=True)
        METADATA_DIR.mkdir(parents=True, exist_ok=True)
        output_path.write_text(text, encoding="utf-8")
        metadata_path.write_text(
            json.dumps(
                {
                    "source_id": source_id,
                    "source_path": local_path,
                    "output_path": output_path.relative_to(ROOT).as_posix(),
                    "extracted_date": TODAY,
                    "method": method,
                    "characters": len(text),
                    "source_status": row.get("status", ""),
                    "sha256": row.get("sha256", ""),
                    "title": row.get("title", ""),
                    "url": row.get("url", ""),
                },
                indent=2,
                sort_keys=True,
            )
            + "\n",
            encoding="utf-8",
        )
        log_row["status"] = "extracted"
        log_row["quality"] = assess_quality(text)
        log_row["method"] = method
        log_row["characters"] = str(len(text))
        log_row["message"] = "ok" if log_row["quality"] == "usable" else f"extracted with quality={log_row['quality']}"
    except (OSError, RuntimeError, subprocess.TimeoutExpired) as exc:
        log_row["status"] = "extract_failed"
        log_row["quality"] = "not_assessed"
        log_row["message"] = str(exc).replace("\n", " ")[:500]
    return log_row


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=0, help="Optional max number of rows to inspect")
    parser.add_argument("--source-id", action="append", default=[], help="Extract only listed source_id values")
    args = parser.parse_args()

    rows = read_csv(SOURCE_REGISTER)
    existing_log = read_csv(LOG_PATH)
    source_filter = set(args.source_id)
    new_log_rows: list[dict[str, str]] = []

    inspected = 0
    for row in rows:
        if source_filter and row.get("source_id") not in source_filter:
            continue
        if args.limit and inspected >= args.limit:
            break
        inspected += 1
        result = extract_one(row)
        new_log_rows.append(result)
        print(
            result["source_id"],
            result["status"],
            result.get("method", ""),
            result.get("characters", "0"),
            result.get("message", ""),
        )

    write_csv(LOG_PATH, LOG_COLUMNS, existing_log + new_log_rows)
    write_csv(MANIFEST_PATH, LOG_COLUMNS, new_log_rows)

    failures = [row for row in new_log_rows if row["status"] in {"missing_source_file", "extract_failed"}]
    if failures:
        print(f"Extraction completed with {len(failures)} hard failures", file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
