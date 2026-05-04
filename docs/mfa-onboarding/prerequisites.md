# Prerequisites

## Software Requirements

| Software | Version | Purpose |
|----------|---------|---------|
| Windows | 10/11 or Server 2019+ | Operating system |
| PowerShell | 7.4+ | Script execution |
| Azure CLI | Latest | Azure resource management |

!!! note
    The installation script (`01-Install-Prerequisites.ps1`) will install most PowerShell modules automatically.

## PowerShell Modules

These are installed automatically during Step 1:

| Module | Version | Purpose |
|--------|---------|---------|
| Az | 11.0.0+ | Azure resource management |
| Az.Functions | 4.0.0+ | Function App management |
| PnP.PowerShell | 2.3.0+ | SharePoint Online management |
| Microsoft.Graph | 2.0.0+ | Microsoft Graph API |
| ExchangeOnlineManagement | 3.2.0+ | Exchange Online management |

## Azure Permissions

You need the following roles in your Azure subscription:

- **Owner** or **Contributor** — Create resources (Function App, Storage, Logic App)
- **User Access Administrator** — Assign RBAC roles to Managed Identities

## Microsoft 365 Permissions

You need the following admin roles:

| Role | Purpose |
|------|---------|
| Global Administrator | App registrations and admin consent |
| SharePoint Administrator | Site and list creation |
| Exchange Administrator | Shared mailbox creation |

!!! tip
    A single Global Administrator account can perform all the above. The deployment scripts will prompt for sign-in when needed.

## Licence Requirements

| Licence | Required | Purpose |
|---------|----------|---------|
| Microsoft 365 E3/E5 or Business Premium | Yes | SharePoint, Exchange, Entra ID |
| Azure Subscription | Yes | Function App, Logic App, Storage, App Insights |
| Entra ID P1 | Recommended | Conditional Access policies |

!!! note
    The shared mailbox does not require an additional licence.

## Network Requirements

The deployment machine needs internet access to:

- `login.microsoftonline.com` — Azure AD authentication
- `graph.microsoft.com` — Microsoft Graph API
- `management.azure.com` — Azure Resource Manager
- `*.sharepoint.com` — SharePoint Online
- `github.com` — Download the tool
- `www.powershellgallery.com` — PowerShell modules
