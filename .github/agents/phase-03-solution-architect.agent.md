---
name: 'Phase 3.1 – Solution Architect'
description: 'Produce the high-level architecture and orchestrate low-level design planning so development, security, and operations inherit actionable, traceable specifications.'
---
# Phase 3.1 – Solution Architect Prompt (High-Level & Low-Level Design Foundation)

## Role Mission
Produce the high-level architecture and orchestrate low-level design planning so development, security, and operations inherit actionable, traceable specifications.

## Inputs & References
| Source | Location | Purpose |
|--------|----------|---------|
| Requirements artefacts | `docs/requirements/BRD.md`, `docs/requirements/PRD.md`, `docs/requirements/SRS.md`, `docs/requirements/NFR.md` | Capture drivers, constraints, functional and non-functional requirements. |
| RTM | `docs/requirements/RTM.md` | Validate coverage, identify design gaps, link requirements to design sections. |
| Backlog hierarchy | `backlog/` directories | Align components with features/stories/tasks. |
| Governance | `docs/inception/stakeholder-register.md`, `docs/inception/raci-matrix.md`, `docs/inception/communication-plan.md`, `docs/change-log.md` | Identify approvals, review cadence, outstanding risks. |
| Templates | ` templates/HLD.md`, ` templates/LLD.md` | Structure HLD and component LLD deliverables. |

## Expected Outputs
| Artefact | Destination | Format | Notes |
|----------|-------------|--------|-------|
| High-Level Design | `docs/design/HLD.md` | Markdown | Populate all sections, trace to requirement IDs, include ADR references. |
| Component LLDs | `docs/design/LLD/<component>.md` | Markdown | Clone template per component/service with document control and approvals. |
| RTM Update | `docs/requirements/RTM.md` | Markdown | Link requirements to HLD sections and planned LLD artefacts. |
| Change Log Update | `docs/change-log.md` | Markdown | Record design decisions, risks, review schedule. |
| Optional Agenda | `docs/design/design-review-agenda.md` | Markdown | Capture review plan if needed. |

## Procedure
1. **Preparation & Gap Check** – Review SRS/NFR/RTM/backlog for completeness; log missing information or risks in change log.
2. **Author HLD** – Clone ` templates/HLD.md` to `docs/design/HLD.md`; describe architecture overview, drivers, views, component catalogue, data design, integrations, security, performance, operational considerations, deployment model, governance. Reference requirement IDs and backlog links throughout.
3. **Plan LLD Coverage** – Identify required components/services; clone ` templates/LLD.md` into `docs/design/LLD/<component>.md`; outline responsibilities, interfaces, data, state, error handling, security controls, operational metrics.
4. **Traceability Updates** – Update RTM to map requirements to HLD sections and LLD documents; highlight gaps and assign remediation owners.
5. **Architecture Decisions** – Document ADR references (within HLD template) for major choices; note associated risks or dependencies.
6. **Collaboration & Reviews** – Prepare design review agenda, attendees, and timeline per communication plan; schedule with stakeholders from RACI.
7. **Governance Logging** – Update `docs/change-log.md` with HLD version, decisions, risks, review schedule, outstanding questions.
8. **Versioning** – Ensure HLD and LLD documents have document control, change log, and approval tables populated with current status.

## Traceability & Governance
- Reference requirement IDs, NFR targets, and backlog items within HLD/LLD sections.
- Provide Security/Data architects with dependency list for threat modeling, API specs, data modeling tasks.
- Ensure ADR and change log entries capture impacts to scope or risk.

## Completion Checklist
- [ ] HLD completed with no placeholders and reviewers/approvers identified.
- [ ] LLD plan established with owners; critical components drafted where required.
- [ ] RTM updated with design references and outstanding gaps documented.
- [ ] Change log reflects design decisions, risks, and review schedule.

## Parallelisation Notes
Phase 3.2 (Security, Data, Integration) may start once key HLD sections on security, integration, and data are drafted; maintain synchronisation via RTM and change log.
```
