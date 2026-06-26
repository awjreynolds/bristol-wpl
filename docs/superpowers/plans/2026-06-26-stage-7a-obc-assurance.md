# Stage 7A OBC Assurance Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add OBC assurance-gate controls that define how a future Stage 7 OBC gate would be reviewed while preserving the current no-go position.

**Architecture:** Keep Stage 6A assembly blocking intact. Add a Stage 7A layer under `analysis/obc/`, `business_case/obc/controls/`, `review/`, `docs/stages/` and validators so the repo controls assurance-panel review, red-team review, decision-report wording and blocked gate behavior.

**Tech Stack:** Markdown, CSV, Python standard library, `unittest`, existing Makefile validation targets.

---

### Task 1: Write Failing Stage 7A Tests

**Files:**
- Create: `tests/test_obc_assurance.py`

- [x] Add tests requiring `scripts/validate_obc_assurance.py`.
- [x] Add tests requiring `business_case/obc/controls/stage-7-obc-gate-checklist.csv`.
- [x] Add tests requiring `business_case/obc/controls/stage-7-assurance-panel-register.csv`.
- [x] Add a test proving `scripts/validate_obc_assurance.py --gate` fails while live blockers remain.
- [x] Run `python3 -m unittest tests.test_obc_assurance` and confirm red failure from missing Stage 7A files.

### Task 2: Add Stage 7A Control Artefacts

**Files:**
- Create: `analysis/obc/stage-7a-obc-assurance-gate-control-package.md`
- Create: `business_case/obc/controls/stage-7-obc-gate-checklist.csv`
- Create: `business_case/obc/controls/stage-7-assurance-panel-register.csv`
- Create: `business_case/obc/controls/stage-7-decision-report-control.md`
- Create: `business_case/obc/controls/stage-7-red-team-packet.md`
- Create: `review/peer_review/stage-7a-obc-assurance-review.md`
- Create: `review/stage_gate_reports/stage-7a-obc-assurance-gate-report.md`
- Create: `docs/stages/stage-7a-obc-assurance.md`

- [x] Add future OBC gate checklist rows covering legal, strategic, economic, spatial, finance, commercial, management, consultation, equality/data/accessibility, statutory route, red team and officer-editability.
- [x] Add assurance panel roles with real-world replacement roles.
- [x] Add decision-report controls banning proceed recommendation wording while blockers remain.
- [x] Add a bounded red-team packet.
- [x] Add Stage 7A review and gate report preserving no-go status.

### Task 3: Add Validator And Wire QA

**Files:**
- Create: `scripts/validate_obc_assurance.py`
- Modify: `Makefile`

- [x] Validate required Stage 7A files and CSV headers.
- [x] Validate checklist coverage and blocked status.
- [x] Validate assurance panel real-world replacements.
- [x] Validate required no-go wording.
- [x] Add `obc-assurance-qa` and include it in `make validate` and `make obc-qa`.

### Task 4: Update Navigation And Registers

**Files:**
- Modify: `README.md`
- Modify: `docs/stages/README.md`
- Modify: `docs/visuals/stage-gate-map.mmd`
- Modify: `docs/officer/assurance-dashboard.md`
- Modify: `CHANGELOG.md`
- Modify: `governance/stage-gate-plan.md`
- Modify: governance and evidence registers.

- [x] Add Stage 7A to public navigation and visual map.
- [x] Add issue, risk, requirement, approval, sign-off, decision, evidence gap and claim rows.
- [x] Add pitfall, checks-and-balances and stage-risk rows.

### Task 5: Verify, Commit And Push

- [x] Run `python3 -m unittest tests.test_obc_assurance`.
- [x] Run `make validate`.
- [x] Run `make obc-qa` and `make obc-assurance-qa`.
- [x] Run expected blocked checks: `python3 scripts/validate_obc_assurance.py --gate`, `make gate-obc`, `make gate-fbc`.
- [x] Run `git diff --check` and no-authored-PDF scan.
- [ ] Commit as `docs: add Stage 7A OBC assurance controls`.
- [ ] Push `main`.
