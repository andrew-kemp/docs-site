# Upload Portal

The upload portal is a web-based interface hosted on Azure Storage as a static website. It provides three main functions for administrators.

## Accessing the Portal

The portal URL is displayed at the end of deployment and stored in `mfa-config.ini` under `[UploadPortal] > PortalUrl`.

Typically: `https://<storageaccount>.z33.web.core.windows.net/`

!!! note
    The portal uses Azure AD authentication. Users must sign in with an account that has been granted access.

## Tab 1: CSV Upload

Upload a CSV file with users to onboard.

### CSV Format

```csv
UserPrincipalName,DisplayName
user1@contoso.com,John Smith
user2@contoso.com,Jane Doe
```

- **UserPrincipalName** — Required. The user's email/UPN.
- **DisplayName** — Optional. Used in personalised emails.

### How It Works

1. Drag and drop a CSV file or click to browse
2. The portal validates the file format
3. Users are sent to the Azure Function (`upload-users`)
4. The function adds each user to the SharePoint list
5. Progress is shown in real-time

## Tab 2: Manual Entry

Add a single user without a CSV file.

1. Enter the user's email address
2. Optionally enter a display name
3. Click Submit
4. User is added to the SharePoint list immediately

## Tab 3: Reports Dashboard

A live dashboard showing MFA rollout progress.

### Metrics

- **Total Users** — Complete count of all users in the rollout
- **Completed** — Users with `InviteStatus = Active`
- **Pending** — Users not yet completed
- **Completion Rate** — Percentage of users completed

### Sections

- **Status Breakdown** — Visual breakdown by `InviteStatus` value
- **Recent Activity** — Enrollments in the last 7 days
- **Users Needing Attention** — Pending 3+ days, clicked but not in group
- **Batch Performance** — Completion rates grouped by `SourceBatchId`

### Data Source

The reports tab queries the SharePoint list in real-time using Microsoft Graph API. Data refreshes on each page load.
