# Quick Start Guide

Get the MFA Onboarding system deployed in under 30 minutes.

## Prerequisites

Before you begin, ensure you have:

- **Windows 10/11** or **Windows Server 2019+**
- **PowerShell 7.4+** (run `pwsh` to check)
- **Azure CLI** installed
- **Azure Subscription** with Owner or Contributor access
- **Microsoft 365** with Global Admin or equivalent roles

## Step 1: Download

### Option A: Bootstrap Script (Recommended)

```powershell
# Download the bootstrap script
wget https://raw.githubusercontent.com/andrew-kemp/MFA-Onboard-Tool/main/Get-MFAOnboarder.ps1 -OutFile Get-MFAOnboarder.ps1

# Run it - it downloads everything and starts deployment
.\Get-MFAOnboarder.ps1
```

### Option B: Manual Download

```powershell
# Download and extract
Invoke-WebRequest -Uri "https://github.com/andrew-kemp/MFA-Onboard-Tool/archive/refs/heads/main.zip" -OutFile mfa-tool.zip
Expand-Archive mfa-tool.zip -DestinationPath . -Force
cd MFA-Onboard-Tool-main\v2
```

## Step 2: Configure

1. Copy the template config:
    ```powershell
    Copy-Item mfa-config.ini.template mfa-config.ini
    ```

2. Edit `mfa-config.ini` with your organisation's details:
    ```ini
    [Tenant]
    TenantId=yourtenant.onmicrosoft.com
    SubscriptionId=your-azure-subscription-id

    [SharePoint]
    SiteUrl=https://yourtenant.sharepoint.com/sites/MFAOps
    SiteOwner=admin@yourtenant.com

    [Security]
    MFAGroupName=MFA Enabled Users

    [Azure]
    ResourceGroup=rg-mfa-onboarding
    Region=uksouth

    [Email]
    MailboxName=MFA Registration
    NoReplyMailbox=MFA-Registration@yourtenant.com
    MailboxDelegate=admin@yourtenant.com
    ```

    !!! tip
        See [Configuration](configuration.md) for all available settings.

## Step 3: Deploy

### Full Automated Deployment

```powershell
.\Run-Complete-Deployment-Master.ps1
```

This runs all 12 steps automatically with retry on failure.

### Or Step-by-Step

```powershell
.\01-Install-Prerequisites.ps1    # Install PowerShell modules
.\02-Provision-SharePoint.ps1     # Create SharePoint site & list
.\03-Create-Shared-Mailbox.ps1    # Create shared mailbox
.\04-Create-Azure-Resources.ps1   # Create Azure resources
.\05-Configure-Function-App.ps1   # Configure Function App
.\06-Deploy-Logic-App.ps1         # Deploy Logic App
.\07-Deploy-Upload-Portal1.ps1    # Deploy upload portal
.\08-Deploy-Email-Reports.ps1     # Deploy email reports (optional)
```

## Step 4: Post-Deployment

After deployment completes:

1. **Authorise API connections** in Azure Portal:
    - Go to Resource Group → API Connections
    - Authorise `office365` connection (sign in with an account that can send mail)
    - Authorise `office365-reports` connection (if using email reports)

2. **Test the system**:
    - Open the Upload Portal URL (shown at end of deployment)
    - Upload a test CSV or enter a test user manually
    - Check the SharePoint list for the new entry
    - Verify the invitation email arrives

## Step 5: Upload Users

Create a CSV file with your users:

```csv
UserPrincipalName,DisplayName
user1@yourtenant.com,John Smith
user2@yourtenant.com,Jane Doe
```

Upload via the web portal or use the upload function directly.

---

## What Happens Next

Once users are uploaded:

1. Logic App runs on schedule and sends invitation emails
2. Users click the tracking link in the email
3. System records the click and adds user to the MFA security group
4. On the next Logic App run, MFA registration status is checked
5. Once MFA is registered, status is set to **Active** with a timestamp

See [Tracking & Status](tracking.md) for details on each status.
