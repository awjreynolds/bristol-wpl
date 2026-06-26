# Stage 10A Statutory Confirmation Dossier Control Package

Status: simulation control package.
Date: 2026-06-26.
Owner: Legal Review Agent.

This package creates statutory confirmation dossier controls. It does not create a statutory submission, certified scheme order, DfT-accepted dossier, Secretary of State confirmation request or implementation-ready legal pack.

## Control Position

Stage 10 statutory submission remains blocked because the repo still has open legal, WECA/MCA, DfT, boundary, consultation, FBC, finance, operations and assurance blockers.

The Stage 10 component list is a working framework, not a definitive DfT checklist. The exact submission route and dossier contents must be verified with DfT and the lawful Bristol decision route before reliance.

## Required Stage 10A Controls

| Control | Path | Status |
|---|---|---|
| Component register | `statutory_dossier/controls/dossier-component-register.csv` | Blocked control rows |
| Dossier readiness gate | `statutory_dossier/controls/dossier-readiness-gate.csv` | Blocked control rows |
| Submission no-go claims | `statutory_dossier/controls/submission-no-go-register.csv` | Blocked controls |
| Statutory route memorandum control | `statutory_dossier/controls/statutory-route-memorandum-control.md` | Control note |
| Clause-by-clause powers matrix | `statutory_dossier/draft_scheme_order/clause-by-clause-powers-matrix.csv` | Blocked controls |
| Validator | `scripts/validate_statutory_dossier.py` | Control created |

## Gate Rule

No statutory submission readiness claim may be made until:

- final Bristol order-maker, statutory submitter and signatory route is settled;
- WECA/MCA role, consent/no-role and funding dependency are settled;
- DfT WPL-specific procedural expectations are logged or accepted as a submission risk;
- boundary, scheme order, consultation statement, FBC, net-proceeds plans, finance, operations, equality, data protection and monitoring evidence are complete;
- all open P0 blockers are closed and P1 blockers have accepted conditions.

## What Stage 10A Does Not Do

- It does not certify a scheme order.
- It does not submit anything to DfT or the Secretary of State.
- It does not confirm that the dossier list is definitive.
- It does not complete consultation, FBC or legal compliance.
- It does not create authored PDF outputs.
