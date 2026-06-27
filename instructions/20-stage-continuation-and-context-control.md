# Stage Continuation And Context Control

Status: standing instruction for future stages.  
Date: 2026-06-27.

## Purpose

Future work must continue stage by stage without loading the whole repository or whole conversation into one agent. The main agent is the coordinator. Subagents do bounded discovery, drafting, QA and red-team review with explicit file and source limits.

This instruction applies to every future stage and continuation stage unless a later stage-specific protocol explicitly replaces it with a stricter protocol. Stage 29A adds the reusable template `docs/agents/subagent-stage-packet-template.md` and validator `scripts/validate_subagent_context_control.py`.

Subagents must receive bounded task packets. This is a context-control requirement, not substantive assurance. For deterministic checks: subagents must receive bounded task packets.

## Stage Continuation Rule

For each new stage:

1. Start from the latest root `README.md`, `docs/stages/README.md`, `governance/stage-gate-plan.md`, the previous stage gate report and the most relevant domain context packet.
2. Do not load long source packs, full raw evidence directories or every previous report by default.
3. Create or update a short stage context packet before substantive drafting. Put it under `analysis/context/` unless a domain folder is more appropriate.
4. The packet must state:
   - stage purpose;
   - files in scope;
   - files out of scope;
   - source IDs in scope;
   - open issue, risk, evidence-gap and pitfall IDs;
   - no-go claims;
   - subagent roles;
   - validator commands;
   - required register updates;
   - commit/push condition.
5. Spawn subagents with bounded task packets, not the entire repo context.
6. Use `fork_context=false` by default when tooling supports it. Only fork full conversation context where the subagent genuinely needs the conversation history.
7. Use `docs/agents/subagent-stage-packet-template.md` unless a narrower stage-specific packet exists.
8. Continue to the next stage only after the current stage has a stage document, gate report, register trail, validation evidence, commit and push.

## Required Subagent Pattern

Each substantive stage must use these four review lanes unless the stage context packet records a justified exception and preserves at least one independent red-team or public/officer review.

| Lane | Default mode | Purpose |
|---|---|---|
| Domain reviewer | Read-only unless assigned a disjoint write set | Tests the technical substance for the stage. |
| Evidence/citation reviewer | Read-only unless assigned a disjoint write set | Checks source IDs, source-note coverage, claim limits and evidence gaps. |
| Public/officer readability reviewer | Read-only | Checks whether a council officer, cabinet member or public reader can understand the stage and its limits. |
| Red-team reviewer | Read-only | Challenges overclaims, missing blockers, hallucination risk and gate leakage. |

For small documentation-control stages, the main agent may combine the domain and evidence lanes, but must still preserve an independent red-team or public/officer review where practical.

## Subagent Packet Rules

Every subagent packet must include:

- exact question to answer;
- role and simulated competence;
- maximum 8-12 first-read files unless the task justifies more;
- specific source IDs or register IDs where relevant;
- context budget and stopping rule;
- files or source sets that are explicitly out of scope;
- explicit no-go claims;
- allowed write paths, or `read-only`;
- output length limit;
- required return structure;
- review criteria;
- instruction to record unknowns as gaps rather than infer.

Subagents must not be asked to "review the whole repo". If they need more context, they must request the specific file, source ID or register row.

Each packet must include lane-specific acceptance criteria, P0/P1/P2/P3 severity rules, no-go claims, evidence/source-ID checks, hallucination controls and the exact condition under which the reviewer may recommend proceed, proceed with conditions, rework, pause or no-go.

If subagent tooling is unavailable, the stage packet must record the limitation, identify which review lanes could not be independently performed, downgrade any affected completion claim and apply the stop-condition rule for unavailable required simulation assurance.

## Durable Packet And Handover Storage

Store stage context packets and subagent task packets under `analysis/context/<stage-id>/` where practical. Existing single-file context packets may remain in `analysis/context/` but new substantive stages should prefer a stage folder when multiple packets are created.

Store subagent handovers under `review/stage_gate_reports/<stage-id>/subagent-handovers/` or cite the exact transcript-derived handover location in the stage peer review if the tool does not persist files. The stage gate report must cite packet and handover paths or record why durable handovers were unavailable.

## Main Agent Synthesis

The main agent must not paste subagent outputs into final documents uncritically. It must:

- compare subagent findings for contradictions;
- decide which findings change the stage artefacts;
- add or update issue, risk, evidence-gap, pitfall, requirement, claim-evidence, decision, approval and simulation sign-off rows where needed;
- keep no-go blockers visible;
- update the README or stage index when public navigation changes;
- run validation before claiming completion.

## Context Bloat Controls

- Prefer compact source-note files, context packets and register rows over reopening raw documents.
- Use source IDs and line/page references instead of long quotations.
- Keep subagent outputs short and structured.
- Archive stage findings into stage artefacts rather than relying on chat history.
- If context becomes large, stop adding broad reads and create a stage handover note with open tasks, validators and next files to inspect.
- Never paste the full conversation, whole source register, full raw evidence tree or full previous-stage history into a subagent packet unless a stage gate report explains why the task cannot be performed with a bounded packet.
- Record contradictions between subagents in the stage context packet or peer review rather than silently choosing the more convenient answer.

## Instruction Validation Limit

`scripts/validate_subagent_context_control.py` checks that this instruction, the master prompt and the reusable packet template still contain the expected context-control requirements.

That validator does not prove future agents obeyed the instruction, that subagent reviews were independent, that findings are correct, that evidence is true, that professional assurance exists or that any WPL readiness gate can pass.

It does not prove legal correctness. It does not prove professional assurance. It does not prove WPL readiness.

## Validation And Commit Rule

Before a stage is complete:

- run the relevant focused validator;
- run `make validate`;
- run `git diff --check`;
- run `python3 scripts/scan_secrets.py --all-history` before public pushes;
- record focused and full command evidence in `evidence/validation/validation-run-register.csv` and a stage-specific validation log where the stage materially changes public/officer navigation, validators, registers or gate reports;
- commit with a stage-specific message;
- push the branch unless the user has prohibited pushing or the remote is unavailable.

Never claim that a stage is complete until the validation evidence has been read and recorded in the stage gate report or final response.

Validation evidence is process evidence only. It can record command text, run date, repo state, exit code and output summary. It does not prove evidence truth, source currentness, legal correctness, substantive gate judgement, professional assurance, blocker completeness, risk adequacy, mitigation adequacy or WPL readiness.
