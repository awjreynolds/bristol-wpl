# Checks And Balances Map

Status: officer-facing control map.  
Date: 2026-06-26.

This is a simulation control map. It is not approval, legal advice, consultation authority, OBC/FBC readiness, statutory submission readiness or official council publication.

## How A Claim Is Controlled

| Claim type | Required evidence | Required review | Gate |
|---|---|---|---|
| Legal route | Current law, Bristol route, WECA/MCA role, DfT process | Legal Review Agent and Monitoring Officer Simulation Agent | Stage 2 and Stage 11 |
| Boundary | Authoritative GIS source, licence, topology QA, legal/GIS reconciliation | GIS/Data Review Agent and Legal Review Agent | Stage 4 |
| Parking inventory | Canonical data, source IDs, confidence, lawful basis and audit history | Spatial Data Agent and Data Protection Review Agent | Stage 4 |
| Nottingham/comparator lesson | Source ID, lesson, transfer condition, prohibited overclaim, displacement checklist and no-transfer note | Comparator Evidence Agent with Spatial Data Agent and Public Officer Review Agent | Stage 5 and Stage 18A |
| Model output | ASR, model card, run manifest, validation and uncertainty | Analytical Assurance Agent | Stage 5 and Stage 7 |
| OBC section | Section dependency, claim evidence, limitation and simulated reviewer status | Integrated Case Review Agent | Stage 7 |
| Consultation material | Authority, privacy, accessibility, EqIA, response analysis and material version controls | Legal, Data, Accessibility and Consultation Agents | Stage 8 |
| Statutory dossier | Scheme order, consultation report, net-proceeds plans, confirmation route, Stage 10A component register and no-go register | Legal, Finance and Integrated Review Agents | Stage 10A controls and Stage 11 gate |
| FBC/statutory gate | Final FBC evidence packet, legal sign-off, Section 151 review, DfT/WECA disposition, operations readiness and residual-risk decision pack | Monitoring Officer Simulation Agent, Section 151 Simulation Agent, Integrated Review Agent, Legal Review Agent, Finance Review Agent, Operations Design Agent and Red Team | Stage 11A controls and Stage 11 gate |
| Public repository release | GitHub visibility, public no-go wording, no authored PDFs, restricted-path scan and blocked WPL gates | Public Release Review Agent, Officer Readability Agent and Red Team | Stage 12A controls |
| Critical-path handover | Work package register, blocker map, 90-day control plan and handover no-go claims | Handover Review Agent, Programme Controls Agent and Red Team | Stage 13A controls |
| Source notes | Source-note coverage-stage register, source-use limits, raw-omitted source controls, no-go claims and handoff to claim summaries | Evidence Librarian, Evidence/Citation Agent, Legal Review Agent and Red Team | Stage 14A, Stage 15A and Stage 15B controls |
| Claim summaries | Current claim-matrix summaries, source IDs, source locations, reviewer status, limitations, no-go claims and `EG-0045` future-claim gap | Evidence/Citation Agent, domain reviewers and Red Team | Stage 16A controls |
| Transferability controls | Blocked Nottingham lesson rows, blocked transferability matrix, residential spillover checklist, current Nottingham refresh gap and cross-register blockers | Comparator Evidence Agent, Spatial Data Agent, Public Officer Review Agent and Red Team | Stage 18A controls |
| Public/cabinet comprehension | Public guide, cabinet guide, RAG legend, gate taxonomy, risk atlas, risk-control crosswalk and simulation sign-off limits | Public Officer Review Agent, Cabinet/Officer Navigation Agent, Risk-Control Reviewer and Red Team | Stage 19A controls |
| WECA-style simulated OBC | Stage 32A status formula, source hierarchy, WECA/MCA trigger tags, no-go claims, subagent handovers, full WPL-focused Markdown draft and OBC validator | WECA Business Case Pattern Agent, Evidence Citation Agent, Officer Readability Agent, Red Team and Simulation Gate Authority | Stage 32A controls |

## Registers

- `governance/checks_and_balances_register.csv`
- `evidence/claim_evidence_matrix.csv`
- `governance/requirements_register.csv`
- `governance/approvals_register.csv`
- `governance/simulation_signoff_register.csv`

## Validator Controls

- `make validate`
- `make officer-pack-qa`
- `make nottingham-qa`
- `make consultation-qa`
- `make statutory-qa`
- `make fbc-statutory-qa`
- `make public-release-qa`
- `make handover-qa`
- `make source-notes-qa`
- `make comprehension-qa`
- `python3 scripts/validate_claim_summaries.py`
- `python3 scripts/validate_statutory_dossier.py --gate`
- `python3 scripts/validate_fbc_statutory_gate.py --gate`
- `python3 scripts/stage_gate_check.py --gate obc`
- `python3 scripts/stage_gate_check.py --gate fbc`
