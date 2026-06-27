# Bristol WPL Simulation Public Summary

Status: public-facing simulation summary.  
Date: 2026-06-26.

## Plain-English Status

No Bristol Workplace Parking Levy has been approved by this repository.

This repo is a learning and assurance simulation. It shows the evidence, decisions, risks, checks and documents that would be needed before a council could safely move towards an Outline Business Case, public consultation, Full Business Case or statutory confirmation dossier.

The GitHub repository is public. Public visibility is not approval, endorsement, legal advice, consultation launch authority or statutory readiness.

Editable files in this repo are drafting scaffolds, not finished documents. They show what would need to be checked before a real decision, but they do not make or approve that decision.

## Common Terms

| Term | Meaning here |
|---|---|
| WPL | Workplace Parking Levy. |
| OBC | Outline Business Case. A simulation release exists in this repo; a real approved OBC is not assembled or approved. |
| FBC | Full Business Case. It is not assembled in this repo. |
| WECA/MCA | West of England Combined Authority / Mayoral Combined Authority role, still unresolved for WPL purposes. |
| DfT | Department for Transport. No WPL-specific DfT process response is held. |
| CPZ/RPZ | Controlled or residents' parking zone. No Bristol CPZ/RPZ mitigation is selected, costed, consulted on or ready. |
| BCR/VFM | Benefit-cost ratio / value for money. No BCR or VFM category exists. |
| Green control | A repo control exists. It does not mean a real scheme is ready. |

Some source pages change or disappear. A source-link/freshness check records what was reachable, when it was checked and whether a source needs refresh before reliance. It is not proof that the source is complete, legally current or enough for a real decision.

Stage 28A adds Bristol live public-source coverage for `SRC-BCC-0001`, `SRC-BCC-0002` and `SRC-BCC-0020`. The first two are official public-body sources with strict claim limits. `SRC-BCC-0020` is Bristol Post media context only. This coverage does not prove source truth, currentness, media accuracy, formal decision status or WPL readiness.

Stage 29A adds subagent context-control hardening for future stages. It provides a bounded packet template and instruction checks. It does not prove future agents obey instructions, evidence truth, legal correctness, professional assurance, substantive gate correctness or WPL readiness.

Stage 30A adds validation coverage for Stage 29A. It checks that Stage 29A validation rows and log are covered by the lagged validator. It does not prove command sufficiency, command authenticity, future agent compliance, evidence truth, legal correctness, professional assurance or WPL readiness.

Stage 31A adds a validation evidence log for Stage 30A. It records the Stage 30A validation commands and repository-state caveat. It does not prove command sufficiency, command authenticity, evidence truth, legal correctness, professional assurance or WPL readiness.

Stage 32A adds a WECA-style WPL OBC simulation. It creates a full editable working draft and comparator corpus, but it is not a real Bristol OBC, not a generic procurement engine, not WECA/MCA endorsed, not officer advice and not WPL readiness evidence.

Stage 33A ships the editable OBC simulation release. It is useful for reading and critique, but it is not a real Bristol OBC, not officer advice, not procurement authority, not consultation-ready and not statutory-ready.

## What This Repo Is

- An auditable simulation workspace.
- A controlled evidence and risk map.
- A way to learn from Nottingham, Leicester, DfT guidance and Bristol public records.
- A record of where future officer, legal, financial, modelling, consultation and data-protection checks would be needed.

Learning from Nottingham means identifying questions for Bristol; it does not mean Bristol would get the same impacts or already has a parking-mitigation plan.

## What This Repo Is Not

- It is not legal advice.
- It is not Bristol City Council approval.
- It is not WECA/MCA approval, consent or objection.
- It is not DfT or Secretary of State confirmation.
- It is not an OBC, FBC, consultation document, scheme order or launch decision.
- It is not an official council publication or professional sign-off.

## Current No-Go Position

The simulation currently says:

