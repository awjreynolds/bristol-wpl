#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

EXPECTED_CLAIM_IDS = {f"CLM-{number:04d}" for number in range(1, 39)}

REQUIRED_FILES = [
    "analysis/context/stage-16a-claim-summary-control-context.md",
    "evidence/claim_summaries/README.md",
    "evidence/claim_summaries/claim-summary-register.csv",
    "evidence/claim_summaries/claim-summary-no-go-register.csv",
    "docs/stages/stage-16a-claim-summary-control.md",
    "review/peer_review/stage-16a-claim-summary-control-review.md",
    "review/stage_gate_reports/stage-16a-claim-summary-control-report.md",
]

REGISTER_COLUMNS = [
    "claim_id",
    "summary_stage",
    "summary_path",
    "materiality",
    "claim_type",
    "reviewer",
    "review_status",
    "source_ids",
    "source_id_count",
    "summary_status",
    "no_go_note",
]

NO_GO_COLUMNS = [
    "claim_id",
    "prohibited_claim",
    "allowed_wording",
    "current_status",
    "gate_effect",
]

REQUIRED_NO_GO_CLAIMS = {
    "claim summary means claim is true",
    "claim summary means OBC or FBC evidence is complete",
    "claim summary replaces legal advice",
    "claim summary closes WPL readiness gates",
    "claim summary can be cited instead of the source",
    "claim summary means source is current",
}

REQUIRED_SUMMARY_PHRASES = [
    "Simulation-only claim summary",
    "Stage 16A current-claim-matrix coverage",
    "What This Claim Can Support",
    "What This Claim Must Not Be Used To Claim",
    "Does not prove the claim is true beyond the recorded simulated review status",
    "Does not replace the underlying source, source note, source-location check or later human professional review",
    "Does not close any WPL readiness gate",
    "Cite the underlying source IDs and source locations, not this summary alone",
    "Recheck source currentness before real-world reliance or external publication",
    "Treat missing or synthetic source locations as gaps",
]

LEGAL_CLAIM_IDS = {
    "CLM-0001",
    "CLM-0002",
    "CLM-0003",
    "CLM-0004",
    "CLM-0005",
    "CLM-0010",
    "CLM-0011",
    "CLM-0012",
    "CLM-0013",
    "CLM-0014",
    "CLM-0015",
    "CLM-0016",
    "CLM-0017",
    "CLM-0018",
    "CLM-0020",
    "CLM-0021",
    "CLM-0028",
    "CLM-0038",
}

APPRAISAL_CLAIM_IDS = {
    "CLM-0009",
    "CLM-0019",
    "CLM-0022",
    "CLM-0024",
    "CLM-0038",
}

COMPARATOR_CLAIM_IDS = {
    "CLM-0008",
    "CLM-0038",
}

CONTROL_OR_BLANK_SOURCE_PHRASE = "No direct source IDs in the claim matrix"

NAV_PHRASES = {
    "README.md": [
        "Stage 16A",
        "claim summaries",
        "claim-level source-summary",
    ],
    "docs/stages/README.md": [
        "Stage 16A",
        "claim-summary control",
    ],
    "docs/officer/assurance-dashboard.md": [
        "Claim summaries",
        "claim truth",
    ],
    "docs/public/README.md": [
        "claim summaries",
        "do not prove",
    ],
    "review/stage_gate_reports/stage-16a-claim-summary-control-report.md": [
        "Accepted for Stage 16A claim-summary control purposes only",
        "does not verify claim truth",
        "EG-0045",
    ],
}

UNSAFE_POSITIVE_PHRASES = [
    "claim verified",
    "evidence complete",
    "source note proves",
    "source is current",
    "legal clearance",
    "legal sign-off",
    "WECA/MCA approval",
    "DfT acceptance",
    "Secretary of State ready",
    "OBC ready",
    "FBC ready",
    "consultation ready",
    "statutory submission ready",
    "implementation ready",
    "Nottingham transferability proven",
    "Green Book compliant",
    "TAG compliant",
    "BCR established",
    "VFM category confirmed",
    "all blockers closed",
]


def read_rows(rel: str) -> list[dict[str, str]]:
    with (ROOT / rel).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def read_header(rel: str) -> list[str]:
    with (ROOT / rel).open(newline="", encoding="utf-8") as handle:
        return next(csv.reader(handle))


def split_ids(value: str) -> list[str]:
    return [item.strip() for item in value.split(";") if item.strip()]


def claim_rows() -> dict[str, dict[str, str]]:
    return {row["claim_id"]: row for row in read_rows("evidence/claim_evidence_matrix.csv")}


def source_register_ids() -> set[str]:
    return {row["source_id"] for row in read_rows("evidence/source_register.csv")}


def source_note_coverage_ids() -> set[str]:
    return {row["source_id"] for row in read_rows("evidence/source_notes/source-note-coverage-register.csv")}


def check_required_files() -> list[str]:
    return [f"missing Stage 16A file: {rel}" for rel in REQUIRED_FILES if not (ROOT / rel).exists()]


