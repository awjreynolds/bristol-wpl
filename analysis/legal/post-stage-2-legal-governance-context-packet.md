# Post-Stage 2 Legal and Governance Context Packet

Status: simulation context-management control.  
Date: 2026-06-26.  
Owner: Programme Orchestrator.  
Review status: Stage 2L simulation reviewed.

This packet is a bounded-read control for future Codex agents working on the Bristol Workplace Parking Levy simulation. It is not legal advice, statutory confirmation, financial certification, officer approval or approval by Bristol City Council, WECA/MCA, DfT or the Secretary of State.

## Purpose

Stage 2B to Stage 2K created many legal, governance, WECA/MCA, DfT and order-change controls. Future agents must not load the whole evidence base by default or promote partial controls into readiness claims.

Use this packet to:

- select the minimum files needed for the task;
- keep unresolved P0/P1 blockers visible;
- stop repeated overclaiming of Bristol, WECA/MCA and DfT status;
- decide when raw evidence or full review files must be opened;
- give subagents precise task packets with review criteria.

This packet does not close any legal, statutory, spatial, appraisal, finance, consultation, data-protection or operational gap.

## Mandatory First Read for Main Agents

Every future main coordinating agent working on legal, governance, statutory, OBC, FBC, DfT, WECA/MCA, order-change or consultation material must read these before drafting:

| File | Purpose |
|---|---|
| `AGENTS.md` | Non-negotiables and repo-level agent rules. |
| `README.md` | Current gate position and live source/evidence state. |
| `instructions/00-operating-model.md` | Full operating model and evidence hierarchy. |
| `instructions/10-stage-gates.md` | Gate rule summary. |
| `governance/stage-gate-plan.md` | Current stage-gate evidence and blocking conditions. |
| `governance/issues_register.csv` | Open issue status and gate blockers. |
| `governance/risk_register.csv` | P0/P1 risk state and accepted controls. |
| `evidence/evidence_gap_register.csv` | Evidence gaps that must not be filled by assumption. |
| `governance/approvals_register.csv` | Simulation approval status and no-go outcomes. |
| `governance/simulation_signoff_register.csv` | Scope and limits of simulated sign-offs. |
| `governance/requirements_register.csv` | Live control requirements for later stages. |

`CODEX_MASTER_PROMPT.md` and `instructions/00-operating-model.md` are expected to remain identical. Do not read both unless checking copy drift.

Do not pass this whole list to every subagent. Subagents should receive a smaller task packet built from this context, normally capped at 5 to 7 primary files, with the exact question, banned claims and P0/P1 blockers extracted into the prompt.

## Stage 2B-K Compact Control Set

Use the stage-gate reports as the first-pass summary of detailed Stage 2 findings:

| Stage | First-pass file |
|---|---|
| Stage 2B current-law role map | `review/stage_gate_reports/stage-2b-current-law-role-map-report.md` |
| Stage 2C Bristol authority source chain | `review/stage_gate_reports/stage-2c-bristol-authority-route-report.md` |
| Stage 2D Bristol internal decision route | `review/stage_gate_reports/stage-2d-bristol-internal-decision-route-report.md` |
| Stage 2E WECA/MCA evidence language | `review/stage_gate_reports/stage-2e-weca-mca-role-classification-report.md` |
| Stage 2F WECA/MCA current-law function map | `review/stage_gate_reports/stage-2f-current-law-function-map-report.md` |
| Stage 2G WECA/MCA meeting-record search | `review/stage_gate_reports/stage-2g-meeting-record-search-report.md` |
| Stage 2H WECA/MCA package funding and assurance | `review/stage_gate_reports/stage-2h-package-funding-assurance-report.md` |
| Stage 2I Bristol final order and submission route | `review/stage_gate_reports/stage-2i-final-order-submission-route-report.md` |
| Stage 2J DfT process and engagement classification | `review/stage_gate_reports/stage-2j-dft-procedural-expectations-report.md` |
| Stage 2K revocation, variation and consultation | `review/stage_gate_reports/stage-2k-revocation-variation-report.md` |

Open full analysis notes only when the task requires the detailed legal chain, exact wording, source line references or reopening of a Stage 2 control.

## Domain Add-Ons

### Legal, Statutory and Governance Work

Add:

- `statutory_dossier/statutory_route_note.md`
- `statutory_dossier/legal_compliance_matrix.csv`
- `statutory_dossier/business_case_to_statutory_crosswalk.csv`
- `analysis/legal/stage-2i-final-order-submission-route-control.md`
- `statutory_dossier/council_resolutions/bristol_wpl_decision_route_map.md`

Do not draft final order-making, statutory submission, signatory, Full Council, committee or officer route conclusions without applying the Stage 2I decision box.

### OBC and FBC Work

Add:

- `statutory_dossier/business_case_to_statutory_crosswalk.csv`
- the exact target section under `business_case/`
- the relevant stage-gate report for any claim the section relies on

