# Threat Model

## Document Control
| Version | Date | Author | Reviewer | Changes |
|---------|------|--------|----------|---------|
| 0.1     |      |        |          | Draft   |
| 1.0     |      |        |          | Baseline |
|         |      |        |          |         |

## Approvals
| Name | Role | Signature | Date |
|------|------|-----------|------|
|      |      |           |      |

## 1. Executive Summary
### 1.1 Purpose
_Define the purpose: to identify, analyse, and mitigate security threats to the system, data, and users through systematic threat modeling._

### 1.2 Threat Modeling Approach
_Describe the methodology used: STRIDE, PASTA, DREAD, Attack Trees, or other frameworks._

### 1.3 Key Findings Summary
| Finding Category | Count | Critical | High | Medium | Low |
|------------------|-------|----------|------|--------|-----|
| Threats Identified |       |          |      |        |     |
| Vulnerabilities |       |          |      |        |     |
| Mitigations Planned |       |          |      |        |     |
| Residual Risks |       |          |      |        |     |

## 2. System Overview
### 2.1 System Description
_High-level description of the system architecture, components, users, and data flows._

### 2.2 System Architecture Diagram
_Include or reference C4 Context, Container, and Component diagrams showing system boundaries._

### 2.3 Technology Stack
| Layer | Technologies | Version | Security Notes |
|-------|--------------|---------|----------------|
| Frontend |              |         |                |
| Backend |              |         |                |
| Data Storage |              |         |                |
| Infrastructure |              |         |                |
| Third-Party Services |              |         |                |

## 3. Assets Inventory
### 3.1 Asset Catalogue
| Asset ID | Asset Name | Asset Type | Description | Value (H/M/L) | Confidentiality | Integrity | Availability | Owner |
|----------|------------|------------|-------------|---------------|-----------------|-----------|--------------|-------|
| A-001    |            | Data, System, User, Service |             |               | H/M/L           | H/M/L     | H/M/L        |       |

### 3.2 Data Classification
| Data Type | Classification (Public/Internal/Confidential/Restricted) | Regulatory Requirements | Retention Period | Disposal Method |
|-----------|----------------------------------------------------------|------------------------|------------------|-----------------|
| Customer PII |                                                          | GDPR, CCPA             |                  |                 |
| Payment Data |                                                          | PCI-DSS                |                  |                 |
| Health Records |                                                          | HIPAA                  |                  |                 |
| Authentication Credentials |                                                          |                        |                  |                 |
| Business IP |                                                          |                        |                  |                 |

## 4. Trust Boundaries & Attack Surface
### 4.1 Trust Boundaries
_Identify boundaries where trust levels change (e.g., internet ↔ DMZ, DMZ ↔ internal network, application ↔ database)._

| Boundary | Description | Security Controls | Entry Points |
|----------|-------------|-------------------|--------------|
|          |             |                   |              |

### 4.2 Entry Points
| Entry Point ID | Description | Protocol | Authentication Required | Authorization | Rate Limiting | Monitoring |
|----------------|-------------|----------|------------------------|---------------|---------------|------------|
| EP-001         | Public API  |          |                        |               |               |            |

### 4.3 Exit Points
| Exit Point ID | Description | Destination | Data Classification | Encryption | Logging |
|---------------|-------------|-------------|---------------------|------------|---------|
| EX-001        |             |             |                     |            |         |

## 5. Data Flow Diagrams (DFD)
### 5.1 Level 0 DFD (Context)
_High-level data flows showing external entities, system boundary, and major data interactions._

### 5.2 Level 1 DFD (Decomposed)
_Detailed data flows showing processes, data stores, and trust boundaries._

### 5.3 Sensitive Data Flows
| Flow ID | Source | Destination | Data Type | Classification | Encryption (In-Transit) | Encryption (At-Rest) | Logging |
|---------|--------|-------------|-----------|----------------|-------------------------|----------------------|---------|
| DF-001  |        |             |           |                |                         |                      |         |

