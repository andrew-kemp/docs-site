# Upload Portal

The upload portal is a single-page application (SPA) hosted on Azure Storage as a static website. It provides three tabs for administrators: CSV upload, manual entry, and a reports dashboard.

## Accessing the Portal

The portal URL is displayed at the end of deployment and stored in `mfa-config.ini` under `[UploadPortal] > PortalUrl`.

Typically: `https://<storageaccount>.z33.web.core.windows.net/`

!!! note
    The portal uses Azure AD authentication via MSAL.js. Users must sign in with an account that has `User.Read` and `Sites.Read.All` scopes.

## Tab 1: CSV Upload

Upload a CSV file with users to onboard.

### CSV Format

The CSV must include a column named `UPN`, `UserPrincipalName`, or `Email` (case-insensitive):

```csv
UserPrincipalName,DisplayName
user1@contoso.com,John Smith
user2@contoso.com,Jane Doe
```

- **UserPrincipalName** (or `UPN` / `Email`) — Required. The user's email/UPN.
- **DisplayName** — Optional. Used in personalised emails.

### How It Works

1. **Drag and drop** a `.csv` file onto the drop zone (or click to browse)
2. **Client-side validation** runs automatically:
    - Parses CSV headers and identifies the email column
    - Validates email format with regex for each row
    - Shows a **preview table** of the first 10 rows with valid/invalid indicators
    - Displays a summary of total valid and invalid counts
3. Click **Upload** to send validated users to the Function App (`/api/upload-users`)
4. An **animated progress bar** shows upload progress
5. **Results** display as stat cards: Total, Added, Updated, Skipped, Errors — with expandable error/skip details
6. On success, a **branded success page** appears with auto-redirect to the Reports tab

### Batch IDs

Every upload gets a `SourceBatchId`:

- Enter a custom batch ID before uploading, or
- One is auto-generated as `yyyy-MM-dd-HHmm`

Batch IDs are used to filter and track groups of users in the Reports tab.

### Duplicate Handling

Re-uploading an existing user resets them to `InviteStatus = Pending` and `MFARegistrationState = Unknown` for re-processing. The `SourceBatchId` is updated to the new batch.

## Tab 2: Manual Entry

Add users without a CSV file.

1. Enter email addresses in the text area — one per line or comma-separated
2. Click **Submit**
3. Users are added to the SharePoint list immediately with `InviteStatus = Pending`

## Tab 3: Reports Dashboard

A real-time dashboard showing MFA rollout progress, powered by Microsoft Graph queries against the SharePoint list.

### Executive Summary

- **Total Users** — Complete count of all users in the rollout
- **MFA Active** — Users who have completed MFA enrollment
- **Pending** — Users who haven't completed yet
- **Completion Rate** — Percentage of users with Active status

### Batch Filter

A dropdown populated dynamically from all `SourceBatchId` values with per-batch user counts. Selecting a batch filters all dashboard sections.

### Status Breakdown

Grid cards for each status (Pending, Sent, Clicked, AddedToGroup, Active, Error, Skipped) showing counts and percentages.

### Recent Activity

Activity from the last 7 days:

- Invitations sent
- Links clicked
- Users added to group

### Alerts

- **High reminder alerts** — Red warning box highlighting users with 2+ reminders who still haven't completed MFA
- **Users needing attention** — List of users requiring follow-up

### Batch Performance

Per-batch completion rates and user counts — useful for comparing rollout waves.

### CSV Export

Click **Export CSV** to download all report data as `mfa-report-YYYY-MM-DD.csv` with proper escaping.

### Email Report

Compose and send an executive summary email directly from the portal to configured recipients.
