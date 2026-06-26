# Stage 7A OBC Assurance Gate Control Package

Status: simulation control package.  
Date: 2026-06-26.  
Owner: Integrated Case Review Agent.  
Review status: Stage 7A simulation control only.

This package defines how a future OBC assurance and decision gate would be controlled. It does not approve an OBC, does not assemble an OBC, does not create an officer-review DOCX and does not authorise consultation.

## Control Position

Stage 7A creates the assurance-panel, red-team, decision-report and gate-checklist controls for a future OBC gate. Stage 7 OBC gate remains blocked because the repo still has open P0 and P1 readiness blockers.

No proceed recommendation may be made while any open P0 remains or while any P1 lacks a named condition, owner, deadline and accepted residual risk. This is the required no proceed recommendation wording for Stage 7A controls.

## Required Artefacts

| Artefact | Path | Status |
|---|---|---|
| Stage 7A control package | `analysis/obc/stage-7a-obc-assurance-gate-control-package.md` | Created |
| OBC gate checklist | `business_case/obc/controls/stage-7-obc-gate-checklist.csv` | Blocked control rows |
| Assurance panel register | `business_case/obc/controls/stage-7-assurance-panel-register.csv` | Simulation roles only |
| Decision report control | `business_case/obc/controls/stage-7-decision-report-control.md` | Control note |
| Red-team packet | `business_case/obc/controls/stage-7-red-team-packet.md` | Bounded packet |
| Validator | `scripts/validate_obc_assurance.py` | Control created |

## Assurance Logic

The Stage 7 assurance gate must test the integrated case, not just the presence of a document. A future gate packet must show:

- legal/governance route and decision authority;
- Strategic Case evidence and no predetermination;
- Economic Case appraisal, OAR, ASR, ASST, model outputs, BCR and VFM treatment;
- spatial boundary, parking inventory and displacement evidence;
- finance, affordability, net-proceeds and funding controls;
- commercial, operational, data, cyber and enforcement readiness;
- consultation readiness, equality, data protection and accessibility controls;
- statutory route and confirmation-dossier alignment;
- red-team challenge and issue disposition;
- officer-editable output provenance and no authored PDF output.

## Stage 7 Gate Rule

Stage 7 OBC gate remains blocked while live readiness registers contain open P0 or unconditioned P1 blockers.

The gate cannot pass by accepting narrative quality alone. The gate can only pass when every checklist row has evidence, reviewer output, residual-risk treatment and a supported pass condition.

## What Stage 7A Does Not Do

- It does not approve an OBC.
- It does not recommend WPL progression.
- It does not create a preferred scheme.
- It does not make consultation launch lawful or ready.
- It does not settle Bristol, WECA/MCA, DfT, boundary, appraisal, finance, commercial, data or statutory blockers.
