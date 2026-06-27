# Stage 32A: WECA OBC/FBC Exemplar Corpus And Simulated OBC Draft

Status: complete as simulation-control stage only.  
Date: 2026-06-27.

## Purpose

Stage 32A creates a WECA-style Bristol WPL OBC working draft and the controls needed to stop that draft being mistaken for a real public-authority document.

It answers two practical questions:

- What does a WECA-style OBC/FBC document discipline look like?
- How can a simulated Bristol WPL OBC use that discipline without claiming real approval, assurance clearance or readiness?

## Key Data Points

- `SRC-WECA-0009` is the strongest full-source WECA-facing FBC comparator. It gives document control, report purpose, Five Case Model ordering and economic, financial, commercial and management-case conventions.
- `SRC-WECA-0008` is a Strategic Outline Case comparator. It gives progression, assurance, risk, issue, benefits and monitoring conventions.
- `SRC-BCC-0036`, `SRC-BCC-0015` and `SRC-WECA-0027` provide route-pattern evidence only. They are not full OBC/FBC documents unless the source itself is a business case.
- The March 2026 Bristol WPL record supports a public decision trail showing OBC work in progress, but not a completed or approved Bristol WPL OBC.
- The simulated OBC is editable Markdown only. No authored PDF distribution output is created.

## Outputs

- `analysis/weca-obc-fbc-exemplars/exemplar-register.csv`
- `analysis/weca-obc-fbc-exemplars/comparator-matrix.csv`
- `analysis/weca-obc-fbc-exemplars/weca-style-obc-authoring-standard.md`
- `business_case/obc/simulated-working-draft/bristol-wpl-simulated-weca-style-obc.md`
- `evidence/source_notes/stage32a/src-weca-0008.md`
- `evidence/source_notes/stage32a/src-weca-0009.md`
- `analysis/context/stage-32a-weca-obc-fbc-exemplar-corpus/synthesis.md`
- `review/stage_gate_reports/stage-32a-weca-obc-fbc-exemplar-corpus-report.md`

## Risk Controls

| Risk | Control |
|---|---|
| WECA-style drafting is mistaken for WECA/MCA approval or assurance clearance. | Stage 32A no-go claims, WECA/MCA trigger tags and validator checks. |
| A full-looking simulated OBC is mistaken for an approved Bristol OBC. | Required status formula in every OBC-facing file. |
| Partial route-pattern evidence is treated as a full OBC/FBC exemplar. | Exemplar source hierarchy and claim limits. |
| Simulation sign-offs are treated as professional assurance. | Sign-off rows and gate report limitations. |
| WPL becomes framed as a generic procurement exercise. | README, dashboard and OBC text state that WPL legal, spatial, licensing, revenue, consultation and statutory requirements remain central. |

## Gate Decision

Stage 32A is accepted as a WECA-style exemplar and simulated OBC drafting-control stage only.

It does not prove evidence truth, source currentness, legal correctness, professional assurance, command sufficiency, public-authority approval, consultation readiness, OBC reliance, FBC reliance, statutory-submission readiness, procurement authority or WPL readiness.
