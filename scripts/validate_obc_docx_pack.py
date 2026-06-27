#!/usr/bin/env python3
from __future__ import annotations

import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.validate_registers import check_no_authored_pdfs

PACK_DIR = ROOT / "business_case" / "obc" / "docx-pack"
ZIP_PATH = PACK_DIR / "bristol-wpl-obc-document-pack.zip"
MANIFEST_PATH = PACK_DIR / "PACK-MANIFEST.txt"

REQUIRED_DOCX = [
    "bristol-wpl-obc-simulation-release.docx",
    "bristol-wpl-obc-reader-support-guide.docx",
    "bristol-wpl-obc-risk-process-control-summary.docx",
]

REQUIRED_FILES = [*REQUIRED_DOCX, "PACK-MANIFEST.txt", "bristol-wpl-obc-document-pack.zip"]

REQUIRED_DOCX_PHRASES = {
    "bristol-wpl-obc-simulation-release.docx": [
        "OBC Simulation Release",
        "not an approved OBC",
        "not for real-world reliance",
        "Stage 7 OBC gate remains blocked",
    ],
    "bristol-wpl-obc-reader-support-guide.docx": [
        "OBC Reader Support Guide",
        "not approve a Bristol Workplace Parking Levy",
        "Safe statements and prohibited inferences",
    ],
    "bristol-wpl-obc-risk-process-control-summary.docx": [
        "OBC Risk, Process And Control Summary",
        "Current no-go position",
        "Priority blockers",
        "OBC gate checklist summary",
    ],
}

REQUIRED_MANIFEST_PHRASES = [
    "Stage 35A simulation-only officer-friendly distribution pack",
    "Not an approved Bristol OBC.",
    "Not officer advice.",
    "Not consultation material.",
]


def docx_text(path: Path) -> str:
    with zipfile.ZipFile(path) as archive:
        xml = archive.read("word/document.xml")
    root = ET.fromstring(xml)
    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    return " ".join(node.text or "" for node in root.findall(".//w:t", ns))


def collect_errors() -> list[str]:
    errors: list[str] = []
    if not PACK_DIR.exists():
        return [f"missing OBC DOCX pack directory: {PACK_DIR.relative_to(ROOT)}"]

    for name in REQUIRED_FILES:
        path = PACK_DIR / name
        if not path.exists():
            errors.append(f"missing OBC DOCX pack file: {path.relative_to(ROOT)}")

    for path in PACK_DIR.iterdir():
        if path.suffix.lower() in {".pdf", ".md"}:
            errors.append(f"officer-facing OBC DOCX pack must not contain {path.suffix}: {path.relative_to(ROOT)}")

    if ZIP_PATH.exists():
        with zipfile.ZipFile(ZIP_PATH) as archive:
            names = set(archive.namelist())
        expected = set(REQUIRED_DOCX + ["PACK-MANIFEST.txt"])
        if names != expected:
            errors.append(f"OBC DOCX ZIP contents mismatch: expected {sorted(expected)}, got {sorted(names)}")
        for name in names:
            if name.lower().endswith((".pdf", ".md")):
                errors.append(f"OBC DOCX ZIP must not include {name}")

    if MANIFEST_PATH.exists():
        manifest = MANIFEST_PATH.read_text(encoding="utf-8")
        for phrase in REQUIRED_MANIFEST_PHRASES:
            if phrase not in manifest:
                errors.append(f"PACK-MANIFEST.txt missing phrase: {phrase}")

    for name, phrases in REQUIRED_DOCX_PHRASES.items():
        path = PACK_DIR / name
        if not path.exists():
            continue
        text = docx_text(path)
        for phrase in phrases:
            if phrase not in text:
                errors.append(f"{name} missing DOCX phrase: {phrase}")

    errors.extend(check_no_authored_pdfs(ROOT))
    return errors


def main() -> int:
    errors = collect_errors()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("OBC DOCX pack QA passed; DOCX pack is simulation-only and not officer reliance")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
