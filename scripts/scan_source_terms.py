#!/usr/bin/env python3
"""Create a term-coverage scan over extracted evidence text."""

from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_REGISTER = ROOT / "evidence/source_register.csv"
TEXT_DIR = ROOT / "evidence/processed/text"
CSV_OUT = ROOT / "analysis/source_term_scan.csv"
MD_OUT = ROOT / "analysis/source_term_scan.md"

TERMS = [
    ("wpl", r"\bWPL\b|workplace parking levy"),
    ("bristol", r"\bBristol\b"),
    ("weca", r"\bWECA\b|West of England|Combined Authority|Mayoral Combined Authority"),
    ("obc", r"\bOBC\b|Outline Business Case"),
    ("fbc", r"\bFBC\b|Full Business Case"),
    ("clean_air_zone", r"Clean Air Zone|\bCAZ\b"),
    ("demand_management", r"demand management"),
    ("secretary_of_state", r"Secretary of State"),
    ("confirmation", r"confirmation|confirm"),
    ("net_proceeds", r"net proceeds"),
    ("variation", r"variation|vary"),
    ("revocation", r"revocation|revoke"),
    ("rpi", r"\bRPI\b|retail prices index|retail price index"),
    ("consultation", r"consultation|consult"),
    ("boundary", r"boundary|boundaries"),
    ("licensing", r"licen[cs]e|licen[cs]ing"),
    ("enforcement", r"enforcement|appeal"),
    ("parking_inventory", r"parking space|parking spaces|parking place|parking places|car park"),
]


def read_sources() -> dict[str, dict[str, str]]:
    with SOURCE_REGISTER.open(newline="", encoding="utf-8") as handle:
        return {row["source_id"]: row for row in csv.DictReader(handle)}


def count_terms(text: str) -> dict[str, int]:
    counts = {}
    for key, pattern in TERMS:
        counts[key] = len(re.findall(pattern, text, flags=re.IGNORECASE))
    return counts


def write_csv(rows: list[dict[str, str]]) -> None:
    columns = ["source_id", "title", "status", "text_path", "characters"] + [key for key, _ in TERMS]
    CSV_OUT.parent.mkdir(parents=True, exist_ok=True)
    with CSV_OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(rows: list[dict[str, str]]) -> None:
    top_wpl = sorted(rows, key=lambda row: int(row["wpl"]), reverse=True)[:15]
    top_weca = sorted(rows, key=lambda row: int(row["weca"]), reverse=True)[:12]
    legal = [row for row in rows if row["source_id"].startswith("SRC-LEG")]

    lines = [
        "# Source Term Scan",
        "",
        "Generated from extracted text under `evidence/processed/text`. Counts are triage aids, not substantive findings.",
        "",
        f"- Extracted sources scanned: {len(rows)}",
        f"- Sources with WPL references: {sum(1 for row in rows if int(row['wpl']) > 0)}",
        f"- Sources with WECA/Combined Authority references: {sum(1 for row in rows if int(row['weca']) > 0)}",
        "",
        "## Highest WPL Coverage",
        "",
        "| source_id | wpl | obc | fbc | consultation | boundary | licensing | title |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in top_wpl:
        lines.append(
            "| {source_id} | {wpl} | {obc} | {fbc} | {consultation} | {boundary} | {licensing} | {title} |".format(
                **row
            )
        )

    lines.extend(
        [
            "",
            "## Highest WECA / Combined Authority Coverage",
            "",
            "| source_id | weca | wpl | obc | fbc | title |",
            "| --- | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in top_weca:
        lines.append("| {source_id} | {weca} | {wpl} | {obc} | {fbc} | {title} |".format(**row))

    lines.extend(
        [
            "",
            "## Statutory Route Term Coverage",
            "",
            "| source_id | secretary_of_state | confirmation | net_proceeds | variation | revocation | rpi | title |",
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in legal:
        lines.append(
            "| {source_id} | {secretary_of_state} | {confirmation} | {net_proceeds} | {variation} | {revocation} | {rpi} | {title} |".format(
                **row
            )
        )

    MD_OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    sources = read_sources()
    rows: list[dict[str, str]] = []
    for text_path in sorted(TEXT_DIR.glob("*.txt")):
        source_id = text_path.stem
        text = text_path.read_text(encoding="utf-8", errors="replace")
        source = sources.get(source_id, {})
        counts = count_terms(text)
        row = {
            "source_id": source_id,
            "title": source.get("title", ""),
            "status": source.get("status", ""),
            "text_path": text_path.relative_to(ROOT).as_posix(),
            "characters": str(len(text)),
        }
        row.update({key: str(value) for key, value in counts.items()})
        rows.append(row)

    write_csv(rows)
    write_markdown(rows)
    print(f"Wrote {CSV_OUT.relative_to(ROOT)} and {MD_OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
