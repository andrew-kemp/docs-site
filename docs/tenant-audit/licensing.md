# Licensing Requirements

The depth and completeness of your audit depends on the Microsoft 365 licences active in your tenant. This page explains what's needed for a full audit, what's possible with lower licence tiers, and how Andy Kemp Consulting can help if your licensing doesn't cover everything.

---

## Why Licensing Matters

The Tenant Audit reads data from **Microsoft Graph API** and **Exchange Online**. The data available through these APIs is directly tied to the features enabled by your Microsoft 365 licences.

For example:

- **Conditional Access policies** require at least Azure AD P1 — without it, there are no policies to audit
- **PIM (Privileged Identity Management)** requires Azure AD P2 — without it, all admin roles appear as permanent
- **Intune compliance policies** require an Intune licence — without it, there's no device compliance data
- **Identity Protection** (risky users) requires Azure AD P2

If a feature isn't licensed, the audit can't assess it — those controls will show as **"Not Assessed"** in your compliance results.

---

## Licence Tiers and Audit Coverage

### :material-check-all: Full Coverage — Microsoft 365 E5

The most complete audit. All 70+ checks and all four compliance frameworks can be fully evaluated.

| Component | Included in E5 | Audit Coverage |
|-----------|----------------|----------------|
| Azure AD P2 | :material-check: | Conditional Access, PIM, Identity Protection, risk-based policies |
| Intune | :material-check: | Device compliance, app protection, configuration profiles |
| Exchange Online Plan 2 | :material-check: | Mailbox forwarding, inbox rules, transport rules, mailbox sizes |
| Defender for Identity | :material-check: | Enhanced identity risk signals |
| Information Protection | :material-check: | Sensitivity labels, auto-labelling, encryption |
| eDiscovery | :material-check: | Case assessment for response planning |

---

### :material-check: Good Coverage — Microsoft 365 E3

A solid audit covering the majority of checks, with some gaps in advanced security features.

| Component | Included in E3 | Audit Coverage |
|-----------|----------------|----------------|
| Azure AD P1 | :material-check: | Conditional Access, named locations, MFA (no PIM, no risk policies) |
| Intune | :material-check: | Device compliance, app protection, configuration profiles |
| Exchange Online Plan 2 | :material-check: | Full mailbox and mail flow analysis |
| Defender for Identity | :material-close: | Not available — identity risk signals limited |
| PIM | :material-close: | Not available — all admin roles shown as permanent assignments |
| Identity Protection | :material-close: | Not available — risky user detection not assessed |

**What you'll miss:** PIM maturity assessment, risk-based Conditional Access evaluation, Identity Protection findings. These controls will show as "Not Assessed" in compliance frameworks.

---

### :material-alert: Partial Coverage — Microsoft 365 Business Premium

Covers the essentials but lacks several enterprise security features.

| Component | Included | Audit Coverage |
|-----------|----------|----------------|
| Azure AD P1 | :material-check: | Conditional Access basic assessment |
| Intune | :material-check: | Device compliance (limited feature set vs. E3/E5) |
| Exchange Online | :material-check: | Mailbox forwarding and inbox rules |
| PIM | :material-close: | Not available |
| Identity Protection | :material-close: | Not available |
| Advanced Compliance | :material-close: | Sensitivity labels may be limited |

---

### :material-close: Limited Coverage — Microsoft 365 Business Basic / Business Standard

Core identity and mailbox checks run, but most advanced security assessments cannot be performed.

| Component | Available | Audit Coverage |
|-----------|-----------|----------------|
| Azure AD Free | :material-check: | Basic user and admin enumeration, MFA registration status |
| Exchange Online | :material-check: | Mailbox forwarding, inbox rules |
| Conditional Access | :material-close: | No CA policies to assess |
| Intune | :material-close: | No device compliance data |
| PIM | :material-close: | Not available |
| Information Protection | :material-close: | Limited or not available |

**What you'll get:** Identity hygiene (stale accounts, admin count, MFA registration), mailbox security, basic licensing analysis, and migration complexity. Many compliance controls will show as "Not Assessed".

---

## Licence Requirements Summary

| Audit Feature | Minimum Licence |
|---------------|----------------|
| User and admin enumeration | Any M365 plan |
| MFA registration status | Any M365 plan |
| Mailbox forwarding and inbox rules | Exchange Online |
| Conditional Access assessment | Azure AD P1 (M365 E3, Business Premium) |
| Intune device compliance | Intune (M365 E3, E5, Business Premium) |
| PIM and eligible role analysis | Azure AD P2 (M365 E5 or P2 add-on) |
| Risk-based CA policies | Azure AD P2 (M365 E5 or P2 add-on) |
| Identity Protection (risky users) | Azure AD P2 (M365 E5 or P2 add-on) |
| Sensitivity labels and auto-labelling | M365 E5 or Information Protection add-on |
| Full compliance framework assessment | M365 E5 (all four frameworks fully evaluated) |

---

## Don't Have the Right Licensing?

### Option 1 — Add Licences

If you're already considering an upgrade, even a small number of Azure AD P2 or E5 licences can unlock the advanced assessment features. You don't need E5 for every user — the audit reads tenant-level policies, so even one E5 or P2 licence enables the features the audit checks.

### Option 2 — Engage Andy Kemp Consulting

If upgrading licensing isn't an option, or you want expert guidance alongside the audit results, **Andy Kemp Consulting** can help.

#### What We Offer

| Service | Description |
|---------|-------------|
| **Managed Audit** | We run the audit on your behalf, interpret the results, and deliver a prioritised remediation plan with expert commentary |
| **Gap Analysis** | For tenants without full licensing, we combine the automated audit data with manual assessment to cover what the tool can't reach |
| **Remediation Support** | Hands-on assistance implementing the recommendations — from Conditional Access policy design to PIM rollout |
| **Cyber Essentials Preparation** | End-to-end support preparing your M365 configuration for Cyber Essentials certification |
| **Compliance Mapping** | Map your audit findings to your specific regulatory requirements (NCSC CAF, ISO 27001, GDPR) |
| **Ongoing Posture Management** | Regular audit cadence with trend tracking and quarterly security reviews |

#### Why Engage a Consultant?

- **Expertise** — Interpret findings in the context of your business, not just your settings
- **Prioritisation** — Know what to fix first based on real-world risk, not just severity scores
- **Implementation** — Get it done right the first time, avoiding misconfigurations
- **Certification readiness** — Proven track record helping organisations achieve Cyber Essentials and CE+
- **No licence dependency** — We can assess and advise regardless of your current licence tier

#### Get in Touch

[:material-email: Contact Andy Kemp Consulting](mailto:andy@andykemp.com){ .md-button .md-button--primary }
[:material-web: andykemp.com](https://andykemp.com){ .md-button }

---

!!! info "The audit always runs — licensing only affects depth"
    Even with basic licensing, the audit will complete successfully and produce reports. You'll get valuable insights into identity hygiene, mailbox security, licensing efficiency, and migration complexity. Higher licence tiers simply unlock **more checks** and **deeper compliance assessments**.
