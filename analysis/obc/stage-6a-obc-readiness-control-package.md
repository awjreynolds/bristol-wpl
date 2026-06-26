# Stage 6A OBC Readiness Control Package

Status: simulation control package.  
Date: 2026-06-26.  
Owner: Integrated Case Review Agent.  
Review status: pending Stage 6A simulation review.

This package is not an Outline Business Case, review draft, approval draft, consultation proposition or officer report. It does not assemble an OBC.

## Control Position

Stage 6A creates OBC section-readiness, claim-control and assembly-blocking controls. It does not draft or assemble an OBC and does not create OBC/FBC, consultation or statutory-submission readiness.

The current position is no-go for OBC assembly because upstream Stage 2, Stage 3, Stage 4 and Stage 5 blockers remain open.

## Required Stage 6A Artefacts

| Artefact | Required path | Stage 6A status |
|---|---|---|
| Stage 6A control package | `analysis/obc/stage-6a-obc-readiness-control-package.md` | Control created |
| Section dependency matrix | `business_case/obc/controls/section-dependency-matrix.csv` | Control rows |
| Section readiness register | `business_case/obc/controls/section-readiness-register.csv` | Control rows |
| Claim dependency register | `business_case/obc/controls/section-claim-dependency-register.csv` | Control rows |
| No-go claim register | `business_case/obc/controls/no-go-claim-register.csv` | Control rows |
| OBC assurance review plan | `business_case/obc/controls/obc-assurance-review-plan.md` | Control created |
| OBC validator | `scripts/validate_obc.py` | Control created |
| OBC assembly guard | `scripts/assemble_obc.py` | Blocks assembly |

## Five Case Control

Every OBC section must map claims to upstream evidence, open issues and reviewer status before drafting reliance.

Every section-level claim must record claim ID, section, claim text, claim type, source IDs, evidence cutoff, linked issues, linked risks, linked evidence gaps, linked requirements, statutory crosswalk rows, model run or dataset ID, package or cost-line ID, dependency status, P0/P1 effect, blocked readiness claims, required reviewer, simulation sign-off ID, limitations, owner and next gate condition.

Required controls:

- Executive Summary must compress approved section findings only and must not introduce new claims.
- Strategic Case must depend on completed Stage 3 problem, baseline, objectives, theory of change, benefits and package evidence.
- Economic Case must depend on Stage 5 OAR, agreed ASR, completed ASST, model cards, model outputs, uncertainty and reviewer sign-off.
- Commercial Case must depend on defined operating model, procurement strategy, market evidence, data/technology requirements, enforcement workflow and cyber controls.
- Financial Case must depend on parking base, chargeable-space forecast, revenue model, cost model, net-proceeds controls, funding stack and sensitivity analysis.
- Management Case must depend on legal route, governance, DfT confirmation path, consultation plan, procurement plan, data/model controls, operations readiness and benefits management.
- Conclusions must present an honest no-go option and must not convert conditions into approval.

## Assembly Block

The Stage 6A assembly rule is simple:

Do not create `business_case/obc/assembled/bristol-wpl-outline-business-case.md` or `deliverables/review/docx/bristol-wpl-outline-business-case-officer-review.docx` while any P0 blocker remains open or while Stage 3, Stage 4 or Stage 5 upstream gates remain blocked.

`scripts/assemble_obc.py` must exit non-zero and state that Stage 6A assembly is blocked until upstream gate evidence is complete.

## Banned Claims

Stage 6A material must not claim:

- OBC is ready for approval;
- a preferred scheme has been selected;
- consultation can launch;
- WECA/MCA has approved, supports, objects to, funds, consents to or has no role in the scheme;
- DfT has accepted or approved a WPL confirmation route;
- boundary, charge base, revenue, benefits, BCR or VFM are decision-grade;
- commercial procurement, operating model, enforcement or appeals are ready;
- statutory submission is ready.

## Acceptance Criteria

Stage 6A can be treated as complete for control purposes only when:

- OBC section dependency and readiness controls exist;
- claim-level dependency controls exist;
- no-go claim controls exist;
- every OBC section has a Stage 6A control note;
- `assemble_obc.py` blocks assembly while open prerequisites remain;
- `obc-qa` passes;
- simulation sign-off records that OBC assembly, officer-review DOCX, consultation and statutory submission remain blocked.
