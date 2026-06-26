# Stage 14B Public Repo Secret Scanning

Status: current-tree remediation complete; remote alert disposition open.
Date: 2026-06-26.

## What Happened

GitGuardian reported a Grafana-token pattern in the public GitHub repository.

The local investigation found that the pattern came from public Power BI report identifiers embedded in Bristol committee-pack evidence, not from a local `.env` file or repo credential configuration.

## What Changed

- Three raw public BCC committee-pack PDFs were removed from the current GitHub tree.
- The corresponding source-register rows now say `downloaded_raw_omitted_from_public_repo`.
- The extracted text for `SRC-BCC-0011` was redacted where it contained the detector-collision payload.
- A redacted scanner was added at `scripts/scan_secrets.py`.
- `make secrets-qa` was added and `make validate` now runs the secret scanner.
- Stage 14B issue, risk, pitfall, requirement, evidence-gap, claim, approval and simulated sign-off rows were added.

## What Did Not Change

Stage 14B does not revoke or rotate external tokens, rewrite git history, close the GitGuardian alert remotely, or approve any WPL business-case or statutory gate.

## Key Artefacts

- `analysis/evidence/stage-14b-public-repo-secret-scan-control-package.md`
- `review/peer_review/stage-14b-public-repo-secret-scan-review.md`
- `review/stage_gate_reports/stage-14b-public-repo-secret-scan-report.md`
- `scripts/scan_secrets.py`
- `tests/test_secret_scan.py`
- `governance/risk_register.csv`
- `governance/stage_risk_matrix.csv`
- `governance/pitfalls_register.csv`

## Current Position

The public current tree is controlled by the new scanner. Git history and hosted alert disposition remain separate residual actions.
