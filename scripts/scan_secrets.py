#!/usr/bin/env python3
"""Secret-pattern scanner with redacted output.

This is intentionally small and dependency-free so public-release checks do not
depend on a locally installed scanner. It is not a replacement for hosted secret
scanning, but it catches the detector families that have already affected this
repo and refuses to print matched values.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
import sys
import zipfile
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAX_FILE_BYTES = 60_000_000

SKIP_DIRS = {
    ".git",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".venv",
    "__pycache__",
    "venv",
}


@dataclass(frozen=True)
class Rule:
    rule_id: str
    pattern: re.Pattern[bytes]


@dataclass(frozen=True)
class Finding:
    location: str
    line: int
    rule_id: str
    length: int
    digest: str


RULES = [
    Rule("grafana_service_account_token", re.compile(rb"glsa_[A-Za-z0-9_-]{20,}")),
    Rule("grafana_cloud_token", re.compile(rb"glc_[A-Za-z0-9_-]{20,}")),
    # Legacy Grafana API keys and Power BI embed IDs share this base64 prefix.
    # In a public repo, either should be removed or redacted to avoid leaking
    # credentials and to avoid noisy hosted secret-scanning alerts.
    Rule("grafana_legacy_or_powerbi_collision", re.compile(rb"eyJrIjoi[A-Za-z0-9_./+=-]{20,}")),
    Rule("bearer_authorization_header", re.compile(rb"Authorization:[ \t]*Bearer[ \t]+[A-Za-z0-9_./+=:-]{16,}", re.I)),
]


def rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def should_skip(path: Path) -> bool:
    return any(part in SKIP_DIRS for part in path.parts)


def iter_files(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if should_skip(path):
            continue
        if path.is_file():
            files.append(path)
        elif path.is_dir():
            for child in path.rglob("*"):
                if child.is_file() and not should_skip(child):
                    files.append(child)
    return files


def scan_bytes(location: str, data: bytes) -> list[Finding]:
    findings: list[Finding] = []
    for rule in RULES:
        for match in rule.pattern.finditer(data):
            secret = match.group(0)
            findings.append(
                Finding(
                    location=location,
                    line=data.count(b"\n", 0, match.start()) + 1,
                    rule_id=rule.rule_id,
                    length=len(secret),
                    digest=hashlib.sha256(secret).hexdigest()[:16],
                )
            )
    return findings


def read_file(path: Path) -> bytes | None:
    try:
        if path.stat().st_size > MAX_FILE_BYTES:
            return None
        return path.read_bytes()
    except OSError:
        return None


def scan_file(path: Path) -> list[Finding]:
    data = read_file(path)
    if data is None:
        return []
    findings = scan_bytes(rel(path), data)
    if path.suffix.lower() == ".zip":
        findings.extend(scan_zip(path, data))
    return findings


def scan_zip(path: Path, data: bytes) -> list[Finding]:
    findings: list[Finding] = []
    try:
        with zipfile.ZipFile(path) as archive:
            for info in archive.infolist():
                if info.is_dir() or info.file_size > MAX_FILE_BYTES:
                    continue
                try:
                    inner = archive.read(info)
                except (KeyError, OSError, RuntimeError, zipfile.BadZipFile):
                    continue
                findings.extend(scan_bytes(f"{rel(path)}::{info.filename}", inner))
    except zipfile.BadZipFile:
        return findings
    return findings


def scan_history() -> list[Finding]:
    rev_list = subprocess.run(
        ["git", "rev-list", "--objects", "--all"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    if rev_list.returncode != 0:
        print("ERROR: unable to enumerate git history", file=sys.stderr)
        return [Finding("git-history", 0, "history_scan_failed", 0, "")]

    findings: list[Finding] = []
    seen: set[str] = set()
    for line in rev_list.stdout.splitlines():
        if not line.strip():
            continue
        object_id, _, name = line.partition(" ")
        if object_id in seen:
            continue
        seen.add(object_id)
        type_result = subprocess.run(
            ["git", "cat-file", "-t", object_id],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        if type_result.stdout.strip() != "blob":
            continue
        size_result = subprocess.run(
            ["git", "cat-file", "-s", object_id],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        try:
            size = int(size_result.stdout.strip())
        except ValueError:
            continue
        if size > MAX_FILE_BYTES:
            continue
        blob = subprocess.run(
            ["git", "cat-file", "-p", object_id],
            cwd=ROOT,
            check=False,
            capture_output=True,
        )
        if blob.returncode != 0:
            continue
        location = f"git:{object_id}:{name or '(unnamed blob)'}"
        findings.extend(scan_bytes(location, blob.stdout))
    return findings


def print_findings(findings: list[Finding]) -> None:
    for finding in findings:
        print(
            f"ERROR: secret-like pattern {finding.rule_id} at "
            f"{finding.location}:{finding.line} "
            f"len={finding.length} sha256={finding.digest}"
        )


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan repo files for secret-like tokens without printing values.")
    parser.add_argument("paths", nargs="*", help="Files or directories to scan; defaults to the repository root.")
    parser.add_argument("--all-history", action="store_true", help="Scan all reachable git blobs as well as current files.")
    args = parser.parse_args()

    paths = [Path(path) for path in args.paths] if args.paths else [ROOT]
    findings: list[Finding] = []
    for path in iter_files(paths):
        findings.extend(scan_file(path))
    if args.all_history:
        findings.extend(scan_history())

    if findings:
        print_findings(findings)
        return 1
    print("Secret scan passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
