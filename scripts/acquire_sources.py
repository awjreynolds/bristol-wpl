#!/usr/bin/env python3
"""Acquire seed and priority added sources into evidence/raw.

Network access is required to use this script. It avoids authored output PDFs:
all third-party PDFs are stored only under evidence/raw/**.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TODAY = dt.date.today().isoformat()

SOURCE_COLUMNS = [
    "source_id",
    "seed_doc_id",
    "priority",
    "workstream",
    "source_body",
    "title",
    "publication_date",
    "document_type",
    "url",
    "local_path",
    "status",
    "hierarchy_tier",
    "accessed_date",
    "sha256",
    "notes",
]

ACQUISITION_COLUMNS = ["source_id", "date", "action", "url", "status", "message"]

ADDED_SOURCES = [
    {
        "source_id": "SRC-LEG-0002",
        "priority": "1_must",
        "workstream": "statutory_and_business_case",
        "source_body": "UK legislation",
        "title": "Transport Act 2000 current contents",
        "publication_date": "current",
        "document_type": "html",
        "url": "https://www.legislation.gov.uk/ukpga/2000/38/contents",
        "hierarchy_tier": "1_current_legislation",
        "notes": "Current legislation spine for WPL powers.",
    },
    {
        "source_id": "SRC-LEG-0003",
        "priority": "1_must",
        "workstream": "statutory_and_business_case",
        "source_body": "UK legislation",
        "title": "Transport Act 2000 section 184 confirmation",
        "publication_date": "current",
        "document_type": "html",
        "url": "https://www.legislation.gov.uk/ukpga/2000/38/section/184",
        "hierarchy_tier": "1_current_legislation",
        "notes": "Confirmation route control.",
    },
    {
        "source_id": "SRC-LEG-0004",
        "priority": "1_must",
        "workstream": "statutory_and_business_case",
        "source_body": "UK legislation",
        "title": "Transport Act 2000 Schedule 12 net proceeds",
        "publication_date": "current",
        "document_type": "html",
        "url": "https://www.legislation.gov.uk/ukpga/2000/38/schedule/12",
        "hierarchy_tier": "1_current_legislation",
        "notes": "General plan and programme requirements for net proceeds.",
    },
    {
        "source_id": "SRC-LEG-0005",
        "priority": "1_must",
        "workstream": "statutory_and_business_case",
        "source_body": "UK legislation",
        "title": "Workplace Parking Levy (England) Regulations 2009",
        "publication_date": "2009",
        "document_type": "html",
        "url": "https://www.legislation.gov.uk/uksi/2009/2085/contents",
        "hierarchy_tier": "1_current_legislation",
        "notes": "Includes RPI-only variation exemption control.",
    },
    {
        "source_id": "SRC-LEG-0006",
        "priority": "1_must",
        "workstream": "statutory_and_business_case",
        "source_body": "UK legislation",
        "title": "Road User Charging and Workplace Parking Levy (Net Proceeds) (England) Regulations 2003",
        "publication_date": "2003",
        "document_type": "html",
        "url": "https://www.legislation.gov.uk/uksi/2003/110/contents",
        "hierarchy_tier": "1_current_legislation",
        "notes": "Net proceeds accounting control.",
    },
    {
        "source_id": "SRC-LEG-0007",
        "priority": "1_must",
        "workstream": "statutory_and_business_case",
        "source_body": "UK legislation",
        "title": "Road User Charging and WPL Classes of Motor Vehicles Regulations 2001",
        "publication_date": "2001",
        "document_type": "html",
        "url": "https://www.legislation.gov.uk/uksi/2001/2793/contents",
        "hierarchy_tier": "1_current_legislation",
        "notes": "Vehicle class control.",
    },
    {
        "source_id": "SRC-LEG-0008",
        "priority": "1_must",
        "workstream": "statutory_and_business_case",
        "source_body": "UK legislation",
        "title": "Road Traffic Regulation Act 1984 section 121A",
        "publication_date": "current",
        "document_type": "html",
        "url": "https://www.legislation.gov.uk/ukpga/1984/27/section/121A",
        "hierarchy_tier": "1_current_legislation",
        "notes": "Local traffic authority definition control.",
    },
    {
        "source_id": "SRC-LEG-0009",
        "priority": "1_must",
        "workstream": "weca_context",
        "source_body": "UK legislation",
        "title": "West of England Combined Authority Order 2017",
        "publication_date": "2017",
        "document_type": "html",
        "url": "https://www.legislation.gov.uk/uksi/2017/126/contents",
        "hierarchy_tier": "1_current_legislation",
        "notes": "WECA/MCA transport-function verification.",
    },
    {
        "source_id": "SRC-LEG-0010",
        "priority": "1_must",
        "workstream": "weca_context",
        "source_body": "UK legislation",
        "title": "SI 2026/519 regulation 29",
        "publication_date": "2026",
        "document_type": "html",
        "url": "https://www.legislation.gov.uk/uksi/2026/519/regulation/29",
        "hierarchy_tier": "1_current_legislation",
        "notes": "Potential WECA/MCA current-law change flagged by discovery.",
    },
    {
        "source_id": "SRC-HMT-0001",
        "priority": "1_must",
        "workstream": "statutory_and_business_case",
        "source_body": "HM Treasury",
        "title": "The Green Book 2026",
        "publication_date": "2026-02-05",
        "document_type": "html",
        "url": "https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-government/the-green-book-2026",
        "hierarchy_tier": "2_official_government_guidance",
        "notes": "Current Green Book metrics and appraisal controls.",
    },
    {
        "source_id": "SRC-HMT-0002",
        "priority": "1_must",
        "workstream": "statutory_and_business_case",
        "source_body": "HM Treasury",
        "title": "The Magenta Book",
        "publication_date": "current",
        "document_type": "html",
        "url": "https://www.gov.uk/government/publications/the-magenta-book",
        "hierarchy_tier": "2_official_government_guidance",
        "notes": "Evaluation guidance control.",
    },
    {
        "source_id": "SRC-HMT-0003",
        "priority": "1_must",
        "workstream": "statutory_and_business_case",
        "source_body": "HM Treasury",
        "title": "Managing Public Money",
        "publication_date": "current",
        "document_type": "html",
        "url": "https://www.gov.uk/government/publications/managing-public-money",
        "hierarchy_tier": "2_official_government_guidance",
        "notes": "Public money control.",
    },
    {
        "source_id": "SRC-HMT-0004",
        "priority": "1_must",
        "workstream": "statutory_and_business_case",
        "source_body": "HM Treasury",
        "title": "The Aqua Book",
        "publication_date": "current",
        "document_type": "html",
        "url": "https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government",
        "hierarchy_tier": "2_official_government_guidance",
        "notes": "Analytical assurance control.",
    },
    {
        "source_id": "SRC-DFT-0002",
        "priority": "1_must",
        "workstream": "statutory_and_business_case",
        "source_body": "Department for Transport",
        "title": "Transport analysis guidance",
        "publication_date": "current",
        "document_type": "html",
        "url": "https://www.gov.uk/guidance/transport-analysis-guidance",
        "hierarchy_tier": "2_official_government_guidance",
        "notes": "TAG landing page and current update control.",
    },
    {
        "source_id": "SRC-LEG-0011",
        "priority": "1_must",
        "workstream": "statutory_and_business_case",
        "source_body": "UK legislation",
        "title": "Workplace Parking Levy (England) Regulations 2009 whole instrument",
        "publication_date": "2009",
        "document_type": "html",
        "url": "https://www.legislation.gov.uk/uksi/2009/2085/made",
        "hierarchy_tier": "1_current_legislation",
        "notes": "Whole-instrument text for confirmation exemption, licensing charges and penalty enforcement controls.",
    },
    {
        "source_id": "SRC-LEG-0012",
        "priority": "1_must",
        "workstream": "statutory_and_business_case",
        "source_body": "UK legislation",
        "title": "Road User Charging and WPL Net Proceeds Regulations 2003 whole instrument",
        "publication_date": "2003",
        "document_type": "html",
        "url": "https://www.legislation.gov.uk/uksi/2003/110/made",
        "hierarchy_tier": "1_current_legislation",
        "notes": "Whole-instrument text for net proceeds accounting and deductions.",
    },
    {
        "source_id": "SRC-LEG-0013",
        "priority": "1_must",
        "workstream": "statutory_and_business_case",
        "source_body": "UK legislation",
        "title": "Road User Charging and WPL Classes of Motor Vehicles Regulations 2001 whole instrument",
        "publication_date": "2001",
        "document_type": "html",
        "url": "https://www.legislation.gov.uk/uksi/2001/2793/made",
        "hierarchy_tier": "1_current_legislation",
        "notes": "Whole-instrument text for vehicle-class controls relevant to any licensing scheme exclusions.",
    },
    {
        "source_id": "SRC-BCC-0022",
        "priority": "1_must",
        "workstream": "bristol_governance",
        "source_body": "Bristol City Council - Transport and Connectivity Policy Committee",
        "title": "Printed minutes - Transport and Connectivity Policy Committee 12 September 2024",
        "publication_date": "2024-09-12",
        "document_type": "pdf",
        "url": "https://democracy.bristol.gov.uk/documents/g11272/Printed%20minutes%2012th-Sep-2024%2017.00%20Transport%20Connectivity%20Policy%20Committee.pdf?T=1",
        "hierarchy_tier": "3_formal_public_body_source",
        "notes": "Minutes companion to the September 2024 WPL Stage One Development decision.",
    },
    {
        "source_id": "SRC-BCC-0023",
        "priority": "1_must",
        "workstream": "bristol_governance",
        "source_body": "Bristol City Council - Transport and Connectivity Policy Committee",
        "title": "Decision notice - Transport and Connectivity Policy Committee 23 October 2025",
        "publication_date": "2025-10-23",
        "document_type": "pdf",
        "url": "https://democracy.bristol.gov.uk/documents/g11586/Decisions%2023rd-Oct-2025%2017.00%20Transport%20Connectivity%20Policy%20Committee.pdf?T=2",
        "hierarchy_tier": "3_formal_public_body_source",
        "notes": "Decision notice needed to distinguish October 2025 WPL update from formal approval.",
    },
    {
        "source_id": "SRC-BCC-0024",
        "priority": "1_must",
        "workstream": "bristol_governance",
        "source_body": "Bristol City Council - Transport and Connectivity Policy Committee",
        "title": "Printed minutes - Transport and Connectivity Policy Committee 23 October 2025",
        "publication_date": "2025-10-23",
        "document_type": "pdf",
        "url": "https://democracy.bristol.gov.uk/documents/g11586/Printed%20minutes%2023rd-Oct-2025%2017.00%20Transport%20Connectivity%20Policy%20Committee.pdf?T=1",
        "hierarchy_tier": "3_formal_public_body_source",
        "notes": "Minutes companion for October 2025 WPL update meeting.",
    },
    {
        "source_id": "SRC-BCC-0025",
        "priority": "1_must",
        "workstream": "bristol_governance",
        "source_body": "Bristol City Council - Transport and Connectivity Policy Committee",
        "title": "Decision notice - Transport and Connectivity Policy Committee 19 March 2026",
        "publication_date": "2026-03-19",
        "document_type": "pdf",
        "url": "https://democracy.bristol.gov.uk/documents/g11589/Decisions%2019th-Mar-2026%2017.00%20Transport%20Connectivity%20Policy%20Committee.pdf?T=2",
        "hierarchy_tier": "3_formal_public_body_source",
        "notes": "Decision notice needed to verify March 2026 WPL update status.",
    },
    {
        "source_id": "SRC-BCC-0026",
        "priority": "1_must",
        "workstream": "bristol_governance",
        "source_body": "Bristol City Council - Transport and Connectivity Policy Committee",
        "title": "Printed minutes - Transport and Connectivity Policy Committee 19 March 2026",
        "publication_date": "2026-03-19",
        "document_type": "pdf",
        "url": "https://democracy.bristol.gov.uk/documents/g11589/Printed%20minutes%2019th-Mar-2026%2017.00%20Transport%20Connectivity%20Policy%20Committee.pdf?T=1",
        "hierarchy_tier": "3_formal_public_body_source",
        "notes": "Minutes companion for March 2026 WPL update meeting.",
    },
    {
        "source_id": "SRC-BCC-0027",
        "priority": "1_must",
        "workstream": "equalities_and_risk",
        "source_body": "Bristol City Council",
        "title": "Appendix B - Equality Impact Assessment - Workplace Parking Levy reviewed Oct 2025",
        "publication_date": "2025-10",
        "document_type": "pdf",
        "url": "https://democracy.bristol.gov.uk/documents/s124298/Appendix%20B%20-%20Equality%20Impact%20Assessment%20-%20Workplace%20Parking%20Levy%20reviewed%20Oct%202025.pdf",
        "hierarchy_tier": "3_formal_public_body_source",
        "notes": "March 2026 pack lists this as an EqIA appendix; compare with August 2024 and September 2025 EqIAs.",
    },
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, columns: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({column: row.get(column, "") for column in columns})


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def slug(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")[:90] or "source"


def raw_category(row: dict[str, str]) -> str:
    source_id = row.get("source_id", "")
    workstream = row.get("workstream", "")
    body = row.get("source_body", "").lower()
    if source_id.startswith("SRC-LEG"):
        return "legislation"
    if source_id.startswith("SRC-HMT"):
        return "hm-treasury"
    if source_id.startswith("SRC-DFT"):
        return "dft-and-tag"
    if "bristol" in body or source_id.startswith("SRC-BCC"):
        if "media" in workstream:
            return "media-and-advocacy"
        if "equality" in workstream:
            return "consultation-and-equality"
        return "bristol-city-council"
    if "west of england" in body or source_id.startswith("SRC-WECA"):
        return "west-of-england-mca"
    if source_id.startswith("SRC-NOTT"):
        return "nottingham"
    if source_id.startswith("SRC-ACADEMIC"):
        return "academic"
    if source_id.startswith("SRC-TFL") or "precedent" in workstream:
        return "uk-comparators"
    if "media" in workstream:
        return "media-and-advocacy"
    return "uk-comparators"


def extension_for(row: dict[str, str], content_type: str = "") -> str:
    url_path = urllib.parse.urlparse(row.get("url", "")).path.lower()
    normalized_content_type = content_type.lower()
    if "html" in normalized_content_type:
        return ".html"
    if "pdf" in normalized_content_type or url_path.endswith(".pdf") or row.get("document_type") == "pdf":
        return ".pdf"
    if url_path.endswith(".xlsx"):
        return ".xlsx"
    if url_path.endswith(".csv"):
        return ".csv"
    return ".html"


def raw_path(row: dict[str, str], content_type: str = "") -> Path:
    ext = extension_for(row, content_type)
    filename = Path(row.get("local_path", "")).name
    if not filename or "." not in filename:
        filename = f"{slug(row.get('title', row.get('source_id', 'source')))}{ext}"
    if not filename.endswith(ext):
        filename = f"{Path(filename).stem}{ext}"
    safe = f"{row['source_id'].lower()}_{slug(Path(filename).stem)}{ext}"
    return ROOT / "evidence" / "raw" / raw_category(row) / safe


def ensure_added_sources(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    existing = {row["source_id"] for row in rows}
    for source in ADDED_SOURCES:
        if source["source_id"] in existing:
            continue
        row = {column: "" for column in SOURCE_COLUMNS}
        row.update(source)
        row["seed_doc_id"] = "added-primary"
        row["local_path"] = raw_path(row).relative_to(ROOT).as_posix()
        row["status"] = "added_not_downloaded"
        rows.append(row)
    return rows


def download(row: dict[str, str], timeout: int) -> tuple[str, str, str]:
    request = urllib.request.Request(
        row["url"],
        headers={
            "User-Agent": "bristol-wpl-simulation/0.1 (source acquisition; no bypass)",
            "Accept": "*/*",
        },
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        content_type = response.headers.get("content-type", "")
        target = raw_path(row, content_type)
        target.parent.mkdir(parents=True, exist_ok=True)
        data = response.read()
        if not data:
            raise OSError(f"empty response content_type={content_type}")
        target.write_bytes(data)
        return target.relative_to(ROOT).as_posix(), content_type, sha256(target)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=0, help="Optional max number of rows to attempt")
    parser.add_argument("--priority", action="append", default=[], help="Priority filter, e.g. 1_must")
    parser.add_argument("--source-id", action="append", default=[], help="Attempt only listed source_id values")
    parser.add_argument("--force", action="store_true", help="Retry rows even if they are already marked downloaded")
    parser.add_argument("--timeout", type=int, default=45)
    parser.add_argument("--sleep", type=float, default=0.2)
    args = parser.parse_args()

    source_path = ROOT / "evidence/source_register.csv"
    acquisition_path = ROOT / "evidence/acquisition_log.csv"
    rows = ensure_added_sources(read_csv(source_path))
    acquisition_rows = read_csv(acquisition_path) if acquisition_path.exists() else []

    attempted = 0
    source_filter = set(args.source_id)
    for row in rows:
        if source_filter and row.get("source_id") not in source_filter:
            continue
        if args.priority and row.get("priority") not in args.priority:
            continue
        if not args.force and row.get("status") == "downloaded" and row.get("sha256"):
            continue
        if args.limit and attempted >= args.limit:
            break
        attempted += 1
        try:
            local_path, content_type, digest = download(row, args.timeout)
            row["local_path"] = local_path
            row["status"] = "downloaded"
            row["accessed_date"] = TODAY
            row["sha256"] = digest
            message = f"downloaded content_type={content_type} path={local_path}"
            status = "downloaded"
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, OSError) as exc:
            row["status"] = "download_failed"
            row["accessed_date"] = TODAY
            row["sha256"] = ""
            message = str(exc).replace("\n", " ")[:500]
            status = "download_failed"
        acquisition_rows.append(
            {
                "source_id": row["source_id"],
                "date": TODAY,
                "action": "download",
                "url": row.get("url", ""),
                "status": status,
                "message": message,
            }
        )
        print(row["source_id"], status, message)
        time.sleep(args.sleep)

    write_csv(source_path, SOURCE_COLUMNS, rows)
    write_csv(acquisition_path, ACQUISITION_COLUMNS, acquisition_rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
