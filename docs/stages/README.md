# Stage Workflow Index

Status: working stage narrative.  
Date: 2026-06-26.

This directory explains the workflow stage by stage. It is a navigation and audit aid only; controlled decisions remain in the registers, gate reports and source-linked analysis files.

A control stage does not pass a readiness gate. It records checks and gaps so a later real-world process can decide what evidence, authority and professional review would be needed.

## Commit Discipline

Each completed stage package should be committed and pushed before the next stage begins. The README should stay as the high-level entry point; detailed stage findings belong here when they would make the README too large.

## Current Stage Map

Terminology note: `Stage 10A` is a control-architecture slice for a future statutory confirmation dossier. `Stage 11A` is a control-architecture slice for the final FBC/statutory assurance gate. Neither is a statutory submission or approval. `Stage 12A` is a public-release control stage only. `Stage 13A` is a critical-path handover control stage only. `Stage 14A` is a source-note control pilot only. `Stage 14B` is a public-repo secret-scanning remediation control only. `Stage 14C` is a history-rewrite dry-run and approval-boundary control only. `Stage 14D` is live history-rewrite execution evidence only. `Stage 14E` is hosted-alert disposition tracking only. `Stage 15A` is a source-note expansion control only. `Stage 15B` is acquired-priority source-note completion only, not claim verification or evidence completion. `Stage 16A` is claim-summary control for the current claim matrix only, not claim truth or readiness. `Stage 17A` is editable authoring guardrails only, not assembled documents or distribution readiness. `Stage 18A` is Nottingham/comparator transferability control only, not evidence that Bristol impacts, mitigation readiness, charge levels, revenue or mode/congestion outcomes transfer. `Stage 19A` is public/cabinet comprehension control only, not evidence that readers understand the repo or that professional/public-authority assurance exists. `Stage 20A` is static visual/accessibility QA control only, not rendered accessibility review, user testing or certification. `Stage 21A` is repo-local link/navigation integrity control only, not external-link liveness, evidence accuracy, content truth or readiness. The future FBC/statutory decision gate remains `Stage 11` in this repo.

## Gate Taxonomy

