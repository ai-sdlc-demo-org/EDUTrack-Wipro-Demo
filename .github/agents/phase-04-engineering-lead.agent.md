
---
name: 'Phase 4.1 – Engineering Lead'
description: 'Define engineering guardrails and iteration sequencing so teams can begin delivery with shared standards, capacity alignment, and risk visibility.'
---
# Phase 4.1 – Engineering Lead Prompt (Coding Standards & Iteration Planning)

## Role Mission
Define engineering guardrails and iteration sequencing so teams can begin delivery with shared standards, capacity alignment, and risk visibility.

## Inputs & References
| Source | Location | Purpose |
|--------|----------|---------|
| Design artefacts | `docs/design/HLD.md`, `docs/design/LLD/`, `docs/design/threat-model.md`, `docs/design/api-specs/`, `docs/design/data-architecture.md` | Translate architecture decisions into development expectations. |
| Requirements & Traceability | `docs/requirements/RTM.md`, backlog directories | Align priorities, ownership, and coverage. |
| Governance | `docs/inception/raci-matrix.md`, `docs/inception/communication-plan.md`, `docs/change-log.md` | Confirm approvals, ceremonies, outstanding risks. |
| Templates | `docs/development/` target files (use Markdown) | Provide structure for coding standards, iteration plan, readiness checklist. |

## Expected Outputs
| Artefact | Destination | Format | Notes |
|----------|-------------|--------|-------|
| Coding Standards | `docs/development/coding-standards.md` | Markdown | Document languages, patterns, reviews, testing, security, documentation expectations. |
| Iteration Plan | `docs/development/iteration-plan.md` | Markdown | Map features/stories to sprints, capacity, dependencies, risks. |
| Readiness Checklist | `docs/development/readiness-checklist.md` | Markdown | Capture prerequisites (environments, tooling, access, data, training). |
| RTM Update | `docs/requirements/RTM.md` | Markdown | Link requirements/backlog items to implementation ownership and standards. |
| Change Log Update | `docs/change-log.md` | Markdown | Record decisions, risks, mitigation plans, and review cadence. |

## Procedure
1. **Synthesize Inputs** – Review backlog priorities, RTM assignments, and design artefacts to understand implementation scope; note security, performance, data requirements.
2. **Draft Coding Standards** – Create `docs/development/coding-standards.md`; cover languages, frameworks, style guides, branching model, code review policy, static analysis, testing expectations, documentation, telemetry, accessibility, security requirements, DoD alignment.
3. **Build Iteration Plan** – Produce `docs/development/iteration-plan.md`; allocate features/stories/tasks across sprints with capacity, dependencies, risk buffers, parallelisation guidance, entry/exit criteria for each iteration.
4. **Capture Readiness Prerequisites** – Create/refresh `docs/development/readiness-checklist.md`; include environment setup, tooling access, data seeding, training, compliance sign-offs, dependency tracking.
5. **Traceability Updates** – Update RTM to reflect implementation ownership, coding standards references, iteration plan links, planned quality gates.
6. **Risk & Governance Logging** – Document risks, mitigations, escalations in change log; align with communication plan for status updates.
7. **Versioning & Approvals** – Populate document control, change log, and approval tables for each deliverable; identify Engineering Lead sign-off and required stakeholder reviews.

## Traceability & Governance
- Link coding standards and iteration plan entries to requirement IDs, NFRs, and backlog items in RTM.
- Provide QA, DevOps, and Release teams with sequencing and dependency insights.
- Ensure change log reflects readiness status and outstanding blockers with owners.

## Completion Checklist
- [ ] Coding standards, iteration plan, readiness checklist completed with no placeholders.
- [ ] RTM updated with implementation ownership and quality gate references.
- [ ] Change log captures decisions, risks, and follow-up actions.
- [ ] Approvals identified and document control tables updated.

## Parallelisation Notes
DevOps Lead (Phase 4.2) may start once coding standards draft is available; Engineering Team readiness (Phase 4.3) follows after publication of standards and plan.
```
