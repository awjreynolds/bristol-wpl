# Stage 23A Context Packet: Register Reference Integrity

Status: bounded controller packet for Stage 23A.  
Date: 2026-06-26.

## Scope

Stage 23A adds deterministic checks that key issue, risk, pitfall, evidence-gap, requirement, control, approval and sign-off references resolve to real register rows.

It is linkage integrity only. It does not prove evidence truth, legal correctness, source authority, content completeness, professional assurance or WPL readiness.

## Inputs

- `governance/issues_register.csv`
- `governance/risk_register.csv`
- `governance/pitfalls_register.csv`
- `evidence/evidence_gap_register.csv`
- `governance/requirements_register.csv`
- `governance/checks_and_balances_register.csv`
- `governance/approvals_register.csv`
- `governance/simulation_signoff_register.csv`
- `docs/officer/risk-control-crosswalk.csv`

## Validator Boundary

`scripts/validate_register_references.py` checks:

- selected cross-register ID references resolve;
- selected evidence, artefact and validator path references exist;
- Stage 22A and Stage 23A baseline rows exist;
- no authored PDFs are introduced.

It intentionally does not infer whether a linked risk is correctly assessed, whether evidence supports a claim or whether a gate can pass.
