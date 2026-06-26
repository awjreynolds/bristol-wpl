# Stage 18A Nottingham Displacement And Transferability

Status: complete as comparator-learning control only.  
Date: 2026-06-26.

## Purpose

Stage 18A responds to a specific public/officer risk: Nottingham is the only implemented UK Workplace Parking Levy precedent, so readers may over-read it as a forecast for Bristol.

The stage converts Nottingham, TfL and Leicester comparator material into transferability questions. It does not treat those sources as Bristol evidence.

## What Was Added

- Expanded `analysis/economic/nottingham_lessons_register.csv` from NLR-0007 to NLR-0015 to cover residential baseline, CPZ/RPZ readiness, monitoring triggers, current Nottingham refresh, revenue, source hierarchy, public acceptability, package attribution and employer behaviour.
- Expanded `analysis/economic/nottingham-transferability-matrix.csv` from NTM-007 to NTM-011 for revenue/net proceeds, source hierarchy, public acceptability, mode/congestion/package separation and employer behaviour.
- Added `analysis/economic/nottingham-displacement-control-checklist.csv` as a no-go checklist for residential street baseline, boundary displacement, CPZ/RPZ options, equality/accessibility, monitoring, employer behaviour and current Nottingham refresh.
- Reworked the officer Nottingham briefing as transferability questions rather than Bristol lessons.
- Updated the assurance dashboard, public README, root README and visual stage map so first-time readers see that lessons are not Bristol forecasts or ready mitigations.
- Hardened `scripts/validate_nottingham_transferability.py` and `tests/test_nottingham_lessons.py` so the stage fails if required rows disappear or key blockers are softened.

## Key Learning

Learning from Nottingham means identifying questions Bristol must answer. It does not mean Bristol would get the same impacts.

The most important Stage 18A control is residential spillover. Any Bristol WPL work would need boundary options, an authoritative parking inventory, street-level parking baseline, affected-street mapping, equality/accessibility review, employer-behaviour evidence and a monitoring/trigger regime before relying on CPZ/RPZ or other mitigation.

## Live Blockers

- `ISS-0028`: comparator lessons could be misconstrued as Bristol forecasts or mitigation readiness.
- `EG-0008`: current Nottingham charge, threshold and operating status are not refreshed.
- `EG-0014`: authoritative Bristol boundary input package and spatial licences are absent.
- `EG-0046`: Bristol-specific transferability evidence for comparator lessons does not exist.
- `RISK-0009`: independent Nottingham congestion source acquisition failed.
- `PIT-0005`: residential spillover and CPZ/RPZ mitigation evidence remain absent.

## No-Go Position

Stage 18A does not:

- prove Bristol displacement, congestion, revenue, mode shift, employer behaviour, acceptability or public-transport outcomes;
- select or test a Bristol boundary;
- create a workplace parking inventory;
- design, cost, consult on or approve CPZ/RPZ controls;
- refresh current Nottingham evidence;
- assemble or approve an OBC, FBC, consultation pack, statutory submission or officer-distribution document.

## Gate Evidence

- `review/peer_review/stage-18a-nottingham-displacement-transferability-review.md`
- `review/stage_gate_reports/stage-18a-nottingham-displacement-transferability-report.md`
- `python3 scripts/validate_nottingham_transferability.py`
- `python3 -m unittest tests.test_nottingham_lessons`
