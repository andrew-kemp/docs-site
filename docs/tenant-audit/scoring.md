# Scoring & Ratings

The audit produces three independent scores that together give a complete picture of your tenant's posture.

---

## Security Risk Score

**Scale:** 0–100 (higher is better)

Your overall security configuration score, calculated from four sub-categories.

### Sub-Categories

| Category | What It Measures |
|----------|-----------------|
| **Identity & Access** | MFA adoption, Global Admin count, PIM usage, stale accounts, guest policies |
| **Data Protection** | Mailbox forwarding, risky inbox rules, sensitivity label adoption |
| **Device Compliance** | Intune policy coverage and assignment scope |
| **App Security** | Expired credentials, high-risk OAuth grants |

### How It's Calculated

Each audit finding has an **impact value** (typically -5 to -30 points). Categories start at 100 and deductions are applied based on what's found:

```
Category Score = 100 + sum of finding impacts
Overall Score = weighted average of all categories
```

Scores are clamped to 0–100.

### Rating Scale

| Rating | Score | Meaning |
|--------|-------|---------|
| :material-shield-check:{ style="color: green" } **Secure** | 90–100 | Strong security posture with minimal gaps |
| :material-shield-half-full:{ style="color: #8bc34a" } **Low Risk** | 80–89 | Good configuration with minor improvements needed |
| :material-shield-alert:{ style="color: orange" } **Medium Risk** | 60–79 | Notable gaps that should be addressed |
| :material-shield-alert:{ style="color: #ff5722" } **High Risk** | 40–59 | Significant security gaps requiring attention |
| :material-shield-off:{ style="color: red" } **Critical** | 0–39 | Serious exposure — immediate action required |

### Examples of Impact

| Finding | Impact |
|---------|--------|
| Less than 90% MFA adoption | -15 to -30 depending on % |
| Permanent Global Admins above break-glass threshold | -20 to -30 |
| No break-glass accounts configured | -25 |
| Stale accounts enabled (90+ days inactive) | -10 to -20 |
| Mailboxes with external forwarding | -15 to -25 |
| High-risk OAuth app grants | -10 to -20 |
| Expired app credentials | -5 to -15 |

---

## Compliance Posture Score

**Scale:** 0–100 (higher is better)

How well your tenant configuration aligns with recognised compliance frameworks.

### Supported Frameworks

| Framework | Origin | Controls Mapped |
|-----------|--------|----------------|
| NCSC Cyber Assessment Framework (CAF) v3.2 | UK | 10 controls |
| Cyber Essentials v3.1 | UK | 8 controls |
| Cyber Essentials Plus v3.1 | UK | 8+ controls (extends CE) |
| NIST SP 800-53 Rev. 5 | US Federal | 6+ controls |

### Control Evaluation

Each control is evaluated against your audit data and assigned a status:

| Status | Meaning |
|--------|---------|
| **Met** | Control requirements are fully satisfied |
| **Partial** | Some aspects are in place but gaps remain |
| **Not Detected** | No evidence found that the control is implemented |
| **Not Assessed** | Insufficient data to evaluate (e.g. missing licence) |
| **Out of Scope** | Control doesn't apply to M365 tenant configuration |

### How It's Calculated

```
Framework Score = weighted sum of control scores
Overall Compliance = average across evaluated frameworks
```

Controls with higher weights (e.g. access control, MFA) have a greater impact on the framework score.

[See full framework details →](compliance.md)

---

## Migration Complexity Score

**Scale:** 0–100 (higher = more complex)

An estimate of how complex it would be to migrate this tenant — useful for planning M365-to-M365 migrations, consolidations, or modernisation projects.

### Factors Assessed

| Factor | Impact on Complexity |
|--------|---------------------|
| Mailbox count and total size | More mailboxes = higher complexity |
| OneDrive adoption and storage | High storage = longer migration windows |
| Teams count and configuration | Teams with channels, tabs, apps add complexity |
| SharePoint site count and templates | Custom templates and large sites increase effort |
| Exchange resource mailboxes | Room/equipment mailboxes need special handling |
| Public folders | Mail-enabled public folders are notoriously complex to migrate |
| Domain count and federation | Federated domains require careful cutover planning |
| Directory sync status | On-premises AD sync adds significant complexity |

### Rating Scale

| Rating | Score | Meaning |
|--------|-------|---------|
| **Simple** | 0–25 | Small, cloud-native tenant — straightforward migration |
| **Moderate** | 26–50 | Medium tenant with some complexity factors |
| **Complex** | 51–75 | Large tenant or significant legacy components |
| **Highly Complex** | 76–100 | Major migration project — federated domains, public folders, hybrid AD |

---

## Score Trends

If you run the audit more than once, your scores are tracked over time so you can see whether your security posture is improving, stable, or degrading. Audit history is retained for 30 days.
