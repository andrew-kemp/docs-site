# Architecture

## Overview

The MFA Onboarding system uses Azure PaaS services and Microsoft 365 to create a fully automated MFA enrollment pipeline.

```
┌─────────────────────────────────────────────────────────────┐
│                   Administrator Workflow                      │
│                                                              │
│  Upload Portal (Azure Storage Static Website)                │
│       ↓                                                      │
│  Azure Function: upload-users                                │
│       ↓                                                      │
│  SharePoint List: "MFA Onboarding"                          │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                   Logic App Orchestration                     │
│                                                              │
│  Recurrence trigger → Get pending users from SharePoint      │
│       ↓                                                      │
│  For each user:                                              │
│    → Check if user exists in Azure AD                        │
│    → Check MFA registration status (Graph API)               │
│    → If MFA registered → Set Active + record date            │
│    → If not registered → Send invitation email               │
│    → If reminder due → Send reminder email                   │
│    → Update SharePoint with latest status                    │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                      User Interaction                        │
│                                                              │
│  User receives email → Clicks tracking link                  │
│       ↓                                                      │
│  Azure Function: enrol                                       │
│    → Records click timestamp                                 │
│    → Adds user to MFA security group                        │
│    → Updates SharePoint status                               │
│       ↓                                                      │
│  User completes MFA enrollment                               │
│  Logic App detects registration → Status = Active            │
└─────────────────────────────────────────────────────────────┘
```

## Azure Resources

| Resource | Type | Purpose |
|----------|------|---------|
| Resource Group | `Microsoft.Resources/resourceGroups` | Contains all resources |
| Function App | `Microsoft.Web/sites` | PowerShell 7.4 runtime, Managed Identity |
| App Service Plan | `Microsoft.Web/serverfarms` | Consumption (Y1) plan |
| Storage Account | `Microsoft.Storage/storageAccounts` | Static website for upload portal |
| Logic App (Invitations) | `Microsoft.Logic/workflows` | Email sending and MFA status checks |
| Logic App (Reports) | `Microsoft.Logic/workflows` | Daily/weekly admin reports |
| Application Insights | `Microsoft.Insights/components` | Monitoring and diagnostics |
| API Connections | `Microsoft.Web/connections` | SharePoint and Office 365 connectors |

## Microsoft 365 Resources

| Resource | Purpose |
|----------|---------|
| SharePoint Site | Hosts the MFA Onboarding tracking list |
| SharePoint List | Central database with 20+ columns tracking each user |
| Security Group | Used in Conditional Access policies for MFA enforcement |
| Shared Mailbox | Sends branded enrollment emails |
| App Registration (SharePoint) | Certificate-based auth for PnP PowerShell |
| App Registration (Portal) | SPA authentication for the upload portal |

## Authentication & Identity

### Managed Identity (Function App)
Used by the Azure Functions to access Microsoft Graph:

- `User.Read.All` — Read user information
- `GroupMember.ReadWrite.All` — Add/remove users from MFA group
- `Sites.ReadWrite.All` — Update SharePoint list items

### Managed Identity (Logic App - Invitations)
Used by the invitation Logic App:

- `Directory.Read.All` — Look up users
- `User.Read.All` — Read user details
- `UserAuthenticationMethod.ReadWrite.All` — Check and reset MFA methods
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
CSV File → Upload Portal → Function App (upload-users) → SharePoint List
```

### Invitation Flow
```
Logic App trigger → SharePoint (get pending users) → Graph API (check user)
    → Graph API (check MFA methods) → Send email via shared mailbox
    → Update SharePoint status
```

### Click Tracking Flow
```
User clicks link → Function App (enrol) → Graph API (add to group)
    → SharePoint (update status: ClickedLinkDate, InGroup, AddedToGroupDate)
```

### MFA Check Flow
```
Logic App trigger → SharePoint (get users) → Graph API (authentication/methods)
    → If MFA registered: Update status to Active + MFARegistrationDate
    → If not registered: Send reminder (if due) + update LastChecked
```

## Security

- **No passwords stored** — All authentication uses Managed Identity or certificates
- **Token-based tracking links** — GUID tokens instead of email addresses in URLs
- **CORS restricted** — Function App only accepts requests from the upload portal origin
- **Managed Identity** — No credentials in code or configuration
- **Admin consent** — All Graph API permissions granted via admin consent
