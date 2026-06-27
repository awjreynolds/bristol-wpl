# Stage 29A Context: Subagent Context-Control Hardening

Status: context packet for Stage 29A.  
Date: 2026-06-27.

## Purpose

Stage 29A hardens the instructions for continuing future stages with bounded subagents, explicit review criteria and durable context-control artefacts.

The user specifically asked that future stages continue using subagents to reduce context bloat and hallucination. This stage turns that into visible instructions, a reusable packet template and an offline validator.

## In Scope

- `CODEX_MASTER_PROMPT.md`
- `instructions/20-stage-continuation-and-context-control.md`
- `docs/agents/subagent-stage-packet-template.md`
- `docs/agents/README.md`
- navigation and register rows needed to make the control discoverable
- `scripts/validate_subagent_context_control.py`

## Out Of Scope

- proving that future agents obey instructions;
- auditing chat history;
- judging actual future subagent behaviour;
- proving evidence truth, legal correctness, professional assurance or WPL readiness.

## Required Review Lanes

- Instruction reviewer: check mandatory language, durable handover storage and packet criteria.
- Validator design reviewer: check the validator is presence-only and no-overclaim.
- Red-team reviewer: challenge false assurance, simulation sign-off and hallucination-prevention claims.

## No-Go Claims

Do not claim Stage 29A proves prompt fidelity, actual context isolation, future-stage compliance, subagent reasoning quality, blocker completeness, evidence truth, legal correctness, professional assurance or WPL readiness.

## Register Trail

- `ISS-0039`
- `RISK-0042`
- `PIT-0036`
- `EG-0057`
- `REQ-0050`
- `CB-0036`
- `DEC-0043`
- `APP-0048`
- `SSO-0106`
- `SSO-0107`

## Validation

- `python3 scripts/validate_subagent_context_control.py`
- `python3 -m unittest tests.test_subagent_context_control`
- `make validate`
- `git diff --check`
- `python3 scripts/scan_secrets.py --all-history`

## Residual Limit

Instruction/template presence only. It does not prove future agents obey instructions, evidence truth, legal correctness, professional assurance, substantive gate correctness or WPL readiness.
