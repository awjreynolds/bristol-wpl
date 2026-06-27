# Document Map

Status: officer-facing navigation guide.  
Date: 2026-06-26.

## Main Areas

Editable authoring outputs are working files only. They help future drafters assemble evidence-linked Markdown, DOCX, XLSX or HTML material. They are not PDFs, not an assembled OBC or FBC, not a statutory submission, not consultation material and not approval by Bristol City Council, WECA/MCA, DfT or any statutory decision-maker.

| Area | What it is for | What it is not |
|---|---|---|
| `docs/public/` | Plain-English public summaries and editable control/drafting areas | Legal advice, decision report or not approved/not assembled/not PDF public pack |
| `docs/officer/` | Officer/cabinet/legal navigation and editable control/drafting areas | Replacement for professional review or not approved/not assembled/not PDF officer pack |
| `business_case/` | Editable OBC/FBC structure and placeholders | Completed OBC/FBC or not approved/not assembled/not PDF business case |
| `statutory_dossier/` | Scheme order, legal compliance and confirmation dossier controls | Ready statutory submission or not approved/not assembled/not PDF statutory pack |
| `analysis/` | Source-linked analysis and stage-control packages | Final advice |
| `analysis/content/` | Content-control decisions and writing-skill application records | User testing, legal assurance or accessibility certification |
| `evidence/` | Source register, source-link/freshness status controls, raw evidence, extraction manifests and source-note controls | Uncontrolled claim library or proof that sources are legally current |
| `governance/` | Risks, issues, decisions, approvals, simulation sign-off rows, requirements and register reference integrity controls | Real public-body approvals or proof that row substance is correct |
| `review/` | Simulated peer review, red team and stage-gate reports | Real officer/legal approval |
| `models/` | Model controls, cards, inputs and outputs | Completed model outputs |
| `spatial/` | Boundary, parking inventory and spatial QA controls | Authoritative boundary or map |
| `consultation/` | Consultation controls and future material locations | Launch-ready consultation pack |
| `docs/agents/` | Bounded subagent packet templates and context-control instructions | Proof that future agents obey prompts or that reviews are assurance-grade |
| `skills/` | Repo-local agent skills such as GOV.UK-style public prose controls | Not official GOV.UK/GDS endorsement, not professional sign-off and not readiness evidence |

## File Type Rule

Officer-facing material should remain editable Markdown, CSV, XLSX, DOCX or HTML. Authored PDFs are prohibited. Downloaded third-party PDFs may remain only under `evidence/raw/**`.

## Public And Cabinet Entry Points

| Reader question | Entry point |
|---|---|
| I am new. What is this? | `docs/public/how-to-read-this-repo.md` |
| What can this repo tell me? | `docs/public/what-this-repo-can-and-cannot-tell-you.md` |
| I need the cabinet/officer route. | `docs/officer/cabinet-and-officer-navigation-guide.md` |
| I need the risk/gate route. | `docs/officer/risk-gate-atlas.md` |
| I need the joined issue-risk-gap view. | `docs/officer/risk-control-crosswalk.csv` |
| I need visual fallback or static visual QA controls. | `docs/visuals/visual-accessibility-qa-register.csv` |
| I need to know whether a cited source link is still reachable or needs refresh. | `docs/public/source-link-and-freshness-status.md` |
| I need the status of the three Bristol public WPL links. | `docs/public/bristol-live-public-source-status.md` |
| I need to know whether register IDs and control paths resolve. | `scripts/validate_register_references.py` |
| I need to know whether visible blocker IDs still resolve to open rows. | `scripts/validate_dashboard_consistency.py` |
| I need to know whether recent gate reports carry the expected validation and limitation wording. | `scripts/validate_stage_gate_reports.py` |
| I need to know what validation evidence has been logged for repo checks. | `evidence/validation/README.md` |
| I need to check validation-log structure and scope limits. | `scripts/validate_validation_evidence_log.py` |
| I need to know whether Stage 26A validation evidence coverage is present. | `scripts/validate_validation_coverage.py` |
| I need to check Bristol live public-source coverage for `SRC-BCC-0001`, `SRC-BCC-0002` and media context `SRC-BCC-0020`. | `scripts/validate_bristol_public_sources.py` |
| I need the bounded subagent packet template for a future stage. | `docs/agents/subagent-stage-packet-template.md` |
| I need to check Stage 29A subagent context-control wording. | `scripts/validate_subagent_context_control.py` |
| I need to know whether Stage 29A validation evidence coverage is present. | `review/stage_gate_reports/stage-30a-validation-coverage-for-stage-29a-report.md` |
| I need to inspect Stage 30A validation command evidence. | `evidence/validation/stage-30a-validation-run-log.md` |
| I need to read the shipped OBC simulation release. | `business_case/obc/simulation-release/bristol-wpl-outline-business-case-simulation-release.md` |
| I need the Stage 33A OBC simulation release gate report. | `review/stage_gate_reports/stage-33a-obc-simulation-release-report.md` |
| I need the Stage 34A GOV.UK style skill. | `skills/govuk-style/SKILL.md` |
| I need to know why the GOV.UK style skill was adopted. | `analysis/content/stage-34a-govuk-style-application.md` |
| I need the Stage 34A GOV.UK style skill gate report. | `review/stage_gate_reports/stage-34a-govuk-style-skill-adoption-report.md` |
| I need to check Stage 34A GOV.UK style skill wiring. | `scripts/validate_govuk_style_skill.py` |
| I need to inspect the Stage 32A simulated OBC working draft. | `business_case/obc/simulated-working-draft/bristol-wpl-simulated-weca-style-obc.md` |
| I need the WECA OBC/FBC exemplar corpus behind Stage 32A. | `analysis/weca-obc-fbc-exemplars/stage-32a-weca-obc-fbc-exemplar-corpus.md` |

The visual fallback route is `docs/visuals/visual-accessibility-qa-register.csv`; it is a static source-control route, not rendered accessibility assurance.

Stage 28A Bristol live public-source coverage does not prove source truth, currentness, media accuracy, formal decision status, legal correctness or WPL readiness.
Stage 29A subagent context-control hardening does not prove future agents obey instructions, evidence truth, legal correctness, professional assurance, substantive gate correctness or WPL readiness.
Stage 30A validation coverage for Stage 29A does not prove command sufficiency, command authenticity, future agent compliance, evidence truth, legal correctness, professional assurance, substantive gate correctness or WPL readiness.
Stage 31A validation evidence logging for Stage 30A does not prove command sufficiency, command authenticity, evidence truth, source currentness, legal correctness, professional assurance, substantive gate correctness or WPL readiness.
Stage 32A WECA-style OBC simulation does not prove real OBC status, WECA/MCA endorsement, procurement authority, consultation readiness, statutory readiness, professional assurance or WPL readiness.
Stage 33A OBC simulation release does not prove real OBC approval, officer advice, procurement authority, consultation readiness, statutory readiness, professional assurance or WPL readiness.
Stage 34A GOV.UK style skill adoption does not prove official GOV.UK/GDS endorsement, legal assurance, accessibility certification, user-tested comprehension, professional assurance or WPL readiness.
