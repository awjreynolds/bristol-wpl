# Source-Link And Freshness Status

Status: public/officer reader route for Stage 22A controls.  
Date: 2026-06-26.

## Plain-English Answer

Some source pages change, move or disappear. This page explains where to check whether priority source links were reachable on the last recorded check, which sources redirected and what still needs review before anyone relies on a source for a real decision.

The latest recorded snapshot is in `evidence/external_source_liveness_register.csv`.

## Latest Snapshot

| Item | Recorded position |
|---|---|
| Snapshot time | 2026-06-26 23:22 UTC |
| Priority-1 source URLs checked | 91 |
| Directly reachable on snapshot date | 89 |
| Reachable via redirect on snapshot date | 2 |
| Checker | `scripts/check_external_source_liveness.py` with `--write --timeout 10` |
| Offline validator | `scripts/validate_external_liveness.py` |

The two redirected sources are:

| Source ID | What changed |
|---|---|
| `SRC-HMT-0004` | GOV.UK redirects the Aqua Book publication URL to the current guidance URL. |
| `SRC-BCC-0031` | Bristol's officer delegation document URL redirects to a `/file` PDF endpoint. |

## How To Use This

Use `evidence/external_source_liveness_register.csv` to answer:

- was the registered URL reachable on the recorded date;
- did the URL redirect;
- what HTTP status, content type, `Last-Modified` value or `ETag` was observed;
- whether a source needs manual refresh before drafting reliance.

Then use the source notes and claim summaries before relying on the source:

- `evidence/source_notes/README.md`
- `evidence/claim_summaries/README.md`
- `evidence/source_register.csv`

## What This Does Not Prove

Stage 22A does not prove that any source is authoritative, legally current, substantively accurate, complete, still applicable or sufficient for OBC, FBC, consultation, statutory submission, approval, funding, procurement or WPL readiness.

A reachable source link only means the endpoint responded during the recorded check. It does not prove the document is unchanged, legally current, correct, complete or suitable for a specific claim.

## Before Decision-Grade Reliance

Before a source is used in a decision-grade OBC, FBC, consultation document or statutory dossier, the reviewer should:

- check whether the registered URL is still reachable;
- compare retrieved content against the relevant source note and claim summary;
- record any redirect, changed metadata, missing attachment or replacement page;
- refresh the source note if the source has changed;
- keep raw omitted public-pack PDFs out of the public repo unless the Stage 14B-E security controls are rerun;
- obtain real professional review where legal, finance, modelling, equality, consultation or statutory judgement is needed.

## Remaining Gaps

`EG-0049` remains open for evidence accuracy, content correctness and register-ID semantic resolution. `EG-0050` records the residual gap that reachability metadata does not prove source authority, legal currentness, content completeness or decision-grade sufficiency.
