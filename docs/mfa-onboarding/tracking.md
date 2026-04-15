# Tracking & Status

The SharePoint list tracks every user through the MFA enrollment journey. Each row represents one user with their current status and timestamps.

## Status Flow

```
Pending → Sent → Clicked → AddedToGroup → Active
```

| Status | Meaning |
|--------|---------|
| **Pending** | User added to list, no email sent yet |
| **Sent** | Invitation email has been sent |
| **Clicked** | User clicked the tracking link in the email |
| **AddedToGroup** | User has been added to the MFA security group |
| **Active** | MFA registration confirmed — enrollment complete |

## SharePoint Columns

| Column | Type | Description |
|--------|------|-------------|
| `Title` | Text | User Principal Name (UPN) |
| `DisplayName_` | Text | User's display name |
| `InviteStatus` | Choice | Current status (see above) |
| `InGroup` | Yes/No | Whether user is in the MFA security group |
| `MFARegistrationState` | Choice | `Registered` or `Not Registered` |
| `MFARegistrationDate` | DateTime | When MFA registration was first detected |
| `ClickedLinkDate` | DateTime | When the user clicked the tracking link |
| `AddedToGroupDate` | DateTime | When the user was added to the security group |
| `InviteSentDate` | DateTime | When the invitation email was sent |
| `LastReminderDate` | DateTime | When the last reminder was sent |
| `LastChecked` | DateTime | When the Logic App last checked this user |
| `Source` | Text | How the user was added (CSV Upload / Manual) |
| `SourceBatchId` | Text | Batch identifier for CSV uploads |
| `TrackingToken` | Text | GUID used in tracking links (no PII in URLs) |
| `ErrorDetails` | Text | Any error messages from processing |

## How Each Status Is Set

### Pending
Set when a user is first uploaded via the portal or manual entry. The `upload-users` function creates the SharePoint item with `InviteStatus = Pending`.

### Sent
Set by the Logic App after successfully sending the invitation email. Also sets `InviteSentDate`.

### Clicked
Set by the `enrol` function when the user clicks the tracking link in their email. Also sets `ClickedLinkDate`.

### AddedToGroup
Set by the `enrol` function after adding the user to the MFA security group. Also sets `AddedToGroupDate` and `InGroup = true`.

### Active
Set by the Logic App when it detects the user has registered MFA methods (phone, authenticator app, FIDO2, etc.). Also sets:

- `MFARegistrationState = Registered`
- `MFARegistrationDate = (current timestamp)`
- `LastChecked = (current timestamp)`

## Tracking Links

Tracking links use GUID-based tokens instead of email addresses:

```
https://func-mfa-yourorg.azurewebsites.net/api/track-mfa-click?token=a1b2c3d4-e5f6-7890-abcd-ef1234567890
```

This prevents PII (email addresses) from appearing in URLs, browser history, and server logs.

## Reminders

The Logic App automatically sends reminder emails:

- **First reminder**: 7 days after the initial invitation
- **Condition**: User has `InviteStatus = Sent` (hasn't clicked yet)
- Updates `LastReminderDate` when sent

## MFA Detection

The Logic App checks MFA registration by querying:

```
GET /users/{userId}/authentication/methods
```

It looks for any of these MFA method types:

- `phoneAuthenticationMethod`
- `microsoftAuthenticatorAuthenticationMethod`
- `softwareOathAuthenticationMethod`
- `fido2AuthenticationMethod`
- `windowsHelloForBusinessAuthenticationMethod`

!!! note
    The `#microsoft.graph.passwordAuthenticationMethod` is excluded — passwords alone don't count as MFA.
