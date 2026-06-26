# Stage 12A Public Release Review

Status: simulated public-release review with conditions.
Date: 2026-06-26.

## Review Scope

This review tests whether public GitHub visibility is recorded without implying WPL approval, legal advice, consultation launch, OBC/FBC readiness or statutory submission readiness.

## Findings

| Finding | Severity | Response |
|---|---|---|
| Public visibility could be mistaken for endorsement or approval. | P1 | README and no-go register state that public visibility is not approval. |
| Public readers need entry points before specialist evidence. | P1 | README retains public, officer, legal, modelling, GIS and consultation routes. |
| Public repo must avoid authored PDF distribution outputs. | P1 | Public-release scan register and validator require no authored PDFs outside `evidence/raw/**`. |
| Restricted or personal consultation data would be unsafe in the normal public repo. | P1 | Sensitive-path checks are part of validation. |
| Future agents could infer readiness from publication. | P1 | Stage 12A adds a bounded-publication control package and no-go claims. |
| Public GitHub visibility could be mistaken for an official council publication. | P2 | Root README, public-release no-go register, control package and gate report now block that claim explicitly. |
| PDF distribution scan was case-sensitive and did not distinguish raw source PDFs from authored PDFs placed under raw evidence. | P1 | Register validator now uses case-insensitive `.pdf` matching and requires raw evidence PDFs to follow the `src-*` source-file convention. |
| Restricted-path controls did not check public/officer page references. | P2 | Register validator now scans public/officer Markdown, CSV and HTML for restricted data path references. |
| Public-release CSV semantics could drift toward readiness wording. | P2 | Public-release validator now restricts publication checklist `gate_effect` values and rejects unsafe positive readiness terms in no-go allowed wording. |
| Checks-and-balances page lacked a standalone simulation/no-approval notice. | P3 | Page now includes a standalone no-approval, no-readiness and no-official-publication notice. |

## Decision

Simulation sign-off with conditions for Stage 12A publication controls only.

Stage 12A records public repository visibility. It does not approve a Bristol WPL, create legal advice, authorise consultation, approve an OBC or FBC, authorise statutory submission or replace real-world professional approvals.

## Conditions

- `scripts/validate_public_release.py` must pass.
- `make validate` must include public-release QA.
- `make gate-obc`, `make gate-fbc` and `python3 scripts/validate_fbc_statutory_gate.py --gate` must remain blocked while live WPL blockers remain.
- No authored PDF outputs may be produced.
