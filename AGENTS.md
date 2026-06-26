# Bristol WPL Simulation Agents

Mission: build a full-simulation, government-grade Bristol Workplace Parking Levy OBC/FBC/statutory dossier workspace.

Non-negotiables:
- Do not invent evidence, citations, approvals, model outputs or consultation responses.
- Do not create authored PDFs, PDF deliverables, or PDFs for officer review/distribution. Downloaded third-party source PDFs are allowed only as immutable raw evidence under `evidence/raw/**`.
- Use bounded subagent context packets and agentic simulation sign-offs.
- Every material claim must be cited, labelled as an assumption/inference/proposal, or recorded as a gap.
- Agent sign-offs are simulation sign-offs only and have no real-world legal, statutory, financial or professional effect.

Detailed operating instructions live in `instructions/`.
Start with `instructions/00-operating-model.md`, `instructions/10-stage-gates.md` and `instructions/20-stage-continuation-and-context-control.md`.

For main-agent legal, governance, statutory, OBC/FBC, DfT, WECA/MCA, order-change or consultation work after Stage 2L, start with `analysis/legal/post-stage-2-legal-governance-context-packet.md` before loading long reports or raw evidence. Subagents should receive bounded task packets rather than the whole context set.

For every future stage, use the Stage Continuation And Context Control protocol: create a compact stage packet, spawn bounded subagents with clear review criteria, synthesize their findings, update the register trail, validate, commit and push before moving on.