## 6. STRIDE Analysis
### 6.1 STRIDE Threat Catalogue
| Threat ID | Component | STRIDE Category | Threat Description | Likelihood (H/M/L) | Impact (H/M/L) | Risk Score | Mitigation | Status |
|-----------|-----------|-----------------|-------------------|-------------------|----------------|------------|------------|--------|
| T-001     |           | **S**poofing    |                   |                   |                |            |            |        |
| T-002     |           | **T**ampering   |                   |                   |                |            |            |        |
| T-003     |           | **R**epudiation |                   |                   |                |            |            |        |
| T-004     |           | **I**nformation Disclosure |                   |                   |                |            |            |        |
| T-005     |           | **D**enial of Service |                   |                   |                |            |            |        |
| T-006     |           | **E**levation of Privilege |                   |                   |                |            |            |        |

**STRIDE Categories Explained:**
- **Spoofing:** Impersonating users, systems, or services
- **Tampering:** Unauthorized modification of data or code
- **Repudiation:** Denying actions without ability to prove otherwise
- **Information Disclosure:** Unauthorized access to confidential data
- **Denial of Service:** Disrupting availability or performance
- **Elevation of Privilege:** Gaining unauthorized access rights

## 7. Attack Trees & Scenarios
### 7.1 Attack Scenarios
| Scenario ID | Attack Goal | Attack Path | Prerequisites | Countermeasures | Residual Risk |
|-------------|-------------|-------------|---------------|-----------------|---------------|
| AS-001      |             |             |               |                 |               |

### 7.2 Attack Tree Diagrams
_Visual representation of attack paths, showing AND/OR relationships between attack steps._

## 8. Security Controls Mapping
### 8.1 Preventive Controls
| Control ID | Control Description | Threat IDs Mitigated | Implementation Status | Owner | Validation Method |
|------------|---------------------|----------------------|----------------------|-------|-------------------|
| SC-P-001   | Multi-Factor Authentication |                      |                      |       |                   |
| SC-P-002   | Input Validation & Sanitization |                      |                      |       |                   |
| SC-P-003   | Encryption (TLS 1.3) |                      |                      |       |                   |
| SC-P-004   | Role-Based Access Control (RBAC) |                      |                      |       |                   |

### 8.2 Detective Controls
| Control ID | Control Description | Threat IDs Detected | Implementation Status | Owner | Alert Mechanism |
|------------|---------------------|---------------------|----------------------|-------|-----------------|
| SC-D-001   | Intrusion Detection System (IDS) |                     |                      |       |                 |
| SC-D-002   | Security Information & Event Management (SIEM) |                     |                      |       |                 |
| SC-D-003   | Audit Logging |                     |                      |       |                 |

### 8.3 Corrective Controls
| Control ID | Control Description | Threat IDs Addressed | Implementation Status | Owner | Recovery SLA |
|------------|---------------------|----------------------|----------------------|-------|--------------|
| SC-C-001   | Incident Response Plan |                      |                      |       |              |
| SC-C-002   | Automated Backup & Recovery |                      |                      |       |              |
| SC-C-003   | Patch Management Process |                      |                      |       |              |

## 9. OWASP Top 10 Assessment
### 9.1 OWASP Top 10 Mapping (2021)
| OWASP Risk | Description | Applicable? | Threat IDs | Mitigation Strategy | Status |
|------------|-------------|-------------|------------|---------------------|--------|
| A01: Broken Access Control |             | Yes/No      |            |                     |        |
| A02: Cryptographic Failures |             | Yes/No      |            |                     |        |
| A03: Injection |             | Yes/No      |            |                     |        |
| A04: Insecure Design |             | Yes/No      |            |                     |        |
| A05: Security Misconfiguration |             | Yes/No      |            |                     |        |
| A06: Vulnerable Components |             | Yes/No      |            |                     |        |
| A07: Identification & Authentication Failures |             | Yes/No      |            |                     |        |
| A08: Software & Data Integrity Failures |             | Yes/No      |            |                     |        |
| A09: Security Logging & Monitoring Failures |             | Yes/No      |            |                     |        |
| A10: Server-Side Request Forgery (SSRF) |             | Yes/No      |            |                     |        |

## 10. Privacy Threat Analysis
### 10.1 Privacy Risks (GDPR/CCPA/HIPAA)
| Privacy Threat ID | Data Type | Regulation | Threat Description | Impact | Mitigation | Compliance Control | Status |
|-------------------|-----------|------------|-------------------|--------|------------|-------------------|--------|
| PT-001            | PII       | GDPR       |                   |        |            |                   |        |

