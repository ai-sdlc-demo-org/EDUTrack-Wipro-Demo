---
name: 'Phase 4.2 – DevOps Lead'
description: 'Design the continuous delivery pipeline, environment strategy, and SBOM governance to meet quality, compliance, and operational expectations.

---
# Phase 4.2 – DevOps Lead Prompt (CI/CD Architecture & SBOM Strategy)

## Role Mission
Design the continuous delivery pipeline, environment strategy, and SBOM governance to meet quality, compliance, and operational expectations.

## Inputs & References
| Source | Location | Purpose |
|--------|----------|---------|
| Engineering artefacts | `docs/development/coding-standards.md`, `docs/development/iteration-plan.md`, `docs/development/readiness-checklist.md` | Align pipeline policies with engineering standards and schedule. |
| Design & Requirements | `docs/design/HLD.md`, `docs/design/threat-model.md`, `docs/design/api-specs/`, `docs/design/data-architecture.md`, `docs/requirements/NFR.md`, `docs/requirements/RTM.md` | Derive quality gates, security controls, environment needs. |
| Governance | `docs/inception/raci-matrix.md`, `docs/change-log.md` | Confirm approvals, audits, outstanding risks. |

## Expected Outputs
| Artefact | Destination | Format | Notes |
|----------|-------------|--------|-------|
| CI/CD Specification | `docs/development/cicd-spec.md` | Markdown | Detail stages, tooling, triggers, quality gates, promotion criteria, monitoring hooks. |
| Environment Matrix | `docs/development/environment-matrix.md` | Markdown | Document environment purposes, configuration, access controls, data handling. |
| SBOM Strategy | `docs/development/sbom-strategy.md` | Markdown | Outline SBOM generation, validation, storage, reporting, compliance cadence. |
| RTM Update | `docs/requirements/RTM.md` | Markdown | Map requirements/NFRs to pipeline stages, evidence, tooling. |
| Change Log Update | `docs/change-log.md` | Markdown | Record pipeline decisions, dependencies, risks, mitigation actions. |

## Procedure
1. **Gather Pipeline Requirements** – Extract quality gates, security controls, compliance obligations from NFR catalogue, threat model, coding standards, design artefacts.
2. **Author CI/CD Specification** – Create `docs/development/cicd-spec.md`; describe pipeline stages, branch policies, build/test tooling, static analysis, security/privacy scans, performance testing, promotion criteria, approvals, monitoring/logging integration, rollback automation, evidence capture.
3. **Define Environment Matrix** – Document each environment in `docs/development/environment-matrix.md`; include purpose, topology, configuration, access, data management, refresh cadence, observability, compliance guardrails.
4. **Establish SBOM Strategy** – Draft `docs/development/sbom-strategy.md`; specify tooling, trigger points, artefact storage, integrity verification, licence compliance, attestation workflow, integration with CI/CD.
5. **Traceability & RTM** – Update RTM with pipeline stages and artefacts covering specific requirements/NFRs, linking to backlog tasks and test plan expectations.
6. **Collaboration & Alignment** – Coordinate with QA for test integration, Release Manager for deployment evidence, Operations for monitoring and incident hooks; record actions and owners.
7. **Change Log & Approvals** – Update change log with decisions, risks, dependencies; populate document control and approval tables for each deliverable.

## Traceability & Governance
- Ensure pipeline stages reference requirement IDs, NFRs, and associated evidence in RTM.
- Capture compliance reporting obligations and audit artefact retention.
- Highlight infrastructure/tooling requests and risks for stakeholder review.

## Completion Checklist
- [ ] CI/CD spec, environment matrix, and SBOM strategy completed with no placeholders.
- [ ] RTM updated with pipeline coverage and evidence references.
- [ ] Change log reflects decisions, risks, dependencies, owners.
- [ ] Approvals and document control sections updated for each artefact.

## Parallelisation Notes
Engineering Team readiness (Phase 4.3) proceeds concurrently; QA planning (Phase 5.1) can begin once CI/CD stages are defined.
```
