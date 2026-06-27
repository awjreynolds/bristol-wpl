# Stage 32A WECA OBC/FBC Exemplar Corpus And Simulated OBC Draft Context

Status: active stage context packet.  
Date: 2026-06-27.  
Owner: Programme Orchestrator.

## Stage Purpose

Stage 32A promotes WECA-facing OBC/FBC examples already present in the evidence base into a controlled exemplar corpus and uses that corpus to shape an editable, WECA-style Bristol WPL simulated OBC working draft.

The intended output is professional Five Case Model drafting that resembles the structure, tone, assurance discipline and decision-route treatment of other WECA-facing OBC/FBC material. It must remain visibly simulation-only and must not impersonate an approved Bristol City Council, WECA/MCA, DfT or Secretary of State document.

## Files In Scope

| Path | Purpose |
|---|---|
| `analysis/weca-obc-fbc-exemplars/` | New exemplar corpus, comparator matrix and WECA-style authoring standard. |
| `business_case/obc/00-front-matter/document-control.md` | Update document status for simulation-only WECA-style working draft. |
| `business_case/obc/01-executive-summary/executive-summary.md` | Full simulated OBC executive summary. |
| `business_case/obc/02-strategic-case/strategic-case.md` | Full simulated Strategic Case. |
| `business_case/obc/03-economic-case/economic-case.md` | Full simulated Economic Case with evidence gaps exposed. |
| `business_case/obc/04-commercial-case/commercial-case.md` | Full simulated Commercial Case. |
| `business_case/obc/05-financial-case/financial-case.md` | Full simulated Financial Case. |
| `business_case/obc/06-management-case/management-case.md` | Full simulated Management Case. |
| `business_case/obc/07-conclusions-and-decisions/recommendations.md` | Simulated OBC decision section with no-go recommendation conditions. |
| `business_case/obc/simulated-working-draft/` | New editable single-file simulated OBC working draft. |
| `scripts/validate_obc.py` and `tests/test_obc.py` | Allow and validate simulation-only working draft while preserving reliance-ready assembly block. |
| `README.md`, `docs/stages/`, `review/stage_gate_reports/` | Public navigation and gate record. |
| `governance/*.csv`, `evidence/*.csv` | Register trail for risks, issues, gaps, decisions and validation evidence. |

## Files Out Of Scope

- `business_case/obc/assembled/`: remains blocked for reliance-ready or officer-review OBC assembly.
- `deliverables/review/docx/`: no officer-review DOCX is created.
- `business_case/fbc/**`: no FBC drafting in this stage.
- `statutory_dossier/draft_scheme_order/**`: no scheme order drafting in this stage.
- `evidence/raw/**`: no broad raw evidence review; open only for targeted provenance checks.
- Authored PDFs: prohibited.

## Source IDs In Scope

| Source ID | Use |
|---|---|
| `SRC-BCC-0001` | Current Bristol public WPL project-page status and timetable. |
| `SRC-BCC-0002` | Bristol public explainer language and OBC-development framing. |
| `SRC-BCC-0003` | September 2024 committee report for Stage One/OBC development authority. |
| `SRC-BCC-0004` | September 2024 decision notice. |
| `SRC-BCC-0006` | Bristol WPL feasibility study. |
| `SRC-BCC-0007` | OBC-stage EqIA. |
| `SRC-BCC-0014` | March 2026 WPL progress report. |
| `SRC-BCC-0015` | March 2026 public reports pack, including WECA-facing FBC examples in extracted text. |
| `SRC-BCC-0036` | May 2025 printed minutes, including WECA-facing OBC/FBC examples. |
| `SRC-WECA-0001` | JLTP4 strategic context. |
| `SRC-WECA-0003` | Bus Strategy context. |
| `SRC-WECA-0004` | BSIP context. |
| `SRC-WECA-0006` | WECA Local Growth Assurance Framework January 2024. |
| `SRC-WECA-0007` | WECA Local Growth Assurance Framework July 2025. |
| `SRC-WECA-0027` | MCA budget outturn with OBC programme-line examples. |
| `SRC-WECA-0028` | Investment Fund Programme and Grant Assurance context. |
| `SRC-WECA-0029` | Delivery Assurance context. |
| `SRC-DFT-0001` | Transport business case guidance. |
| `SRC-DFT-0002` | TAG landing-page control. |
| `SRC-HMT-0001` | Green Book. |
| `SRC-HMT-0002` | Magenta Book. |
| `SRC-HMT-0003` | Managing Public Money. |
| `SRC-NOTT-0001`, `SRC-NOTT-0002`, `SRC-ACADEMIC-0002` | Nottingham/comparator precedent with transferability limits. |
| `SRC-LEG-0002`, `SRC-LEG-0003`, `SRC-LEG-0004`, `SRC-LEG-0005`, `SRC-LEG-0006`, `SRC-LEG-0017`, `SRC-LEG-0018`, `SRC-LEG-0026`, `SRC-LEG-0027` | Statutory WPL route, order, consultation and net-proceeds controls. |

