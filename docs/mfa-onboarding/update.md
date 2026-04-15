# Resume & Update

## Updating an Existing Deployment

Use `Update-Deployment.ps1` to update specific components without redeploying everything.

### Interactive Menu

```powershell
.\Update-Deployment.ps1
```

Presents a menu with options to update individual components.

### CLI Switches

```powershell
# Update everything
.\Update-Deployment.ps1 -UpdateAll

# Update specific components
.\Update-Deployment.ps1 -FunctionCode     # Redeploy function code only
.\Update-Deployment.ps1 -LogicApp         # Redeploy Logic App template
.\Update-Deployment.ps1 -Branding         # Update branding in emails
.\Update-Deployment.ps1 -Permissions      # Reapply Graph permissions
.\Update-Deployment.ps1 -SharePointSchema # Update SharePoint columns
.\Update-Deployment.ps1 -BackfillTokens   # Generate tracking tokens for existing users
```

### Quick Fix

```powershell
.\Update-Deployment.ps1 -QuickFix
```

Runs common fixes: Function Auth, Graph Permissions, Logic App Permissions.

---

## Using Setup.ps1

`Setup.ps1` is the single entry point for all operations:

```powershell
.\Setup.ps1
```

### Menu Options

| Option | Description |
|--------|-------------|
| **[1] Update existing deployment** | Opens `Update-Deployment.ps1` menu |
| **[2] Pull latest code + Update** | Downloads latest from GitHub, then updates |
| **[3] Upgrade to v2** | Migrates from v1 to v2 (schema + tokens + function + Logic App + permissions) |
| **[4] Fresh install** | Runs full deployment from scratch |
| **[5] Resume deployment** | Continues from last completed step |
| **[6] Quick fix** | Runs common permission and auth fixes |
| **[0] Exit** | Exit |

---

## Downloading Latest Code

To update the scripts on a deployment machine:

```powershell
cd C:\path\to\MFA-Onboard-Tool-main

iwr https://github.com/andrew-kemp/MFA-Onboard-Tool/archive/refs/heads/main.zip -OutFile $env:TEMP\mfa-update.zip; Expand-Archive $env:TEMP\mfa-update.zip $env:TEMP\mfa-update -Force; if (Test-Path .\v2\mfa-config.ini) { Copy-Item .\v2\mfa-config.ini $env:TEMP\mfa-config.ini.bak }; Remove-Item .\v2 -Recurse -Force -ErrorAction SilentlyContinue; Copy-Item $env:TEMP\mfa-update\MFA-Onboard-Tool-main\v2 .\v2 -Recurse -Force; if (Test-Path $env:TEMP\mfa-config.ini.bak) { Copy-Item $env:TEMP\mfa-config.ini.bak .\v2\mfa-config.ini -Force; Remove-Item $env:TEMP\mfa-config.ini.bak }; Remove-Item $env:TEMP\mfa-update,$env:TEMP\mfa-update.zip -Recurse -Force
```

This preserves your `mfa-config.ini` while updating all scripts.

---

## Resuming a Failed Deployment

### Automatic Resume

```powershell
.\Run-Complete-Deployment-Master.ps1 -Resume
```

Reads `logs\deployment-state.json` and continues from the next incomplete step.

### Manual Resume

```powershell
.\Run-Complete-Deployment-Master.ps1 -StartFromStep 7
```

Skips steps 1-6 and starts from step 7.

### Step Reference

| Step | Script | Description |
|------|--------|-------------|
| 1 | `01-Install-Prerequisites.ps1` | Install PowerShell modules |
| 2 | `02-Provision-SharePoint.ps1` | Create SharePoint site & list |
| 3 | `03-Create-Shared-Mailbox.ps1` | Create shared mailbox |
| 4 | `04-Create-Azure-Resources.ps1` | Create Azure resources |
| 5 | `05-Configure-Function-App.ps1` | Configure Function App |
| 6 | `06-Deploy-Logic-App.ps1` | Deploy Logic App |
| 7 | `07-Deploy-Upload-Portal1.ps1` | Deploy upload portal |
| 8 | `08-Deploy-Email-Reports.ps1` | Deploy email reports |
| 9 | `Fix-Function-Auth.ps1` | Fix function authentication |
| 10 | `Fix-Graph-Permissions.ps1` | Fix Graph permissions |
| 11 | `Check-LogicApp-Permissions.ps1` | Fix Logic App permissions |
| 12 | `Generate-Deployment-Report.ps1` | Generate final report |

---

## Upgrading from v1 to v2

If you have an existing v1 installation:

```powershell
.\Setup.ps1
# Choose option [3] Upgrade to v2
```

The upgrade performs 5 steps:

1. **SharePoint Schema** — Adds new columns (TrackingToken, LastChecked, etc.)
2. **Backfill Tokens** — Generates tracking tokens for existing users
3. **Function Code** — Deploys updated function code with token support
4. **Logic App** — Redeploys Logic App with token-based URLs
5. **Permissions** — Reapplies all Graph API permissions
