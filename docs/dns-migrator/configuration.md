# Configuration

Configuration options for DNS Migrator.

## Web UI

The web UI requires no configuration files — all settings are entered interactively through the wizard:

- **Cloudflare API Token** — entered in Step 1
- **Azure credentials** — entered in Step 2 (if using Azure source)
- **Zone selection** — chosen in Step 3

!!! info "Security"
    Tokens are passed per-request and used in-memory only. They are never logged, stored on disk, or persisted between sessions.

## PowerShell Batch Config

For batch migrations using `Migrate-Batch.ps1`, create a JSON config file listing your zones.

### Config File Format

Copy `config.example.json` to `config.json`:

```bash
cp config.example.json config.json
```

```json title="config.json"
{
  "zones": [
    {
      "zoneName": "example.com",
      "resourceGroup": "my-dns-resource-group",
      "cloudflareZoneId": "paste-cloudflare-zone-id-here"
    },
    {
      "zoneName": "example.co.uk",
      "resourceGroup": "my-dns-resource-group",
      "cloudflareZoneId": "paste-cloudflare-zone-id-here"
    }
  ]
}
```

### Config Fields

| Field | Required | Description |
|-------|----------|-------------|
| `zones` | Yes | Array of zone objects to migrate |
| `zones[].zoneName` | Yes | The DNS zone name (e.g. `example.com`) |
| `zones[].resourceGroup` | Yes | Azure resource group containing the DNS zone |
| `zones[].cloudflareZoneId` | Yes | Target Cloudflare Zone ID |

### Finding Your Cloudflare Zone ID

1. Open [Cloudflare Dashboard](https://dash.cloudflare.com)
2. Select the zone
3. On the **Overview** page, scroll down to the **API** section on the right
4. Copy the **Zone ID**

!!! warning
    The Cloudflare Zone must already exist when using PowerShell batch mode. The batch script pushes records to existing zones — it does not create new ones.

## Environment Variables

### Local Express Server

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | `3000` | Port for the Express server |

### Cloudflare Pages

No environment variables required — functions run in the Cloudflare Workers runtime with zero config.