## Open Issue, Risk And Gap IDs

Core blockers that remain live during this stage:

- Issues: `ISS-0001`, `ISS-0002`, `ISS-0003`, `ISS-0004`, `ISS-0008`, `ISS-0011`, `ISS-0012`, `ISS-0015`, `ISS-0025`, `ISS-0026`, `ISS-0027`, `ISS-0028`, `ISS-0029`, `ISS-0030`, `ISS-0031`, `ISS-0032`, `ISS-0033`, `ISS-0034`, `ISS-0035`, `ISS-0036`, `ISS-0037`, `ISS-0038`, `ISS-0039`, `ISS-0040`, `ISS-0041`.
- Risks: `RISK-0001`, `RISK-0002`, `RISK-0003`, `RISK-0004`, `RISK-0005`, `RISK-0006`, `RISK-0007`, `RISK-0011`, `RISK-0012`, `RISK-0044`.
- Evidence gaps: `EG-0005`, `EG-0008`, `EG-0014`, `EG-0045`, `EG-0046`, `EG-0047`, `EG-0048`, `EG-0049`, `EG-0050`, `EG-0051`, `EG-0052`, `EG-0053`, `EG-0054`, `EG-0055`, `EG-0056`, `EG-0057`, `EG-0058`, `EG-0059`.

Stage 32A should add new rows for any gap specifically caused by WECA-style OBC exemplar capture or simulation-draft overclaim risk.

## No-Go Claims

The stage must not claim that:

- a real Bristol WPL OBC exists, has been approved, has been submitted, or can be relied on;
- WECA/MCA has approved, supported, objected to, consented to, funded or sponsored Bristol WPL;
- WECA/MCA has no role or consent is not required;
- DfT or the Secretary of State has accepted, cleared or confirmed the scheme;
- a preferred WPL option, boundary, charge, threshold, exemption package or investment package has been selected;
- model outputs, BCR, VFM, demand response, revenue, net proceeds or affordability are decision-grade;
- consultation can launch;
- agentic simulation sign-off is legal advice, Section 151 certification, Monitoring Officer clearance, officer approval, member approval or professional assurance;
- the simulated working draft may be distributed as a council or WECA officer report without real-world review.

## Subagent Roles

| Lane | Role | Packet |
|---|---|---|
| Domain reviewer | WECA Business Case Pattern Agent | `analysis/context/stage-32a-weca-obc-fbc-exemplar-corpus/weca-pattern-review-packet.md` |
| Evidence/citation reviewer | Evidence And Citation Control Agent | `analysis/context/stage-32a-weca-obc-fbc-exemplar-corpus/evidence-citation-review-packet.md` |
| Public/officer readability reviewer | Officer Readability Agent | `analysis/context/stage-32a-weca-obc-fbc-exemplar-corpus/officer-readability-review-packet.md` |
| Red-team reviewer | Red Team Overclaim Agent | `analysis/context/stage-32a-weca-obc-fbc-exemplar-corpus/red-team-review-packet.md` |

## Validator Commands

Focused:

- `python3 scripts/validate_obc.py`
- `python3 -m unittest tests.test_obc`

Full:

- `make validate`
- `git diff --check`
- `python3 scripts/scan_secrets.py --all-history`

## Required Register Updates

- `governance/issues_register.csv`
- `governance/risk_register.csv`
- `governance/stage_risk_matrix.csv`
- `governance/pitfalls_register.csv`
- `evidence/evidence_gap_register.csv`
- `evidence/claim_evidence_matrix.csv`
- `governance/requirements_register.csv`
- `governance/decision_log.csv`
- `governance/approvals_register.csv`
- `governance/simulation_signoff_register.csv`
- `evidence/validation/validation-run-register.csv`

## Commit And Push Condition

Stage 32A may be committed and pushed only after the focused validator, full validation, whitespace check and all-history secret scan pass, and after validation evidence is recorded.

