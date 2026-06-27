# Cabinet And Officer Navigation Guide

Status: public/officer comprehension control.  
Date: 2026-06-26.

## Thirty-Second Status

No Bristol Workplace Parking Levy has been approved by this repository.

The repo records a simulation workflow: evidence gathered, risks found, controls created and gates still blocked. It does not approve consultation, spending, procurement, an OBC, an FBC, a statutory submission or implementation.

## Gate Taxonomy

| Term | Plain meaning | What it does not mean |
|---|---|---|
| Control stage | A stage that creates checks, registers, templates, validators or readable explanations. | A real decision or readiness approval. |
| Readiness gate | A point where real evidence would need to be sufficient before progressing. | Passed just because a template or validator exists. |
| Blocker | A missing decision, evidence item, legal route, model, consultation step or operational control. | A minor drafting issue. |
| Simulation sign-off | An agent-recorded QA conclusion inside the simulation. | Human officer, legal, finance, modelling, consultation or elected-member sign-off. |

## Current Gate Board

| Gate | Current status | Why |
|---|---|---|
| OBC reliance | Blocked | No boundary, parking inventory, appraisal outputs, evidence-populated sections or real officer/legal review. |
| Consultation launch | Blocked | No launch authority, materials, privacy notice, accessibility approval or response-analysis route. |
| Statutory dossier | Blocked | No certified scheme order, confirmation route, consultation statement, boundary schedule or legal sign-off. |
| FBC/statutory decision | Blocked | No FBC evidence packet, Monitoring Officer route, Section 151 review, DfT/WECA disposition or implementation readiness. |
| Spend/procurement | Blocked | The critical path is a planning control only and does not authorise expenditure or procurement. |
| Public repository | Controlled only | Public visibility is not official council publication, endorsement or approval. |
| Bristol live public-source coverage | Controlled only | `SRC-BCC-0001`, `SRC-BCC-0002` and media context `SRC-BCC-0020` are visible and claim-limited; this does not prove source truth, currentness, legal correctness, formal decision status or WPL readiness. |
| Subagent context-control hardening | Controlled only | Future-stage bounded packet instructions and `docs/agents/subagent-stage-packet-template.md` exist; this does not prove future agents obey instructions, evidence truth, legal correctness, professional assurance, substantive gate correctness or WPL readiness. |
| Stage 29A validation coverage | Controlled only | Stage 29A validation rows and log are covered by `scripts/validate_validation_coverage.py`; this does not prove command sufficiency, command authenticity, future agent compliance, evidence truth, legal correctness, professional assurance or WPL readiness. |

## Top Blockers In Plain English

| Blocker | IDs | Consequence | Next proof needed |
|---|---|---|---|
| Who legally makes and submits the scheme? | `ISS-0001`; `RISK-0001` | Wrong democratic or statutory route. | Monitoring Officer route and decision authority evidence. |
| What is WECA/MCA's role? | `ISS-0002`; `RISK-0002` | Wrong consent, no-role or funding assumption. | Current-law role and funding-dependency disposition. |
| Where is the boundary and parking base? | `ISS-0003`; `EG-0014`; `RISK-0004` | Revenue, displacement, equality and consultation claims cannot be relied on. | Authoritative GIS, licences and canonical parking inventory. |
| What is the business-case value? | `ISS-0004`; `RISK-0005` | BCR, VFM and preferred-option claims cannot be made. | OAR, ASR, ASST, model outputs and uncertainty analysis. |
| Can Nottingham lessons transfer? | `ISS-0005`; `ISS-0028`; `EG-0046`; `RISK-0031` | Bristol impacts, revenue, congestion, acceptability and CPZ/RPZ readiness could be overstated. | Bristol-specific transferability evidence and current Nottingham refresh. |
| Can consultation launch? | `ISS-0012`; `RISK-0015` | Public-law, privacy or accessibility challenge. | Authority, materials, privacy, accessibility and response-analysis controls. |

## Question-Led Routes

| Question | Start here | Then deep dive |
|---|---|---|
| Can this be approved now? | `docs/officer/assurance-dashboard.md` | `governance/issues_register.csv` and `governance/risk_register.csv` |
| What could go wrong? | `docs/officer/risk-gate-atlas.md` | `docs/officer/risk-control-crosswalk.csv` |
| What does Nottingham tell us? | `docs/officer/nottingham-and-comparator-lessons.md` | `analysis/economic/nottingham-transferability-matrix.csv` |
| What is known, assumed, missing or prohibited? | `docs/public/what-this-repo-can-and-cannot-tell-you.md` | `docs/public/evidence-and-assumptions-summary.md` |
| Are the three Bristol public links already tracked? | `docs/public/bristol-live-public-source-status.md` | `evidence/bristol_public_source_status.csv` and `scripts/validate_bristol_public_sources.py` |
| How should future stages use subagents without context bloat? | `docs/agents/subagent-stage-packet-template.md` | `instructions/20-stage-continuation-and-context-control.md` and `scripts/validate_subagent_context_control.py` |
| Is Stage 29A validation coverage tracked? | `review/stage_gate_reports/stage-30a-validation-coverage-for-stage-29a-report.md` | `scripts/validate_validation_coverage.py` and `tests/test_validation_coverage.py` |
| What documents exist? | `docs/officer/document-map.md` | `docs/authoring/README.md` |

## Simulation Sign-Off Rule

Every sign-off in this repository is an agentic simulation sign-off unless a future real-world process replaces it. Treat it as a QA record, not as officer advice, legal advice, financial certification, modelling assurance, consultation approval or democratic authority.
