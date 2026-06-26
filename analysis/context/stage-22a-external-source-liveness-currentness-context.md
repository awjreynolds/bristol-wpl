# Stage 22A Context Packet: External Source Liveness And Currentness Metadata

Status: bounded controller packet for Stage 22A.  
Date: 2026-06-26.

## Scope

Stage 22A adds URL-status and source-link freshness controls for priority-1 source-register rows.

It is not a content audit, legal-currentness review, source adequacy review, raw evidence reacquisition stage, GitGuardian disposition stage or WPL readiness gate.

## Inputs

- `evidence/source_register.csv`
- `evidence/external_source_liveness_register.csv`
- `scripts/check_external_source_liveness.py`
- `scripts/validate_external_liveness.py`
- Stage 21A navigation controls and reports
- Stage 14B-E public-repo security controls for raw-PDF and hosted-alert caveats

## Subagent Review Lanes

Three bounded review lanes were used:

- Source-register/liveness design reviewer: metadata fields, deterministic validation and no-claim wording.
- Red-team reviewer: HTTP 200 weakness, redirects, raw-omitted PDFs, GitGuardian caveats and no-readiness conditions.
- Public/officer navigation reviewer: canonical reader route and minimal README updates.

## Snapshot Result

The network refresh command checked 91 priority-1 source URLs:

- 89 `reachable_http_ok`;
- 2 `redirected_reachable`;
- 0 network, HTTP error or manual-review outcomes in the recorded snapshot.

The two redirected sources are `SRC-HMT-0004` and `SRC-BCC-0031`.

## Constraints

- Routine `make validate` must validate recorded metadata only.
- Network refresh must be explicit through `make refresh-external-liveness`.
- The register must not be used as proof of evidence truth, legal currentness, content completeness, source authority or WPL readiness.
- Raw omitted public-pack PDFs must remain omitted unless reacquisition and security checks are explicitly rerun.
