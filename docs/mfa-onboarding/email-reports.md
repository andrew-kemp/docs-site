# Email Reports

Automated email reports sent to administrators showing MFA rollout progress.

## Overview

A separate Logic App sends scheduled email reports to a configured list of recipients. Reports provide an executive summary of the MFA rollout status.

## Report Contents

Each email contains:

- **Total Users** — Complete count of all users in the rollout
- **Completed** — Users who have completed MFA enrollment
- **Pending** — Users who haven't completed yet
- **Completion Rate** — Percentage of users completed
- **Quick Links** — Direct links to SharePoint list and Upload Portal

## Frequency Options

| Option | Schedule |
|--------|----------|
| Daily | Every day at 9:00 AM |
| Weekly | Every Monday at 9:00 AM |
| Both | Daily and weekly reports |

## Setup

### During Deployment

When running `08-Deploy-Email-Reports.ps1`, you'll be prompted for:

1. **Recipient email addresses** (comma-separated)
2. **Frequency** (Daily, Weekly, or Both)

### Standalone Setup

```powershell
.\08-Deploy-Email-Reports.ps1
```

### Configuration

Settings in `mfa-config.ini`:

```ini
[EmailReports]
LogicAppName=logic-mfa-reports-123456
Recipients=admin1@domain.com,admin2@domain.com
Frequency=Day
```

## Post-Setup: Authorise Connection

!!! warning "Required"
    The Office 365 API connection must be authorised before reports will send.

1. Go to **Azure Portal** → **Resource Groups** → your resource group
2. Find the connection named **office365-reports**
3. Click **Edit API connection**
4. Click **Authorize** → Sign in with an account that can send mail
5. Click **Save**

## Testing

### Manual Test Run

1. Go to **Azure Portal** → **Logic Apps**
2. Select your reports Logic App
3. Click **Run Trigger** → **Recurrence**
4. Check your inbox for the report

### Check Run History

1. Open the Logic App in Azure Portal
2. Click **Overview**
3. View **Run History** for successful/failed runs
4. Click any run to see the detailed execution flow

## Changing Recipients

1. Edit `Recipients` in `mfa-config.ini`
2. Redeploy:
    ```powershell
    .\08-Deploy-Email-Reports.ps1
    ```

## Changing Frequency

1. Edit `Frequency` in `mfa-config.ini` to `Day` or `Week`
2. Redeploy the reports Logic App
