# Tracking & Status

The SharePoint list tracks every user through the MFA enrollment journey. Each row represents one user with their current status, engagement data, and timestamps.

## Status Flow

```
Pending → Sent → Clicked → AddedToGroup → Active
                    ↘ (if 2+ reminders without completion)
                      → EscalatedToManager
```

| Status | Meaning |
|--------|---------|
| **Pending** | User added to list, no email sent yet |
| **Sent** | Invitation email has been sent |
| **Clicked** | User clicked the tracking link in the email |
| **AddedToGroup** | User has been added to the MFA security group |
| **Active** | MFA registration confirmed — enrollment complete |

## SharePoint Columns

The SharePoint list uses 24 columns to track each user:

| Column | Type | Description |
|--------|------|-------------|
| `Title` | Text | User Principal Name (UPN) |
| `DisplayName_` | Text | User's display name |
| `InviteStatus` | Choice | Current status (Pending, Sent, Clicked, AddedToGroup, Active) |
| `InGroup` | Yes/No | Whether user is in the MFA security group |
| `MFARegistrationState` | Choice (indexed) | `Registered` or `Not Registered` |
| `MFARegistrationDate` | DateTime | When MFA registration was first detected |
| `TrackingToken` | Text (indexed) | Unique GUID for secure enrolment links |
| `ClickedLinkDate` | DateTime | When the user clicked the tracking link |
| `AddedToGroupDate` | DateTime | When the user was added to the security group |
| `InviteSentDate` | DateTime | When the invitation email was sent |
| `LastReminderDate` | DateTime | When the last reminder was sent |
| `ReminderCount` | Number | How many reminders the user has received |
| `LastChecked` | DateTime | When the Logic App last checked this user |
| `EmailOpenedDate` | DateTime | When the email was first opened (tracking pixel) |
| `EscalatedToManager` | Boolean | Whether the user's manager has been escalated |
| `EscalationDate` | DateTime | When the escalation email was sent |
| `ManagerUPN` | Text | Manager's email address from Entra ID |
| `Source` | Text | How the user was added (CSV Upload / Manual) |
| `SourceBatchId` | Text | Batch identifier for CSV uploads |
| `ErrorDetails` | Text | Any error messages from processing |
| `CorrelationId` | Text | Links related operations for audit trails |

!!! info "Indexed Columns"
    `TrackingToken`, `InviteStatus`, and `MFARegistrationState` are indexed in SharePoint. This is required for Graph API `$filter` queries to work correctly.

## How Each Status Is Set

### Pending
Set when a user is first uploaded via the portal or manual entry. The `upload-users` function creates the SharePoint item with `InviteStatus = Pending` and generates a unique `TrackingToken` (GUID).

### Sent
Set by the Logic App after successfully sending the invitation email. Also sets `InviteSentDate`. The email contains:

- An enrolment link using the user's `TrackingToken`
- An invisible tracking pixel (`/api/track-open?token={GUID}`)
- A "Lost your setup link?" resend link in the footer
- Microsoft Authenticator App Store links for iOS and Android

### Clicked
Set by the `enrol` function when the user clicks the tracking link in their email. Also sets `ClickedLinkDate`. The user sees a branded "MFA Enrolment Started" page with an auto-redirect countdown to `aka.ms/mfasetup`.

### AddedToGroup
Set by the `enrol` function after adding the user to the MFA security group. Also sets `AddedToGroupDate` and `InGroup = true`.

### Active
Set by the Logic App when it detects the user has registered MFA methods. Also sets:

- `MFARegistrationState = Registered`
- `MFARegistrationDate = (current timestamp)`
- `LastChecked = (current timestamp)`

## Email Open Tracking

Every outgoing email includes an invisible 1×1 pixel image:

```html
<img src="https://func-mfa-yourorg.azurewebsites.net/api/track-open?token={GUID}" width="1" height="1" />
```

- Records `EmailOpenedDate` in SharePoint on **first open only**
- Fire-and-forget: tracking failures never block the pixel response
- Always returns 200 OK with a valid GIF regardless of outcome

## Tracking Links

Tracking links use GUID-based tokens instead of email addresses:

```
https://func-mfa-yourorg.azurewebsites.net/api/enrol?token=a1b2c3d4-e5f6-7890-abcd-ef1234567890
```

This prevents PII (email addresses) from appearing in URLs, browser history, and server logs.

### Duplicate-Click Protection

If a user clicks the enrolment link again after already clicking, they see a branded "Already Registered" page instead of being re-processed.

### Branded Response Pages

The `enrol` endpoint returns styled HTML pages for all outcomes:

| Outcome | Colour | Description |
|---------|--------|-------------|
| **MFA Enrolment Started** | Green | Success — redirects to `aka.ms/mfasetup` |
| **Already Registered** | Green | User already clicked previously |
| **Invalid Link** | Red | Missing parameters |
| **Link Not Recognised** | Orange | Token/user not found in SharePoint |
| **Error** | Red | Unexpected failure |

## Reminders

The Logic App automatically sends reminder emails:

- **Frequency**: Every 7 days after the initial invitation
- **Condition**: User has `InviteStatus = Sent` (hasn't clicked yet)
- Updates `LastReminderDate` and increments `ReminderCount` when sent
- Reminder emails use a separate configurable subject line (`ReminderSubject`)

## Manager Escalation

After 2+ reminder emails without MFA completion:

1. The user's **manager** is looked up via Microsoft Graph (`/users/{id}/manager`)
2. An **escalation email** is sent to the manager with a red "Manager Action Required" header
3. The email includes the employee's name, reminder count, and clear action instructions
4. SharePoint records `EscalatedToManager = true`, `EscalationDate`, and `ManagerUPN`
5. Only escalates **once per user** (checks `EscalatedToManager` before sending)

## Self-Service Resend

Every email includes a "Lost your setup link?" link in the footer pointing to `/api/resend`:

1. User clicks the link and sees a branded HTML form
2. User enters their email address and submits
3. System resets `InviteStatus` to Pending and clears `ReminderCount`
4. **Anti-enumeration**: an identical success message is returned regardless of whether the user exists
5. Logic App picks up the reset user on its next scheduled run

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
