# Stage 33A OBC Simulation Release Context

Status: bounded context packet for Stage 33A.  
Date: 2026-06-27.

## Scope

Stage 33A ships the editable Bristol WPL OBC simulation as a release package under `business_case/obc/simulation-release/`.

It does not create a real assembled OBC, officer-review DOCX, consultation pack, procurement authority, WECA/MCA submission, DfT submission, statutory dossier or public-authority approval.

## Inputs

- Stage 32A simulated WECA-style OBC working draft.
- Stage 32A WECA exemplar corpus and authoring standard.
- OBC completeness reviewer PASS for simulation-only use.
- WECA/evidence discipline reviewer PASS after citation and label corrections.
- `python3 scripts/validate_obc.py`.
- `make validate`.
- `python3 scripts/scan_secrets.py --all-history`.

## Release Rule

The release may be described as a shipped simulation OBC only if the phrase below remains visible in release-facing files:

> Stage 33A simulated OBC release package. Not an approved Bristol OBC, not officer advice, not a consultation document, not WECA/MCA/DfT endorsed, not Secretary of State confirmed, not procurement authority and not for real-world reliance.

## No-Go Claims

Do not claim that Stage 33A:

- approves the OBC;
- passes Stage 7;
- authorises consultation;
- creates a real WECA/MCA assurance submission;
- settles procurement or spend authority;
- settles legal, finance, modelling, equalities, data, consultation or statutory readiness;
- creates professional assurance;
- confirms WPL readiness.

## Required Register Updates

Stage 33A must update:

- `governance/issues_register.csv`;
- `governance/risk_register.csv`;
- `governance/pitfalls_register.csv`;
- `evidence/evidence_gap_register.csv`;
- `governance/requirements_register.csv`;
- `governance/checks_and_balances_register.csv`;
- `governance/decision_log.csv`;
- `governance/approvals_register.csv`;
- `governance/simulation_signoff_register.csv`;
- `governance/stage_risk_matrix.csv`.
