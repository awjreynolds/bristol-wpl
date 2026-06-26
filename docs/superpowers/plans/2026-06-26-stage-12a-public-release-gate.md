# Stage 12A Public Release Gate Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Record public GitHub visibility and add controls that prevent public-release overclaims.

**Architecture:** Add a Stage 12A publication-control layer under `analysis/publication/`, `publication/controls/`, `review/`, `docs/stages/` and validators. Keep it separate from WPL readiness gates; publication QA may pass while OBC/FBC/statutory gates remain blocked.

**Tech Stack:** Markdown, CSV, Python standard library, `unittest`, existing Makefile validation targets.

---

### Task 1: Write Failing Public-Release Tests

**Files:**
- Create: `tests/test_public_release_gate.py`

- [x] Add tests requiring `scripts/validate_public_release.py`.
- [x] Add tests requiring `publication/controls/repository-publication-checklist.csv`.
- [x] Add tests requiring `publication/controls/public-release-no-go-register.csv`.
- [x] Add tests requiring `publication/controls/public-release-scan-register.csv`.
- [x] Add README wording tests for public visibility and no-readiness status.
- [x] Run `python3 -m unittest tests.test_public_release_gate` and confirm red failure from missing Stage 12A files.

### Task 2: Add Stage 12A Publication Controls

**Files:**
- Create: `analysis/publication/stage-12a-public-release-control-package.md`
- Create: `publication/controls/repository-publication-checklist.csv`
- Create: `publication/controls/public-release-no-go-register.csv`
- Create: `publication/controls/public-release-scan-register.csv`
- Create: `review/peer_review/stage-12a-public-release-review.md`
- Create: `review/stage_gate_reports/stage-12a-public-release-gate-report.md`
- Create: `docs/stages/stage-12a-public-release.md`

- [x] Record GitHub visibility as public.
- [x] Add no-go claims for publication overclaims.
- [x] Add no-authored-PDF restricted-path and prompt-parity scan controls.

### Task 3: Add Validator And Wire QA

**Files:**
- Create: `scripts/validate_public_release.py`
- Modify: `Makefile`
- Modify: `scripts/validate_registers.py`

- [x] Validate required Stage 12A files and CSV headers.
- [x] Validate required public-release no-go claims.
- [x] Validate no authored PDFs and restricted paths.
- [x] Add `public-release-qa` and include it in `make validate`.

### Task 4: Update Navigation And Registers

- [x] Add Stage 12A to README, stage index, visual map and gate plan.
- [x] Add issue, risk, requirement, approval, sign-off, decision and claim rows.
- [x] Add pitfall, checks-and-balances, real-world adoption and stage-risk rows.

### Task 5: Verify, Review, Commit And Push

- [x] Run `python3 -m unittest tests.test_public_release_gate`.
- [x] Run `python3 scripts/validate_public_release.py`.
- [x] Run `make validate` and targeted QA commands.
- [x] Run expected blocked gate checks.
- [x] Run `git diff --check`, prompt parity and no-authored-PDF scan.
- [x] Use simulated public-release reviewer agents for publication and overclaim due diligence.
- [x] Fix findings.
- [x] Commit as `docs: add Stage 12A public release controls`.
- [x] Push `main`.
