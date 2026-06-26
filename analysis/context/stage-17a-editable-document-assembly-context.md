# Stage 17A Editable Document Assembly Context

Status: context packet for editable authoring guardrails.  
Date: 2026-06-26.

## Stage Purpose

Stage 17A creates a clear officer-editable document assembly map and validator. It explains how future OBC, FBC, statutory, officer and public outputs should be assembled from sources, source notes, claim summaries and registers without producing PDFs or implying readiness.

This stage does not assemble an OBC, FBC, statutory submission, consultation pack or officer-distribution pack. It makes the authoring workflow safer and easier to inspect.

## Files In Scope

- `business_case/obc/**`
- `business_case/fbc/**`
- `statutory_dossier/**`
- `docs/officer/**`
- `docs/public/README.md`
- `evidence/source_notes/README.md`
- `evidence/claim_summaries/README.md`
- `scripts/assemble_obc.py`
- `scripts/assemble_fbc.py`
- `docs/authoring/`
- `docs/visuals/authoring-control-flow.mmd`
- `scripts/validate_authoring_guardrails.py`
- `tests/test_authoring_guardrails.py`
- relevant register files under `governance/` and `evidence/evidence_gap_register.csv`

## Files Out Of Scope

- Producing PDF officer-distribution outputs.
- Assembling `business_case/obc/assembled/bristol-wpl-outline-business-case.md`.
- Assembling `business_case/fbc/assembled/bristol-wpl-full-business-case.md`.
- Creating a statutory submission pack or certified scheme order.
- Creating consultation launch materials.
- Inventing evidence, model outputs, boundary maps, parking inventories, BCR, VFM category, charge level, revenue estimate or legal advice.

## Open Register IDs

- Existing readiness blockers: `ISS-0001`, `ISS-0002`, `ISS-0003`, `ISS-0004`, `ISS-0008`, `ISS-0011`, `ISS-0012`, `ISS-0015`, `ISS-0016`.
- Current control risks: `ISS-0025`, `ISS-0026`, `EG-0045`, `RISK-0028`, `RISK-0029`.
- Stage 17A must add a new issue, risk, pitfall, requirement, check, decision, approval and simulated sign-off row if it creates the authoring guardrail layer.

## No-Go Claims

Stage 17A must not claim:

- an OBC, FBC, statutory dossier or consultation pack is assembled;
- an officer-review DOCX is ready;
- any PDF is authored for officer distribution;
- legal advice, Monitoring Officer clearance, Section 151 clearance or public-authority approval exists;
- WECA/MCA, DfT or Secretary of State positions are settled;
- appraisal, model, BCR, VFM, boundary, inventory, consultation, procurement or implementation gates have changed.

## Subagent Roles

- Document assembly reviewer: test whether editable outputs, blocked assembly and no-PDF rules are clear.
- Legal/statutory reviewer: test whether statutory dossier and scheme-order language remains control-only.
- Public/officer readability reviewer: test whether a non-technical reader can understand what can be edited and what remains blocked.
- Red-team reviewer: test false readiness, authored-PDF leakage, claim-summary overread and context-bloat risk.

## Validator Commands

```bash
python3 scripts/validate_authoring_guardrails.py
python3 -m unittest tests.test_authoring_guardrails
make validate
git diff --check
python3 scripts/scan_secrets.py --all-history
```

## Commit/Push Condition

Do not proceed past Stage 17A until the authoring guardrail docs, visual, validator, register trail, peer review, gate report and validation evidence are committed and pushed.
