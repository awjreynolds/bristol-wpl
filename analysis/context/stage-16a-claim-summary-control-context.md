# Stage 16A Claim Summary Control Context

Status: context packet for next stage.  
Date: 2026-06-26.

## Stage Purpose

Stage 16A creates an editable claim-level source-summary layer for the existing `evidence/claim_evidence_matrix.csv`. The goal is to reduce hallucination and citation drift before any future OBC, FBC, statutory, consultation or public/officer drafting.

This stage responds to `EG-0044`: claim-level source summaries are not yet complete even though downloaded priority source-note coverage is complete.

## Files In Scope

- `evidence/claim_evidence_matrix.csv`
- `evidence/source_register.csv`
- `evidence/source_notes/source-note-coverage-register.csv`
- `evidence/claim_summaries/`
- `scripts/validate_claim_summaries.py`
- `tests/test_claim_summaries.py`
- `README.md`
- `docs/stages/README.md`
- `docs/officer/assurance-dashboard.md`
- `docs/officer/programme-risk-briefing.md`
- `governance/stage-gate-plan.md`
- register files under `governance/` and `evidence/evidence_gap_register.csv`
- `review/peer_review/stage-16a-claim-summary-control-review.md`
- `review/stage_gate_reports/stage-16a-claim-summary-control-report.md`

## Files Out Of Scope

- Raw evidence re-extraction.
- New OBC, FBC, statutory dossier, consultation or officer-distribution documents.
- Legal advice, Monitoring Officer sign-off, Section 151 sign-off or real public-authority approvals.
- New substantive Bristol WPL claims not already present in the claim matrix.
- Boundary selection, parking inventory creation, model outputs, BCR, VFM category, charge level, revenue estimate or consultation launch material.

## Claim IDs In Scope

`CLM-0001` to `CLM-0038`, as currently listed in `evidence/claim_evidence_matrix.csv`.

## Source IDs In Scope

Only source IDs already recorded in `evidence/claim_evidence_matrix.csv`. The source-summary layer must not invent source IDs, line references, page references, reviewers or evidence quality.

## Open Register IDs

- `EG-0044`: claim-level source summaries open.
- `EG-0024`: partially closed; claim-level summaries remain.
- `ISS-0025`: Stage 15B source-note coverage overclaim risk.
- Continuing WPL blockers: `ISS-0001`, `ISS-0002`, `ISS-0003`, `ISS-0004`, `ISS-0008`, `ISS-0011`, `ISS-0012`, `ISS-0015`, `ISS-0016`.
- Stage 16A must add a new issue, risk, pitfall, requirement, check, claim-control, decision, approval and simulated sign-off row if it completes a new control layer.

## No-Go Claims

Stage 16A must not claim:

- claim truth beyond the current simulated reviewer status;
- legal advice, legal clearance, WECA/MCA closure or DfT closure;
- Green Book/TAG compliance, BCR, VFM category, model acceptance or appraisal readiness;
- Nottingham, TfL or Leicester transferability to Bristol;
- OBC/FBC evidence completion, consultation readiness, statutory submission readiness or implementation readiness;
- that a claim summary replaces the underlying source, source-note, reviewer check or later human professional review.

## Subagent Roles

- Legal/governance reviewer: test legal, Bristol governance, WECA/MCA, DfT and statutory no-go wording.
- Appraisal/comparator reviewer: test appraisal, Nottingham, TfL, Leicester and transferability wording.
- Public/officer readability reviewer: test whether the README, dashboard and stage docs explain the claim-summary layer clearly.
- Red-team reviewer: test leakage from "summary complete" into claim truth, OBC/FBC readiness or statutory readiness.

## Validator Commands

```bash
python3 scripts/validate_claim_summaries.py
python3 -m unittest tests.test_claim_summaries
make validate
git diff --check
python3 scripts/scan_secrets.py --all-history
```

## Required Register Updates

If Stage 16A passes, update:

- `evidence/evidence_gap_register.csv`
- `governance/issues_register.csv`
- `governance/risk_register.csv`
- `governance/pitfalls_register.csv`
- `governance/requirements_register.csv`
- `governance/checks_and_balances_register.csv`
- `evidence/claim_evidence_matrix.csv`
- `governance/decision_log.csv`
- `governance/approvals_register.csv`
- `governance/simulation_signoff_register.csv`
- `governance/stage_risk_matrix.csv`

## Commit/Push Condition

Do not proceed to Stage 16B until Stage 16A has an editable claim-summary register, per-claim summary files or an explicitly bounded pilot, focused validator, stage document, peer review, gate report, register trail, validation evidence, commit and push.
