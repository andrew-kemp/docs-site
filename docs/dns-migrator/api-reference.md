# API Reference

REST API endpoints for the DNS Migrator backend.

All endpoints accept `POST` requests with JSON bodies. Responses are JSON or NDJSON (newline-delimited JSON) for streaming endpoints.

---

## POST /api/cloudflare/validate

Validate a Cloudflare API token and retrieve associated accounts.

### Request

```json
{
  "apiToken": "your-cloudflare-api-token"
}
```

### Response

```json
{
  "success": true,
  "accounts": [
    {
      "id": "account-id-hex",
      "name": "My Account"
    }
  ]
}
```

### Errors

| Status | Meaning |
|--------|---------|
| 401 | Invalid or expired token |
| 403 | Token lacks required permissions |

---

## POST /api/azure/validate

Authenticate with Azure and retrieve available subscriptions.

### Request — Bearer Token

```json
{
  "authMethod": "bearer",
  "bearerToken": "eyJ0eXAiOiJKV1Q..."
}
```

### Request — Service Principal

```json
{
  "authMethod": "servicePrincipal",
  "tenantId": "tenant-guid",
  "clientId": "client-guid",
  "clientSecret": "client-secret"
}
```

### Response

```json
{
  "success": true,
  "subscriptions": [
    {
      "subscriptionId": "sub-guid",
      "displayName": "My Subscription"
    }
  ]
}
```

---

## POST /api/azure/zones

List DNS zones in an Azure subscription.

### Request

```json
{
  "token": "bearer-or-sp-token",
  "subscriptionId": "sub-guid"
}
```

### Response

```json
{
  "success": true,
  "zones": [
    {
      "name": "example.com",
      "resourceGroup": "my-dns-rg",
      "recordCount": 15
    }
  ]
}
```

---

## POST /api/dns/scan

Scan a domain via DNS-over-HTTPS to discover existing DNS records. Returns an NDJSON stream.

### Request

```json
{
  "domain": "example.com"
}
```

### Response (NDJSON stream)

```json
{"type":"progress","message":"Scanning apex records..."}
{"type":"progress","message":"Probing common subdomains..."}
{"type":"info","message":"Found 5 apex records"}
{"type":"info","message":"Probed 80 subdomains, found 12"}
{"type":"done","records":[...],"total":42,"subdomainsFound":["www","mail","ftp"]}
```

### Record Format

Each record in the `records` array:

```json
{
  "type": "A",
  "name": "www",
  "content": "93.184.216.34",
  "ttl": 300
}
```

---

## POST /api/migrate

Migrate DNS zones to Cloudflare. Returns an NDJSON stream with real-time progress.

### Request

```json
{
  "cfToken": "cloudflare-api-token",
  "cfAccountId": "cloudflare-account-id",
  "zones": [
    {
      "name": "example.com",
      "records": [
        {
          "type": "A",
          "name": "www",
          "content": "93.184.216.34",
          "ttl": 300
        }
      ]
    }
  ],
  "azureToken": "optional-azure-bearer-token",
  "subscriptionId": "optional-azure-subscription-id"
}
```

### Response (NDJSON stream)

```json
{"type":"status","zone":"example.com","message":"Creating zone..."}
{"type":"success","zone":"example.com","message":"Zone created (ID: abc123)"}
{"type":"info","zone":"example.com","message":"Found 10 records"}
{"type":"record","zone":"example.com","message":"[1/10] A www → 93.184.216.34"}
{"type":"record","zone":"example.com","message":"[2/10] A @ → 93.184.216.34"}
{"type":"skip","zone":"example.com","message":"[3/10] CNAME mail — already exists"}
{"type":"error","zone":"example.com","message":"[4/10] TXT @ — API error: invalid content"}
{"type":"zone-complete","zone":"example.com","result":{"created":8,"skipped":1,"failed":1,"nameServers":["ns1.cloudflare.com","ns2.cloudflare.com"]}}
{"type":"done","results":[{"zone":"example.com","created":8,"skipped":1,"failed":1}]}
```

### Stream Event Types

| Type | Description |
|------|-------------|
| `status` | Zone-level status update |
| `success` | Zone-level success (e.g. zone created) |
| `info` | Informational message |
| `record` | Record created successfully |
| `skip` | Record skipped (duplicate) |
| `error` | Record creation error |
| `zone-complete` | Zone migration finished with summary |
| `done` | All zones complete with final results |

---

## Authentication

All credentials are passed in request bodies — there are no stored sessions, cookies, or server-side credential storage.

| Credential | Passed In | Stored |
|------------|-----------|--------|
| Cloudflare API Token | Request body | Never |
| Azure Bearer Token | Request body | Never |
| Azure Service Principal | Request body | Never |

!!! info
    Tokens are used in-memory for the duration of the request only.
