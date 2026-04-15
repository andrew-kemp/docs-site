# Getting Started

Run your first tenant audit in minutes. This guide walks you through the process from sign-up to downloading your reports.

---

## Prerequisites

Before you begin, you'll need:

- **A Microsoft 365 tenant** you want to audit
- **Global Administrator** or **Application Administrator** privileges (to grant the app permissions on first use)
- **A modern web browser** (Edge, Chrome, Firefox, Safari)

!!! note "No software to install"
    The Tenant Audit runs entirely in the browser. There's nothing to download, install, or configure on your machine.

---

## Step 1 — Sign In

Navigate to the audit portal and sign in with your account.

New users are created automatically on first sign-in — there's no separate registration step.

---

## Step 2 — Create a New Audit

From the dashboard, select **New Audit** and provide:

| Field | Description |
|-------|-------------|
| **Project name** | A friendly name for this audit (e.g. "Contoso Q1 2025 Audit") |
| **Tenant details** | The Microsoft 365 tenant to audit |

---

## Step 3 — Grant Permissions

On first use for a tenant, you'll need to grant the audit application the required Microsoft Graph permissions. This is a one-time admin consent step.

The application requests the following **read-only application permissions**:

| Permission | Purpose |
|------------|---------|
| `User.Read.All` | Enumerate users, check MFA registration, identify stale accounts |
| `Directory.Read.All` | Read directory objects, roles, groups, domains |
| `Policy.Read.All` | Read Conditional Access policies, authentication methods |
| `RoleManagement.Read.All` | Read admin role assignments and PIM eligible assignments |
| `DeviceManagementConfiguration.Read.All` | Read Intune compliance and configuration policies |
| `DeviceManagementApps.Read.All` | Read app protection policies |
| `Application.Read.All` | Read enterprise app registrations and credentials |
| `SecurityEvents.Read.All` | Read security alerts |
| `IdentityRiskyUser.Read.All` | Read Identity Protection risky user data |
| `Organization.Read.All` | Read tenant organisation details |
| `Reports.Read.All` | Read usage reports |
| `Sites.Read.All` | Read SharePoint site information |
| `Group.Read.All` | Read M365 Groups and Teams |
| `Mail.Read` | Read mail flow rules and mailbox configuration |
| `InformationProtectionPolicy.Read.All` | Read sensitivity and retention labels |

!!! warning "Read-only permissions only"
    The audit uses **application-level read-only permissions**. It cannot modify users, policies, settings, or data in your tenant. No interactive user consent is required — the admin consent covers all users.

---

## Step 4 — Run the Audit

Once permissions are granted, start the audit. You'll see real-time progress as the audit works through each category:

1. **Identity & Access** — Users, admins, MFA, Conditional Access
2. **Data Protection** — Mailboxes, forwarding rules, sensitivity labels
3. **Device Compliance** — Intune policies and device configuration
4. **App Security** — Enterprise apps, OAuth grants, credentials
5. **Governance** — Domains, groups, SharePoint, Teams
6. **Licensing** — Subscriptions, utilisation, storage
7. **Compliance** — Framework assessment (NCSC CAF, CE, CE+, NIST)
8. **Intelligence** — 8 analysers generate findings and recommendations
9. **Scoring** — Final scores calculated
10. **Reports** — PDF and PowerPoint generated

**Typical duration:** 2–5 minutes depending on tenant size.

---

## Step 5 — Review Results

When the audit completes, you'll see:

- **Score dashboard** — Security Risk, Compliance Posture, and Migration Complexity at a glance
- **Findings list** — All findings sorted by severity with recommendations
- **Compliance summary** — Per-framework control status
- **Action plan** — Prioritised remediation steps

---

## Step 6 — Download Reports

Download your reports from the results page:

| Report | Format | Best For |
|--------|--------|----------|
| **Technical Report** | PDF | IT teams, detailed analysis |
| **CXO Executive Report** | PDF | Board, C-suite, management |
| **CXO Presentation** | PPTX | Meetings, client presentations |

All three reports are available immediately after the audit completes.

---

## What's Next?

- **Re-run monthly** — Track your posture over time with score trends
- **Address quick wins first** — Start with critical and high severity findings that are easy to fix
- **Plan strategic items** — Budget and schedule larger remediation projects
- **Prepare for certification** — Use compliance framework results to guide Cyber Essentials preparation

---

## Need Help?

If you need assistance interpreting results, implementing recommendations, or preparing for compliance certification, [Andy Kemp Consulting](licensing.md#option-2-engage-andy-kemp-consulting) can help.
