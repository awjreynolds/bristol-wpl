# Stage 6A OBC Readiness Controls

Status: completed as control architecture. OBC assembly no-go remains.

## Purpose

Stage 6A creates OBC readiness and assembly controls before any five-case OBC package is described as ready. It prevents section templates, placeholder scripts or earlier control stages from being mistaken for an assembled Outline Business Case.

## Key Data Points

- No OBC has been assembled.
- No officer-review DOCX has been created.
- `scripts/assemble_obc.py` now exits non-zero while upstream blockers remain open.
- Every main OBC section has a Stage 6A control note.
- OBC section dependency, section readiness, no-go claim and claim-level dependency registers exist.
- The current gate position remains no-go for consultation, OBC recommendation, FBC, statutory submission and officer distribution.

## Main Artefacts

- `analysis/obc/stage-6a-obc-readiness-control-package.md`
- `business_case/obc/controls/section-dependency-matrix.csv`
- `business_case/obc/controls/section-readiness-register.csv`
- `business_case/obc/controls/section-claim-dependency-register.csv`
- `business_case/obc/controls/no-go-claim-register.csv`
- `business_case/obc/controls/obc-assurance-review-plan.md`
- `scripts/validate_obc.py`
- `tests/test_obc.py`
- `review/stage_gate_reports/stage-6a-obc-readiness-control-report.md`

## Key Findings

- OBC readiness depends on all five cases; the Executive Summary cannot introduce unsupported claims.
- Strategic Case reliance remains blocked by incomplete Stage 3 problem, baseline, objectives, stakeholder, theory-of-change, benefits and package evidence.
- Economic Case reliance remains blocked by missing OAR, agreed ASR, ASST, model outputs, BCR, VFM and uncertainty review.
- Financial Case reliance remains blocked by absent boundary, parking base, revenue model, cost model, net-proceeds controls and package funding assurance.
- Management Case reliance remains blocked by Bristol final route, WECA/MCA role, DfT process, consultation, procurement, operations and assurance dependencies.
- Conclusions must present no-go, pause, rework or stop unless P0 blockers close.

## What Stage 6A Does Not Claim

- It does not assemble an OBC.
- It does not create an officer-review DOCX.
- It does not approve a preferred option.
- It does not support consultation launch.
- It does not provide commercial, financial, operational, legal, appraisal or statutory readiness.
- It does not replace Stage 7 OBC assurance.

## Continuing Issues

- `ISS-0001`, `ISS-0002`, `ISS-0003` and `ISS-0004` remain P0 blockers.
- `ISS-0011` is controlled-open: OBC assembly controls exist, but section evidence and upstream gates are not complete.
- `RISK-0014` remains controlled-open for false OBC readiness and placeholder-template misuse.
- `EG-0018` is partially closed only; assembly is now blocked, but real document assembly remains unavailable until upstream gates pass.
