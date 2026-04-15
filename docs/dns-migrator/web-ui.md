# Web UI Guide

Step-by-step walkthrough of the DNS Migrator web interface.

## Overview

The web UI is a 4-step wizard with a dark theme. Each step must be completed before advancing to the next.

---

## Step 1: Cloudflare Authentication

1. Enter your **Cloudflare API token**
2. Click **Validate**
3. If valid, a dropdown appears with your Cloudflare accounts
4. Select the target account

!!! tip
    Your token needs **Zone DNS Edit**, **Zone Edit**, and **Account Settings Read** permissions. See [Prerequisites](prerequisites.md) for details.

---

## Step 2: Choose DNS Source

Select how DNS records will be discovered:

=== "DNS Scan"

    Probes live DNS using Cloudflare's DNS-over-HTTPS resolver.

    1. Enter one or more domain names (one per line)
    2. Click **Scan**
    3. The scanner probes ~80 common subdomains plus SRV records
    4. Progress streams in real-time
    5. Discovered records are displayed with counts

    **Best for:** Migrating from providers where you don't have API access (GoDaddy, Namecheap, etc.)

    !!! note
        Only common subdomain names are probed. Uncommon subdomains may be missed.

=== "Azure DNS"

    Full zone export via Azure Management API.

    **Bearer Token auth:**

    1. Select **Bearer Token**
    2. Paste a token from `az account get-access-token --query accessToken -o tsv`
    3. Click **Validate**

    **Service Principal auth:**

    1. Select **Service Principal**
    2. Enter Tenant ID, Client ID, and Client Secret
    3. Click **Validate**

    Once authenticated:

    4. Select your Azure subscription from the dropdown
    5. Click **Load Zones**
    6. All DNS zones are listed with full record counts

    **Best for:** Complete, accurate migration of all Azure DNS records.

=== "Manual"

    Create empty zones in Cloudflare without importing records.

    1. Enter domain names (one per line)
    2. Click **Submit**

    **Best for:** Setting up new zones where you'll add records manually.

---

## Step 3: Select Domains

All discovered zones are displayed in a list with:

- Checkbox for selection
- Domain name
- Record count (if scanned or imported)

Use the **Select All** option for bulk selection, or pick individual zones.

Click **Next** to proceed.

---

## Step 4: Migrate

The migration begins automatically. For each selected zone:

1. **Zone creation** — Creates the zone in Cloudflare (or detects it already exists)
2. **Record fetching** — Pulls records from the chosen source
3. **Transformation** — Strips FQDN suffixes, removes trailing dots, validates format
4. **Duplicate check** — Compares against existing Cloudflare records
5. **Record creation** — Pushes each record via Cloudflare API

### Live Log

Every action streams to the log in real-time with colour-coded entries:

| Colour | Type | Meaning |
|--------|------|---------|
| :material-circle:{ style="color: green" } Green | `record` | Record created successfully |
| :material-circle:{ style="color: orange" } Yellow | `skip` | Record already exists, skipped |
| :material-circle:{ style="color: red" } Red | `error` | Record creation failed |
| :material-circle:{ style="color: dodgerblue" } Blue | `info` | Informational message |
| :material-circle:{ style="color: purple" } Purple | `status` | Status update |
| :material-circle:{ style="color: gray" } Grey | `progress` | Scanner progress |

### Results

When migration completes, you'll see:

- **Per-zone summary** — Records created, skipped, and failed
- **Nameservers** — The Cloudflare nameservers to set at your registrar

!!! warning "Don't forget the nameservers"
    Migration creates records in Cloudflare, but your domain won't use them until you update the nameservers at your registrar.

### Example Log Output

```
[status] example.com — Creating zone...
[success] example.com — Zone created (ID: abc123)
[info] example.com — Found 10 records in Azure
[record] example.com — [1/10] A www → 93.184.216.34 ✓
[record] example.com — [2/10] A @ → 93.184.216.34 ✓
[skip] example.com — [3/10] CNAME mail — already exists
[record] example.com — [4/10] MX @ → mail.example.com (priority: 10) ✓
...
[zone-complete] example.com — Created: 8, Skipped: 1, Failed: 0
[done] Migration complete
```