Do not load the whole OBC/FBC tree by default. Most business-case files are templates or working drafts and are not evidence of readiness.

### WECA/MCA Work

Add:

- `analysis/weca-role-and-evidence/post-stage-2h-context-packet.md`
- `analysis/weca-role-and-evidence/support-status.md`
- `analysis/weca-role-and-evidence/funding-and-assurance-dependency-matrix.md`
- `analysis/weca-role-and-evidence/stage-2h-package-funding-assurance-trigger-map.md`
- `governance/dependencies_register.csv`

Do not treat strategy, assurance, CRSTS, TCR, mass-transit, investment-fund or delivery-assurance material as WPL approval, support, objection, consent, sponsorship, funding approval, statutory confirmation, transferred function or no-role evidence.

### DfT Work

Add:

- `analysis/legal/stage-2j-dft-procedural-expectations-and-engagement-classification.md`
- `statutory_dossier/dft_pre_application/questions_for_dft.md`
- `statutory_dossier/dft_pre_application/confirmation_dossier_checklist.md`
- `statutory_dossier/dft_pre_application/engagement_log.csv`

Do not treat generic DfT business-case guidance, TAG guidance, local engagement or GOV.UK search results as DfT approval, accepted dossier format, statutory confirmation or WPL-specific process closure.

### Order-Change, Revocation and Consultation Work

Add:

- `analysis/legal/stage-2k-revocation-variation-and-consultation-control.md`
- `statutory_dossier/draft_scheme_order/scheme_order_working_draft.md`
- `statutory_dossier/consultation_statement/consultation_statement.md`

Every order-change note must distinguish initial order, ordinary variation, RPI-only variation, revocation, licence-level variation, statutory consultation, public-law consultation, inquiry, publication, objection, notice, DfT process and Bristol decision/signatory authority.

## Do Not Read Unless Needed

Do not open these by default:

- `evidence/raw/**`
- `evidence/processed/**`
- acquisition logs and extraction logs
- full source packs
- specialist review files under `review/legal_review/`, `review/peer_review/`, `review/financial_review/`, `review/red_team/` and `review/analytical_assurance/`
- full WECA/MCA history files beyond the Stage 2H packet
- the full OBC/FBC tree

Open them only to verify a specific claim, source line, provenance issue, contradiction, newly discovered document or review challenge.

## Banned Claims

Future agents must not make these claims unless a later controlled source and simulation review explicitly changes the status:

- Bristol final WPL licensing-scheme order-maker, statutory submitter or signatory route is settled.
- Bristol committee, Full Council or officer-only route is confirmed for final order-making.
- WECA/MCA has approved, supported, objected to, consented to, funded, sponsored or confirmed the WPL.
- WECA/MCA has no role, no consent role or no funding dependency.
- DfT has approved, cleared, accepted or confirmed the WPL.
- Generic DfT/TAG guidance is the WPL-specific confirmation process.
- A bounded search absence proves a legal absence, no-role position or no-procedure position.
- The RPI-only variation exemption applies to initial orders, ordinary variations, revocation or broader scheme changes.
- Stage 2 controls mean the OBC, FBC, consultation, operations or statutory submission is ready.
- Agentic simulation sign-off has real-world professional, statutory, legal, financial, officer or public-authority effect.

## Required Subagent Packet Rules

Subagent packets must include:

- maximum 5 to 7 primary files unless a larger review is justified;
- exact question and claim boundary;
- files the subagent must not open unless needed;
- acceptance criteria and banned claims;
- source hierarchy and citation expectations;
- explicit P0/P1 blocker checks;
- required output format with findings, limitations, confidence and simulation sign-off scope.

For legal/governance subagents, include the relevant risk IDs and issue IDs in the prompt. For WECA/MCA tasks, include RISK-0002 and RISK-0011. For Bristol final route tasks, include RISK-0001 and ISS-0001. For DfT tasks, include RISK-0003 and ISS-0008. For order-change tasks, include EG-0022.

## Context Escalation Decision Tree

1. Main coordinating agent starts with the mandatory first read and this packet.
2. Add the domain add-on files for the current task.
3. Read the compact Stage 2B-K gate report for each claim being used.
4. If the claim still needs source-line support, open the full analysis note.
5. If the full analysis note is insufficient or contradicted, open processed source extracts.
6. Open raw evidence only when needed to resolve provenance, extraction or exact-source questions.
7. If a later source changes a control, update the risk, issue, requirement, approval and sign-off registers in the same work package.

## Current Stage 2L Outcome

Stage 2L controls future context use. It does not alter the no-go state for:

- preferred scheme selection;
- statutory consultation launch;
- OBC recommendation;
- FBC readiness;
- final order-making;
- statutory submission;
- operational readiness;
- WECA/MCA role or funding dependency;
- DfT process readiness.
