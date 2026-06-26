# Stage 9A Public Officer Assurance Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a public and officer-facing assurance layer that explains the Bristol WPL simulation in plain English, surfaces stage risks and Nottingham lessons, and validates that summaries remain aligned with the controlled registers.

**Architecture:** Keep the existing agent/control architecture intact. Add a thin human-facing documentation layer under `docs/public/` and `docs/officer/`, structured registers under `governance/` and `analysis/economic/`, and validators that compare those summaries to the risk, issue, evidence-gap and sign-off registers.

**Tech Stack:** Markdown, CSV, Mermaid, Python standard library, `unittest`, existing `Makefile` validation targets.

---

### Task 1: Add Public And Officer Pack Tests

**Files:**
- Create: `tests/test_officer_pack.py`
- Create: `tests/test_nottingham_lessons.py`
- Modify: `Makefile`

- [x] Write tests that require `scripts/validate_officer_pack.py`, `scripts/validate_nottingham_transferability.py`, and real `scripts/stage_gate_check.py` behavior.
- [x] Run `python3 -m unittest tests.test_officer_pack tests.test_nottingham_lessons` and confirm the tests fail because the validators and officer pack do not exist yet.

### Task 2: Add Officer/Public Documentation Layer

**Files:**
- Create: `docs/public/README.md`
- Create: `docs/public/evidence-and-assumptions-summary.md`
- Create: `docs/officer/assurance-dashboard.md`
- Create: `docs/officer/legal-and-governance-briefing.md`
- Create: `docs/officer/programme-risk-briefing.md`
- Create: `docs/officer/nottingham-and-comparator-lessons.md`
- Create: `docs/officer/checks-and-balances-map.md`
- Create: `docs/officer/document-map.md`
- Create: `docs/visuals/stage-gate-map.mmd`

- [x] Write public-first explanations with no approval, consultation, OBC/FBC or statutory-readiness overclaim.
- [x] Include explicit read paths for cabinet/leader, officer, legal, appraisal, spatial, consultation and evidence users.
- [x] Include Mermaid visual flow showing completed control stages, blocked gates and future stages.

### Task 3: Add Stage 9A Registers

**Files:**
- Create: `governance/pitfalls_register.csv`
- Create: `governance/stage_risk_matrix.csv`
- Create: `governance/checks_and_balances_register.csv`
- Create: `governance/real_world_adoption_checklist.csv`
- Create: `analysis/economic/nottingham_lessons_register.csv`

- [x] Add stage-linked pitfalls for legal route, WECA/MCA role, DfT route, boundary, parking inventory, displacement, Nottingham transfer, appraisal, OBC, consultation, data protection and operations.
- [x] Add Nottingham/comparator lessons as lessons only, with transfer conditions and prohibited overclaims.

### Task 4: Add Validators

**Files:**
- Create: `scripts/validate_officer_pack.py`
- Create: `scripts/validate_nottingham_transferability.py`
- Modify: `scripts/stage_gate_check.py`
- Modify: `scripts/validate_claims.py`
- Modify: `Makefile`

- [x] `validate_officer_pack.py` must require the public/officer docs, Stage 9A registers, current P0/P1 blocker coverage and visual map.
- [x] `validate_nottingham_transferability.py` must require Nottingham lessons to include displacement/CPZ, non-transfer of charge, non-transfer of elasticity, public transport package dependence and evidence-strength caveats.
- [x] `stage_gate_check.py` must fail OBC/FBC gates while open P0 issues or risks remain, and must keep red-team bounded-review behavior non-passing.
- [x] `validate_claims.py` must check material claim rows are non-empty and have source, assumption or explicit gap control.

### Task 5: Restructure README And Stage Index

**Files:**
- Modify: `README.md`
- Modify: `docs/stages/README.md`
- Modify: `CHANGELOG.md`
- Modify: `governance/stage-gate-plan.md`
- Modify: governance/evidence registers as needed.

- [x] Move plain-English public status to the top of `README.md`.
- [x] Add “What can I rely on?” and “Where should I start?” sections.
- [x] Mark historical startup material as historical if referenced.
- [x] Add Stage 9A to the stage map and gate plan.

### Task 6: Verify, Review, Commit And Push

**Files:**
- Create: `review/peer_review/stage-9a-public-officer-assurance-review.md`
- Create: `review/stage_gate_reports/stage-9a-public-officer-assurance-report.md`

- [x] Run `make validate`, `make officer-pack-qa`, `make nottingham-qa`, `make red-team`, `make gate-obc`, `make gate-fbc`, `git diff --check`, prompt parity and no-authored-PDF scan.
- [x] Use simulated subagent review for public readability and assurance consistency. Final live reviewer agents were attempted but blocked by platform usage limits; the review provenance is recorded in Stage 9A review artefacts.
- [x] Fix findings.
- [ ] Commit as `docs: add Stage 9A public officer assurance layer`.
- [ ] Push `main`.
