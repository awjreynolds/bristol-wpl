# Stage 7A OBC Assurance

Status: complete as OBC assurance-gate control architecture.  
Date: 2026-06-26.

## ELI5 Summary

Stage 7A defines the exam paper for a future OBC gate. It does not pass the exam.

The repo now records who would need to review a future OBC, what they would need to see, what would block a proceed recommendation, and how red-team challenge would be bounded.

## What Stage 7A Adds

- OBC gate checklist: `business_case/obc/controls/stage-7-obc-gate-checklist.csv`
- Assurance panel register: `business_case/obc/controls/stage-7-assurance-panel-register.csv`
- Decision-report control: `business_case/obc/controls/stage-7-decision-report-control.md`
- Red-team packet: `business_case/obc/controls/stage-7-red-team-packet.md`
- Validator: `scripts/validate_obc_assurance.py`
- Gate report: `review/stage_gate_reports/stage-7a-obc-assurance-gate-report.md`

## Key Issues Captured

| Issue | Why it matters | Stage 7A response |
|---|---|---|
| OBC gate could be mistaken for document formatting review. | A polished OBC can still be unsupported. | Gate checklist requires evidence, blocker IDs, reviewer and pass condition. |
| Agent sign-offs could be mistaken for real professional approvals. | OBC gates need legal, finance, modelling, spatial, data and officer accountability. | Panel register records real-world replacements. |
| Red-team review could become unbounded and context-heavy. | Overloaded agents miss readiness overclaims. | Red-team packet defines bounded inputs and outputs. |
| Decision-report wording could imply approval before evidence exists. | This creates public-law and governance risk. | Decision-report control bans proceed wording while blockers remain. |

## Current Gate Position

Stage 7 OBC gate remains blocked. No OBC, officer-review DOCX, consultation launch, FBC readiness or statutory submission readiness is created.
