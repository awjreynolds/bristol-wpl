# Stage 14A Source Note Controls Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development or superpowers:executing-plans. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a source-note pilot and QA controls so source-heavy drafting has bounded, editable evidence guidance without claiming the evidence base is complete.

**Architecture:** Add source-note artefacts under `evidence/source_notes/`, Stage 14A narrative docs, a validator and tests. Keep `ISS-0007` open.

**Tech Stack:** Markdown, CSV, Python standard library, `unittest`, existing Makefile validation targets.

---

### Task 1: Red Test Source-Note Controls

- [x] Create `tests/test_source_notes.py`.
- [x] Require source-note validator, coverage register, no-go register and core note files.
- [x] Require README/stage navigation.
- [x] Run `python3 -m unittest tests.test_source_notes` and confirm red failure.

### Task 2: Add Source-Note Artefacts

- [x] Create `analysis/evidence/stage-14a-source-note-control-package.md`.
- [x] Create `evidence/source_notes/README.md`.
- [x] Create `evidence/source_notes/source-note-coverage-register.csv`.
- [x] Create `evidence/source_notes/source-note-no-go-register.csv`.
- [x] Create pilot source notes under `evidence/source_notes/core/`.
- [x] Create peer-review and gate-report files.

### Task 3: Add Validator And Wire QA

- [x] Create `scripts/validate_source_notes.py`.
- [x] Add `source-notes-qa` to `Makefile` and include it in `make validate`.
- [x] Add source-note CSV headers to `scripts/validate_registers.py`.

### Task 4: Update Navigation And Registers

- [x] Update README, stage index, visual map, officer dashboard and stage-gate plan.
- [x] Add issue, risk, requirement, approval, sign-off, decision, claim, evidence-gap, pitfall, control, stage-risk and adoption rows.

### Task 5: Verify, Review, Commit And Push

- [x] Run `python3 -m unittest tests.test_source_notes`.
- [x] Run `python3 scripts/validate_source_notes.py`.
- [x] Run `make validate` and targeted QA commands.
- [x] Run expected blocked gate checks.
- [x] Run reviewer agents for evidence/source-note clarity and no-go risk.
- [x] Fix findings.
- [x] Commit as `docs: add Stage 14A source note controls`.
- [x] Push `main`.
