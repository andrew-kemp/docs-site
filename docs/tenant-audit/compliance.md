# Compliance Frameworks

The audit maps your tenant configuration against four recognised compliance frameworks, giving you evidence-based control assessments rather than guesswork.

---

## NCSC Cyber Assessment Framework (CAF) v3.2

**Origin:** UK National Cyber Security Centre  
**Purpose:** Assess overall cyber resilience for organisations operating essential services  
**Scope:** Risk management, protective security, detection, and response

### Controls Assessed

| Control | Objective | What We Check |
|---------|-----------|---------------|
| **A1 — Governance** | Board-level ownership of cyber risk | Organisation structure, admin role distribution, security alert review |
| **A2 — Risk Management** | Systematic risk identification | Audit coverage, Secure Score, security posture assessment |
| **B1 — Identity & Access Control** | Only authorised users access systems | MFA adoption, CA policy coverage, privileged access management |
| **B2 — Device Management** | Devices are securely managed | Intune compliance policies, device configuration, app protection |
| **B3 — Data Security** | Data at rest and in transit is protected | Sensitivity labels, encryption, DLP indicators, external sharing |
| **B4 — System Security** | Secure configuration of systems | Security Defaults, legacy auth blocking, credential management |
| **B5 — Resilient Networks** | Network segmentation and resilience | Named locations, network-based CA conditions |
| **C1 — Security Monitoring** | Detect anomalies and attacks | Conditional Access monitoring, risk-based policies, sign-in risk |
| **C2 — Proactive Detection** | Threat hunting capability | Identity Protection, risky user detection |
| **D1 — Response Planning** | Planned incident response | eDiscovery readiness, security alert posture, break-glass accounts |

---

## Cyber Essentials v3.1

**Origin:** UK NCSC certification scheme  
**Purpose:** Baseline security controls to defend against common internet-based attacks  
**Scope:** Five technical control themes

### Controls Assessed

| Control | Requirement | What We Check |
|---------|-------------|---------------|
| **Firewalls** | Boundary protection | Named locations, network-based CA conditions |
| **Secure Configuration** | Harden systems and reduce attack surface | Security Defaults, legacy auth blocking, default security settings |
| **User Access Control** | Least privilege, controlled access | Global Admin count, PIM usage, role assignments, CA policy enforcement |
| **Malware Protection** | Defences against malicious software | App protection policies, device compliance requirements |
| **Patch Management** | Keep software up to date | Device compliance policy assessment |
| **Authentication** | Strong user authentication | MFA adoption, authentication methods, phishing-resistant methods |
| **Account Management** | Account lifecycle management | Stale accounts, never-signed-in accounts, guest policies |
| **Data Protection** | Basic data safeguards | External sharing settings, mailbox forwarding controls |

---

## Cyber Essentials Plus v3.1

**Origin:** UK NCSC (enhanced certification)  
**Purpose:** Extends Cyber Essentials with verified testing  
**Scope:** Same five themes as CE with deeper verification requirements

### Additional Controls

All Cyber Essentials controls apply, plus:

| Control | Enhancement | What We Check |
|---------|------------|---------------|
| **MFA Enforcement** | Verified multi-factor enforcement | MFA registration rate, CA policy enforcement, phishing-resistant methods |
| **Device Compliance** | Verified device security | Intune compliance policy assignment, configuration profiles |
| **Access Testing** | Verified access control | Break-glass accounts, conditional access coverage scope |
| **Vulnerability Management** | Verified patch status | Credential expiry monitoring, app security posture |

---

## NIST SP 800-53 Rev. 5

**Origin:** US National Institute of Standards and Technology  
**Purpose:** Security and privacy controls for federal information systems  
**Scope:** Access control, audit, identification, risk assessment, system protection

### Controls Assessed

| Control Family | ID | What We Check |
|---------------|-----|---------------|
| **Access Control** | AC-2 | Account management, lifecycle, stale accounts, privilege assignments |
| **Access Control** | AC-6 | Least privilege, Global Admin minimisation, PIM maturity |
| **Identification & Authentication** | IA-2 | Multi-factor authentication adoption and enforcement |
| **Identification & Authentication** | IA-5 | Credential management, expiry, rotation |
| **Risk Assessment** | RA-5 | Risk-based CA policies, Identity Protection, risky user detection |
| **System & Communications Protection** | SC-7 | Named locations, network boundaries, CA location conditions |

---

## Control Status Reference

Every control receives one of these statuses:

| Status | Icon | Meaning |
|--------|------|---------|
| **Met** | :material-check-circle:{ style="color: green" } | Fully satisfied based on audit evidence |
| **Partial** | :material-alert-circle:{ style="color: orange" } | Partially met — some gaps identified |
| **Not Detected** | :material-close-circle:{ style="color: red" } | No evidence found for this control |
| **Not Assessed** | :material-help-circle:{ style="color: grey" } | Couldn't evaluate — typically due to missing licence or data |
| **Out of Scope** | :material-minus-circle: | Control doesn't apply to M365 tenant audit |

---

## Using Compliance Results

!!! tip "Compliance scores support — they don't replace — formal assessment"
    The audit provides **evidence gathering** and **gap identification** to help you prepare for formal Cyber Essentials certification or framework assessments. The results are not a substitute for official certification audits but will significantly reduce the time and effort required.

For organisations preparing for **Cyber Essentials certification**, the audit report highlights exactly where gaps exist so you can prioritise remediation before the formal assessment.