| Type | Meaning | Current effect |
|---|---|---|
| `A` control stage | Creates checks, registers, templates, validators or explanations. | Does not pass a readiness gate. |
| Numbered readiness gate | Future point where real evidence and authority would be assessed. | Currently blocked where evidence is absent. |
| Public/cabinet guide | Helps readers navigate the simulation. | Does not approve policy, spend, consultation, OBC, FBC or statutory submission. |

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
| Stage 14B | Public-repo secret-scanning remediation after GitGuardian detector collision | Complete as current-tree control; history and remote alert disposition remain open | `review/stage_gate_reports/stage-14b-public-repo-secret-scan-report.md` |
| Stage 14C | History rewrite dry run and force-push decision boundary | Dry run complete; live rewrite subsequently completed in Stage 14D | `review/stage_gate_reports/stage-14c-history-rewrite-decision-report.md` |
| Stage 14D | Live history rewrite execution and post-push verification | Complete as repository-history remediation; hosted alert disposition remains external | `review/stage_gate_reports/stage-14d-live-history-rewrite-completion-report.md` |
| Stage 14E | Hosted alert disposition and repository-side checks | Repository-side checks complete; GitGuardian disposition remains external | `review/stage_gate_reports/stage-14e-hosted-alert-disposition-report.md` |
| Stage 15A | Source-note expansion for legal and Bristol governance sources | Complete as source-note expansion; later Stage 15B closes downloaded priority note coverage only | `review/stage_gate_reports/stage-15a-source-note-expansion-report.md` |
| Stage 15B | Acquired-priority source-note completion for remaining downloaded priority-1 sources | Complete as source-note completion; claim-level source summaries and all WPL readiness gates remain open | `review/stage_gate_reports/stage-15b-source-note-completion-report.md` |
| Stage 16A | Current-claim-matrix claim-summary control | Complete as claim-summary control; future drafting-specific summaries and all WPL readiness gates remain open | `review/stage_gate_reports/stage-16a-claim-summary-control-report.md` |
| Stage 17A | Editable document assembly and authoring guardrails | Complete as authoring control; assembled OBC/FBC/statutory/consultation/officer outputs remain blocked | `review/stage_gate_reports/stage-17a-editable-document-assembly-report.md` |
| Stage 18A | Nottingham displacement and transferability controls | Complete as comparator-learning control; Bristol impact transfer, CPZ/RPZ readiness, current Nottingham refresh and all WPL readiness gates remain blocked | `review/stage_gate_reports/stage-18a-nottingham-displacement-transferability-report.md` |
| Stage 19A | Public and cabinet comprehension controls | Complete as navigation/comprehension control; user testing, professional assurance and all WPL readiness gates remain blocked | `review/stage_gate_reports/stage-19a-public-cabinet-comprehension-report.md` |
| Stage 20A | Visual and accessibility static QA controls | Complete as static-source visual QA control; rendered accessibility review user testing and all WPL readiness gates remain blocked | `review/stage_gate_reports/stage-20a-visual-accessibility-qa-report.md` |
| Stage 21A | Link and navigation integrity controls | Complete as repo-local navigation control; external liveness evidence accuracy content truth and all WPL readiness gates remain blocked | `review/stage_gate_reports/stage-21a-link-navigation-integrity-report.md` |

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
- [Stage 14B Public Repo Secret Scanning](stage-14b-public-repo-secret-scanning.md)
- [Stage 14C History Rewrite Decision](stage-14c-history-rewrite.md)
- [Stage 14D Live History Rewrite](stage-14d-live-history-rewrite.md)
- [Stage 14E Hosted Alert Disposition](stage-14e-hosted-alert-disposition.md)
- [Stage 15A Source Note Expansion](stage-15a-source-note-expansion.md)
- [Stage 15B Source Note Completion](stage-15b-source-note-completion.md)
- [Stage 16A Claim Summary Control](stage-16a-claim-summary-control.md)
- [Stage 17A Editable Document Assembly](stage-17a-editable-document-assembly.md)
- [Stage 18A Nottingham Displacement And Transferability](stage-18a-nottingham-displacement-transferability.md)
- [Stage 19A Public And Cabinet Comprehension](stage-19a-public-cabinet-comprehension.md)
- [Stage 20A Visual And Accessibility QA](stage-20a-visual-accessibility-qa.md)
- [Stage 21A Link And Navigation Integrity](stage-21a-link-navigation-integrity.md)

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
- Stage 14B public-repo secret-scanning controls are explanatory and current-tree only; they do not revoke tokens, close GitGuardian remotely, rewrite history or change any WPL readiness gate.
- Stage 14C history-rewrite controls were dry-run and decision-only; they did not themselves close GitGuardian remotely or change any WPL readiness gate.
- Stage 14D live history-rewrite controls record repository-history remediation only; they do not close GitGuardian remotely, clean forks or old clones, revoke tokens or change any WPL readiness gate.
- Stage 14E hosted-alert disposition controls record repository-side checks only; they do not close GitGuardian remotely, revoke tokens or change any WPL readiness gate.
- Stage 15A source-note expansion controls are explanatory and control-only; later Stage 15B closes downloaded priority note coverage only.
- Stage 15B source-note completion controls are explanatory and control-only; they do not verify claims, create claim-level summaries, provide legal advice, settle WECA/MCA or DfT positions, prove appraisal compliance, transfer Nottingham or comparator findings to Bristol or change any WPL readiness gate.
- Stage 16A claim-summary controls are explanatory and control-only; they do not prove claim truth, provide legal advice, cover future drafting-specific claims, settle WECA/MCA or DfT positions, prove appraisal compliance, transfer Nottingham or comparator findings to Bristol or change any WPL readiness gate.
- Stage 17A editable authoring controls are explanatory and control-only; they do not assemble an OBC, FBC, statutory dossier, consultation pack, officer-review DOCX, public pack, scheme order, statutory submission or authored officer-distribution PDF.
- Stage 18A Nottingham transferability controls are explanatory and control-only; they do not prove Bristol impacts, select CPZ/RPZ mitigation, refresh current Nottingham evidence or close spatial, appraisal, consultation, OBC, FBC or statutory gates.
- Stage 19A public/cabinet comprehension controls are explanatory and control-only; they do not prove reader understanding, provide professional assurance, close any readiness gate or replace officer, legal, finance, modelling, consultation, equalities, data-protection or elected-member decisions.
- Stage 20A visual/accessibility controls are explanatory and static-source-only; they do not prove rendered accessibility, user comprehension, screen-reader performance, colour-blind usability, mobile usability, certification or WPL readiness.
- Stage 21A link/navigation controls are explanatory and repo-local-only; they do not prove external link liveness, evidence accuracy, content truth, public comprehension, accessibility assurance or WPL readiness.
