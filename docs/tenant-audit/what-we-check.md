# What We Check

A complete breakdown of every area the Tenant Audit examines.

---

## Identity & Access

The largest and most critical audit area — identity is the primary attack surface in Microsoft 365.

### MFA & Authentication

| Check | What We Look For |
|-------|-----------------|
| MFA registration | Percentage of users registered for MFA (members, privileged users, guests) |
| Authentication methods | Which methods are enabled — FIDO2, Windows Hello, Authenticator, SMS, voice, email |
| Phishing-resistant MFA | Whether strong methods (FIDO2, Windows Hello) are enforced vs. weaker methods (SMS, voice) |
| Security Defaults | Whether Security Defaults are enabled (baseline protection) |

### Conditional Access

| Check | What We Look For |
|-------|-----------------|
| Policy inventory | Total policies: enabled, report-only, and disabled |
| Coverage analysis | Percentage of users covered by active policies |
| MFA requirements | Whether CA policies enforce MFA for sign-in |
| Device compliance | Whether CA policies require compliant/managed devices |
| Risk-based policies | Whether sign-in risk and user risk conditions are used |
| Named locations | Trusted network boundaries defined for CA |
| Legacy auth blocking | Whether legacy authentication protocols are blocked |

### Privileged Access

| Check | What We Look For |
|-------|-----------------|
| Global Administrator count | Number of permanent GAs (ideally 2 break-glass + 0 standing) |
| Break-glass accounts | Whether dedicated emergency access accounts exist with strong auth |
| Privileged role assignments | Permanent vs. eligible (PIM) assignments across 15+ admin roles |
| PIM maturity | Ratio of eligible-to-permanent assignments |
| Role overlap | Users with 3+ admin roles (excessive privilege concentration) |

### Account Hygiene

| Check | What We Look For |
|-------|-----------------|
| Stale accounts | Enabled accounts with no sign-in for 90+ days |
| Never-signed-in accounts | Provisioned but unused accounts |
| Guest invite policy | Who can invite guest users (everyone, members only, admins only) |
| Guest user permissions | Default guest role restrictions |
| Cross-tenant access | External collaboration policies |

---

## Data Protection

How well your organisation's data is guarded against exfiltration and misuse.

### Email Security

| Check | What We Look For |
|-------|-----------------|
| Mailbox forwarding | Mailboxes with forwarding enabled (internal and external targets) |
| Inbox rules | Rules that forward, redirect, or delete mail — common attack persistence technique |
| Transport rules | Mail flow rules that may route mail externally |

### Information Protection

| Check | What We Look For |
|-------|-----------------|
| Sensitivity labels | Active labels, labels with encryption/protection, labels with auto-labelling |
| Retention labels | Defined vs. in-use retention policies |
| DLP indicators | Data Loss Prevention policy presence via label configuration |

### External Sharing

| Check | What We Look For |
|-------|-----------------|
| OneDrive sharing | External sharing scope (anyone, authenticated, internal only) |
| SharePoint sharing | External user access to sites and documents |
| External domains | Which external domains have access to your content |

---

## Device Compliance

Whether devices accessing your tenant meet your security standards.

| Check | What We Look For |
|-------|-----------------|
| Compliance policies | Number and assignment scope of Intune compliance policies |
| App protection policies | Mobile app management policies for BYOD scenarios |
| Device configuration | Intune configuration profiles and their assignments |
| Enrollment coverage | Percentage of devices managed by Intune |

---

## Application & API Security

Third-party and internal applications with access to your tenant data.

| Check | What We Look For |
|-------|-----------------|
| OAuth grants | Scope analysis with risk classification (high-risk scopes like `Directory.ReadWrite.All`, `Mail.ReadWrite`) |
| App credentials | Expired, expiring (30/60/90 days), and active credentials |
| Enterprise app permissions | Password-based vs. certificate authentication |
| Risky users | Users flagged by Identity Protection (high-risk indicators) |

---

## Organisational Governance

The broader structure and configuration of your tenant.

| Check | What We Look For |
|-------|-----------------|
| Domains | Verified, initial, and federated domains |
| Directory sync | On-premises vs. cloud-only identity model |
| Public folders | Mail-enabled public folders (migration complexity indicator) |
| Teams | Team count and configuration |
| SharePoint sites | Site count, storage usage, ownership, templates |
| M365 Groups | Group inventory and classification |
| Distribution lists | Legacy distribution group count |
| Security groups | Security group inventory |
| eDiscovery | Active eDiscovery cases |
| Security alerts | Summary of active security alerts |

---

## Licensing & Capacity

Whether you're getting value from what you're paying for.

| Check | What We Look For |
|-------|-----------------|
| Subscription inventory | All SKUs with total, consumed, and available licence counts |
| Utilisation efficiency | Percentage of purchased licences actually assigned |
| Unused licences | Licences purchased but not assigned to users |
| Mailbox storage | Per-user mailbox size and total storage consumption |
| OneDrive storage | Per-user OneDrive usage and total capacity |
| Secure Score | Microsoft's own security score percentage |

---

## What We Don't Do

!!! info "Read-only by design"
    The audit **never makes changes** to your tenant. We use read-only application permissions only — no write access, no data modification, no user impersonation.

- We don't access email content, file content, or chat messages
- We don't store tenant data beyond the audit results (retained for 30 days, then purged)
- We don't require interactive user consent — the app uses application-level permissions
