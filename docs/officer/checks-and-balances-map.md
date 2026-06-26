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
| Nottingham lesson | Source ID, lesson, transfer condition and prohibited overclaim | Comparator Evidence Agent | Stage 5 |
| Model output | ASR, model card, run manifest, validation and uncertainty | Analytical Assurance Agent | Stage 5 and Stage 7 |
| OBC section | Section dependency, claim evidence, limitation and reviewer sign-off | Integrated Case Review Agent | Stage 7 |
| Consultation material | Authority, privacy, accessibility, EqIA, response analysis and material version controls | Legal, Data, Accessibility and Consultation Agents | Stage 8 |
| Statutory dossier | Scheme order, consultation report, net-proceeds plans, confirmation route, Stage 10A component register and no-go register | Legal, Finance and Integrated Review Agents | Stage 10A controls and Stage 11 gate |
| FBC/statutory gate | Final FBC evidence packet, legal sign-off, Section 151 review, DfT/WECA disposition, operations readiness and residual-risk decision pack | Monitoring Officer Simulation Agent, Section 151 Simulation Agent, Integrated Review Agent, Legal Review Agent, Finance Review Agent, Operations Design Agent and Red Team | Stage 11A controls and Stage 11 gate |
| Public repository release | GitHub visibility, public no-go wording, no authored PDFs, restricted-path scan and blocked WPL gates | Public Release Review Agent, Officer Readability Agent and Red Team | Stage 12A controls |
| Critical-path handover | Work package register, blocker map, 90-day control plan and handover no-go claims | Handover Review Agent, Programme Controls Agent and Red Team | Stage 13A controls |
| Source notes | Source-note coverage-stage register, source-use limits, raw-omitted source controls, no-go claims, `EG-0044` claim-summary gap and claim-evidence linkage | Evidence Librarian, Evidence/Citation Agent, Legal Review Agent and Red Team | Stage 14A, Stage 15A and Stage 15B controls |

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
- `python3 scripts/validate_statutory_dossier.py --gate`
- `python3 scripts/validate_fbc_statutory_gate.py --gate`
- `python3 scripts/stage_gate_check.py --gate obc`
- `python3 scripts/stage_gate_check.py --gate fbc`
