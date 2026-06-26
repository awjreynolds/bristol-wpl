# Stage 9A Public And Officer Assurance

Status: complete as communication and assurance-control architecture.  
Date: 2026-06-26.

## ELI5 Summary

This stage turns the repo from an expert-only working file into something a public reader, cabinet member, council leader, officer or future reviewer can understand quickly.

It says, in plain English: this is a simulation, not an approved Bristol Workplace Parking Levy. It shows what is known, what is missing, what must not be claimed, and where each risk sits in the workflow.

## What Stage 9A Adds

- A public summary in `docs/public/README.md`.
- A public evidence and assumptions note in `docs/public/evidence-and-assumptions-summary.md`.
- Officer briefings in `docs/officer/`.
- A Mermaid stage-gate map in `docs/visuals/stage-gate-map.mmd`.
- A pitfalls register in `governance/pitfalls_register.csv`.
- A stage risk matrix in `governance/stage_risk_matrix.csv`.
- A checks and balances register in `governance/checks_and_balances_register.csv`.
- A real-world adoption checklist in `governance/real_world_adoption_checklist.csv`.
- A Nottingham lessons register in `analysis/economic/nottingham_lessons_register.csv`.
- Validators for officer pack consistency and Nottingham transferability.

## Key Data Points And Issues Discovered

| Issue | Why it matters | Control created |
|---|---|---|
| The old README opened as a technical build log. | A public reader could miss the no-go status. | Public-first README with no-go and safe-reliance sections. |
| Stage 1 was linked to a non-existent gate-report filename. | Navigation was brittle for officer review. | Corrected stage index link. |
| Nottingham dashboard wording needed clearer linkage from evidence gaps to active issue and risk blockers. | Weak cross-referencing reduces trust in the assurance layer. | Dashboard links Nottingham evidence gaps to controlled issue and risk IDs. |
| Nottingham lessons can be over-read. | Nottingham is the only UK WPL precedent but Bristol cannot copy its effects without evidence. | Nottingham lessons register with prohibited overclaims and Bristol transfer conditions. |
| Displaced parking and CPZ/RPZ mitigation need early visibility. | Nottingham and comparator experience shows workplace charges can create residential street pressure. | Pitfalls register and officer lessons briefing. |
| Agent sign-offs could be mistaken for real professional sign-off. | The user requested a simulation, but public readers need the boundary made explicit. | Real-world adoption checklist and repeated no-real-world-effect wording. |

## Nottingham Lessons Captured

The stage records Nottingham as lessons only:

- residential spillover and CPZ/RPZ mitigation need early assessment;
- public transport package credibility matters;
- employer support and shadow/testing arrangements are operationally important;
- charge levels, thresholds and exemptions cannot be copied;
- elasticity, congestion and mode-share effects cannot be transferred without Bristol modelling;
- media and comparator evidence is useful for pitfalls, not for decision-grade causal claims.

## Checks And Balances

Every public-facing readiness claim should pass these checks:

1. Is the claim allowed by `docs/officer/assurance-dashboard.md`?
2. Is it supported by a row in `evidence/claim_evidence_matrix.csv`?
3. Is the relevant blocker closed in `governance/issues_register.csv` and `governance/risk_register.csv`?
4. Does the relevant validator pass?
5. Does the wording avoid banned approval, consultation, OBC/FBC, DfT, WECA/MCA, boundary, appraisal and Nottingham transfer overclaims?

## Gate Position

Stage 9A does not close:

- Stage 2 legal/governance route blockers;
- Stage 3 strategic assessment blockers;
- Stage 4 boundary and inventory blockers;
- Stage 5 appraisal and model blockers;
- Stage 6 OBC assembly blockers;
- Stage 8 consultation launch blockers;
- Stage 11 FBC/statutory confirmation blockers.

The OBC and FBC gate scripts are expected to fail while those blockers remain open.

## Review Evidence

- Peer review: `review/peer_review/stage-9a-public-officer-assurance-review.md`
- Gate report: `review/stage_gate_reports/stage-9a-public-officer-assurance-report.md`
- Tests: `tests/test_officer_pack.py`; `tests/test_nottingham_lessons.py`
- Validators: `scripts/validate_officer_pack.py`; `scripts/validate_nottingham_transferability.py`; `scripts/stage_gate_check.py`
