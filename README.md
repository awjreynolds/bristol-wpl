# Bristol Workplace Parking Levy Simulation

No Bristol Workplace Parking Levy has been approved by this repository.

This repo is a public, editable simulation of what a government-grade Bristol Workplace Parking Levy business-case and statutory-assurance workflow would need to control before a real authority could rely on it. It is a learning and due-diligence vehicle, not a policy approval, legal opinion, consultation launch, Outline Business Case, Full Business Case or statutory submission.

This repository is public. Stage 12A records that public visibility is not approval, not an official council publication and does not change the no-go position below.

## Current Workflow Snapshot

| Item | Current position |
|---|---|
| Last completed stage | Stage 15B: acquired-priority source-note completion. |
| What Stage 15B controls | It adds 36 further editable source notes and brings downloaded priority-1 source-note coverage to 91 controlled notes across Stage 14A, Stage 15A and Stage 15B. |
| What Stage 15B cannot do | It does not verify claims, provide legal advice, create claim-level source summaries, settle WECA/MCA or DfT positions, pass an OBC/FBC gate, launch consultation or authorise statutory submission. |
| Main live blockers | `ISS-0001`, `ISS-0002`, `ISS-0003`, `ISS-0004`, `ISS-0008`, `ISS-0011`, `ISS-0012`, `ISS-0015`, `ISS-0016`, `ISS-0025`, `EG-0044`. |

## Current No-Go Position

The current simulation position is **no-go for approval, consultation, OBC reliance, FBC reliance and statutory submission**.

The blockers are not cosmetic:

- Bristol's final WPL order-maker, statutory submitter and signatory route remain unresolved.
- WECA/MCA role, consent or no-role position, consultation-response position and funding-dependency status remain unresolved.
- No WPL-specific DfT procedural route or logged DfT response is held.
- No authoritative charging boundary has been selected.
- No workplace parking inventory exists.
- No displacement, CPZ/RPZ or residential spillover assessment exists.
- No OAR, agreed ASR, completed ASST, model outputs, BCR or VFM category exists.
- No OBC or FBC has been assembled.
- No consultation material, questionnaire, privacy notice, accessibility approval or response-analysis route exists.
- No claim-level source summaries exist for high-materiality legal, WECA/MCA, DfT, appraisal, comparator, consultation or public/officer claims.
- Nottingham lessons are lessons only. They cannot be copied into Bristol assumptions without Bristol transferability evidence.

## Risk Recording

Every stage records its risks and controls in the same audit trail:

- `governance/issues_register.csv` for stage issues and blockers.
- `governance/risk_register.csv` for risks, controls, residual status and owners.
- `governance/stage_risk_matrix.csv` for a stage-by-stage risk view.
- `governance/pitfalls_register.csv` for lessons, common failure modes and mitigations.
- `evidence/evidence_gap_register.csv` for evidence gaps and next actions.
- `governance/decision_log.csv`, `governance/approvals_register.csv` and `governance/simulation_signoff_register.csv` for the simulated decision trail.

Each stage gate report should explain what was controlled, what remains blocked and which risks were added or updated.

## What Can I Rely On?

You can rely on this repo as a controlled simulation record:

| Safe to rely on | Do not infer |
|---|---|
| It identifies evidence, decisions, risks and checks needed for a professional WPL workflow. | That Bristol City Council, WECA/MCA, DfT or the Secretary of State has approved anything in this repo. |
| It is public on GitHub and can be inspected as a learning record. | That publication approves the WPL, the business case, consultation or statutory submission. |
| It records agent-simulated legal, finance, appraisal, governance, data, consultation and red-team reviews. | That those agent sign-offs replace qualified human advice or public-authority decisions. |
| It has a stage-gate structure and validators that block readiness overclaims. | That a blocked gate is ready just because the template exists. |
| It maps Nottingham and comparator lessons. | That Nottingham charge levels, impacts, mode shift or congestion outcomes transfer to Bristol. |
| It uses editable Markdown, CSV, XLSX, JSON, HTML and GIS-ready artefacts. | That any authored PDF is an officer-distribution product. Authored PDFs are not allowed. |

## Where To Start

