# Step-by-Step Deployment

## Getting Started

The recommended way to start is with `Setup.ps1`:

```powershell
.\Setup.ps1
```

For a fresh install, select **[1] New deployment** — this launches `Run-Complete-Deployment-Master.ps1` which runs all 12 steps automatically with retry on failure.

!!! tip "Don't have the scripts yet?"
    See [Quick Start](quick-start.md) for the one-liner bootstrap command to download everything.

## Advanced: Running Steps Individually

### Option 1: Full Automated Deployment

```powershell
.\Run-Complete-Deployment-Master.ps1
```

This runs all 12 steps in order with automatic retry on failure. It supports resuming from where you left off if interrupted.

### Option 2: Two-Part Deployment

**Part 1 — Microsoft 365 Resources:**
```powershell
.\01-Install-Prerequisites.ps1
.\02-Provision-SharePoint.ps1
.\03-Create-Shared-Mailbox.ps1
```

**Part 2 — Azure Resources:**
```powershell
.\04-Create-Azure-Resources.ps1
.\05-Configure-Function-App.ps1
.\06-Deploy-Logic-App.ps1
.\07-Deploy-Upload-Portal1.ps1
.\08-Deploy-Email-Reports.ps1
```

**Post-Deployment Fixes:**
```powershell
.\Fix-Function-Auth.ps1
.\Fix-Graph-Permissions.ps1
.\Check-LogicApp-Permissions.ps1 -AddPermissions
```

### Option 3: Individual Scripts

Run each script one at a time for maximum control.

---

## Step Details

### Step 01: Install Prerequisites

```powershell
.\01-Install-Prerequisites.ps1
```

Installs required PowerShell modules:

- Az, Az.Functions
- PnP.PowerShell
- Microsoft.Graph
- ExchangeOnlineManagement

### Step 02: Provision SharePoint

```powershell
.\02-Provision-SharePoint.ps1
```

Creates:

- SharePoint site (if it doesn't exist)
- App registration with certificate auth
- MFA Onboarding list with 20+ columns
- Indexed columns for Graph API filtering

### Step 03: Create Shared Mailbox

```powershell
.\03-Create-Shared-Mailbox.ps1
```

Creates:

- Shared mailbox for sending enrollment emails
- Delegate access for the specified admin

### Step 04: Create Azure Resources

```powershell
.\04-Create-Azure-Resources.ps1
```

Creates:

- Resource Group
- Storage Account (with static website enabled)
- App Service Plan (Consumption/Y1)
- Function App (PowerShell 7.4, Managed Identity enabled)
- Application Insights

### Step 05: Configure Function App

```powershell
.\05-Configure-Function-App.ps1
```

Configures:

- Function App settings (SharePoint URL, List ID, Group ID, etc.)
- CORS settings for the upload portal
- Deploys function code (`enrol` and `upload-users` functions)

### Step 06: Deploy Logic App

```powershell
.\06-Deploy-Logic-App.ps1
```

Deploys:

- Logic App with Managed Identity
- API connections (SharePoint, Office 365)
- Invitation orchestration workflow from template
- Placeholder replacement with your config values

!!! note
    After deployment, you must authorise the Office 365 API connection in the Azure Portal.

### Step 07: Deploy Upload Portal

```powershell
.\07-Deploy-Upload-Portal1.ps1
```

Deploys:

- Static website to Azure Storage
- Upload portal HTML with your configuration baked in
- App registration for SPA authentication

### Step 08: Deploy Email Reports (Optional)

```powershell
.\08-Deploy-Email-Reports.ps1
```

Deploys:

- Reports Logic App with separate Managed Identity
- Office 365 API connection for sending reports
- Daily or weekly schedule
- Recipient configuration

---

## Post-Deployment

### Authorise API Connections

!!! warning "Required"
    Without this step, the Logic App cannot send emails.

1. Go to **Azure Portal** → **Resource Groups** → your resource group
2. Find the API connection named **office365**
3. Click **Edit API connection** → **Authorize** → Sign in → **Save**
4. Repeat for **office365-reports** if using email reports

### Verify Permissions

Run the permission checker to confirm everything is in place:

```powershell
.\Check-LogicApp-Permissions.ps1
```

To add any missing permissions:

```powershell
.\Check-LogicApp-Permissions.ps1 -AddPermissions
```

### Generate Technical Summary

```powershell
.\Create-TechnicalSummary.ps1
```

Creates a comprehensive document in the `logs\` folder with all resource IDs, URLs, and troubleshooting commands.

---

## Resume a Failed Deployment

If the deployment was interrupted, you can resume:

```powershell
# Automatic resume from last completed step
.\Run-Complete-Deployment-Master.ps1 -Resume

# Resume from a specific step
.\Run-Complete-Deployment-Master.ps1 -StartFromStep 7
```

See [Resume & Update](update.md) for more details.
