# Troubleshooting

## Common Issues

### Logic App Emails Not Sending

**Symptom**: Logic App runs succeed but no emails arrive.

**Fix**: Authorise the Office 365 API connection:

1. Azure Portal → Resource Groups → your RG
2. Find the `office365` API connection
3. Edit API connection → Authorize → Sign in → Save

---

### Tracking Link Returns 400 Error

**Symptom**: Clicking the tracking link in the email shows a 400 Bad Request.

**Possible causes**:

1. **Function code not deployed** — Redeploy:
    ```powershell
    .\Update-Deployment.ps1 -FunctionCode
    ```

2. **TrackingToken column not indexed** — Update SharePoint schema:
    ```powershell
    .\Update-Deployment.ps1 -SharePointSchema
    ```

3. **Token not in SharePoint** — Check the user's row has a `TrackingToken` value. If not:
    ```powershell
    .\Update-Deployment.ps1 -BackfillTokens
    ```

---

### MFA Status Not Updating

**Symptom**: Users have registered MFA but status stays "Not Registered".

**Fix**: Check Logic App permissions:

```powershell
.\Check-LogicApp-Permissions.ps1
```

The Logic App needs `UserAuthenticationMethod.ReadWrite.All`. If missing:

```powershell
.\Check-LogicApp-Permissions.ps1 -AddPermissions
```

---

### MFA Registration Date Not Populating

**Symptom**: Status updates to "Active" but `MFARegistrationDate` is blank.

**Fix**: You're running an older Logic App template. Redeploy:

```powershell
.\Update-Deployment.ps1 -LogicApp
```

---

### MSAL DLL Assembly Conflict

**Symptom**: Error about `Microsoft.Identity.Client` assembly version when running permission scripts.

**Fix**: The v2 permission scripts use `az rest` instead of the Microsoft.Graph module. Ensure you're running scripts from the `v2\` folder:

```powershell
cd v2
.\Fix-Graph-Permissions.ps1
.\Check-LogicApp-Permissions.ps1
```

---

### Function App Managed Identity Token Error

**Symptom**: Function App logs show errors getting Managed Identity tokens.

**Fix**: The v2 function code supports both the new `IDENTITY_ENDPOINT` (Azure Functions v4) and legacy `MSI_ENDPOINT`. Redeploy:

```powershell
.\Update-Deployment.ps1 -FunctionCode
```

---

### SharePoint List Not Found

**Symptom**: Function App or Logic App can't find the SharePoint list.

**Check**:

1. Verify `ListId` in `mfa-config.ini` matches the actual list GUID
2. Verify `SiteUrl` is correct
3. Ensure Managed Identity has `Sites.ReadWrite.All` permission

---

### Upload Portal Authentication Error

**Symptom**: Portal shows authentication error on login.

**Check**:

1. App registration has correct redirect URIs (the portal URL)
2. Admin consent has been granted for `User.Read` and `Sites.Read.All`
3. The portal URL matches what's in the app registration

---

## Diagnostic Scripts

### Check All Permissions

```powershell
.\Check-LogicApp-Permissions.ps1
```

Lists all current permissions and highlights any missing ones.

### Generate Technical Summary

```powershell
.\Create-TechnicalSummary.ps1
```

Creates a file in `logs\` with all resource IDs, object IDs, URLs, and troubleshooting commands.

### Quick Fix (All Common Issues)

```powershell
.\Update-Deployment.ps1 -QuickFix
```

Runs Function Auth fix, Graph Permissions fix, and Logic App Permissions fix in sequence.

## Getting Help

If you're stuck:

1. Check **Application Insights** for Function App errors (live metrics, request failures, exceptions)
2. Check the Logic App **run history** in Azure Portal for error details
3. Run `.\Create-TechnicalSummary.ps1` and review the output
4. Check the `logs\` folder for deployment logs

!!! tip "Application Insights"
    Navigate to your Application Insights resource in the Azure Portal. Use **Live Metrics** during active rollouts, **Failures** to investigate errors, and **Transaction search** to trace individual requests through the system.
