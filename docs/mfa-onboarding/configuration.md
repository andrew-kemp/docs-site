# Configuration

All settings are managed in `mfa-config.ini`. This file is created from the template during first setup.

## Configuration Sections

### `[Tenant]`

```ini
[Tenant]
TenantId=yourtenant.onmicrosoft.com
SubscriptionId=your-azure-subscription-id
```

| Setting | Description | Example |
|---------|-------------|---------|
| `TenantId` | Microsoft 365 tenant ID or `.onmicrosoft.com` domain | `contoso.onmicrosoft.com` |
| `SubscriptionId` | Azure subscription ID | `12345678-1234-1234-1234-123456789012` |

### `[SharePoint]`

```ini
[SharePoint]
SiteUrl=https://yourtenant.sharepoint.com/sites/MFAOps
SiteOwner=admin@yourtenant.com
AppRegName=YourOrg-SPO-Automation-MFA
SiteTitle=MFA Operations
ListTitle=MFA Onboarding
```

| Setting | Description | Auto-filled |
|---------|-------------|-------------|
| `SiteUrl` | Full URL to SharePoint site | No |
| `SiteOwner` | Email of site owner | No |
| `AppRegName` | App registration name for SharePoint | No |
| `SiteTitle` | Display title for SharePoint site | No |
| `ListTitle` | Name of tracking list | No (default: `MFA Onboarding`) |
| `ClientId` | App registration client ID | Yes |
| `CertificatePath` | Path to auth certificate | Yes |
| `CertificateThumbprint` | Certificate thumbprint | Yes |
| `ListId` | SharePoint list GUID | Yes |

### `[Security]`

```ini
[Security]
MFAGroupName=MFA Enabled Users
```

| Setting | Description | Auto-filled |
|---------|-------------|-------------|
| `MFAGroupName` | Name of MFA security group | No |
| `MFAGroupId` | Group object ID | Yes |

### `[Azure]`

```ini
[Azure]
ResourceGroup=rg-mfa-onboarding
Region=uksouth
FunctionAppName=func-mfa-yourorg-001
StorageAccountName=stmfayourorg001
```

| Setting | Description | Auto-filled |
|---------|-------------|-------------|
| `ResourceGroup` | Azure resource group name | No |
| `Region` | Azure region | No |
| `FunctionAppName` | Function App name (must be globally unique) | No |
| `StorageAccountName` | Storage account name (must be globally unique) | No |
| `MFAPrincipalId` | Managed Identity principal ID | Yes |
| `AppInsightsName` | Application Insights resource name | Yes |
| `AppInsightsKey` | Instrumentation key | Yes |
| `AppInsightsConnectionString` | Connection string | Yes |

### `[Email]`

```ini
[Email]
MailboxName=MFA Registration
NoReplyMailbox=MFA-Registration@yourtenant.com
MailboxDelegate=admin@yourtenant.com
EmailSubject=ACTION REQUIRED: Complete your MFA Registration
ReminderSubject=REMINDER: Complete your MFA Registration
```

| Setting | Description |
|---------|-------------|
| `MailboxName` | Display name for the shared mailbox |
| `NoReplyMailbox` | Email address for the shared mailbox |
| `MailboxDelegate` | Admin who can access the mailbox |
| `EmailSubject` | Subject line for initial invitation emails |
| `ReminderSubject` | Subject line for reminder emails |

### `[LogicApp]`

```ini
[LogicApp]
LogicAppName=mfa-invite-orchestrator
RecurrenceHours=12
```

| Setting | Description | Auto-filled |
|---------|-------------|-------------|
| `LogicAppName` | Logic App name | No |
| `RecurrenceHours` | Hours between Logic App runs (default: `12`) | No |
| `TriggerUrl` | HTTP trigger URL for immediate invocation | Yes |
| `ConnectionId` | SharePoint API connection ID | Yes |
| `Office365ConnectionId` | Office 365 API connection ID | Yes |

### `[UploadPortal]`

```ini
[UploadPortal]
AppRegName=YourOrg-MFA-Upload-Portal
```

| Setting | Description | Auto-filled |
|---------|-------------|-------------|
| `AppRegName` | App registration name for portal | No |
| `PortalUrl` | Static website URL | Yes |

### `[Branding]`

```ini
[Branding]
CompanyName=Your Organisation
LogoUrl=https://yourorg.com/logo.png
SupportTeam=IT Security Team
SupportEmail=itsupport@yourtenant.com
```

| Setting | Description |
|---------|-------------|
| `CompanyName` | Organisation name shown in emails |
| `LogoUrl` | URL to company logo (optional) |
| `SupportTeam` | Support team name shown in email footers |
| `SupportEmail` | Support contact email shown in email footers |

### `[OpsGroup]`

```ini
[OpsGroup]
OpsGroupEmail=mfa-ops@yourtenant.com
OpsGroupName=MFA Operations Team
```

| Setting | Description |
|---------|-------------|
| `OpsGroupEmail` | Mail-enabled security group for ops notifications |
| `OpsGroupName` | Display name for the ops group |

### `[EmailReports]`

```ini
[EmailReports]
LogicAppName=logic-mfa-reports-123456
Recipients=admin1@domain.com,admin2@domain.com
Frequency=Day
```

| Setting | Description |
|---------|-------------|
| `LogicAppName` | Reports Logic App name | 
| `Recipients` | Comma-separated list of report recipients |
| `Frequency` | `Day` (daily at 9 AM) or `Week` (Monday at 9 AM) |

## Auto-Filled Settings

Settings marked as "Auto-filled" are populated automatically during deployment. You do not need to set these manually — the deployment scripts will write them to `mfa-config.ini` as resources are created.

!!! warning
    Do not manually edit auto-filled settings unless you know what you're doing. Incorrect values will break the deployment.
