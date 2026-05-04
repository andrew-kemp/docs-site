# Architecture

## Overview

The MFA Onboarding system uses Azure PaaS services and Microsoft 365 to create a fully automated MFA enrollment pipeline with engagement tracking, automated escalation, and operational reporting.

```
┌──────────────────────────────────────────────────────────────────────┐
│                        Upload Portal (SPA)                           │
│   Azure Storage Static Website · MSAL.js · 3 tabs                   │
│   CSV Upload (drag-drop) │ Manual Entry │ Reports + CSV Export       │
└─────────────────────────────────────┬────────────────────────────────┘
                                      │ POST /api/upload-users
                                      ▼
┌──────────────────────────────────────────────────────────────────────┐
│                     Azure Function App (PowerShell 7.4)              │
│   Managed Identity · Application Insights                            │
│                                                                      │
│   /api/upload-users   — Validate CSV, create/update SharePoint items │
│   /api/enrol          — Track clicks, add to group, branded HTML     │
│   /api/track-open     — 1×1 pixel, stamp EmailOpenedDate             │
│   /api/resend         — Self-service resend form (GET) + reset (POST)│
└──────────────┬───────────────────────────────────────────────────────┘
               │ SharePoint REST + Graph API
               ▼
┌─────────────────────────────┐   ┌────────────────────────────────────┐
│   SharePoint Online List    │   │         Logic App (Consumption)    │
│   24 tracked columns        │   │   Recurrence trigger (configurable)│
│   Per-user status tracking  │◄──│   Process Pending/Sent/Active users│
│   Batch IDs, tokens, dates  │   │   Send emails via shared mailbox  │
│   Manager UPN, escalation   │   │   Check MFA via Graph API         │
└─────────────────────────────┘   │   Automated reminders (7-day)     │
                                  │   Manager escalation (2+ reminders)│
┌─────────────────────────────┐   │   Retry policies (exponential)    │
│   Entra ID / Microsoft 365  │◄──│   Tracking pixels + resend links  │
│   Security Group (CA policy)│   └────────────────────────────────────┘
│   Shared Mailbox (sender)   │
│   User MFA auth methods     │
└─────────────────────────────┘
```

## Azure Resources

| Resource | Type | Purpose |
|----------|------|---------|
| Resource Group | `Microsoft.Resources/resourceGroups` | Contains all resources |
| Function App | `Microsoft.Web/sites` | PowerShell 7.4 runtime, 4 HTTP endpoints, Managed Identity |
| App Service Plan | `Microsoft.Web/serverfarms` | Consumption (Y1) plan |
| Storage Account | `Microsoft.Storage/storageAccounts` | Static website for upload portal |
| Logic App (Invitations) | `Microsoft.Logic/workflows` | Email sending, MFA checks, reminders, and manager escalation |
| Logic App (Reports) | `Microsoft.Logic/workflows` | Daily/weekly admin reports |
| Application Insights | `Microsoft.Insights/components` | Telemetry, request logging, exception tracking, live metrics |
| API Connections | `Microsoft.Web/connections` | SharePoint and Office 365 connectors |

!!! info "Infrastructure as Code"
    All Azure resources can also be deployed via `infra/main.bicep` with secure defaults (TLS 1.2, HTTPS-only, FTPS disabled).

## Microsoft 365 Resources

| Resource | Purpose |
|----------|---------|
| SharePoint Site | Hosts the MFA Onboarding tracking list |
| SharePoint List | Central database with 24 columns tracking each user |
| Security Group | Used in Conditional Access policies for MFA enforcement |
| Shared Mailbox | Sends branded enrollment emails |
| App Registration (SharePoint) | Certificate-based auth for PnP PowerShell |
| App Registration (Portal) | SPA authentication for the upload portal |

## Function App Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/upload-users` | POST | Validates CSV data, creates/updates SharePoint list items, generates tracking tokens, triggers Logic App |
| `/api/enrol` | GET | Handles tracking link clicks — records click, adds to security group, returns branded HTML response |
| `/api/track-open` | GET | Returns 1×1 invisible GIF pixel, stamps `EmailOpenedDate` in SharePoint on first open |
| `/api/resend` | GET/POST | GET returns branded HTML form; POST resets user to Pending for re-processing |

## Authentication & Identity

### Managed Identity (Function App)
Used by the Azure Functions to access Microsoft Graph and SharePoint:

- `User.Read.All` — Read user information
- `GroupMember.ReadWrite.All` — Add/remove users from MFA group
- `Group.ReadWrite.All` — Read group information
- `Sites.ReadWrite.All` — Update SharePoint list items

### Managed Identity (Logic App - Invitations)
Used by the invitation Logic App:

- `Directory.Read.All` — Look up users and managers
- `User.Read.All` — Read user details
- `UserAuthenticationMethod.ReadWrite.All` — Check MFA registration status
- `GroupMember.ReadWrite.All` — Manage group membership
- `Group.Read.All` — Read group information

### Managed Identity (Logic App - Reports)
Used by the reports Logic App:

- `Sites.Read.All` — Read SharePoint list for report generation

### Certificate Authentication (SharePoint)
PnP PowerShell uses a self-signed certificate for automated SharePoint operations during deployment.

## Data Flow

### Upload Flow
```
CSV File → Upload Portal (validate) → Function App (upload-users) → SharePoint List
                                             ↓ (optional)
                                      Trigger Logic App immediately
```

### Invitation Flow
```
Logic App trigger → SharePoint (get pending users) → Graph API (check user)
    → Graph API (check MFA methods) → Send email via shared mailbox
    → Embed tracking pixel + resend link in email body
    → Update SharePoint status
```

### Click Tracking Flow
```
User clicks link → Function App (enrol)
    → Token lookup in SharePoint
    → Duplicate-click check (returns "Already Registered" if repeated)
    → Graph API (add to group)
    → SharePoint (update status: ClickedLinkDate, InGroup, AddedToGroupDate)
    → Branded HTML confirmation → Auto-redirect to aka.ms/mfasetup
```

### Email Open Tracking Flow
```
Email client loads images → GET /api/track-open?token={GUID}
    → SharePoint (stamp EmailOpenedDate, first-open only)
    → Return 1×1 transparent GIF
```

### MFA Check Flow
```
Logic App trigger → SharePoint (get users) → Graph API (authentication/methods)
    → If MFA registered: Update status to Active + MFARegistrationDate
    → If not registered + reminder due: Send reminder + update LastChecked
    → If 2+ reminders sent: Look up manager via Graph → Send escalation email
```

### Self-Service Resend Flow
```
User clicks "Lost your setup link?" in email footer
    → GET /api/resend → Branded HTML form
    → User enters email → POST /api/resend
    → Reset InviteStatus to Pending + clear ReminderCount
    → Anti-enumeration: identical success message regardless of user existence
    → Logic App picks up on next run
```

## Security

- **No passwords stored** — All authentication uses Managed Identity or certificates
- **Token-based tracking links** — GUID tokens instead of email addresses in URLs
- **Anti-enumeration** — Resend endpoint returns identical response for known and unknown users
- **Duplicate-click protection** — Repeated clicks show "Already Registered" instead of re-processing
- **CORS restricted** — Function App only accepts requests from the upload portal origin
- **Managed Identity** — No credentials in code or configuration
- **Admin consent** — All Graph API permissions granted via admin consent
- **Secure defaults** — TLS 1.2, HTTPS-only, FTPS disabled on all Azure resources