### 10.2 Data Subject Rights
| Right | Applicable? | Implementation | Validation | Owner |
|-------|-------------|----------------|------------|-------|
| Right to Access |             |                |            |       |
| Right to Rectification |             |                |            |       |
| Right to Erasure (Deletion) |             |                |            |       |
| Right to Data Portability |             |                |            |       |
| Right to Object |             |                |            |       |

## 11. Third-Party & Supply Chain Risks
### 11.1 Third-Party Risk Assessment
| Vendor / Service | Data Access | Classification | Risk Level | Security Assessment | Contractual Controls | Owner |
|------------------|-------------|----------------|------------|---------------------|---------------------|-------|
|                  |             |                |            | SOC 2, ISO 27001, Pen Test |                     |       |

### 11.2 Dependency Vulnerabilities
| Dependency | Version | Known Vulnerabilities (CVE) | Severity | Remediation Plan | Owner | Status |
|------------|---------|----------------------------|----------|------------------|-------|--------|
|            |         |                            |          |                  |       |        |

## 12. Residual Risk Assessment
### 12.1 Residual Risks
| Risk ID | Threat ID | Residual Risk Description | Likelihood (Post-Mitigation) | Impact (Post-Mitigation) | Risk Score | Risk Acceptance | Accepted By | Date |
|---------|-----------|---------------------------|------------------------------|--------------------------|------------|-----------------|-------------|------|
| RR-001  |           |                           |                              |                          |            | Yes/No          |             |      |

### 12.2 Risk Acceptance Criteria
_Define acceptable risk thresholds and conditions under which residual risks will be accepted._

## 13. Security Testing & Validation
### 13.1 Security Test Plan
| Test Type | Scope | Tools | Frequency | Pass Criteria | Owner |
|-----------|-------|-------|-----------|---------------|-------|
| Static Application Security Testing (SAST) |       |       |           |               |       |
| Dynamic Application Security Testing (DAST) |       |       |           |               |       |
| Software Composition Analysis (SCA) |       |       |           |               |       |
| Penetration Testing |       |       |           |               |       |
| Security Code Review |       |       |           |               |       |

### 13.2 Threat Model Validation
_How and when the threat model will be reviewed, updated, and validated (e.g., design reviews, pen test findings, incident learnings)._

## 14. Incident Response Integration
### 14.1 Threat-Specific Response Plans
| Threat ID | Detection Method | Response Procedure | Recovery SLA | Owner |
|-----------|------------------|-------------------|--------------|-------|
|           |                  |                   |              |       |

### 14.2 Escalation & Communication
_Define escalation paths for security incidents related to identified threats._

## 15. Appendices
### Appendix A: Glossary
_Define threat modeling terms, security acronyms, and frameworks._

### Appendix B: Reference Documents
- Link to HLD, LLD, security policies, compliance frameworks, pen test reports

### Appendix C: Threat Modeling Session Notes
_Document workshops, participants, assumptions, and decisions made during threat modeling sessions._

### Appendix D: Compliance Mappings
_Map threats and controls to ISO 27001, NIST CSF, CIS Controls, SOC 2, etc._

## Validation & Quality Checklist
- [ ] System architecture and data flows are documented with diagrams (DFD, C4).
- [ ] All critical assets are inventoried and classified by value and data sensitivity.
- [ ] Trust boundaries, entry/exit points, and attack surface are identified.
- [ ] STRIDE analysis is complete for all components with threat catalogue.
- [ ] Attack scenarios and attack trees are documented.
- [ ] Security controls (preventive, detective, corrective) are mapped to threats.
- [ ] OWASP Top 10 risks are assessed with mitigation strategies.
- [ ] Privacy threats (GDPR/CCPA/HIPAA) are identified with compliance controls.
- [ ] Third-party and supply chain risks are assessed.
- [ ] Residual risks are documented with acceptance criteria and sign-off.
- [ ] Security testing plan is defined with tools, frequency, and pass criteria.
- [ ] Incident response procedures are integrated for identified threats.
- [ ] Threat model has been reviewed by security team and approved by stakeholders.
