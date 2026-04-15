# PowerShell CLI

Command-line scripts for migrating DNS zones from Azure DNS to Cloudflare.

## Migrate-DNS.ps1 (Single Zone)

Migrates one Azure DNS zone to Cloudflare.

### Usage

```powershell
.\Migrate-DNS.ps1 `
  -AzureResourceGroup "my-dns-rg" `
  -ZoneName "example.com" `
  -CloudflareApiToken "your-cf-token" `
  -CloudflareZoneId "your-zone-id"
```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `-AzureResourceGroup` | Yes | Azure resource group containing the DNS zone |
| `-ZoneName` | Yes | DNS zone name (e.g. `example.com`) |
| `-CloudflareApiToken` | Yes | Cloudflare API token |
| `-CloudflareZoneId` | Yes | Target Cloudflare Zone ID |
| `-DryRun` | No | Preview changes without creating records |
| `-Proxied` | No | Enable Cloudflare proxy (orange cloud) for A, AAAA, and CNAME records |
| `-SkipExisting` | No | Skip records that already exist in Cloudflare |

### Examples

**Dry run — preview what would be migrated:**

```powershell
.\Migrate-DNS.ps1 `
  -AzureResourceGroup "prod-dns-rg" `
  -ZoneName "andykemp.com" `
  -CloudflareApiToken "cf-token-here" `
  -CloudflareZoneId "zone-id-here" `
  -DryRun
```

**Full migration with proxy enabled:**

```powershell
.\Migrate-DNS.ps1 `
  -AzureResourceGroup "prod-dns-rg" `
  -ZoneName "andykemp.com" `
  -CloudflareApiToken "cf-token-here" `
  -CloudflareZoneId "zone-id-here" `
  -Proxied -SkipExisting
```

### How It Works

1. Calls `az network dns record-set list` to export all records from the Azure DNS zone
2. Converts Azure record format to Cloudflare format (strips FQDNs, removes trailing dots)
3. Skips SOA records and apex NS records
4. Creates each record via the Cloudflare API (`POST /zones/{id}/dns_records`)
5. Reports created / skipped / failed counts

### Output

```
Migrating zone: andykemp.com
  [1/15] A www → 93.184.216.34 ... Created
  [2/15] A @ → 93.184.216.34 ... Created
  [3/15] CNAME mail → mail.example.com ... Skipped (exists)
  [4/15] MX @ → mail.example.com (priority: 10) ... Created
  ...
Summary: 12 created, 2 skipped, 1 failed
```

---

## Migrate-Batch.ps1 (Multiple Zones)

Migrates multiple zones sequentially from a JSON config file.

### Usage

```powershell
.\Migrate-Batch.ps1 `
  -ConfigFile ".\config.json" `
  -CloudflareApiToken "your-cf-token"
```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `-ConfigFile` | Yes | Path to JSON config file (see [Configuration](configuration.md)) |
| `-CloudflareApiToken` | Yes | Cloudflare API token (used for all zones) |
| `-DryRun` | No | Preview changes for all zones |
| `-Proxied` | No | Enable Cloudflare proxy for all zones |
| `-SkipExisting` | No | Skip duplicates for all zones |

### Config File

```json title="config.json"
{
  "zones": [
    {
      "zoneName": "example.com",
      "resourceGroup": "my-dns-rg",
      "cloudflareZoneId": "zone-id-1"
    },
    {
      "zoneName": "example.co.uk",
      "resourceGroup": "my-dns-rg",
      "cloudflareZoneId": "zone-id-2"
    }
  ]
}
```

See [Configuration](configuration.md) for full details.

### Examples

**Dry run for all zones:**

```powershell
.\Migrate-Batch.ps1 `
  -ConfigFile ".\config.json" `
  -CloudflareApiToken "cf-token-here" `
  -DryRun
```

**Full batch migration:**

```powershell
.\Migrate-Batch.ps1 `
  -ConfigFile ".\config.json" `
  -CloudflareApiToken "cf-token-here" `
  -SkipExisting
```

### How It Works

1. Reads the `zones` array from the config file
2. For each zone, calls `Migrate-DNS.ps1` with the zone's parameters
3. Collects results (OK / FAILED) for each zone
4. Displays a final summary table

### Output

```
=== Batch DNS Migration ===
Processing 3 zones...

[1/3] example.com
  12 created, 2 skipped, 0 failed — OK

[2/3] example.co.uk
  8 created, 0 skipped, 0 failed — OK

[3/3] example.net
  0 created, 0 skipped, 5 failed — FAILED

=== Summary ===
Zone              Status  Created  Skipped  Failed
----              ------  -------  -------  ------
example.com       OK      12       2        0
example.co.uk     OK      8        0        0
example.net       FAILED  0        0        5
```

## Prerequisites

- Azure CLI installed and logged in (`az login`)
- Cloudflare API token with Zone DNS Edit permissions
- Cloudflare Zone IDs for target zones (must already exist)

See [Prerequisites](prerequisites.md) for full requirements.
