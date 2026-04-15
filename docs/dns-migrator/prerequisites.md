# Prerequisites

Everything you need before running DNS Migrator.

## All Deployment Modes

### Cloudflare Account & API Token

You need a Cloudflare account (free tier is sufficient) and an API token with the following permissions:

| Permission | Scope | Required For |
|------------|-------|-------------|
| Zone → DNS → Edit | All zones | Creating DNS records |
| Zone → Zone → Edit | All zones | Creating new zones |
| Account → Account Settings → Read | Account | Listing accounts for selection |

!!! tip "Creating a Cloudflare API Token"
    1. Go to [Cloudflare Dashboard](https://dash.cloudflare.com/profile/api-tokens)
    2. Click **Create Token**
    3. Use **Custom Token** template
    4. Add the three permissions listed above
    5. Set zone/account resources as needed
    6. Click **Continue to summary** → **Create Token**
    7. Copy the token — you won't see it again

### Domain Access

You need access to your domain registrar to update nameservers after migration.

---

## Web UI (Cloudflare Pages or Local)

### Node.js

- **Node.js 18.0.0** or later
- npm (included with Node.js)

### Wrangler (for Cloudflare Pages deployment)

```bash
npm install -g wrangler
```

Or use it via `npx` without global install.

---

## PowerShell CLI

### PowerShell

- **PowerShell 5.0** or later (Windows PowerShell or PowerShell Core)

### Azure CLI

Required for Azure DNS source:

```bash
# Check if installed
az --version

# Login to Azure
az login
```

!!! info "Azure CLI Installation"
    If you don't have Azure CLI installed, see the [official installation guide](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli).

### Azure Permissions

The Azure identity used needs **DNS Zone Reader** role (or higher) on the subscription or resource group containing your DNS zones.

---

## Azure DNS Source (Web UI)

When using Azure DNS as the source in the web UI, you need one of:

=== "Bearer Token"

    Obtain a token from an active Azure CLI session:

    ```bash
    az account get-access-token --query accessToken -o tsv
    ```

    Paste this into the web UI.

=== "Service Principal"

    Create a service principal with DNS Reader access:

    ```bash
    az ad sp create-for-rbac \
      --name "dns-migrator" \
      --role "DNS Zone Contributor" \
      --scopes "/subscriptions/{subscription-id}"
    ```

    You'll need the **Tenant ID**, **Client ID**, and **Client Secret** returned.

---

## DNS Scan Source

No additional prerequisites — the DNS scan uses Cloudflare's public DNS-over-HTTPS resolver. It works against any DNS provider without credentials.

!!! note
    The scanner probes ~80 common subdomain names. Uncommon subdomains may not be discovered. For a complete export, use the Azure DNS source or zone file import.
