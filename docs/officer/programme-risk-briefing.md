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
| Treating final FBC/statutory gate controls as approval to submit or implement | Stage 11A | False FBC approval, procurement authority, legal sign-off or implementation recommendation | FBC/statutory no-go register and `python3 scripts/validate_fbc_statutory_gate.py --gate` |
| Treating public repo visibility as public-body endorsement | Stage 12A | Public misunderstanding, political overclaim or reliance on simulation sign-offs | Public-release no-go register and `python3 scripts/validate_public_release.py` |
| Treating the critical path as an approved programme | Stage 13A | False authority to spend procure consult or progress gates | Handover no-go register and `python3 scripts/validate_handover.py` |
| Treating source notes as verified claim evidence | Stage 14A | False confidence in OBC/FBC drafting and unsupported source-heavy claims | Source-note no-go register and `python3 scripts/validate_source_notes.py` |
| Treating repository-side secret-scanning remediation as GitGuardian closure | Stage 14B-E | False security or hosted-alert claim | Secret-scan reports, history-rewrite reports and direct GitGuardian follow-up requirement |
| Treating source-note expansion as legal clearance or complete evidence review | Stage 15A | Legal-route overclaim and premature source-heavy drafting | Coverage-stage register, raw-omitted source controls and `python3 scripts/validate_source_notes.py` |
| Treating acquired-priority source-note completion as evidence completion | Stage 15B | Unsupported legal, WECA/MCA, DfT, appraisal, comparator, OBC/FBC or statutory claims | Stage 15B validator no-go wording and Stage 16A claim-summary handoff controls |
| Treating claim summaries as claim truth or drafting readiness | Stage 16A | Unsupported public, officer, legal, OBC/FBC, consultation or statutory reliance | `EG-0045`, claim-summary no-go register and `python3 scripts/validate_claim_summaries.py` |
| Treating editable authoring scaffolds as assembled decision papers | Stage 17A | Premature OBC/FBC, statutory, consultation, officer-review or PDF distribution claims | Authoring output register, blocked assembly scripts and `python3 scripts/validate_authoring_guardrails.py` |
| Treating Nottingham lessons as Bristol forecasts or ready parking mitigation | Stage 18A | Unsupported displacement, CPZ/RPZ, congestion, revenue, mode-shift, acceptability or employer-behaviour claims | Transferability matrix, displacement checklist and `python3 scripts/validate_nottingham_transferability.py` |

## Risk Registers

- `governance/risk_register.csv`
- `governance/issues_register.csv`
- `governance/pitfalls_register.csv`
- `governance/stage_risk_matrix.csv`

## Escalation Rule

No P0 gate may pass. A P1 may pass only with a named condition, owner, deadline and accepted residual risk in the simulation registers. Real-world use would require human professional and public-authority approvals.
