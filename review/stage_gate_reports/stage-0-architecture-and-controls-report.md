# Stage 0 Architecture And Controls Report

Status: simulation gate report.

## Scope

This report covers repository architecture, prompt improvements, seed-source ingestion, bounded discovery packets, initial registers, validation scripts and discovery-agent synthesis.

## Stage 0 Findings

- Repo architecture has been created.
- `inputs/bristol_wpl_codex_sources.csv` has been copied and ingested.
- `evidence/source_register.csv` contains 44 seed rows.
- Bounded discovery packets were created and seven discovery agents were run.
- Simulation sign-offs are recorded for D1-D7 with conditions.
- No OBC or FBC prose has been drafted.
- Validation passed using `python3 scripts/validate_registers.py`.
- Unit validation passed using `python3 -m unittest discover -s tests` with 9 tests.
- `make validate` passed.

## Blocking Controls

The next work must not proceed to preferred scheme design, options appraisal, consultation launch, OBC assembly or statutory route conclusions until the relevant P0 gaps are closed.

## Gate Decision

Simulation Stage 0 gate: **simulation sign-off with conditions**.

Conditions:

- Acquire and hash priority legal, Bristol, WECA/MCA, DfT/TAG and comparator sources.
- Populate legal compliance matrix and statutory crosswalk beyond header rows.
- Produce Stage 2 legal/governance simulation review.
- Replace placeholder parking-inventory schema before Stage 4 appraisal.
- Keep real-world adoption gaps visible.

## Evidence Of Validation

Validation was run after synthesis updates. The no-authored-PDF test, register header tests and seed-source tests passed.