- no boundary has been selected;
- no charge level has been set;
- no workplace parking inventory exists;
- no OBC or FBC has been assembled;
- no public consultation is launch-ready;
- no statutory submission is ready;
- no assembled OBC, FBC, consultation pack, officer-review DOCX or authored officer-distribution PDF is ready;
- downloaded priority source-note coverage is complete;
- current claim-matrix summaries exist, but they do not prove claim truth and future drafting-specific summaries remain open;
- stage-gate report structure checks exist, but they do not prove command execution history, substantive gate correctness, evidence truth, source currentness or readiness;
- validation evidence logs exist, but they do not prove evidence truth, source currentness, legal correctness, professional assurance or readiness;
- validation evidence coverage checks exist, but they do not prove command authenticity, command sufficiency, evidence truth, source currentness, legal correctness, professional assurance or readiness;
- Bristol live public-source coverage exists, but it does not prove source truth, currentness, media accuracy, formal decision status, legal correctness, professional assurance or readiness;
- subagent context-control hardening exists, but it does not prove future agents obey instructions, prompt fidelity, actual context isolation, reasoning quality, professional assurance or readiness;
- Stage 29A validation coverage exists, but it does not prove command sufficiency, command authenticity, future agent compliance, prompt fidelity, actual context isolation, reasoning quality, professional assurance or readiness;
- Stage 30A validation evidence logging exists, but it does not prove command sufficiency, command authenticity, evidence truth, source currentness, legal correctness, professional assurance or readiness;
- Stage 32A WECA-style OBC drafting exists, but it does not prove real OBC status, WECA/MCA endorsement, procurement authority, consultation readiness, statutory readiness, professional assurance or readiness;
- Stage 33A OBC simulation release exists, but it does not prove real OBC approval, officer advice, procurement authority, consultation readiness, statutory readiness, professional assurance or readiness;
- Nottingham lessons cannot be copied to Bristol without transferability evidence.

## Where To Start

