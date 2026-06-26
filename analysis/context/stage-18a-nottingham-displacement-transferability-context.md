# Stage 18A Nottingham Displacement Transferability Context

Status: context packet for Nottingham and comparator displacement lessons.  
Date: 2026-06-26.

## Stage Purpose

Stage 18A deepens Nottingham and comparator lesson controls, especially residential spillover, employment-area parking displacement, CPZ/RPZ mitigation, employer behaviour and public-transport package dependence.

The stage turns existing lessons into an operational checklist for Bristol. It does not transfer Nottingham, TfL or Leicester outcomes to Bristol.

## Files In Scope

- `analysis/economic/nottingham_lessons_register.csv`
- `analysis/economic/nottingham-transferability-matrix.csv`
- `docs/officer/nottingham-and-comparator-lessons.md`
- `governance/pitfalls_register.csv`
- `governance/risk_register.csv`
- `evidence/evidence_gap_register.csv`
- `evidence/claim_evidence_matrix.csv`
- `scripts/validate_nottingham_transferability.py`
- `tests/test_nottingham_lessons.py`
- Stage 18A review and gate report files.

## Files Out Of Scope

- New revenue, congestion, mode-share, charge-level or employer-response assumptions.
- New Bristol boundary, parking inventory, CPZ/RPZ map, consultation material or model output.
- New web acquisition or replacement of failed `SRC-ACADEMIC-0001`.
- OBC/FBC drafting or consultation launch material.

## Source IDs In Scope

- `SRC-BCC-0006`
- `SRC-NOTT-0001`
- `SRC-NOTT-0002`
- `SRC-ACADEMIC-0002`
- `SRC-TFL-0001`
- `SRC-UK-0003`
- `SRC-ACADEMIC-0001` only as a failed-acquisition gap.

## Open Register IDs

- `ISS-0003`: boundary and parking inventory absent.
- `ISS-0004`: appraisal and model evidence absent.
- `ISS-0005`: independent Nottingham congestion source failed acquisition.
- `EG-0004`, `EG-0008`, `EG-0009`: comparator classification/currentness/publication gaps.
- `EG-0014`, `EG-0027`, `EG-0045`: spatial evidence, strategic baseline and future drafting-specific claim gaps.
- `PIT-0005`, `PIT-0006`, `RISK-0004`, `RISK-0006`, `RISK-0009`: existing displacement and transferability risks.

## No-Go Claims

Stage 18A must not claim:

- Nottingham proves Bristol displacement scale, congestion effect, mode shift, revenue, employer response or public transport benefits.
- Leicester or TfL proposal material proves Bristol effects or public acceptability.
- CPZ/RPZ mitigation is selected, designed, costed, consulted on or ready.
- A Bristol boundary, parking inventory, residential street baseline or displacement model exists.
- OBC/FBC, consultation, statutory or implementation readiness changes.

## Subagent Roles

- Comparator evidence reviewer: test Nottingham/TfL/Leicester transferability and source hierarchy.
- Spatial/displacement reviewer: test CPZ/RPZ, residential baseline, boundary and monitoring controls.
- Public/officer readability reviewer: test whether the lessons are understandable without implying Bristol transfer.
- Red-team reviewer: test overclaim, false mitigation readiness and context-bloat risks.

## Validator Commands

```bash
python3 scripts/validate_nottingham_transferability.py
python3 -m unittest tests.test_nottingham_lessons
make validate
git diff --check
python3 scripts/scan_secrets.py --all-history
```

## Commit/Push Condition

Do not proceed past Stage 18A until the lesson register, officer briefing, validator, register trail, review, gate report and validation evidence are committed and pushed.
