# Requirements Traceability Matrix (RTM)

## Document Control
| Version | Date | Author | Reviewer | Notes |
|---------|------|--------|----------|-------|
| 0.1     |      |        |          | Draft |
| 1.0     |      |        |          | Baseline |

## Purpose
Provide end-to-end traceability from business intent through design, implementation, testing, and deployment to ensure completeness and compliance.

## Usage Guidelines
- _Maintain bidirectional traceability between BRD/PRD, SRS, design specs, code commits, test artefacts, defects, and deployment evidence._
- _Update the RTM at each stage gate (requirements sign-off, design approval, test readiness, release)._ 
- _Highlight coverage gaps, orphan requirements, and verification status._

## Traceability Matrix
| Req ID | Requirement Type (Business / Functional / NFR / Compliance) | Requirement Description | Priority | Source Document & Section | Design / Architecture Reference | User Story / Work Item | Code Reference (Branch/Commit) | Test Case IDs | Defect IDs | Status (Not Started / In Progress / Verified / Blocked / Deferred) | Verification Evidence | Comments |
|--------|-------------------------------------------------------------|-------------------------|----------|----------------------------|-------------------------------|------------------------|-------------------------------|---------------|------------|-------------------------------------------------------------------|-----------------------|----------|
|        |                                                             |                         |          |                            |                               |                        |                               |               |            |                                                                   |                       |          |

## Coverage Summary
| Requirement Category | Total Requirements | Covered by Design | Covered by Test | Pending Coverage | Coverage % |
|----------------------|--------------------|-------------------|-----------------|------------------|------------|
| Business             |                    |                   |                 |                  |            |
| Functional           |                    |                   |                 |                  |            |
| Non-Functional       |                    |                   |                 |                  |            |
| Compliance           |                    |                   |                 |                  |            |

## Status Legend
- **Not Started**: Requirement documented but no downstream artefacts linked.
- **In Progress**: Design or implementation underway; partial traceability exists.
- **Verified**: Requirement validated through testing with evidence captured.
- **Blocked**: Progress impeded by dependency, issue, or risk.
- **Deferred**: Requirement postponed to a future release with rationale documented.

## Change Log
| Change ID | Date | Description | Impacted Requirements | Owner | Notes |
|-----------|------|-------------|------------------------|-------|-------|
|           |      |             |                        |       |       |

## Governance & Review Cadence
- _Frequency of updates (e.g., weekly, per sprint, per PI)._ 
- _Review forums (architecture board, QA governance, change advisory board)._ 
- _Approvers and sign-off expectations._

## Tool Integration & Automation
### Jira / Azure DevOps Integration
**Integration Strategy:**
- **Requirement IDs:** Sync RTM IDs with Jira Issue Keys or ADO Work Item IDs
- **Bidirectional Sync:** Changes in Jira/ADO automatically update RTM and vice versa
- **Traceability Links:** Use Jira "Links" or ADO "Related Work" to map requirements → stories → tasks → test cases
- **Custom Fields:** Add RTM ID as custom field in Jira/ADO for filtering and reporting

**Jira Integration Example:**
```
Requirement ID: FR-001
Jira Issue: PROJ-123
Link Type: "implements" (Jira issue link)
Query: project = PROJ AND "RTM ID" = "FR-001"
```

**Azure DevOps Integration Example:**
```
Requirement ID: NFR-005
Work Item ID: 456
Link Type: "Related" or "Parent-Child"
Query: SELECT [System.Id], [System.Title] FROM WorkItems WHERE [Custom.RTMID] = 'NFR-005'
```

### Automation Scripts
**RTM Validation Script:**
```python
# Validate RTM completeness and coverage
def validate_rtm(rtm_data):
    gaps = []
    for req in rtm_data:
        if not req['design_ref']:
            gaps.append(f"{req['id']}: Missing design reference")
        if not req['test_cases']:
            gaps.append(f"{req['id']}: Missing test coverage")
    return gaps
```

**Sync Script (Jira → RTM):**
```python
from jira import JIRA
# Fetch Jira issues with RTM ID custom field
jira = JIRA('https://company.atlassian.net', basic_auth=('user', 'token'))
issues = jira.search_issues('project=PROJ AND "RTM ID" is not EMPTY')
for issue in issues:
    rtm_id = issue.fields.customfield_10001
    # Update RTM with Jira issue key, status, assignee
    update_rtm(rtm_id, jira_key=issue.key, status=issue.fields.status.name)
```

### Dashboard & Reporting
**Power BI / Tableau Integration:**
- **Data Source:** Export RTM as CSV/JSON for BI tools
- **Metrics:** Requirements coverage %, test pass rate, defect density by requirement
- **Visualizations:** Traceability graph, coverage heatmap, status timeline

**Real-Time Dashboard:**
- **Tool:** Grafana, Datadog, custom web app
- **Metrics:** Requirements by status, coverage gaps, verification trends
- **Alerts:** Notify when coverage drops below threshold (e.g., <80%)

### Version Control Integration
**Git Commit Linking:**
- Include requirement IDs in commit messages: `git commit -m "feat(FR-001): Implement user authentication"`
- Automated parsing to populate "Code Reference" column in RTM
- Use Git hooks to enforce requirement ID in commit messages

**Pull Request Traceability:**
- PR template includes "Implements: FR-001, FR-002"
- CI checks validate that PRs reference valid RTM IDs
- Automated comment on PR with traceability links

## Validation Checklist
- [ ] Every requirement has unique ID, priority, and source reference.
- [ ] All requirements link to design artefacts and implementation work items.
- [ ] Each requirement has associated verification evidence (test cases, results).
- [ ] Non-functional and compliance requirements have explicit validation coverage.
- [ ] Coverage summary highlights gaps with remediation plans and owners.
- [ ] Change log captures requirement updates with impact analysis.
- [ ] RTM aligns with current release scope, with deferred items clearly marked.
- [ ] Approvals and review cadence are defined and communicated to stakeholders.
- [ ] Tool integration (Jira/ADO) is configured with bidirectional sync procedures.
- [ ] Automation scripts validate RTM completeness and coverage.
- [ ] Dashboard and reporting provide real-time visibility into traceability metrics.