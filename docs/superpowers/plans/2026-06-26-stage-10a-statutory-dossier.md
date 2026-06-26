# Stage 10A Statutory Dossier Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add statutory confirmation dossier controls that define how a future Stage 10 statutory submission pack would be assembled and reviewed, while preserving the current no-go position.

**Architecture:** Keep the Stage 2, Stage 7A and Stage 8A blockers intact. Add a Stage 10A control layer under `analysis/legal/`, `statutory_dossier/controls/`, `statutory_dossier/draft_scheme_order/`, `review/`, `docs/stages/` and validators so future agents can test component coverage, route readiness, no-go wording and clause-by-clause powers traceability without claiming a ready submission.

**Tech Stack:** Markdown, CSV, Python standard library, `unittest`, existing Makefile validation targets.

---

### Task 1: Write Failing Stage 10A Tests

**Files:**
- Create: `tests/test_statutory_dossier.py`

- [x] Add tests requiring `scripts/validate_statutory_dossier.py`.
- [x] Add tests requiring `statutory_dossier/controls/dossier-component-register.csv`.
- [x] Add tests requiring `statutory_dossier/controls/submission-no-go-register.csv`.
- [x] Add tests requiring `statutory_dossier/draft_scheme_order/clause-by-clause-powers-matrix.csv`.
- [x] Add a test proving `scripts/validate_statutory_dossier.py --gate` fails while live blockers remain.
- [x] Run `python3 -m unittest tests.test_statutory_dossier` and confirm red failure from missing Stage 10A files.

### Task 2: Add Stage 10A Control Artefacts

**Files:**
- Create: `analysis/legal/stage-10a-statutory-confirmation-dossier-control-package.md`
- Create: `statutory_dossier/controls/dossier-component-register.csv`
- Create: `statutory_dossier/controls/dossier-readiness-gate.csv`
- Create: `statutory_dossier/controls/submission-no-go-register.csv`
- Create: `statutory_dossier/controls/statutory-route-memorandum-control.md`
- Create: `statutory_dossier/draft_scheme_order/clause-by-clause-powers-matrix.csv`
- Create: `review/peer_review/stage-10a-statutory-dossier-review.md`
- Create: `review/stage_gate_reports/stage-10a-statutory-dossier-control-report.md`
- Create: `docs/stages/stage-10a-statutory-dossier.md`

- [x] Add the 23 anticipated statutory confirmation dossier components from the master prompt.
- [x] Mark every dossier component as `blocked_control_only`.
- [x] Add submission no-go controls for statutory submission readiness, certified order, DfT acceptance, completed consultation statement, FBC and implementation-ready legal pack claims.
- [x] Add statutory route memorandum and clause powers matrix controls.
- [x] Add simulated legal, Monitoring Officer, DfT process, finance, consultation and red-team review artefacts preserving no-go status.

### Task 3: Add Validator And Wire QA

**Files:**
- Create: `scripts/validate_statutory_dossier.py`
- Modify: `Makefile`
- Modify: `scripts/validate_registers.py`

- [x] Validate required Stage 10A files and CSV headers.
- [x] Validate exact 23-component dossier coverage.
- [x] Validate every component remains `blocked_control_only`.
- [x] Validate clause-by-clause powers matrix coverage and no-go wording.
- [x] Add `statutory-qa` and include it in `make validate`.
- [x] Add statutory dossier controls to register validation.

### Task 4: Update Navigation And Registers

**Files:**
- Modify: `README.md`
- Modify: `docs/stages/README.md`
- Modify: `docs/visuals/stage-gate-map.mmd`
- Modify: `docs/officer/assurance-dashboard.md`
- Modify: `CHANGELOG.md`
- Modify: `governance/stage-gate-plan.md`
- Modify: governance and evidence registers.

- [x] Add Stage 10A to public navigation and visual map.
- [x] Add Stage 10A to officer dashboard and stage index.
- [x] Add issue, risk, requirement, approval, sign-off, decision, evidence gap and claim rows.
- [x] Add pitfall, checks-and-balances and stage-risk rows.

### Task 5: Verify, Review, Commit And Push

- [x] Run `python3 -m unittest tests.test_statutory_dossier`.
- [x] Run `python3 scripts/validate_statutory_dossier.py`.
- [x] Run expected blocked check: `python3 scripts/validate_statutory_dossier.py --gate`.
- [x] Run `make validate` and targeted QA commands.
- [x] Run `git diff --check`, prompt parity and no-authored-PDF scan.
- [x] Use simulated subagent review for statutory dossier due diligence and public/officer comprehension risk.
- [x] Fix findings.
- [ ] Commit as `docs: add Stage 10A statutory dossier controls`.
- [ ] Push `main`.