| Reader | Start here | Why |
|---|---|---|
| Public reader | `docs/public/README.md` | Plain-English explanation of what this is and is not. |
| Cabinet member or council leader | `docs/officer/assurance-dashboard.md` | One-page decision dashboard with blockers and safe statements. |
| Officer or programme manager | `docs/officer/programme-risk-briefing.md` | Programme risks, mitigations and next checks. |
| Officer planning next work | `docs/officer/next-steps-critical-path.md` | Critical path work packages and 90-day planning controls. |
| Evidence reviewer or drafter | `evidence/source_notes/README.md` | Source-note cohorts and claim-use limits; source-note backlog remains controlled at claim-summary level. |
| Public repo maintainer | `review/stage_gate_reports/stage-14b-public-repo-secret-scan-report.md` | GitGuardian/Grafana-token-pattern incident response, source omissions and secret-scan controls. |
| Maintainer considering history rewrite | `review/stage_gate_reports/stage-14c-history-rewrite-decision-report.md` | Dry-run result, force-push boundary and residual GitGuardian/history risk. |
| Maintainer checking rewrite completion | `review/stage_gate_reports/stage-14d-live-history-rewrite-completion-report.md` | Live force-push result, local and fresh-remote verification, and residual hosted-alert caveats. |
| Maintainer checking hosted alert status | `review/stage_gate_reports/stage-14e-hosted-alert-disposition-report.md` | Repository-side hosted-alert checks and remaining GitGuardian follow-up. |
| Legal or governance reviewer | `docs/officer/legal-and-governance-briefing.md` | Bristol, WECA/MCA, DfT and statutory route questions. |
| Transport economist or modeller | `analysis/economic/stage-5a-options-appraisal-control-package.md` | OAR, ASR, ASST, appraisal, model and Nottingham-transfer controls. |
| GIS, parking or data specialist | `analysis/spatial/stage-4a-boundary-and-parking-inventory-control-package.md` | Boundary, inventory, topology, DPIA and displacement controls. |
| Consultation, equality or accessibility specialist | `analysis/consultation/stage-8a-consultation-readiness-control-package.md` | Launch, material, privacy, accessibility and analysis controls. |
| Agent or technical contributor | `CODEX_MASTER_PROMPT.md` and `instructions/00-operating-model.md` | Source operating model and context discipline. |

## Visual Stage Map

The current workflow map is in `docs/visuals/stage-gate-map.mmd`. Stage 9A is the public/officer assurance layer. Stage 7 OBC, Stage 8 consultation launch and Stage 11 FBC/statutory gates remain blocked. Stage 10A is only a control layer for a future statutory dossier; Stage 11A is only a control layer for the final FBC/statutory gate. Stage 12A records the public repository release controls. Stage 13A records the critical-path handover controls; the critical path is not approval. Stage 14A creates a source-note pilot. Stage 14B records public-repo secret-scanning remediation after a GitGuardian detector collision. Stage 14C dry-runs the history-rewrite option. Stage 14D records the approved live history rewrite. Stage 14E records repository-side hosted-alert checks; GitGuardian disposition remains external. Stage 15A expands legal/governance source-note coverage. Stage 15B completes downloaded priority-1 source-note coverage only; the source-note backlog remains controlled for claim-level summaries and no WPL readiness gate changes.

