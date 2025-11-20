---
name: 'Phase 4.3 – Engineering Team'
description: 'Validate that each development task is fully ready for execution, address gaps, and confirm forward traceability before implementation begins.'

---
# Phase 4.3 – Engineering Team Prompt (Task Readiness & Execution Prep)

## Role Mission
Validate that each development task is fully ready for execution, address gaps, and confirm forward traceability before implementation begins.

## Inputs & References
| Source | Location | Purpose |
|--------|----------|---------|
| Engineering standards | `docs/development/coding-standards.md`, `docs/development/iteration-plan.md`, `docs/development/readiness-checklist.md`, `docs/development/cicd-spec.md`, `docs/development/environment-matrix.md`, `docs/development/sbom-strategy.md` | Align task readiness with standards, pipeline, environment expectations. |
| Backlog artefacts | `backlog/tasks/`, `backlog/stories/`, `backlog/features/`, `backlog/epics/` | Review task content, dependencies, DoR/DoD status. |
| Design references | `docs/design/LLD/`, `docs/design/api-specs/`, `docs/design/threat-model.md`, `docs/design/data-architecture.md` | Ensure tasks link to required technical specifications. |
| Traceability & governance | `docs/requirements/RTM.md`, `docs/change-log.md` | Confirm coverage, log blockers, report readiness status. |

## Expected Outputs
| Artefact | Destination | Format | Notes |
|----------|-------------|--------|-------|
| Updated Tasks | `backlog/tasks/` | Markdown | Fill gaps using ` templates/Task.md` structure; maintain document control/approvals. |
| Task Readiness Log | `docs/development/task-readiness.md` | Markdown | Capture readiness status, blockers, dependencies, ETA, owners. |
| RTM Update | `docs/requirements/RTM.md` | Markdown | Confirm forward traceability from requirements to tasks/test coverage. |
| Change Log Update | `docs/change-log.md` | Markdown | Log blockers, risks, decisions stemming from readiness review. |

## Procedure
1. **Task Audit** – Review each task in scope; verify objective, prerequisites, dependencies, acceptance tests, DoD checklist, traceability fields, and approvals.
2. **Enrich Task Content** – Update tasks to remove placeholders, add implementation notes, link to design artefacts, RTM IDs, pipeline steps, telemetry requirements, and evidence expectations as per ` templates/Task.md`.
3. **Log Readiness Status** – Create or update `docs/development/task-readiness.md`; summarise each task's status (Ready/Blocked/Needs Clarification), blockers, dependencies, owners, target resolution dates.
4. **Traceability Confirmation** – Update RTM to ensure each requirement maps through backlog items to tasks and planned test/validation artefacts; flag gaps with actions.
5. **Risk & Dependency Management** – Record technical/resource risks, cross-team dependencies, and mitigation plans in change log and/or readiness log.
6. **Communication** – Notify Engineering Lead, DevOps Lead, QA of blockers or sequencing issues per communication plan.
7. **Versioning & Approvals** – Ensure updated tasks and readiness log include document control, change log, approvals as required; collect sign-off or log pending approvals.

## Traceability & Governance
- Maintain clear linkage from requirement IDs → backlog items → tasks → CI/CD stages/tests.
- Document blockers with owners and due dates in change log for transparency.
- Provide QA with insight into implementation sequencing for test planning.

## Completion Checklist
- [ ] Tasks updated with complete details, traceability, and DoD/DoR coverage.
- [ ] Task readiness log reflects go/no-go status, blockers, and mitigation plans.
- [ ] RTM updated to confirm end-to-end traceability through tasks.
- [ ] Change log captures blockers, risks, actions, and communication updates.

## Parallelisation Notes
QA planning (Phase 5.1) can proceed once readiness log is available; continue syncing change log and RTM as readiness evolves.
```
