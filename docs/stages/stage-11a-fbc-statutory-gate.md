# Stage 11A FBC And Statutory Gate Controls

Status: complete as final gate control architecture.
Date: 2026-06-26.

## ELI5 Summary

Stage 11A is the final stop sign. It says what would need to be true before anyone could recommend approving the FBC, submitting the statutory dossier or implementing a Bristol WPL.

It does not approve anything.

## What Stage 11A Adds

- FBC/statutory gate checklist: `business_case/fbc/controls/stage-11-fbc-statutory-gate-checklist.csv`
- Assurance panel register: `business_case/fbc/controls/stage-11-assurance-panel-register.csv`
- No-go claim register: `business_case/fbc/controls/stage-11-no-go-claim-register.csv`
- Decision-report control: `business_case/fbc/controls/stage-11-decision-report-control.md`
- Red-team packet: `business_case/fbc/controls/stage-11-red-team-packet.md`
- Validator: `scripts/validate_fbc_statutory_gate.py`
- Gate report: `review/stage_gate_reports/stage-11a-fbc-statutory-gate-report.md`

## Key Issues Captured

| Issue | Why it matters | Stage 11A response |
|---|---|---|
| FBC approval could be confused with statutory submission. | They require overlapping but distinct evidence and approvals. | No-go register blocks both FBC approval and submit/implement recommendations. |
| Agent sign-offs could be mistaken for real professional approval. | Real-world use needs Monitoring Officer, Section 151 and specialist review. | Assurance panel maps simulation roles to real-world replacements. |
| Decision-makers could see a gate report without open risks. | That would be misleading. | Gate checklist requires residual-risk and downside-case visibility. |
| Upstream controls could look complete because they have templates. | A template is not evidence. | Validator requires Stage 11 to remain blocked while checklist and no-go rows are blocked. |

## Current Gate Position

Stage 11 FBC/statutory gate remains blocked. No FBC approval, statutory submission, scheme order approval, procurement approval or implementation recommendation is created.
