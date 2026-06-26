# Stage 2L Context Management Review

Status: simulation peer review.  
Date: 2026-06-26.  
Scope: bounded context policy for future legal, governance, OBC/FBC, statutory, WECA/MCA, DfT and order-change agents.

This review records simulated agent due diligence only. It is not legal advice, statutory confirmation, professional certification or approval by any public body.

## Review Criteria

The Stage 2L packet was assessed against these criteria:

- main coordinating agents can identify a small mandatory read set before drafting;
- domain add-ons are task-specific and do not require loading the whole repo;
- raw evidence and full source packs are deferred until a claim requires them;
- P0/P1 blockers remain visible;
- Stage 2B-K narrowing controls cannot be mistaken for readiness;
- subagent task packets include bounded file sets, acceptance criteria and banned claims;
- the packet distinguishes main-agent context loading from bounded subagent task packets;
- the packet distinguishes agentic simulation sign-off from real-world approval.

## Peer Review Findings

The Context Management Review Agent recommended the following control structure:

- use `AGENTS.md`, `README.md`, `instructions/00-operating-model.md`, `instructions/10-stage-gates.md`, `governance/stage-gate-plan.md` and active registers as the mandatory first read for the main coordinating agent;
- treat `CODEX_MASTER_PROMPT.md` as a duplicate of `instructions/00-operating-model.md` unless copy drift is being checked;
- prefer Stage 2B-K gate reports over full analysis and specialist-review files for first-pass context;
- add domain-specific files only for legal/governance, OBC/FBC, DfT, WECA/MCA or order-change tasks;
- do not read raw evidence, processed evidence, acquisition logs, full WECA/MCA history files or full OBC/FBC trees unless a claim or contradiction requires them.

Finding: the Stage 2L packet satisfies the bounded-read objective for simulation purposes.

Limitation: this is a process control. It does not validate the underlying law, evidence, modelling, finance, spatial data, consultation approach or business-case content.

## Red-Team Findings

The Red-Team Context Agent identified eight high-risk future hallucination modes:

| Failure mode | Stage 2L control |
|---|---|
| Bristol final order-maker drift | Keep RISK-0001 and ISS-0001 P0; require the Stage 2I decision box. |
| Bristol authority-status overclaim | Use only Bristol-led working assumption wording until the internal route is closed. |
| WECA/MCA silence becomes no-role | Prohibit no-role, consent-required and consent-not-required conclusions without a formal source. |
| WECA/MCA funding context becomes approval | Require Stage 2H funding and assurance classification before OBC/FBC reliance. |
| DfT engagement becomes confirmation | Classify DfT interactions as engagement, expectation, requirement, decision or confirmation material. |
| Order-change or revocation shortcut | Separate initial order, ordinary variation, RPI-only variation, revocation and consultation controls. |
| OBC/FBC or consultation readiness creep | State that Stage 2B-K are narrowing controls only and do not unblock readiness. |
| Source absence treated as proof | Label every absence as bounded search evidence only, never proof of no role or no process. |

Finding: the packet directly addresses the main hallucination risks if future agents follow the mandatory first-read and banned-claim rules.

Limitation: the control can fail if agents ignore the packet, overload subagents with raw evidence by default, or fail to update registers when new sources change the position.

## Simulation Sign-Off

Decision: simulation sign-off with conditions.

Conditions:

- update `AGENTS.md`, `README.md`, `instructions/00-operating-model.md`, `CODEX_MASTER_PROMPT.md` and `governance/stage-gate-plan.md` to point future agents to the Stage 2L packet;
- record the Stage 2L control in the approvals, requirements, risk, issue and simulation sign-off registers;
- retain no-go status for OBC/FBC readiness, statutory consultation, preferred scheme selection, final order-making and statutory submission.
