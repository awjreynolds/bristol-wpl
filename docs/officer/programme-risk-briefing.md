# Programme Risk Briefing

Status: officer-facing simulation briefing.  
Date: 2026-06-26.

## Risk Pattern

The simulation has mostly completed control architecture, not substantive case evidence. The main risk is false readiness: treating a control template, bounded source search or simulated sign-off as if it were a real decision, legal view, model output, consultation document or public-body approval.

## Top Pitfalls

| Pitfall | Stage | Consequence | Current mitigation |
|---|---|---|---|
| Treating Bristol Stage One/OBC work as implementation approval | Stage 2 | Governance overclaim and public-law risk | Bristol decision chronology controls and no-go claims |
| Treating WECA/MCA strategy as consent or no-role evidence | Stage 2 | Wrong statutory or funding route | WECA/MCA role classifier and bounded context packet |
| Assuming Nottingham results transfer to Bristol | Stages 1 and 5 | Unsupported revenue, congestion, mode-share or employer claims | Transferability matrix and lessons register |
| Choosing a boundary before data is ready | Stage 4 | Invalid revenue, displacement, EqIA and consultation material | Boundary and parking inventory controls |
| Missing residential spillover and CPZ mitigation | Stage 4 | Resident impact, consultation challenge and operational cost | Displacement control and pitfalls register |
| Modelling before ASR/OAR/ASST | Stage 5 | Weak economic case and VFM challenge | Appraisal QA and model-card controls |
| Assembling OBC before evidence dependencies exist | Stage 6 | False officer/cabinet readiness | OBC assembly guard and section dependency register |
| Launching consultation without authority/material/privacy/accessibility controls | Stage 8 | Public-law and data-protection risk | Stage 8A launch-readiness controls |
| Treating statutory dossier controls as a submission pack | Stage 10A | Premature statutory submission, DfT-process overclaim and scheme-order challenge | Statutory dossier no-go register and `python3 scripts/validate_statutory_dossier.py --gate` |
| Treating final FBC/statutory gate controls as approval to submit or implement | Stage 11A | False FBC approval, procurement authority, legal review or implementation recommendation | FBC/statutory no-go register and `python3 scripts/validate_fbc_statutory_gate.py --gate` |
| Treating public repo visibility as public-body endorsement | Stage 12A | Public misunderstanding, political overclaim or reliance on simulation sign-offs | Public-release no-go register and `python3 scripts/validate_public_release.py` |
| Treating the critical path as an approved programme | Stage 13A | False authority to spend procure consult or progress gates | Handover no-go register and `python3 scripts/validate_handover.py` |
| Treating source notes as verified claim evidence | Stage 14A | False confidence in OBC/FBC drafting and unsupported source-heavy claims | Source-note no-go register and `python3 scripts/validate_source_notes.py` |
| Treating repository-side secret-scanning remediation as GitGuardian closure | Stage 14B-E | False security or hosted-alert claim | Secret-scan reports, history-rewrite reports and direct GitGuardian follow-up requirement |
| Treating source-note expansion as legal clearance or complete evidence review | Stage 15A | Legal-route overclaim and premature source-heavy drafting | Coverage-stage register, raw-omitted source controls and `python3 scripts/validate_source_notes.py` |
| Treating acquired-priority source-note completion as evidence completion | Stage 15B | Unsupported legal, WECA/MCA, DfT, appraisal, comparator, OBC/FBC or statutory claims | Stage 15B validator no-go wording and Stage 16A claim-summary handoff controls |
| Treating claim summaries as claim truth or drafting readiness | Stage 16A | Unsupported public, officer, legal, OBC/FBC, consultation or statutory reliance | `EG-0045`, claim-summary no-go register and `python3 scripts/validate_claim_summaries.py` |
| Treating editable authoring scaffolds as assembled decision papers | Stage 17A | Premature OBC/FBC, statutory, consultation, officer-review or PDF distribution claims | Authoring output register, blocked assembly scripts and `python3 scripts/validate_authoring_guardrails.py` |
| Treating Nottingham lessons as Bristol forecasts or ready parking mitigation | Stage 18A | Unsupported displacement, CPZ/RPZ, congestion, revenue, mode-shift, acceptability or employer-behaviour claims | Transferability matrix, displacement checklist and `python3 scripts/validate_nottingham_transferability.py` |
| Treating public pages, press releases and media articles as equivalent evidence | Stage 28A | Unsupported source-truth, media-accuracy, formal-decision, legal-route or WPL-readiness claims | Bristol live public-source coverage table, `SRC-BCC-0001`, `SRC-BCC-0002`, media context `SRC-BCC-0020` and `python3 scripts/validate_bristol_public_sources.py`; does not prove source truth, currentness or WPL readiness |
| Treating bounded subagent packets as proof of future compliance or assurance | Stage 29A | False confidence that future agents will avoid hallucination, have complete context or provide professional review | `docs/agents/subagent-stage-packet-template.md` and `python3 scripts/validate_subagent_context_control.py`; does not prove future agents obey instructions, evidence truth, legal correctness, professional assurance or WPL readiness |
| Treating Stage 29A validation coverage as command sufficiency or future compliance proof | Stage 30A | False confidence that Stage 29A commands were sufficient, independently authenticated or proved future agents will comply | `review/stage_gate_reports/stage-30a-validation-coverage-for-stage-29a-report.md` and `python3 scripts/validate_validation_coverage.py`; does not prove command sufficiency, future agent compliance, evidence truth, legal correctness, professional assurance or WPL readiness |
| Treating Stage 30A validation evidence as command sufficiency or assurance proof | Stage 31A | False confidence that Stage 30A logged commands prove evidence truth, source currentness, legal correctness or WPL readiness | `evidence/validation/stage-30a-validation-run-log.md` and `python3 scripts/validate_validation_evidence_log.py`; does not prove command sufficiency, command authenticity, evidence truth, legal correctness, professional assurance or WPL readiness |
| Treating a WECA-style simulated OBC as a real OBC or procurement authority | Stage 32A | False confidence that the repo now contains official officer advice, WECA/MCA endorsement, consultation readiness, statutory readiness or WPL readiness | `business_case/obc/simulated-working-draft/bristol-wpl-simulated-weca-style-obc.md`, `analysis/weca-obc-fbc-exemplars/stage-32a-weca-obc-fbc-exemplar-corpus.md` and `python3 scripts/validate_obc.py`; does not prove evidence truth, legal correctness, professional assurance or WPL readiness |
| Treating the shipped OBC simulation release as an approved OBC | Stage 33A | False confidence that the repo now contains a real Bristol OBC, officer advice, procurement authority, consultation readiness, statutory readiness or WPL readiness | `business_case/obc/simulation-release/bristol-wpl-outline-business-case-simulation-release.md`, `review/stage_gate_reports/stage-33a-obc-simulation-release-report.md` and `python3 scripts/validate_obc.py`; does not prove evidence truth, legal correctness, professional assurance or WPL readiness |

## Risk Registers

- `governance/risk_register.csv`
- `governance/issues_register.csv`
- `governance/pitfalls_register.csv`
- `governance/stage_risk_matrix.csv`

## Risk-Control Crosswalk

Use `docs/officer/risk-control-crosswalk.csv` when a reader needs the joined view: stage, blocker, issue ID, risk ID, pitfall ID, evidence-gap ID, current control, residual blocker, gate effect, owner, next evidence or decision, and validator.

The crosswalk is still a navigation control. It does not mean mitigations are complete, residual risk is accepted or a gate can pass.

## Escalation Rule

No P0 gate may pass. A P1 may pass only with a named condition, owner, deadline and accepted residual risk in the simulation registers. Real-world use would require human professional and public-authority approvals.
