# MFA Onboarding System

Automated Multi-Factor Authentication enrollment for Microsoft 365 environments.

## What It Does

The MFA Onboarding system provides an end-to-end automated workflow for rolling out MFA across your organisation:

1. **Upload users** via a web portal (CSV or manual entry)
2. **Send personalised emails** with enrollment instructions and tracking links
3. **Track progress** in real-time via SharePoint and a reports dashboard
4. **Automatically manage** security group membership for Conditional Access
5. **Send reports** to administrators on a daily/weekly schedule

## User Journey

```
Administrator uploads CSV
        ↓
Logic App sends invitation email → User receives email
        ↓                                    ↓
SharePoint status: "Sent"          User clicks tracking link
                                             ↓
                                   Function App records click
                                   + adds to security group
                                             ↓
                                   SharePoint status: "AddedToGroup"
                                             ↓
                                   Logic App checks MFA registration
                                             ↓
                                   SharePoint status: "Active" ✓
```

## Components

| Component | Purpose |
|-----------|---------|
| **Upload Portal** | Web interface for CSV upload and manual user entry |
| **Azure Function App** | Handles tracking link clicks and user processing |
| **Logic App (Invitations)** | Sends emails, checks MFA status, manages reminders |
| **Logic App (Reports)** | Sends daily/weekly status reports to admins |
| **SharePoint List** | Central tracking database for all user enrollments |
| **Security Group** | Managed automatically for Conditional Access policies |
| **Shared Mailbox** | Sends enrollment emails from a branded address |

## Quick Links

- [Quick Start Guide](quick-start.md) — Get up and running fast
- [Architecture](architecture.md) — How it all fits together
- [Deployment](deployment.md) — Step-by-step deployment guide
- [Troubleshooting](troubleshooting.md) — Common issues and fixes

## Source Code

[:material-github: GitHub Repository](https://github.com/andrew-kemp/MFA-Onboard-Tool){ .md-button }