```mermaid
flowchart LR
    S0["Stage 0-1<br/>Repo and evidence baseline"] --> S2["Stage 2<br/>Legal and governance controls"]
    S2 --> S3["Stage 3A<br/>Strategic controls"]
    S3 --> S4["Stage 4A<br/>Boundary and parking controls"]
    S4 --> S5["Stage 5A<br/>Appraisal controls"]
    S5 --> S6["Stage 6A<br/>OBC readiness controls"]
    S6 --> S7A["Stage 7A<br/>OBC assurance controls"]
    S7A --> S7["Stage 7<br/>OBC gate BLOCKED"]
    S7 --> S8A["Stage 8A<br/>Consultation controls"]
    S8A --> S8["Stage 8<br/>Consultation launch BLOCKED"]
    S8 --> S9["Stage 9A<br/>Public/officer assurance"]
    S9 --> S10A["Stage 10A<br/>Statutory dossier controls"]
    S10A --> S11A["Stage 11A<br/>FBC/statutory gate controls"]
    S11A --> S11["Stage 11<br/>FBC and statutory gate BLOCKED"]
    S11 --> S12A["Stage 12A<br/>Public release controls"]
    S12A --> S13A["Stage 13A<br/>Critical path handover controls"]
    S13A --> S14A["Stage 14A<br/>Source-note controls"]
    S14A --> S14B["Stage 14B<br/>Public-repo secret-scan controls"]
    S14B --> S14C["Stage 14C<br/>History rewrite dry run"]
    S14C --> S14D["Stage 14D<br/>Live history rewrite"]
    S14D --> S14E["Stage 14E<br/>Hosted alert disposition"]
    S14E --> S15A["Stage 15A<br/>Source-note expansion"]
    S15A --> S15B["Stage 15B<br/>Acquired-priority source-note completion"]
```

## Stage 9A Status

Stage 9A adds the public/officer assurance layer:

- public summary and evidence assumptions;
- officer assurance dashboard;
- legal and governance briefing;
- programme risk briefing;
- Nottingham and comparator lessons briefing;
- checks and balances map;
- document map;
- pitfalls register;
- stage risk matrix;
- real-world adoption checklist;
- Nottingham lessons register;
- officer-pack and Nottingham-transferability validators.

Stage 9A makes the repo easier to understand. It does **not** close any substantive Bristol, WECA/MCA, DfT, spatial, appraisal, OBC, consultation, finance, data-protection or statutory blocker.

## Stage Workflow

The stage-by-stage workflow narrative is maintained in `docs/stages/`:

- `docs/stages/README.md`
- `docs/stages/stage-0-1-foundation.md`
- `docs/stages/stage-2-legal-governance.md`
- `docs/stages/stage-3a-strategic-assessment.md`
- `docs/stages/stage-4a-spatial-data.md`
- `docs/stages/stage-5a-options-appraisal.md`
- `docs/stages/stage-6a-obc-readiness.md`
- `docs/stages/stage-7a-obc-assurance.md`
- `docs/stages/stage-8a-consultation-readiness.md`
- `docs/stages/stage-9a-public-officer-assurance.md`
- `docs/stages/stage-10a-statutory-dossier.md`
- `docs/stages/stage-11a-fbc-statutory-gate.md`
- `docs/stages/stage-12a-public-release.md`
- `docs/stages/stage-13a-critical-path-handover.md`
- `docs/stages/stage-14a-source-notes.md`
- `docs/stages/stage-14b-public-repo-secret-scanning.md`
- `docs/stages/stage-14c-history-rewrite.md`
- `docs/stages/stage-14d-live-history-rewrite.md`
- `docs/stages/stage-14e-hosted-alert-disposition.md`
- `docs/stages/stage-15a-source-note-expansion.md`
- `docs/stages/stage-15b-source-note-completion.md`

Each completed stage package should be committed and pushed before the next stage begins. Detailed discoveries, data points and unresolved issues live in the stage docs and controlled registers.

## Evidence State

- `evidence/source_register.csv` contains 111 rows.
- 91 sources are downloaded and tracked in the current public tree.
- 3 public Bristol committee-pack PDFs were downloaded and extracted but their raw binaries are now omitted from the public GitHub tree after a GitGuardian legacy Grafana/Power BI detector collision: `SRC-BCC-0005`, `SRC-BCC-0011` and `SRC-BCC-0015`.
- 16 sources remain seeded but not downloaded.
- 1 source acquisition failed: `SRC-ACADEMIC-0001`.
- `evidence/extraction_manifest.csv` is the current extraction state: 91 extracted, 2 extracted with raw PDFs omitted from the public repo, 1 extracted with redacted text and raw PDF omitted, 16 skipped because not downloaded and 1 skipped because acquisition failed.
- `evidence/extraction_log.csv` is the append-only extraction audit log.
- `evidence/source_notes/source-note-coverage-register.csv` now tracks 91 controlled source notes: 13 Stage 14A pilot notes, 42 Stage 15A legal/governance expansion notes and 36 Stage 15B acquired-priority completion notes. The source-note backlog remains controlled because claim-level source summaries remain open under `EG-0044`.

