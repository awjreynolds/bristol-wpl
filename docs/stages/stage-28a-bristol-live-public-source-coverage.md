# Stage 28A: Bristol Live Public Source Coverage

Status: complete as a public-source coverage control only.  
Date: 2026-06-27.

This stage is the Bristol live public-source coverage control for `SRC-BCC-0001`, `SRC-BCC-0002` and media context `SRC-BCC-0020`. It does not prove source truth, currentness or WPL readiness.

## Purpose

Stage 28A makes the three user-provided Bristol WPL public links visible to officers, cabinet readers and future agents.

It answers a practical question: are these sources relevant and tracked?

Answer: yes, they are relevant and tracked, but they are not equal.

- `SRC-BCC-0001` is an official Bristol project page and can support public narrative only.
- `SRC-BCC-0002` is an official Bristol news release and can support public communications chronology only.
- `SRC-BCC-0020` is a Bristol Post media article, seeded but not downloaded, and cannot support substantive claims.

## Artefacts

- `evidence/bristol_public_source_status.csv`
- `docs/public/bristol-live-public-source-status.md`
- `analysis/context/stage-28a-bristol-live-public-source-coverage-context.md`
- `review/peer_review/stage-28a-bristol-live-public-source-coverage-review.md`
- `review/stage_gate_reports/stage-28a-bristol-live-public-source-coverage-report.md`
- `scripts/validate_bristol_public_sources.py`
- `tests/test_bristol_public_sources.py`

## Controls Added

- Source ID and URL reconciliation for the three Bristol public links.
- Source-type distinction between official project page, official news release and media context.
- Access-state controls for `SRC-BCC-0002` script-placeholder extraction and `SRC-BCC-0020` payment-required access.
- No-go wording that prevents public pages, press releases or media articles being treated as formal decisions.
- Navigation from the root README and public source-link pages.

## What This Stage Does Not Prove

Stage 28A does not prove:

- complete public-source discovery;
- source truth;
- legal currentness;
- content completeness;
- media accuracy;
- official approval;
- consultation readiness;
- OBC or FBC readiness;
- statutory readiness;
- charge level;
- WPL readiness.

## Gate Decision

Stage 28A is accepted for public-source coverage and claim-boundary control only.

All WPL readiness gates remain blocked. `ISS-0038`, `RISK-0041`, `PIT-0035` and `EG-0056` remain open controls.
