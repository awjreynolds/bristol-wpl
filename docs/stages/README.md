# Stage Workflow Index

Status: working stage narrative.  
Date: 2026-06-26.

This directory explains the workflow stage by stage. It is a navigation and audit aid only; controlled decisions remain in the registers, gate reports and source-linked analysis files.

## Commit Discipline

Each completed stage package should be committed and pushed before the next stage begins. The README should stay as the high-level entry point; detailed stage findings belong here when they would make the README too large.

## Current Stage Map

Terminology note: `Stage 10A` is a control-architecture slice for a future statutory confirmation dossier. `Stage 11A` is a control-architecture slice for the final FBC/statutory assurance gate. Neither is a statutory submission or approval. `Stage 12A` is a public-release control stage only. `Stage 13A` is a critical-path handover control stage only. `Stage 14A` is a source-note control pilot only. The future FBC/statutory decision gate remains `Stage 11` in this repo.

## Stage Risk Recording

Each stage should leave a register trail, not just a narrative note. The minimum stage trail is: issue row where a blocker or drift risk exists, risk row, requirements row, decision-log row, claim-evidence row, evidence-gap row where evidence remains incomplete, pitfall/checks row where overclaim risk exists, simulated sign-off row, approvals row and a stage-gate report. The stage risk matrix provides the cross-stage view.

| Stage | Purpose | Current status | Main gate report or control |
|---|---|---|---|
| Stage 0 | Repo architecture, operating model, registers and validation baseline | Complete with conditions | `review/stage_gate_reports/stage-0-architecture-and-controls-report.md` |
| Stage 1 | Source acquisition, extraction and first simulated assurance | Complete with conditions | `review/stage_gate_reports/stage-1-source-acquisition-and-simulated-assurance-report.md` |
| Stage 2 | Legal, governance, WECA/MCA, DfT and statutory route controls | Complete as a narrowing/control stage; no-go remains | `review/stage_gate_reports/stage-2l-context-management-report.md` |
| Stage 3A | Strategic assessment, objectives, benefits and package-funding controls | Complete as control architecture; Stage 3 no-go remains | `review/stage_gate_reports/stage-3a-strategic-assessment-control-report.md` |
| Stage 4A | Boundary, parking-inventory, DPIA and operations data-control architecture | Complete as control architecture; Stage 4 no-go remains | `review/stage_gate_reports/stage-4a-boundary-parking-control-report.md` |
| Stage 5A | Options, OAR, ASR, ASST, model-card and appraisal-control architecture | Complete as control architecture; Stage 5 no-go remains | `review/stage_gate_reports/stage-5a-options-appraisal-control-report.md` |
| Stage 6A | OBC section-readiness, claim-dependency and assembly controls | Complete as control architecture; OBC assembly no-go remains | `review/stage_gate_reports/stage-6a-obc-readiness-control-report.md` |
| Stage 7A | OBC assurance panel, gate checklist, red-team and decision-report controls | Complete as control architecture; Stage 7 OBC gate remains blocked | `review/stage_gate_reports/stage-7a-obc-assurance-gate-report.md` |
| Stage 8A | Consultation launch, material, stakeholder, privacy, accessibility and analysis controls | Complete as control architecture; consultation launch no-go remains | `review/stage_gate_reports/stage-8a-consultation-readiness-control-report.md` |
| Stage 9A | Public/officer assurance layer, pitfalls register, Nottingham lessons and readability controls | Complete as communication/control architecture; no substantive readiness gate closes | `review/stage_gate_reports/stage-9a-public-officer-assurance-report.md` |
| Stage 10A | Statutory confirmation dossier component, no-go and route-memorandum controls | Complete as control architecture; statutory submission remains blocked | `review/stage_gate_reports/stage-10a-statutory-dossier-control-report.md` |
| Stage 11A | Final FBC/statutory gate checklist, assurance panel, no-go and decision-report controls | Complete as control architecture; Stage 11 FBC/statutory gate remains blocked | `review/stage_gate_reports/stage-11a-fbc-statutory-gate-report.md` |
| Stage 11 | Future combined FBC/statutory decision gate | Blocked; no FBC approval, statutory submission, procurement approval or implementation recommendation | `python3 scripts/validate_fbc_statutory_gate.py --gate` |
| Stage 12A | Public repository release and no-overclaim controls | Complete as publication control; no WPL gate closes | `review/stage_gate_reports/stage-12a-public-release-gate-report.md` |
| Stage 13A | Critical-path handover, blocker mapping and 90-day planning controls | Complete as handover control; no WPL gate closes | `review/stage_gate_reports/stage-13a-critical-path-handover-gate-report.md` |
| Stage 14A | Source-note control pilot and source-use no-go controls | Complete as source-note control; `ISS-0007` remains open | `review/stage_gate_reports/stage-14a-source-note-control-report.md` |

## Detailed Notes

- [Stage 0 and Stage 1 Foundation](stage-0-1-foundation.md)
- [Stage 2 Legal and Governance](stage-2-legal-governance.md)
- [Stage 3A Strategic Assessment Controls](stage-3a-strategic-assessment.md)
- [Stage 4A Spatial and Parking Data Controls](stage-4a-spatial-data.md)
- [Stage 5A Options and Appraisal Controls](stage-5a-options-appraisal.md)
- [Stage 6A OBC Readiness Controls](stage-6a-obc-readiness.md)
- [Stage 7A OBC Assurance Controls](stage-7a-obc-assurance.md)
- [Stage 8A Consultation Readiness Controls](stage-8a-consultation-readiness.md)
- [Stage 9A Public And Officer Assurance](stage-9a-public-officer-assurance.md)
- [Stage 10A Statutory Dossier Controls](stage-10a-statutory-dossier.md)
- [Stage 11A FBC And Statutory Gate Controls](stage-11a-fbc-statutory-gate.md)
- [Stage 12A Public Release Controls](stage-12a-public-release.md)
- [Stage 13A Critical Path Handover Controls](stage-13a-critical-path-handover.md)
- [Stage 14A Source Note Controls](stage-14a-source-notes.md)

## Current Hard Blockers

- Bristol final WPL order-maker, statutory submitter and signatory route remains unresolved.
- WECA/MCA role, consent, consultation-response and final funding-dependency status remain unresolved.
- DfT WPL-specific process and any formal DfT response remain unresolved.
- Strategic problem definition, baseline, final objectives, theory of change, benefit claims and investment package remain unresolved.
- Authoritative boundary, spatial licences and workplace parking inventory are absent.
- DPIA, lawful basis and operating procedures are not complete.
- OAR, agreed ASR, completed ASST, completed/decision-grade model cards, model outputs, BCR and VFM category do not exist.
- OBC section evidence, OBC assembly, officer-review DOCX and Stage 7 assurance do not exist.
- Consultation launch authority, consultation materials, questionnaire, response data, privacy notice, accessibility-ready material and response-analysis plan do not exist.
- Public/officer summaries are explanatory only and must not be treated as approval, legal advice, OBC/FBC readiness or consultation authority.
- Statutory dossier controls are explanatory and control-only; no statutory submission or certified scheme order exists.
- Stage 11A final gate controls are explanatory and control-only; no FBC approval, statutory submission, procurement approval or implementation recommendation exists.
- Stage 12A public-release controls are explanatory and control-only; public visibility does not approve the WPL or close any readiness gate.
- Stage 13A critical-path controls are explanatory and control-only; work packages and the 90-day plan do not approve a programme, authorise spend or close blockers.
- Stage 14A source-note controls are explanatory and control-only; source notes do not verify all claims or close the acquired-source note backlog.
