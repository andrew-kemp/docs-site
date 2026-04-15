# Troubleshooting

Common issues and solutions for DNS Migrator.

## Cloudflare API Errors

### "Authentication error" when validating token

**Cause:** The API token is invalid, expired, or has insufficient permissions.

**Fix:**

1. Check the token hasn't expired in [Cloudflare Dashboard → API Tokens](https://dash.cloudflare.com/profile/api-tokens)
2. Ensure the token has these permissions:
    - Zone → DNS → Edit
    - Zone → Zone → Edit
    - Account → Account Settings → Read
3. Regenerate the token if needed

### "Could not find zone" or zone creation fails

**Cause:** The token's zone resources are scoped too narrowly, or account-level permissions are missing.

**Fix:** Edit the token and set zone resources to **All zones** (or include the specific zone).

### Records created but not resolving

**Cause:** Nameservers haven't been updated at the registrar.

**Fix:** After migration, update your domain's nameservers at your registrar to the Cloudflare nameservers shown in the migration results.

!!! warning
    DNS propagation can take up to 48 hours after updating nameservers, though it's usually much faster.

---

## Azure DNS Errors

### "Bearer token expired or invalid"

**Cause:** Azure bearer tokens expire after ~1 hour.

**Fix:** Generate a fresh token:

```bash
az account get-access-token --query accessToken -o tsv
```

### "No subscriptions found"

**Cause:** The authenticated identity doesn't have access to any subscriptions, or the token is for the wrong tenant.

**Fix:**

1. Check you're logged into the correct tenant: `az account show`
2. Ensure the identity has at least **Reader** role on the subscription
3. For service principals, verify the tenant ID matches

### "No DNS zones found in subscription"

**Cause:** The subscription has no Azure DNS zones, or the identity lacks DNS-level permissions.

**Fix:**

1. Verify zones exist: `az network dns zone list --subscription {id}`
2. Ensure the identity has **DNS Zone Reader** role or higher

---

## DNS Scan Issues

### Scanner finds very few records

**Cause:** The scanner probes ~80 common subdomain names. Uncommon subdomains won't be discovered.

**Fix:**

- Use **Azure DNS** source for a complete export (if zones are in Azure)
- Manually add missing records after migration
- Check your current provider's zone file export for a full record list

### Scanner times out or shows errors

**Cause:** Network issues or DNS-over-HTTPS blocked.

**Fix:**

1. Check your network allows HTTPS connections to `cloudflare-dns.com`
2. Try again — transient DoH errors are usually temporary
3. If behind a corporate proxy, the proxy may block DoH queries

---

## PowerShell Issues

### "az: command not found"

**Cause:** Azure CLI is not installed or not in PATH.

**Fix:** Install Azure CLI:

- Windows: `winget install Microsoft.AzureCLI`
- macOS: `brew install azure-cli`
- Linux: [Installation guide](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux)

### "Please run 'az login' first"

**Cause:** Not authenticated to Azure CLI.

**Fix:**

```bash
az login
```

### Batch script fails on one zone and stops

**Cause:** `Migrate-Batch.ps1` processes zones sequentially. A critical error in one zone may halt the batch.

**Fix:**

1. Check the error for the failed zone
2. Fix the issue (wrong resource group, missing permissions, etc.)
3. Re-run the batch — zones with `-SkipExisting` will skip already-migrated records

---

## Deployment Issues

### Wrangler deploy fails

**Cause:** Not authenticated to Cloudflare via Wrangler.

**Fix:**

```bash
npx wrangler login
npx wrangler pages deploy public
```

### Local server won't start (port in use)

**Cause:** Port 3000 is already in use by another process.

**Fix:** Use a different port:

=== "PowerShell"

    ```powershell
    $env:PORT = 3001; npm start
    ```

=== "Bash"

    ```bash
    PORT=3001 npm start
    ```

### Functions return 404 on Cloudflare Pages

**Cause:** Functions directory structure doesn't match expected routes.

**Fix:** Ensure the `functions/api/` directory structure matches the API routes. Redeploy with:

```bash
npx wrangler pages deploy public
```

---

## General Tips

- **Always dry-run first** — Use `-DryRun` (PowerShell) or review the scan results before migrating
- **Check existing records** — The tool detects duplicates and skips them, but review the skip count to ensure nothing unexpected
- **One zone at a time** — If a batch migration has issues, migrate the problematic zone individually to isolate the error
- **Keep your old DNS active** — Don't delete records from your source provider until you've confirmed everything works in Cloudflare
