# Stage 18A Gate Report: Nottingham Displacement And Transferability

Status: accepted for Stage 18A control purposes only.  
Date: 2026-06-26.

## Gate Question

Can the repo explain Nottingham and UK comparator lessons in a way that is useful for officers and cabinet readers without implying that Nottingham impacts, mitigation or operating assumptions transfer to Bristol?

## Gate Answer

Yes, for simulation control purposes only.

Stage 18A strengthens the comparator-learning layer and makes the no-transfer position visible in the README, public summary, officer dashboard, Nottingham briefing, registers and validator.

## Artefacts Checked

- `analysis/context/stage-18a-nottingham-displacement-transferability-context.md`
- `analysis/economic/nottingham_lessons_register.csv`
- `analysis/economic/nottingham-transferability-matrix.csv`
- `analysis/economic/nottingham-displacement-control-checklist.csv`
- `docs/officer/nottingham-and-comparator-lessons.md`
- `docs/officer/assurance-dashboard.md`
- `docs/public/README.md`
- `README.md`
- `scripts/validate_nottingham_transferability.py`
- `tests/test_nottingham_lessons.py`
- Stage 18A rows in the issue, risk, pitfall, evidence-gap, requirement, checks, decision, approval, sign-off and stage-risk registers.

## Acceptance Criteria

| Criterion | Result |
|---|---|
| Required Stage 18A lesson rows `NLR-0007` to `NLR-0015` exist and remain blocked | Pass |
| Required transferability rows `NTM-007` to `NTM-011` exist and remain blocked | Pass |
| Displacement checklist exists and all controls remain blocked | Pass |
| Officer and public wording says lessons are not Bristol forecasts or ready mitigations | Pass |
| Current Nottingham evidence gap remains open | Pass |
| Failed independent congestion-source gap remains open | Pass |
| CPZ/RPZ readiness is not claimed | Pass |
| Stage 18A risks and blockers are recorded in registers | Pass |

## Validation

Focused validation run:

```text
python3 scripts/validate_nottingham_transferability.py
Nottingham transferability QA passed
```

Focused unit test run:

```text
python3 -m unittest tests.test_nottingham_lessons
Ran 4 tests
OK
```

Full validation and secret scan are required before commit and push under the stage-continuation protocol.

## Remaining Blockers

- No authoritative Bristol boundary or workplace parking inventory exists.
- No residential street baseline, occupancy/stress map or affected-street evidence exists.
- No CPZ/RPZ option maps, costs, enforcement capacity, equality screening, consultation approach or decision route exists.
- No Bristol revenue, compliance, operating-cost or net-proceeds model exists.
- No Bristol mode-share, congestion or package-attribution model exists.
- No Bristol employer segmentation or behavioural-response evidence exists.
- Current Nottingham charge, threshold, operating status and latest reporting are not refreshed.
- The independent Nottingham congestion source remains unavailable.

## Gate Decision

Stage 18A passes as a comparator-transferability control stage only.

It does not approve a Bristol WPL, close any OBC/FBC/statutory gate, create current Nottingham certification, or make CPZ/RPZ mitigation ready.
