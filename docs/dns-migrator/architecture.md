# Architecture

How DNS Migrator's components fit together.

## High-Level Overview

```
┌──────────────────────────────────────────────┐
│           Frontend (Web UI)                  │
│  Tailwind CSS · 4-step wizard · NDJSON logs  │
└──────────────────┬───────────────────────────┘
                   │ REST API (POST)
┌──────────────────▼───────────────────────────┐
│           Backend API Layer                  │
│  Express (local) or Cloudflare Workers       │
└───┬──────────┬──────────┬──────────┬─────────┘
    │          │          │          │
┌───▼───┐ ┌───▼────┐ ┌───▼───┐ ┌───▼──────┐
│ Azure │ │Cloudfl.│ │  DNS  │ │Transform │
│  API  │ │  API   │ │ Scan  │ │  Logic   │
│Module │ │ Module │ │ (DoH) │ │          │
└───────┘ └────────┘ └───────┘ └──────────┘
```

## Components

### Frontend (`public/`)

| File | Purpose |
|------|---------|
| `index.html` | Dark-themed wizard UI built with Tailwind CSS |
| `app.js` | State management, step navigation, NDJSON stream parsing |

The frontend is a single-page application with a 4-step wizard:

1. **Cloudflare** — Token validation, account selection
2. **DNS Source** — Choose Scan, Azure, or Manual
3. **Domains** — Select zones with record counts
4. **Migrate** — Live streaming log with colour-coded results

### Backend Modules (`src/`)

| Module | Purpose |
|--------|---------|
| `api.js` | Express route definitions and request handling |
| `azure.js` | Azure DNS Management API integration (zone listing, record export) |
| `cloudflare.js` | Cloudflare API integration (zone creation, record insertion, duplicate detection) |
| `dns-scan.js` | DNS-over-HTTPS scanning via Cloudflare DoH (probes ~80 common subdomains) |
| `transform.js` | Record normalisation — strips FQDNs, removes trailing dots, maps Azure → Cloudflare format |

### Serverless Functions (`functions/api/`)

Mirror of the `src/` modules adapted for Cloudflare Workers runtime:

| Function | Endpoint |
|----------|----------|
| `cloudflare/validate.js` | `/api/cloudflare/validate` |
| `azure/validate.js` | `/api/azure/validate` |
| `azure/zones.js` | `/api/azure/zones` |
| `dns/scan.js` | `/api/dns/scan` |
| `migrate.js` | `/api/migrate` |
| `_helpers.js` | Shared NDJSON streaming utilities |

### PowerShell Scripts

| Script | Purpose |
|--------|---------|
| `Migrate-DNS.ps1` | Single-zone migration from Azure DNS to Cloudflare |
| `Migrate-Batch.ps1` | Multi-zone batch migration using JSON config |

## Data Flow

### Web UI Migration Flow

```
User enters Cloudflare token
        ↓
POST /api/cloudflare/validate
        ↓ returns accounts
User selects account, chooses DNS source
        ↓
┌───────────────────────────────┐
│  Scan: POST /api/dns/scan     │
│  Azure: POST /api/azure/zones │
│  Manual: client-side only     │
└───────────────┬───────────────┘
                ↓
User selects zones (checkboxes)
                ↓
POST /api/migrate (NDJSON stream)
                ↓
For each zone:
  1. Create zone in Cloudflare (or use existing)
  2. Fetch records from source
  3. Transform records (strip FQDN suffixes, normalise)
  4. Check for duplicates in Cloudflare
  5. Push new records via Cloudflare API
  6. Stream per-record status back to UI
                ↓
Display nameservers for registrar update
```

### PowerShell Migration Flow

```
Migrate-DNS.ps1 / Migrate-Batch.ps1
        ↓
az network dns record-set list (Azure CLI)
        ↓
Convert-AzureToCloudflareRecords (transform)
        ↓
Cloudflare API: POST /zones/{id}/dns_records
        ↓
Console output: created / skipped / failed per record
```

## Real-Time Streaming

The `/api/migrate` and `/api/dns/scan` endpoints use **NDJSON** (newline-delimited JSON) for real-time progress:

```json
{"type":"status","zone":"example.com","message":"Creating zone..."}
{"type":"success","zone":"example.com","message":"Zone created"}
{"type":"record","zone":"example.com","message":"[1/10] A www → 1.2.3.4"}
{"type":"skip","zone":"example.com","message":"[2/10] CNAME mail — already exists"}
{"type":"zone-complete","zone":"example.com","result":{"created":9,"skipped":1,"failed":0}}
{"type":"done","results":[...]}
```

## Supported Record Types

| Type | Supported | Notes |
|------|-----------|-------|
| A | :material-check: | IPv4 address |
| AAAA | :material-check: | IPv6 address |
| CNAME | :material-check: | Canonical name |
| MX | :material-check: | Mail exchange (includes priority) |
| TXT | :material-check: | Text records |
| SRV | :material-check: | Service records (priority, weight, port) |
| CAA | :material-check: | Certificate Authority Authorization |
| NS | :material-check: | Non-apex only (apex NS skipped) |
| PTR | :material-check: | Pointer records |
| SOA | :material-close: | Skipped (Cloudflare manages SOA) |
