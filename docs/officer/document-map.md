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
| `evidence/` | Source register, source-link/freshness status controls, raw evidence, extraction manifests and source-note controls | Uncontrolled claim library or proof that sources are legally current |
| `governance/` | Risks, issues, decisions, approvals, simulation sign-off rows, requirements and register reference integrity controls | Real public-body approvals or proof that row substance is correct |
| `review/` | Simulated peer review, red team and stage-gate reports | Real officer/legal approval |
| `models/` | Model controls, cards, inputs and outputs | Completed model outputs |
| `spatial/` | Boundary, parking inventory and spatial QA controls | Authoritative boundary or map |
| `consultation/` | Consultation controls and future material locations | Launch-ready consultation pack |

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
| I need to know whether register IDs and control paths resolve. | `scripts/validate_register_references.py` |
| I need to know whether visible blocker IDs still resolve to open rows. | `scripts/validate_dashboard_consistency.py` |
