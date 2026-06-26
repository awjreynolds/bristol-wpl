# Checks And Balances Map

Status: officer-facing control map.  
Date: 2026-06-26.

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
| Statutory dossier | Scheme order, consultation report, net-proceeds plans and confirmation route | Legal, Finance and Integrated Review Agents | Stage 11 |

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
- `python3 scripts/stage_gate_check.py --gate obc`
- `python3 scripts/stage_gate_check.py --gate fbc`
