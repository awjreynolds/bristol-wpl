# Stage 11A FBC Statutory Gate Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development or local TDD with simulated reviewer agents to implement this plan task-by-task.

**Goal:** Add final FBC/statutory assurance gate controls that prevent false FBC approval, statutory submission or implementation readiness claims while preserving current no-go status.

**Architecture:** Add a Stage 11A layer under `analysis/fbc/`, `business_case/fbc/controls/`, `review/`, `docs/stages/` and validators. Reuse Stage 10A statutory blocker collection so the final gate sees statutory dossier blockers as well as FBC-specific gate blockers.

**Tech Stack:** Markdown, CSV, Python standard library, `unittest`, existing Makefile validation targets.

---

### Task 1: Write Failing Stage 11A Tests

**Files:**
- Create: `tests/test_fbc_statutory_gate.py`

- [x] Add tests requiring `scripts/validate_fbc_statutory_gate.py`.
- [x] Add tests requiring `business_case/fbc/controls/stage-11-fbc-statutory-gate-checklist.csv`.
- [x] Add tests requiring `business_case/fbc/controls/stage-11-assurance-panel-register.csv`.
- [x] Add tests requiring `business_case/fbc/controls/stage-11-no-go-claim-register.csv`.
- [x] Add a test proving `scripts/validate_fbc_statutory_gate.py --gate` fails while live blockers remain.
- [x] Run `python3 -m unittest tests.test_fbc_statutory_gate` and confirm red failure from missing Stage 11A files.

### Task 2: Add Stage 11A Control Artefacts

**Files:**
- Create: `analysis/fbc/stage-11a-fbc-statutory-gate-control-package.md`
- Create: `business_case/fbc/controls/stage-11-fbc-statutory-gate-checklist.csv`
- Create: `business_case/fbc/controls/stage-11-assurance-panel-register.csv`
- Create: `business_case/fbc/controls/stage-11-no-go-claim-register.csv`
- Create: `business_case/fbc/controls/stage-11-decision-report-control.md`
- Create: `business_case/fbc/controls/stage-11-red-team-packet.md`
- Create: `review/peer_review/stage-11a-fbc-statutory-assurance-review.md`
- Create: `review/stage_gate_reports/stage-11a-fbc-statutory-gate-report.md`
- Create: `docs/stages/stage-11a-fbc-statutory-gate.md`

- [x] Add Stage 11 master-prompt gate conditions.
- [x] Add assurance panel with real-world replacements including Monitoring Officer and Section 151 Officer.
- [x] Add no-go claims for FBC approval, statutory submission and implementation recommendations.
- [x] Add decision-report and red-team controls.

### Task 3: Add Validator And Wire QA

**Files:**
- Create: `scripts/validate_fbc_statutory_gate.py`
- Modify: `Makefile`
- Modify: `scripts/validate_registers.py`

- [x] Validate required Stage 11A files and CSV headers.
- [x] Validate exact gate-condition coverage.
- [x] Validate no-go claims and blocked status.
- [x] Add `fbc-statutory-qa` and include it in `make validate`.

### Task 4: Update Navigation And Registers

- [x] Add Stage 11A to README, stage index, visual map, officer dashboard and gate plan.
- [x] Add issue, risk, requirement, approval, sign-off, decision, evidence gap and claim rows.
- [x] Add pitfall, checks-and-balances and stage-risk rows.

### Task 5: Verify, Review, Commit And Push

- [x] Run `python3 -m unittest tests.test_fbc_statutory_gate`.
- [x] Run `python3 scripts/validate_fbc_statutory_gate.py`.
- [x] Run expected blocked check: `python3 scripts/validate_fbc_statutory_gate.py --gate`.
- [x] Run `make validate` and targeted QA commands.
- [x] Run `git diff --check`, prompt parity and no-authored-PDF scan.
- [x] Use simulated subagent review for final gate due diligence and public/officer comprehension risk.
- [x] Fix findings.
- [x] Commit as `docs: add Stage 11A FBC statutory gate controls`.
- [x] Push `main`.
