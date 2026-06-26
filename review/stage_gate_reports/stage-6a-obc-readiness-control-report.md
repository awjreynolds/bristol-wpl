# Stage 6A OBC Readiness Control Gate Report

Status: simulation gate report.  
Date: 2026-06-26.  
Gate authority: Simulation Gate Authority.  
Primary artefact: `analysis/obc/stage-6a-obc-readiness-control-package.md`.

This report has no real-world legal, statutory, financial, commercial, analytical, Bristol officer or professional approval effect.

## Evidence Reviewed

- `analysis/obc/stage-6a-obc-readiness-control-package.md`
- `business_case/obc/controls/section-dependency-matrix.csv`
- `business_case/obc/controls/section-readiness-register.csv`
- `business_case/obc/controls/section-claim-dependency-register.csv`
- `business_case/obc/controls/no-go-claim-register.csv`
- `business_case/obc/controls/obc-assurance-review-plan.md`
- `business_case/obc/*/*.md`
- `business_case/shared/assembly_manifest.md`
- `scripts/assemble_obc.py`
- `scripts/validate_obc.py`
- `tests/test_obc.py`
- `review/peer_review/stage-6a-obc-readiness-review.md`

## Gate Criteria

| Criterion | Result |
|---|---|
| OBC assembled | Not met; deliberately blocked |
| Officer-review DOCX created | Not met; deliberately blocked |
| OBC section control notes present | Met |
| Section dependency matrix created | Met |
| Section readiness register created | Met |
| Claim dependency register created | Met |
| No-go claim register created | Met |
| Assurance review plan created | Met |
| Assembly script blocks output | Met |
| OBC no-go preserved | Met |

## Gate Finding

Stage 6A creates OBC readiness and assembly-blocking controls. It reduces the risk that OBC templates, placeholder scripts or earlier control-stage outputs are mistaken for a review-draft OBC.

Stage 6A does not create an OBC, officer-review DOCX, preferred option, consultation proposition, BCR, VFM, revenue estimate, commercial readiness, financial readiness, operational readiness, statutory submission readiness or officer approval route.

## Continuing Blockers

- `ISS-0001` remains P0: Bristol final WPL licensing-scheme order-maker and statutory submitter route is unresolved.
- `ISS-0002` remains P0: WECA/MCA current-law role, consent, consultation-response and funding-dependency status are unresolved.
- `ISS-0003` remains P0: authoritative WPL boundary and workplace parking inventory are absent.
- `ISS-0004` remains P0: no agreed OAR, ASR, ASST, completed model outputs or decision-grade uncertainty analysis exists.
- `ISS-0011` remains controlled-open: Stage 6A controls exist, but OBC section evidence and upstream gates are not complete.
- `EG-0018` remains partially closed only: assembly is now blocked, but real OBC/FBC assembly is not implemented.

## Decision

Decision: simulation sign-off with conditions for Stage 6A controls only; simulation no-go remains for OBC assembly, officer-review DOCX, Stage 7 OBC gate, consultation launch, FBC readiness and statutory submission readiness.

Conditions:

- future OBC section drafting must populate claim dependency rows before relying on any claim;
- every P0 must be closed before a proceed recommendation can be made;
- any P1 condition must have owner, due date, action plan and residual-risk acceptance;
- `scripts/assemble_obc.py` must continue to block output until upstream gates pass and assembly logic is replaced with reviewed, source-linked assembly controls;
- no authored PDF output may be produced.