| Reader | First document | Purpose |
|---|---|---|
| New reader | `docs/public/how-to-read-this-repo.md` | Five-minute route and safeguards |
| Anyone asking what this can tell them | `docs/public/what-this-repo-can-and-cannot-tell-you.md` | Known assumptions gaps and prohibited claims |
| Public reader | `docs/public/evidence-and-assumptions-summary.md` | What is known, assumed, open or prohibited |
| Cabinet member or leader | `docs/officer/assurance-dashboard.md` | One-page status and blockers |
| Cabinet member checking gates | `docs/officer/cabinet-and-officer-navigation-guide.md` | Gate taxonomy and decision routes |
| Cabinet member checking risks | `docs/officer/risk-gate-atlas.md` | Risk location mitigation limits and next proof |
| Visual/accessibility reviewer | `docs/visuals/visual-accessibility-qa-register.csv` | Static visual QA controls and text fallback route |
| Navigation maintainer | `scripts/validate_navigation_integrity.py` | Repo-local navigation integrity checks |
| Checking whether sources are still usable | `docs/public/source-link-and-freshness-status.md` | Link status, last-check dates, refresh flags and source-use limits |
| Source-link QA maintainer | `scripts/validate_external_liveness.py` | Offline validation of recorded source-link reachability metadata |
| Checking the three Bristol public links | `docs/public/bristol-live-public-source-status.md` | Stage 28A Bristol live public-source coverage for `SRC-BCC-0001`, `SRC-BCC-0002` and media context `SRC-BCC-0020` |
| Bristol public-source QA maintainer | `scripts/validate_bristol_public_sources.py` | Checks source-status rows and no-overclaim wording; does not prove source truth, currentness or WPL readiness |
| Future-stage agent/context maintainer | `docs/agents/subagent-stage-packet-template.md` | Bounded subagent packet template; instruction/template presence only |
| Subagent context-control QA maintainer | `scripts/validate_subagent_context_control.py` | Checks Stage 29A context-control wording; does not prove future agents obey instructions |
| Shipped OBC simulation reader | `business_case/obc/simulation-release/bristol-wpl-outline-business-case-simulation-release.md` | Complete editable Stage 33A Bristol WPL OBC simulation release; not for real-world reliance |
| WECA-style simulated OBC reader | `business_case/obc/simulated-working-draft/bristol-wpl-simulated-weca-style-obc.md` | Full editable Stage 32A WPL-focused OBC working draft; simulation-only and not for reliance |
| WECA OBC/FBC exemplar reviewer | `analysis/weca-obc-fbc-exemplars/stage-32a-weca-obc-fbc-exemplar-corpus.md` | Source hierarchy, comparator matrix and drafting standard for WECA-style OBC discipline |
| Register integrity reviewer | `scripts/validate_register_references.py` | Cross-register ID and selected control-path checks |
| Dashboard consistency reviewer | `scripts/validate_dashboard_consistency.py` | README and officer-dashboard blocker surfacing checks |
| Stage-gate report reviewer | `scripts/validate_stage_gate_reports.py` | Recent gate-report structure checks; not evidence truth, source currentness or readiness |
| Validation evidence reviewer | `evidence/validation/README.md` | Logged repo-check evidence; QA evidence for the simulation only |
| Validation evidence QA maintainer | `scripts/validate_validation_evidence_log.py` | Checks validation-log rows and scope limits, including Stage 30A validation evidence |
| Validation coverage QA maintainer | `scripts/validate_validation_coverage.py` | Checks Stage 26A and Stage 29A validation evidence coverage; not command sufficiency, future agent compliance or readiness |
| Officer or programme manager | `docs/officer/programme-risk-briefing.md` | Risks, mitigations and next checks |
| Anyone asking what happens next | `docs/officer/next-steps-critical-path.md` | Critical path work packages; critical path is not approval |
| Evidence reviewer or drafter | `evidence/source_notes/README.md` | Source-note cohorts; source notes do not verify every claim |
| Claim reviewer or drafter | `evidence/claim_summaries/README.md` | Existing claim summaries; summaries do not prove claim truth |
| Nottingham/comparator reader | `docs/officer/nottingham-and-comparator-lessons.md` | Transferability questions; lessons are not Bristol forecasts |
| Legal reviewer | `docs/officer/legal-and-governance-briefing.md` | Bristol, WECA/MCA and DfT route issues |
| Appraisal or transport specialist | `analysis/economic/stage-5a-options-appraisal-control-package.md` | Appraisal and model controls |
| GIS or data specialist | `analysis/spatial/stage-4a-boundary-and-parking-inventory-control-package.md` | Boundary, inventory and displacement controls |
| Consultation specialist | `analysis/consultation/stage-8a-consultation-readiness-control-package.md` | Consultation launch controls |

## Visual Map

See `docs/visuals/stage-gate-map.mmd` for the current stage-gate flow, `docs/visuals/risk-control-atlas.mmd` for the simplified risk-control flow, `docs/visuals/visual-accessibility-qa-register.csv` for static visual QA and text fallback controls, `docs/public/source-link-and-freshness-status.md` for source-link/freshness status, `docs/public/bristol-live-public-source-status.md` for Bristol live public-source coverage, `docs/agents/subagent-stage-packet-template.md` for future-stage bounded subagent packets, `review/stage_gate_reports/stage-30a-validation-coverage-for-stage-29a-report.md` for Stage 29A validation coverage, `evidence/validation/stage-30a-validation-run-log.md` for Stage 30A validation evidence, `business_case/obc/simulation-release/bristol-wpl-outline-business-case-simulation-release.md` for the Stage 33A shipped OBC simulation, `business_case/obc/simulated-working-draft/bristol-wpl-simulated-weca-style-obc.md` for the Stage 32A simulated OBC working draft, and `evidence/validation/README.md` for logged validation evidence and coverage limits.