def check_csv_widths(rel: str) -> list[str]:
    errors = []
    with (ROOT / rel).open(newline="", encoding="utf-8") as handle:
        reader = csv.reader(handle)
        try:
            header = next(reader)
        except StopIteration:
            return [f"{rel} is empty"]
        expected = len(header)
        for line_number, row in enumerate(reader, start=2):
            if len(row) != expected:
                errors.append(f"{rel}:{line_number} has {len(row)} fields; expected {expected}")
    return errors


def check_csv_headers() -> list[str]:
    errors = []
    for rel, columns in {
        "evidence/claim_summaries/claim-summary-register.csv": REGISTER_COLUMNS,
        "evidence/claim_summaries/claim-summary-no-go-register.csv": NO_GO_COLUMNS,
    }.items():
        if not (ROOT / rel).exists():
            errors.append(f"missing Stage 16A CSV: {rel}")
            continue
        header = read_header(rel)
        for column in columns:
            if column not in header:
                errors.append(f"{rel} missing column {column}")
        errors.extend(check_csv_widths(rel))
    return errors


def check_claim_matrix_scope() -> list[str]:
    rows = claim_rows()
    errors = []
    ids = set(rows)
    if ids != EXPECTED_CLAIM_IDS:
        errors.append(
            "evidence/claim_evidence_matrix.csv Stage 16A scope must be exactly CLM-0001 through CLM-0038"
        )
        for claim_id in sorted(EXPECTED_CLAIM_IDS - ids):
            errors.append(f"claim matrix missing required Stage 16A claim {claim_id}")
        for claim_id in sorted(ids - EXPECTED_CLAIM_IDS):
            errors.append(f"claim matrix has out-of-scope Stage 16A claim {claim_id}")
    for claim_id, row in rows.items():
        if row.get("review_status") not in {"verified_simulation", "verified_simulation_synthesis"}:
            errors.append(f"{claim_id} has unsupported review_status {row.get('review_status')}")
    return errors


def check_summary_register() -> list[str]:
    errors = []
    rows = read_rows("evidence/claim_summaries/claim-summary-register.csv")
    claims = claim_rows()
    by_claim = {}
    source_ids = source_register_ids()
    coverage_ids = source_note_coverage_ids()

    for row in rows:
        claim_id = row.get("claim_id", "")
        if claim_id in by_claim:
            errors.append(f"duplicate claim-summary register row for {claim_id}")
        by_claim[claim_id] = row

    ids = set(by_claim)
    if ids != EXPECTED_CLAIM_IDS:
        for claim_id in sorted(EXPECTED_CLAIM_IDS - ids):
            errors.append(f"claim-summary register missing {claim_id}")
        for claim_id in sorted(ids - EXPECTED_CLAIM_IDS):
            errors.append(f"claim-summary register has out-of-scope claim {claim_id}")

    for claim_id in sorted(EXPECTED_CLAIM_IDS):
        row = by_claim.get(claim_id)
        claim = claims.get(claim_id)
        if not row or not claim:
            continue
        if row.get("summary_stage") != "Stage 16A":
            errors.append(f"{claim_id} summary_stage must be Stage 16A")
        if row.get("summary_status") != "stage_16a_summary_created":
            errors.append(f"{claim_id} summary_status must be stage_16a_summary_created")
        if row.get("review_status") != claim.get("review_status"):
            errors.append(f"{claim_id} summary review_status must match claim matrix")
        if row.get("reviewer") != claim.get("reviewer"):
            errors.append(f"{claim_id} summary reviewer must match claim matrix")
        if row.get("source_ids") != claim.get("source_ids"):
            errors.append(f"{claim_id} summary source_ids must match claim matrix exactly")
        expected_count = len(split_ids(claim.get("source_ids", "")))
        if row.get("source_id_count") != str(expected_count):
            errors.append(f"{claim_id} source_id_count must be {expected_count}")
        path = row.get("summary_path", "")
        expected_path = f"evidence/claim_summaries/summaries/{claim_id.lower()}.md"
        if path != expected_path:
            errors.append(f"{claim_id} summary_path must be {expected_path}")
        if "Does not close any WPL readiness gate" not in row.get("no_go_note", ""):
            errors.append(f"{claim_id} missing readiness-gate no-go note")
        for source_id in split_ids(row.get("source_ids", "")):
            if source_id not in source_ids:
                errors.append(f"{claim_id} uses source_id absent from source_register.csv: {source_id}")
            if source_id not in coverage_ids:
                errors.append(f"{claim_id} uses source_id without source-note coverage: {source_id}")
    return errors


