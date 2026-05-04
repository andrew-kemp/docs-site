# What's New

## v2 — Latest

### New Entry Points

- **`Setup.ps1`** — Single entry point replacing the old Part 1 / Part 2 flow. Auto-detects new install vs existing deployment. Self-updating with config preservation.
- **`Get-MFAOnboarder.ps1`** — One-line bootstrap: downloads the full repo and launches Setup.ps1
- **`Update-Deployment.ps1`** — Granular update tool with 8 CLI switches or interactive menu. Update function code, Logic App, branding, permissions, schema, or manage the Operations Group — all independently.

### New Function Endpoints

- **`/api/track-open`** — Invisible 1×1 tracking pixel embedded in every email. Records `EmailOpenedDate` in SharePoint on first open only. Always returns 200 OK with a valid GIF.
- **`/api/resend`** — Self-service resend form. GET returns a branded HTML page where users enter their email. POST resets to Pending. Anti-enumeration: identical success message regardless of user existence.

### Enhancements to `/api/enrol`

- **Duplicate-click protection** — Repeated clicks show a branded "Already Registered" page
- **Branded HTML responses** with auto-redirect countdown for all outcomes (Invalid Link, Link Not Recognised, Already Registered, MFA Enrolment Started, Error)
- **API detection** — Returns JSON instead of HTML for programmatic callers (based on `Accept` header / User-Agent)

### Manager Escalation

- After 2+ reminders, the user's **manager** is automatically looked up via Graph API and sent an escalation email
- Red "Manager Action Required" header with employee name, reminder count, and clear action instructions
- Records `EscalatedToManager`, `EscalationDate`, and `ManagerUPN` in SharePoint
- Only escalates once per user

### Token-Based Tracking Links
- Tracking links now use GUID tokens instead of email addresses in URLs
- Prevents PII exposure in browser history, logs, and server telemetry
- Backward compatible — existing `?user=` links still work

### MFA Registration Date Tracking
- `MFARegistrationDate` is now set when MFA is first detected
- `LastChecked` timestamp updated on every Logic App run
- Full audit trail for compliance reporting

### Email Open Tracking
- Invisible 1×1 pixel in every email records when the email is opened
- `EmailOpenedDate` stamped in SharePoint on first open only
- Fire-and-forget: tracking failures never block the pixel response

### Logic App Retry Policies
- **Exponential backoff** on all 16 API-connected actions
- 3 retries with 10-second minimum and 1-hour maximum interval
- Eliminates transient failures causing stuck users

### Application Insights
- Full telemetry for all Function App endpoints: request logging, exception tracking, performance metrics
- Live Metrics Stream for real-time monitoring during rollouts
- Auto-provisioned during deployment with instrumentation key saved to config

### Infrastructure as Code (Bicep)
- `infra/main.bicep` defines all Azure resources with secure defaults (TLS 1.2, HTTPS-only, FTPS disabled)
- `infra/main.parameters.json` for environment-specific values

### Upload Portal Improvements
- **Drag-and-drop** CSV upload with visual drop zone
- **Client-side validation** — parses headers, validates email format, shows preview table (10 rows)
- **Progress bar** — animated upload progress with stat card results
- **Reports tab** — executive summary, batch filter, status breakdown, recent activity, high-reminder alerts, CSV export, email report
- **Branded success page** with auto-redirect to reports tab

### Improved Managed Identity Support
- Function App supports both `IDENTITY_ENDPOINT` (Azure Functions v4) and legacy `MSI_ENDPOINT`
- Eliminates token acquisition errors on newer runtimes

### Configurable Email Subjects
- Separate `EmailSubject` and `ReminderSubject` in `mfa-config.ini`
- No need to edit Logic App templates

### Operations Group
- Configure a mail-enabled security group for ops notifications
- Automatically grants FullAccess + SendAs on mailbox and SharePoint site access
- Managed via `Update-Deployment.ps1 -Permissions` → Manage Operations Group

### Permission Fixes (No MSAL Dependency)
- `Fix-Graph-Permissions.ps1` and `Check-LogicApp-Permissions.ps1` rewritten to use `az rest`
- Eliminates `Microsoft.Identity.Client` DLL assembly conflicts
- Works reliably on any machine with Azure CLI installed

### SharePoint Column Indexing
- `TrackingToken`, `InviteStatus`, and `MFARegistrationState` columns are now indexed
- Required for Graph API `$filter` queries to work correctly

### New SharePoint Columns
- `TrackingToken` — Unique GUID for secure enrolment links
- `EmailOpenedDate` — First email open timestamp (tracking pixel)
- `EscalatedToManager` — Whether manager has been escalated
- `EscalationDate` — When the escalation email was sent
- `ManagerUPN` — Manager's email from Entra ID
- `MFARegistrationDate` — When MFA auth methods were first detected
- `SourceBatchId` — Batch identifier from upload

---

## Deployment Enhancements

### Comprehensive Logging
- All deployment actions logged with timestamps
- Log files saved to `logs\` folder
- Error messages with stack traces for debugging

### Error Handling with Retry
- Failed steps can be retried up to 3 times
- Critical vs optional steps clearly marked
- User controls whether to retry, skip, or abort

### Technical Summary Generation
- Automatic generation of comprehensive technical document
- All resource IDs, object IDs, URLs, and troubleshooting commands
- Portal direct links for quick navigation

### Resume Support
- Deployment state saved after each step
- Resume from where you left off with `-Resume` flag
- Manual resume from any step with `-StartFromStep`

---

## Email Reports

### Automated Admin Reports
- Daily and/or weekly email reports
- Executive summary with completion metrics
- Direct links to SharePoint list and Upload Portal
- Configurable recipients and frequency
