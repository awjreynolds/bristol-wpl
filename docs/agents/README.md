# Agent Context Controls

Status: Stage 29A context-control guide.  
Date: 2026-06-27.

This folder holds reusable templates for bounded subagent work.

Start with `docs/agents/subagent-stage-packet-template.md` when dispatching future stage subagents. The template is designed to reduce context bloat and hallucination risk by forcing exact questions, limited first-read files, source/register IDs, no-go claims, review criteria and simulation-only sign-off wording.

The control is checked by `scripts/validate_subagent_context_control.py`.

This does not prove future agents obeyed the instruction, that findings are correct, that reviews are independent, that evidence is true, that professional assurance exists or that WPL readiness has changed.