def check_summary_files() -> list[str]:
    errors = []
    claims = claim_rows()
    for claim_id, claim in sorted(claims.items()):
        path = ROOT / "evidence/claim_summaries/summaries" / f"{claim_id.lower()}.md"
        if not path.exists():
            errors.append(f"missing claim summary file: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        for phrase in REQUIRED_SUMMARY_PHRASES:
            if phrase not in text:
                errors.append(f"{path.relative_to(ROOT)} missing required phrase: {phrase}")
        if claim.get("claim_text", "") not in text:
            errors.append(f"{path.relative_to(ROOT)} missing exact claim text")
        if f"Review status: `{claim.get('review_status')}`" not in text:
            errors.append(f"{path.relative_to(ROOT)} missing matrix review_status")
        if f"Reviewer: `{claim.get('reviewer')}`" not in text:
            errors.append(f"{path.relative_to(ROOT)} missing matrix reviewer")
        if f"Last verified: `{claim.get('last_verified')}`" not in text:
            errors.append(f"{path.relative_to(ROOT)} missing matrix last_verified")
        sources = split_ids(claim.get("source_ids", ""))
        if sources:
            for source_id in sources:
                if f"`{source_id}`" not in text:
                    errors.append(f"{path.relative_to(ROOT)} missing source_id {source_id}")
        elif CONTROL_OR_BLANK_SOURCE_PHRASE not in text:
            errors.append(f"{path.relative_to(ROOT)} missing blank-source control phrase")
        if claim_id in LEGAL_CLAIM_IDS and "Does not provide legal advice or settle Bristol order-maker" not in text:
            errors.append(f"{path.relative_to(ROOT)} missing legal/governance no-go phrase")
        if claim_id in APPRAISAL_CLAIM_IDS and "Does not prove Green Book or TAG compliance" not in text:
            errors.append(f"{path.relative_to(ROOT)} missing appraisal no-go phrase")
        if claim_id in COMPARATOR_CLAIM_IDS and "without Bristol-specific transferability evidence" not in text:
            errors.append(f"{path.relative_to(ROOT)} missing comparator transferability no-go phrase")
        if claim_id == "CLM-0038" and "does not verify claims" not in text:
            errors.append(f"{path.relative_to(ROOT)} must preserve source-note coverage limitation")
        for phrase in UNSAFE_POSITIVE_PHRASES:
            pattern = re.compile(rf"(?<!not )(?<!no )(?<!Does not )\\b{re.escape(phrase)}\\b", re.IGNORECASE)
            if pattern.search(text):
                errors.append(f"{path.relative_to(ROOT)} contains unsafe positive phrase: {phrase}")
    return errors


def check_no_go_register() -> list[str]:
    errors = []
    rows = read_rows("evidence/claim_summaries/claim-summary-no-go-register.csv")
    claims = {row["prohibited_claim"] for row in rows}
    for claim in sorted(REQUIRED_NO_GO_CLAIMS - claims):
        errors.append(f"claim-summary no-go register missing prohibited claim: {claim}")
    for row in rows:
        if row.get("current_status") != "blocked":
            errors.append(f"{row.get('claim_id')} must remain blocked")
    return errors


def check_register_statuses() -> list[str]:
    errors = []
    gaps = {row["gap_id"]: row for row in read_rows("evidence/evidence_gap_register.csv")}
    issues = {row["issue_id"]: row for row in read_rows("governance/issues_register.csv")}
    risks = {row["risk_id"]: row for row in read_rows("governance/risk_register.csv")}
    pitfalls = {row["pitfall_id"]: row for row in read_rows("governance/pitfalls_register.csv")}
    if gaps.get("EG-0044", {}).get("status") != "partially_closed_stage_16a":
        errors.append("EG-0044 must be partially_closed_stage_16a after current-matrix summaries are created")
    if gaps.get("EG-0045", {}).get("status") != "open":
        errors.append("EG-0045 must remain open for future drafting-specific claim summaries")
    if issues.get("ISS-0026", {}).get("status") != "controlled_open":
        errors.append("ISS-0026 must remain controlled_open")
    if risks.get("RISK-0029", {}).get("status") != "controlled_open":
        errors.append("RISK-0029 must remain controlled_open")
    if pitfalls.get("PIT-0023", {}).get("current_status") != "controlled_open":
        errors.append("PIT-0023 must remain controlled_open")
    for issue_id in ["ISS-0001", "ISS-0002", "ISS-0008"]:
        if issues.get(issue_id, {}).get("status") != "narrowed_open":
            errors.append(f"{issue_id} must remain narrowed_open")
    for issue_id in ["ISS-0011", "ISS-0012", "ISS-0015", "ISS-0016", "ISS-0025"]:
        if issues.get(issue_id, {}).get("status") != "controlled_open":
            errors.append(f"{issue_id} must remain controlled_open")
    return errors


def check_nav_phrases() -> list[str]:
    errors = []
    for rel, phrases in NAV_PHRASES.items():
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing navigation file: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in text:
                errors.append(f"{rel} missing required phrase: {phrase}")
    return errors


def collect_errors() -> list[str]:
    errors = []
    errors.extend(check_required_files())
    if errors:
        return errors
    errors.extend(check_csv_headers())
    errors.extend(check_claim_matrix_scope())
    errors.extend(check_summary_register())
    errors.extend(check_summary_files())
    errors.extend(check_no_go_register())
    errors.extend(check_register_statuses())
    errors.extend(check_nav_phrases())
    return errors


def main() -> int:
    errors = collect_errors()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Claim summaries QA passed; Stage 16A remains a claim-use control layer only")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
