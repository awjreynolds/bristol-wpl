# Stage 22A Peer Review: External Source Liveness And Currentness Metadata

Status: simulated peer review complete.  
Date: 2026-06-26.

## Review Roles

- Source-register/liveness design reviewer.
- Red-team reviewer.
- Public/officer navigation reviewer.

## Findings Accepted

- Stage 22A must validate recorded URL-status metadata and not evidence truth.
- `HTTP 200` or a successful redirect is weak evidence and must not be described as proof that a source is current, authoritative, complete or suitable for reliance.
- Raw omitted public-pack PDFs remain controlled by Stage 14B-E security decisions and must not be silently reintroduced into public history.
- Routine validation should be deterministic; live network refresh should be explicit.
- Public/officer navigation should use one canonical source-link/freshness page instead of expanding the root README into a control manual.

## Implementation Response

- Added `evidence/external_source_liveness_register.csv` as a recorded snapshot.
- Added `scripts/check_external_source_liveness.py` for explicit live refresh.
- Added `scripts/validate_external_liveness.py` for deterministic offline QA.
- Added `docs/public/source-link-and-freshness-status.md` as the public/officer route.
- Updated stage maps and registers with no-readiness wording.

## Residual Concerns

- Reachability metadata does not prove content has not changed.
- Redirects require human review before decision-grade reliance.
- Source notes and claim summaries still need refreshing before any new high-materiality drafting claim.
- GitGuardian hosted alert disposition remains external.
- All WPL readiness gates remain blocked.
