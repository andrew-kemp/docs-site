# Intelligence & Insights

Beyond raw scores, the audit runs **eight specialised intelligence analysers** that examine your data from different angles and produce actionable findings.

---

## How Intelligence Works

Each analyser examines a specific attack surface or risk domain. It considers the raw audit data, applies context (e.g. tenant size, licensing), and generates **findings** — each with a severity, description, and recommendation.

Findings are categorised by severity:

| Severity | Meaning |
|----------|---------|
| :material-alert-octagon:{ style="color: red" } **Critical** | Immediate action required — active risk |
| :material-alert:{ style="color: #ff5722" } **High** | Significant gap — address promptly |
| :material-alert-circle:{ style="color: orange" } **Medium** | Notable concern — plan remediation |
| :material-information:{ style="color: #2196f3" } **Low** | Minor issue or improvement opportunity |
| :material-lightbulb:{ style="color: green" } **Info** | Observation or best-practice recommendation |

---

## The Eight Analysers

### 1. Identity Attack Surface Analysis

**Focus:** How exposed is your identity perimeter?

Examines:

- MFA adoption gaps (what percentage of users are unprotected?)
- Authentication method strength (SMS/voice vs. FIDO2/Windows Hello)
- Security Defaults status
- Account hygiene (stale, never-signed-in, guest policies)

**Example finding:** _"34% of users have not registered for MFA. These accounts are vulnerable to credential-based attacks."_

---

### 2. Privileged Access Exposure

**Focus:** Are admin accounts properly secured?

Examines:

- Number of permanent Global Admins vs. break-glass threshold
- PIM adoption — eligible vs. standing assignments
- Users with 3+ admin roles (privilege concentration)
- Break-glass account configuration
- Admin role distribution across 15+ roles

**Example finding:** _"5 permanent Global Administrators found. Best practice is 2 break-glass accounts with all other admin access via PIM eligible assignments."_

---

### 3. Conditional Access Coverage

**Focus:** How comprehensive is your policy enforcement?

Examines:

- Percentage of users covered by active CA policies
- Policies in report-only mode (not enforcing)
- MFA enforcement via CA
- Device compliance requirements
- Risk-based policies (sign-in risk, user risk)
- Legacy authentication blocking
- Named location usage

**Example finding:** _"3 of 12 Conditional Access policies are in report-only mode and not actively enforcing. Consider enabling them after validation."_

---

### 4. Device Trust Analysis

**Focus:** Are devices accessing your tenant under management?

Examines:

- Intune compliance policy count and assignment scope
- App protection policies for BYOD
- Device configuration profiles
- Whether CA policies require compliant devices
- Gap between policy existence and enforcement

**Example finding:** _"Intune compliance policies exist but no Conditional Access policy requires a compliant device for sign-in."_

---

### 5. External Exposure Assessment

**Focus:** What's visible or accessible to the outside world?

Examines:

- Mailboxes with external forwarding (data exfiltration risk)
- Inbox rules forwarding or redirecting to external addresses
- External sharing settings for SharePoint and OneDrive
- Guest user invitation policies
- Guest user access scope
- External domains with access

**Example finding:** _"12 mailboxes have forwarding enabled to external addresses. This is a common persistence mechanism used by attackers."_

---

### 6. Application Risk Analysis

**Focus:** Are third-party apps a risk vector?

Examines:

- OAuth grants with high-risk scopes (`Mail.ReadWrite`, `Directory.ReadWrite.All`, etc.)
- Applications with expired credentials (abandoned but still granted access)
- Credential expiry timeline (expiring within 30/60/90 days)
- Application-to-scope risk mapping

**Example finding:** _"4 enterprise applications have expired credentials but retain active OAuth grants. These may be abandoned apps with unnecessary access."_

---

### 7. Licensing Optimisation

**Focus:** Are you getting value from your licences?

Examines:

- Subscription inventory (SKUs, counts, costs)
- Licence utilisation rate (assigned vs. purchased)
- Unused licences (cost waste)
- Storage consumption vs. entitlements

**Example finding:** _"87 Office 365 E5 licences purchased but only 62 assigned — 25 unused licences represent potential cost savings."_

---

### 8. Migration Readiness

**Focus:** How complex would a migration or consolidation be?

Examines:

- Mailbox volume and total size
- OneDrive storage footprint
- Teams and SharePoint complexity
- Public folder presence (major complexity driver)
- Directory sync model (cloud-only vs. hybrid)
- Domain count, federation status
- Resource mailboxes, distribution lists, security groups

**Example finding:** _"Hybrid Active Directory detected with 3 federated domains and mail-enabled public folders — this qualifies as a highly complex migration."_

---

## How Findings Map to Scores

Each intelligence finding carries an **impact value** that feeds back into the three scoring dimensions:

| Analyser | Affects |
|----------|---------|
| Identity Attack Surface | Security Risk, Compliance Posture |
| Privileged Access Exposure | Security Risk, Compliance Posture |
| Conditional Access Coverage | Security Risk, Compliance Posture |
| Device Trust | Security Risk, Compliance Posture |
| External Exposure | Security Risk |
| Application Risk | Security Risk |
| Licensing Optimisation | _(advisory only — no score impact)_ |
| Migration Readiness | Migration Complexity |

---

## Prioritised Action Plan

After analysis, findings are sorted by severity and grouped into:

- **Quick Wins** — High-impact, low-effort changes you can make immediately
- **Strategic Items** — Larger projects that need planning and potentially new licensing
- **Monitoring Recommendations** — Ongoing checks to maintain posture

The prioritised action plan is included in all three report formats.
