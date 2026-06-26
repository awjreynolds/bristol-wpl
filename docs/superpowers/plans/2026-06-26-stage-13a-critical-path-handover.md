# Stage 13A Critical Path Handover Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a handover and critical-path layer that maps open blockers to actionable work packages without implying approval or readiness.

**Architecture:** Add handover controls under `analysis/handover/`, `handover/controls/`, `docs/officer/`, `review/`, and validators. Keep the layer separate from WPL readiness gates; handover QA can pass while approval gates remain blocked.

**Tech Stack:** Markdown, CSV, Python standard library, `unittest`, existing Makefile validation targets.

---

### Task 1: Write Failing Handover Tests

- [x] Create `tests/test_handover.py`.
- [x] Require `scripts/validate_handover.py`.
- [x] Require critical-path work package, blocker map, 90-day plan and no-go CSVs.
- [x] Require README links and no-approval wording.
- [x] Run `python3 -m unittest tests.test_handover` and confirm red failure.

### Task 2: Add Handover Artefacts

- [x] Create `analysis/handover/stage-13a-critical-path-handover-control-package.md`.
- [x] Create `docs/officer/next-steps-critical-path.md`.
- [x] Create `handover/controls/critical-path-work-package-register.csv`.
- [x] Create `handover/controls/blocker-to-workstream-map.csv`.
- [x] Create `handover/controls/next-90-day-plan.csv`.
- [x] Create `handover/controls/handover-no-go-register.csv`.
- [x] Create peer-review and gate-report files.

### Task 3: Add Validator And Wire QA

- [x] Create `scripts/validate_handover.py`.
- [x] Add `handover-qa` to `Makefile` and include it in `make validate`.
- [x] Add handover CSV headers to `scripts/validate_registers.py`.

### Task 4: Update Navigation And Registers

- [x] Update README, stage index, visual map, officer dashboard, checks map and stage-gate plan.
- [x] Add issue, risk, requirement, approval, sign-off, decision, claim, evidence-gap, pitfall, control, stage-risk and adoption rows.

### Task 5: Verify, Review, Commit And Push

- [x] Run `python3 -m unittest tests.test_handover`.
- [x] Run `python3 scripts/validate_handover.py`.
- [x] Run `make validate` and targeted QA commands.
- [x] Run expected blocked gate checks.
- [x] Run reviewer agents for officer handover clarity and gate/no-go risk.
- [x] Fix findings.
- [x] Commit as `docs: add Stage 13A critical path handover controls`.
- [x] Push `main`.
