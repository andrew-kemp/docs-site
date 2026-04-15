# What's New

## v2 — Latest

### Token-Based Tracking Links
- Tracking links now use GUID tokens instead of email addresses in URLs
- Prevents PII exposure in browser history, logs, and server telemetry
- Backward compatible — existing `?user=` links still work

### MFA Registration Date Tracking
- `MFARegistrationDate` is now set when MFA is first detected
- `LastChecked` timestamp updated on every Logic App run
- Full audit trail for compliance reporting

### Improved Managed Identity Support
- Function App supports both `IDENTITY_ENDPOINT` (Azure Functions v4) and legacy `MSI_ENDPOINT`
- Eliminates token acquisition errors on newer runtimes

### Configurable Email Subjects
- Invitation and reminder email subjects can be customised in `mfa-config.ini`
- No need to edit Logic App templates

### Operations Group
- Configure a mail-enabled security group for ops notifications
- Set via `[OpsGroup]` section in `mfa-config.ini`

### Permission Fixes (No MSAL Dependency)
- `Fix-Graph-Permissions.ps1` and `Check-LogicApp-Permissions.ps1` rewritten to use `az rest`
- Eliminates `Microsoft.Identity.Client` DLL assembly conflicts
- Works reliably on any machine with Azure CLI installed

### SharePoint Column Indexing
- `TrackingToken`, `InviteStatus`, and `MFARegistrationState` columns are now indexed
- Required for Graph API `$filter` queries to work correctly

### Update & Upgrade Tooling
- `Setup.ps1` — Single entry point for all operations
- `Update-Deployment.ps1` — Menu-driven update tool with CLI switches
- Upgrade path from v1 to v2 with config migration
- One-liner for pulling latest code while preserving config

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
