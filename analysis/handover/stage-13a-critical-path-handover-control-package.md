# Stage 13A Critical Path Handover Control Package

Status: handover control architecture.
Date: 2026-06-26.

## Control Question

Can a public reader, officer, cabinet member, specialist reviewer or future agent understand what work remains after the simulation without treating the backlog as approval or readiness?

## Decision

Stage 13A creates a critical-path handover layer. The critical path is not approval. It is a map of blocked work packages, evidence dependencies, review roles and no-go claims.

It does not close any WPL gate, authorise spending, start procurement, instruct officers, launch consultation, approve an OBC or FBC, or settle any legal, finance, DfT, WECA/MCA, boundary, appraisal, data, operations or statutory submission question.

## Handover Products

- `handover/controls/critical-path-work-package-register.csv`
- `handover/controls/blocker-to-workstream-map.csv`
- `handover/controls/next-90-day-plan.csv`
- `handover/controls/handover-no-go-register.csv`
- `docs/officer/next-steps-critical-path.md`

## Handover Rules

- Work packages remain blocked work packages until evidence is produced and reviewed.
- No work package closes a blocker by existing.
- The 90-day plan is a planning control only and does not authorise spend or procurement.
- Any future real-world use requires public-authority and professional replacement sign-offs.
- Future agents must start from the blocker map and no-go register rather than summarising the whole repo from memory.

## Validation

Run:

```bash
python3 scripts/validate_handover.py
make handover-qa
make validate
```

Expected result: handover QA passes while all WPL readiness gates remain blocked.
