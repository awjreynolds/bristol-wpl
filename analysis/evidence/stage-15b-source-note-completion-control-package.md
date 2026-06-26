# Stage 15B Source Note Completion Control Package

Status: complete as a bounded source-note completion stage.  
Date: 2026-06-26.

## Purpose

Stage 15B completes source-note coverage for downloaded priority-1 sources that were not covered by Stage 14A or Stage 15A. The purpose is source-use control, not claim verification.

This stage closes `ISS-0007`, `EG-0038` and `EG-0043` only for downloaded priority source-note coverage. It leaves `EG-0024` partially closed and opens `EG-0044` for claim-level source summaries.

## Cohort Boundary

Stage 15B adds 36 editable source notes in `evidence/source_notes/stage15b/`:

- WECA/MCA strategy, governance, assurance and function-mapping context.
- HMT, DfT, Green Book, TAG and business-case method guidance.
- Bounded GOV.UK search-control snapshots for WPL/DfT process discovery.
- Nottingham, TfL and Leicester comparator evidence.

It does not cover seeded-but-not-downloaded sources, failed acquisitions, lower-priority downloaded sources outside the controlled cohorts or any future source added after this date.

## Control Boundary

Stage 15B source notes:

- do not verify legal, governance, appraisal, finance, consultation, equality, public/officer or statutory claims;
- do not prove WECA/MCA approval, consent, support, objection, no-role status, assurance approval or funding allocation;
- do not prove DfT acceptance, Secretary of State readiness or absence of an unpublished or non-indexed process;
- do not prove Green Book or TAG compliance, BCR, VFM category, model acceptance or business-case readiness;
- do not transfer Nottingham, TfL or Leicester assumptions to Bristol without Bristol-specific transferability evidence;
- do not replace claim-level source summaries with source IDs, page or line references, reviewer status and limitations;
- do not close any OBC, FBC, consultation, statutory, procurement or implementation gate.

## Register Trail

- `ISS-0007`: closed only for acquired-priority source-note coverage.
- `ISS-0025`: controlled-open overclaim issue for Stage 15B wording.
- `EG-0024`: partially closed because source-note coverage is complete but claim-level summaries are not.
- `EG-0038` and `EG-0043`: closed only for downloaded priority source-note coverage.
- `EG-0044`: open claim-level source-summary gap.
- `RISK-0028`, `PIT-0022`, `REQ-0036`, `CB-0022`, `CLM-0038`, `DEC-0029`, `APP-0034`, `SSO-0078` and `SSO-0079`: Stage 15B controls and sign-offs.

## Validation Evidence Required

The Stage 15B gate must not pass unless:

- `scripts/validate_source_notes.py` passes;
- `tests/test_source_notes.py` passes;
- `make validate` passes;
- `git diff --check` passes;
- `python3 scripts/scan_secrets.py --all-history` passes;
- the gate report says "Accepted for acquired-priority source-note completion purposes only";
- the public README, stage index and officer dashboard all preserve the claim-level source-summary gap.

## Next Work

The next evidence stage should create claim-level source summaries for high-materiality claims. It should use bounded subagents with separate legal/governance, WECA/DfT, appraisal/economic, comparator/displacement, consultation/equality and public/officer review packets.
