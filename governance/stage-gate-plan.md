# Stage-Gate Plan

Status: working simulation control.

## Gate Rule

No gate may pass with an unresolved P0 finding. P1 findings block the gate unless a named simulation gate authority accepts a written condition, owner, deadline and residual risk.

## Simulation Sign-Offs

Simulation sign-offs are recorded in `governance/simulation_signoff_register.csv`. They have no real-world legal, statutory, financial or professional effect.

## Stage Gates

| Gate | Required Evidence | Required Simulation Reviews | Blocking Conditions |
|---|---|---|---|
| Stage 0 Bootstrap | Repo architecture, registers, validation scripts, source ingest | Programme Orchestrator | Missing controls, authored PDFs, sensitive data in normal repo |
| Stage 1 Evidence Baseline | Source register, acquisition log, source notes plan, gaps | Evidence Librarian, Red Team | Unverified core source set or unsupported material claims |
| Stage 2 Legal/Governance | Legal route note, compliance matrix, WECA/MCA role evidence | Legal Review Agent, Governance Review Agent | Unresolved promoter or confirmation-route P0 |
| Stage 2H WECA/MCA Funding/Assurance Dependency | Funding and assurance dependency matrix, Stage 2H trigger map, post-Stage 2H context packet, dependencies register, claim rows | Funding Assurance Agent, WECA Governance Agent, Finance Review Agent, Legal Review Agent, Red Team | Any unclassified MCA funding, CRSTS, Single Pot, CAZ repayment, mass-transit, bus, cross-boundary or delivery-assurance dependency |
| Stage 2I Bristol Final Order/Submission Route | Final order decision-box control, council route map, legal review, risk and issue rows | Legal Review Agent, Monitoring Officer Simulation Agent, Bristol Governance Agent, Red Team | Any claim that final order-maker, statutory submitter, signatory route, Full Council exclusion or officer-only route is settled |
| Stage 2J DfT Process/Engagement Classification | DfT classification note, questions for DfT, confirmation checklist, bounded search-control sources | Legal Review Agent, DfT Process Simulation Agent, Appraisal Guidance Agent, Red Team | Any claim that DfT has approved, accepted, confirmed or issued a WPL-specific process without formal source evidence |
| Stage 2K Revocation/Variation Controls | Order-change control note, scheme order working draft controls, consultation statement controls, legal review | Legal Review Agent, Consultation Review Agent, Red Team | Any unclassified order-change, RPI-only exemption, revocation, publication, consultation, DfT process or Bristol signatory claim |
| Stage 2L Context Management | Post-Stage 2 legal/governance context packet, peer review, banned-claim controls, register updates | Context Management Review Agent, Red Team, Simulation Gate Authority | Future legal/governance/OBC/FBC/statutory agents lack bounded read rules, banned claims or P0/P1 blocker visibility |
| Stage 3 Strategic Assessment | Problem definition, objectives, theory of change | Strategic Case Review Agent | Objectives prejudge WPL |
| Stage 4 Spatial/Data | Boundary options, parking inventory method, data controls | GIS/Data Review Agent | Boundary/data cannot support appraisal |
| Stage 5 Options/ASR | Longlist, shortlist, OAR, ASR, ASST | TAG/Appraisal Review Agent, Red Team | Predetermined shortlist or unreviewed ASR |
| Stage 7 OBC Gate | OBC, model outputs, finance, equality, operations | Integrated Case Review Agent, Red Team | Open P0 or unsupported recommendation |
| Stage 8 Consultation Launch | Materials, privacy, accessibility, formative consultation test | Legal, Equality, Data, Accessibility Agents | Launch-blocking legal/privacy/accessibility issue |
| Stage 11 FBC/Statutory Gate | FBC, scheme order, dossier, consultation report | Legal, Finance, Operations, Integrated Review Agents | Open P0 or simulated statutory-route failure |

## Real-World Adoption Gaps

If outputs are ever used outside the simulation, agent sign-offs must be replaced by appropriate human professional and public-authority approvals.
