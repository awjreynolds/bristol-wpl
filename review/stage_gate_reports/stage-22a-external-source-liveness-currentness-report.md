# Stage 22A Gate Report: External Source Liveness And Currentness Metadata

Status: accepted for source-link/freshness metadata control only.  
Date: 2026-06-26.

## Gate Question

Does the repo now record and validate priority-1 external source-link reachability metadata without overclaiming source truth or readiness?

## Gate Answer

Yes, for URL-status and source-refresh metadata control only.

Stage 22A does not prove that any source is authoritative, legally current, substantively accurate, complete, still applicable or sufficient for OBC, FBC, consultation, statutory submission, approval, funding, procurement or WPL readiness.

## Artefacts Checked

- `docs/public/source-link-and-freshness-status.md`
- `evidence/external_source_liveness_register.csv`
- `scripts/check_external_source_liveness.py`
- `scripts/validate_external_liveness.py`
- `tests/test_external_liveness.py`
- `README.md`
- `docs/public/README.md`
- `docs/officer/assurance-dashboard.md`
- `docs/officer/document-map.md`
- `docs/stages/README.md`

## Snapshot Evidence

The network refresh checked 91 priority-1 source URLs:

- 89 `reachable_http_ok`;
- 2 `redirected_reachable`;
- 0 network error, HTTP error or manual-review outcomes.

The redirected rows are `SRC-HMT-0004` and `SRC-BCC-0031`.

## Acceptance Criteria

| Criterion | Result |
|---|---|
| Priority-1 URL rows are covered by the liveness register | Pass |
| URL values match the source register | Pass |
| Snapshot timestamp is parseable and recent | Pass |
| Outcome vocabulary is controlled | Pass |
| Redirects are visible rather than hidden | Pass |
| Routine validation is offline and deterministic | Pass |
| Refresh command is explicit and network-dependent | Pass |
| No authored PDFs are introduced | Pass |
| Gate wording preserves no evidence-truth and no-readiness limits | Pass |

## Validation

Focused validation:

```text
python3 scripts/validate_external_liveness.py
python3 -m unittest tests.test_external_liveness
```

Full validation before commit:

```text
make validate
git diff --check
python3 scripts/scan_secrets.py --all-history
```

## Remaining Blockers

- `EG-0049` remains open for evidence accuracy, content correctness and register-ID semantic resolution.
- `EG-0050` remains open for source authority, legal currentness, content completeness and decision-grade sufficiency.
- GitGuardian hosted-alert disposition remains external.
- Raw omitted public-pack PDFs are not restored to public history.
- All WPL approval, consultation, OBC, FBC and statutory-submission gates remain blocked.

## Gate Decision

Stage 22A passes for URL-status and source-refresh metadata control only.

It does not create approval, professional assurance, legal-currentness certification, evidence truth or WPL readiness.