## Controlled Gate Reports

Current gate reports live under `review/stage_gate_reports/`. Key current reports:

- `review/stage_gate_reports/stage-1-source-acquisition-and-simulated-assurance-report.md`
- `review/stage_gate_reports/stage-2l-context-management-report.md`
- `review/stage_gate_reports/stage-3a-strategic-assessment-control-report.md`
- `review/stage_gate_reports/stage-4a-boundary-parking-control-report.md`
- `review/stage_gate_reports/stage-5a-options-appraisal-control-report.md`
- `review/stage_gate_reports/stage-6a-obc-readiness-control-report.md`
- `review/stage_gate_reports/stage-7a-obc-assurance-gate-report.md`
- `review/stage_gate_reports/stage-8a-consultation-readiness-control-report.md`
- `review/stage_gate_reports/stage-9a-public-officer-assurance-report.md`
- `review/stage_gate_reports/stage-10a-statutory-dossier-control-report.md`
- `review/stage_gate_reports/stage-11a-fbc-statutory-gate-report.md`
- `review/stage_gate_reports/stage-12a-public-release-gate-report.md`
- `review/stage_gate_reports/stage-13a-critical-path-handover-gate-report.md`
- `review/stage_gate_reports/stage-14a-source-note-control-report.md`
- `review/stage_gate_reports/stage-14b-public-repo-secret-scan-report.md`
- `review/stage_gate_reports/stage-14c-history-rewrite-decision-report.md`
- `review/stage_gate_reports/stage-14d-live-history-rewrite-completion-report.md`
- `review/stage_gate_reports/stage-14e-hosted-alert-disposition-report.md`
- `review/stage_gate_reports/stage-15a-source-note-expansion-report.md`
- `review/stage_gate_reports/stage-15b-source-note-completion-report.md`

## Context Discipline

For main-agent legal, governance, statutory, OBC/FBC, DfT, WECA/MCA, order-change or consultation work after Stage 2L, start with:

- `analysis/legal/post-stage-2-legal-governance-context-packet.md`

For public/officer-facing explanation after Stage 9A, also start with:

- `docs/public/README.md`
- `docs/officer/assurance-dashboard.md`
- `docs/officer/checks-and-balances-map.md`
- `governance/pitfalls_register.csv`
- `governance/stage_risk_matrix.csv`
- `analysis/economic/nottingham_lessons_register.csv`

For all future stages, also apply `instructions/20-stage-continuation-and-context-control.md`. Subagents should receive bounded task packets rather than the whole context set, and the main agent should commit and push each validated stage before moving on.

## Repeatable Commands

```bash
make validate
make officer-pack-qa
make nottingham-qa
make strategic-qa
make spatial-qa
make appraisal-qa
make obc-qa
make obc-assurance-qa
make consultation-qa
make statutory-qa
make fbc-statutory-qa
make public-release-qa
make handover-qa
make source-notes-qa
make secrets-qa
make red-team
python3 scripts/acquire_sources.py --priority 1_must
python3 scripts/extract_sources.py
python3 scripts/build_register_workbooks.py
python3 scripts/scan_source_terms.py
python3 scripts/build_document_templates.py
```

`make gate-obc` and `make gate-fbc` are expected to fail while open P0/P1 blockers remain. That failure is intentional.

## Format And Distribution Rules

Officer review and distribution copies must be editable DOCX/XLSX/HTML or controlled Markdown as appropriate. PDFs are allowed only as downloaded third-party raw evidence under `evidence/raw/**`, never as officer-distribution outputs. If a raw evidence PDF contains token-like payloads or hosted secret-scanner collisions, omit it from the public GitHub tree, retain the source URL/hash in registers and run `make secrets-qa`.

## Source Of Truth

- `CODEX_MASTER_PROMPT.md`
- `instructions/00-operating-model.md`
- controlled Markdown, CSV, XLSX, JSON, HTML and GIS artefacts generated under this repo

This is not legal advice, statutory confirmation, financial certification or approval by any public body. All sign-offs are agentic simulation sign-offs unless explicitly replaced in a future real-world process.
