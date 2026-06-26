# Stage 14B Public Repository Secret-Scan Control Package

Status: current-tree remediation complete; remote alert disposition open.
Date: 2026-06-26.

## Trigger

GitGuardian reported a `Grafana Token` pattern in the public GitHub repository on 2026-06-26.

The local investigation did not find a repo credential file. It found token-detector collisions in public Bristol City Council committee-pack evidence:

- `SRC-BCC-0005`
- `SRC-BCC-0011`
- `SRC-BCC-0015`

The matching byte pattern was a public Power BI report identifier beginning with the same base64 prefix used by some legacy Grafana-token detectors.

## Controls Added

- Removed the three raw public PDF binaries from the current GitHub tree.
- Redacted the matching Power BI/Grafana-detector collision payloads from `evidence/processed/text/SRC-BCC-0011.txt`.
- Retained the source URLs, official source identifiers and original hashes in `evidence/source_register.csv`.
- Marked the three sources as `downloaded_raw_omitted_from_public_repo`.
- Added `scripts/scan_secrets.py`, a dependency-free scanner that reports only rule, path, line, length and hash.
- Added `tests/test_secret_scan.py`.
- Added `make secrets-qa` and included the scanner in `make validate`.
- Added exact `.gitignore` entries for the three omitted PDFs to reduce accidental re-addition.

## What This Stage Does Not Do

Stage 14B does not:

- prove that an externally issued Grafana token is safe;
- revoke or rotate any external token;
- confirm GitGuardian remote alert closure;
- rewrite git history;
- certify all third-party source files as disclosure-safe forever;
- change any WPL business-case, statutory, consultation or approval gate.

## Current Working Rule

Public documents are not automatically safe to mirror into a public repository. Before any future public push or source-acquisition refresh, run:

```bash
make secrets-qa
make validate
```

If raw binary inspection of the omitted BCC committee packs is needed, reacquire them outside the public repo or in a local scratch area and keep the source URL/hash trail in the registers.

## Open Items

- `ISS-0020`: public evidence can still contain token-like material.
- `RISK-0023`: public repo may expose real or detector-colliding token-like content.
- `EG-0039`: GitGuardian remote alert disposition is not recorded in this repo.

History rewrite remains a separate action requiring explicit approval because it would alter public git history and require a force push.
