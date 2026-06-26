# Stage 22A External Source Liveness And Currentness Metadata

Status: complete as source-link/freshness metadata control only.  
Date: 2026-06-26.

## Purpose

Stage 22A records a priority-1 source-link reachability snapshot and adds deterministic validation around that snapshot.

## What Was Added

- `docs/public/source-link-and-freshness-status.md`
- `evidence/external_source_liveness_register.csv`
- `scripts/check_external_source_liveness.py`
- `scripts/validate_external_liveness.py`
- `tests/test_external_liveness.py`
- `make external-liveness-qa`
- `make refresh-external-liveness`

## Snapshot

The recorded refresh checked 91 priority-1 source URLs:

- 89 were directly reachable on the snapshot date;
- 2 were reachable via redirect;
- no network, HTTP error or manual-review outcomes were recorded.

The redirected rows are `SRC-HMT-0004` and `SRC-BCC-0031`.

## What It Checks

- every priority-1 source-register URL has a liveness snapshot row;
- URL values match the source register;
- snapshot timestamps are parseable and not older than the configured freshness window;
- outcomes use controlled values;
- non-reachable outcomes must carry notes;
- no authored PDFs have been introduced.

## What It Does Not Check

- evidence truth;
- source authority;
- legal currentness;
- content completeness;
- content diff against previous versions;
- source-note or claim-summary sufficiency;
- GitGuardian hosted-alert disposition;
- WPL readiness.

## Gate Evidence

- `review/peer_review/stage-22a-external-source-liveness-currentness-review.md`
- `review/stage_gate_reports/stage-22a-external-source-liveness-currentness-report.md`
- `python3 scripts/validate_external_liveness.py`
