# Stage Continuation And Context Control

Status: standing instruction for future stages.  
Date: 2026-06-26.

## Purpose

Future work must continue stage by stage without loading the whole repository or whole conversation into one agent. The main agent is the coordinator. Subagents do bounded discovery, drafting, QA and red-team review with explicit file and source limits.

This instruction applies to every stage after Stage 15A unless a later stage replaces it with a stricter protocol.

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
7. Continue to the next stage only after the current stage has a stage document, gate report, register trail, validation evidence, commit and push.

## Required Subagent Pattern

Each substantive stage should use at least these lanes:

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
- explicit no-go claims;
- allowed write paths, or `read-only`;
- output length limit;
- required return structure;
- instruction to record unknowns as gaps rather than infer.

Subagents must not be asked to "review the whole repo". If they need more context, they must request the specific file, source ID or register row.

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

## Validation And Commit Rule

Before a stage is complete:

- run the relevant focused validator;
- run `make validate`;
- run `git diff --check`;
- run `python3 scripts/scan_secrets.py --all-history` before public pushes;
- commit with a stage-specific message;
- push the branch unless the user has prohibited pushing or the remote is unavailable.

Never claim that a stage is complete until the validation evidence has been read and recorded in the stage gate report or final response.
