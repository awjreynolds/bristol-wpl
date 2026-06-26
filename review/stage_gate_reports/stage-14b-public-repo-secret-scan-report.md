# Stage 14B Public Repo Secret-Scan Gate Report

Status: current-tree remediation complete; history and remote alert disposition open.
Date: 2026-06-26.

## Gate Decision

Stage 14B passes only as a current-tree public-repository control stage.

It does not close GitGuardian remotely, revoke or rotate any token, rewrite git history, or change the no-go position for WPL approval, OBC, FBC, consultation or statutory submission.

## Evidence Checked

- Current-tree filename-only and redacted content scan.
- Reachable-history filename-only pattern scan.
- Zip-content check for `bristol_wpl_codex_authoring_pack.zip`.
- Source-register rows for `SRC-BCC-0005`, `SRC-BCC-0011` and `SRC-BCC-0015`.
- Extraction manifest and metadata updates.
- `scripts/scan_secrets.py`.
- `tests/test_secret_scan.py`.
- `governance/issues_register.csv`, `governance/risk_register.csv`, `governance/stage_risk_matrix.csv`, `governance/pitfalls_register.csv`, `evidence/evidence_gap_register.csv`.

## Remediation Summary

The following current-tree files were removed:

- `evidence/raw/bristol-city-council/src-bcc-0005_public-reports-pack-transport-connectivity-policy-committee-2024-09-12.pdf`
- `evidence/raw/bristol-city-council/src-bcc-0011_public-reports-pack-transport-connectivity-policy-committee-2025-10-23.pdf`
- `evidence/raw/bristol-city-council/src-bcc-0015_public-reports-pack-transport-connectivity-policy-committee-2026-03-19.pdf`

The extracted text for `SRC-BCC-0011` was redacted where public Power BI report identifiers matched the legacy Grafana-token detector pattern.

## Residual Position

- Current-tree validation is controlled by `make secrets-qa` and `make validate`.
- The three source records remain in `evidence/source_register.csv` with official source URLs and original hashes.
- Git history still contains the earlier blobs until a separate history rewrite is explicitly approved and performed.
- GitGuardian remote alert status must be checked outside this repo after the remediation push.

## No-Go Statements

Do not claim:

- "the token is safe";
- "the token has been revoked";
- "GitGuardian is closed";
- "git history has been cleaned";
- "all public-source PDFs are safe to commit";
- "Stage 14B changes any WPL readiness gate".

## Simulated Gate Sign-Off

The current-tree public-repository secret-scan controls are accepted for simulation purposes with open residual actions. All WPL approval, consultation, OBC, FBC and statutory-submission gates remain blocked.
