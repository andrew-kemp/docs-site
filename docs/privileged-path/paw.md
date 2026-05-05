# Privileged Access Workstations

A Privileged Access Workstation (PAW) is a dedicated, hardened environment used exclusively for privileged administration. It is the primary isolation control within the [Isolation pillar](framework.md#pillar-3--isolation) of the Privileged Path Framework.

---

## What Is a PAW?

A PAW is an environment — physical or virtual — where privileged administrative tasks are performed in isolation from standard user activity. The core principle is simple: **admin tasks and user tasks never share the same execution environment**.

Without PAWs, an administrator who opens a phishing email on their work laptop and then logs into the Azure Portal from the same session is performing privileged work from a potentially compromised device. Identity controls like MFA and PIM cannot compensate for a compromised execution environment.

### What a PAW Is Not

| Misconception | Reality |
|---|---|
| A PAW is a laptop for IT staff | A PAW is a dedicated environment used only for admin work — no email, no browsing |
| Any managed device is a PAW | A managed device with email and productivity apps is not a PAW |
| A PAW requires dedicated hardware | PAWs can be virtual (Windows 365, AVD, Hyper-V VM) |
| PIM replaces the need for a PAW | PIM controls access activation — PAWs control execution environment |

---

## PAW Deployment Options

There are four main approaches to deploying PAWs. The right choice depends on your organisation's size, existing infrastructure, and Tier 0 security requirements.

### Physical PAW

A dedicated physical device used exclusively for privileged administration.

**Characteristics:**

- Highest possible isolation — no hypervisor attack surface
- Dedicated hardware not shared with any other workload
- No email, web browsing, or productivity applications installed
- Network access restricted to admin management interfaces
- Bitlocker, Secure Boot, and TPM required
- Managed via Intune with strict compliance policy

**When to use:**

- Tier 0 administration (Global Admin, Domain Admin, Azure root management)
- Organisations with the highest security requirements (financial services, critical national infrastructure)
- Where hardware budget allows dedicated devices per administrator

**Limitations:**

- Highest cost — requires a dedicated device per admin
- Less flexible for distributed or remote teams

---

### Virtual PAW (Hyper-V / Client VM)

A dedicated virtual machine running on the administrator's standard device, used exclusively for privileged work.

**Characteristics:**

- Host device is used for standard user activity; VM is used only for admin tasks
- VM is isolated from the host — no clipboard sharing, no network bridging
- VM connects to a separate admin network segment via VPN or managed gateway
- Intune manages the host; the VM is separately managed or not licensed for productivity apps

**When to use:**

- Where dedicated hardware per admin is not feasible
- Organisations already running Hyper-V or VMware Workstation
- Supplementing physical PAWs for lower-tier administration

**Limitations:**

- Host compromise can potentially affect VM isolation
- Requires discipline to maintain the separation between host and VM use cases
- More complex to manage and evidence compliance

---

### Windows 365 PAW

A Windows 365 Cloud PC used exclusively for privileged administration, accessed from the administrator's standard device via the Windows 365 client or browser.

**Characteristics:**

- Cloud-native — no local hardware requirement beyond the endpoint used to connect
- Persistent Cloud PC assigned per administrator
- Strict Conditional Access policy on the Cloud PC: phishing-resistant MFA, compliant device
- No productivity apps provisioned — only admin tooling (M365 Admin Center, Azure Portal, PowerShell)
- Intune policy enforces clipboard and file transfer restrictions between host and Cloud PC
- Network access controlled via private endpoints or VNet integration

**When to use:**

- Cloud-first organisations without significant on-premises infrastructure
- Distributed admin teams where physical PAWs are impractical
- Organisations scaling PAW programmes across a large admin population

**Limitations:**

- Dependency on Microsoft infrastructure availability
- Persistent Cloud PC costs (Windows 365 licence per admin)
- Outbound internet from the Cloud PC must be controlled separately

---

### AVD PAW (Azure Virtual Desktop)

A session-based privileged access environment delivered via Azure Virtual Desktop. Administrators connect to a dedicated AVD session host used only for admin work.

**Characteristics:**

- Session-based — no persistent desktop assigned; session ends when admin work is complete
- Shared session host infrastructure (multi-session or dedicated, depending on security requirements)
- Conditional Access enforced on AVD sign-in
- Session hosts are domain-joined or Entra-joined with strict Intune policy
- No persistent local profile — admin tools available via MSIX App Attach or traditional installation
- Network access to admin management interfaces via private endpoints or VNet peering

**When to use:**

- Large admin populations where per-admin persistent Cloud PCs are cost-prohibitive
- Organisations with existing AVD infrastructure
- Where session-based (ephemeral) access is preferred over persistent environments

**Limitations:**

- Multi-session hosts introduce lateral movement risk if not properly hardened
- Session persistence and profile management require careful design
- More complex to deploy and operate than Windows 365

---

## PAW Configuration Requirements

Regardless of deployment model, all PAW environments should meet the following baseline:

### Identity & Access

- [ ] Admin account is cloud-only (not synchronised from on-premises AD)
- [ ] Sign-in requires phishing-resistant MFA (FIDO2 or certificate-based)
- [ ] Conditional Access policy enforces compliant device for admin sign-in
- [ ] PIM used for all privileged role activations from this environment

### Device Hardening

- [ ] No email client installed or accessible
- [ ] No general-purpose web browser (or browser restricted to admin URLs only)
- [ ] No productivity applications (Office, Teams) installed
- [ ] Attack Surface Reduction rules enabled
- [ ] Defender for Endpoint deployed with strict policy
- [ ] Application control (WDAC or AppLocker) restricts execution to approved apps only
- [ ] Outbound internet access blocked or restricted to admin management endpoints

### Network

- [ ] PAW connects to a dedicated admin network segment
- [ ] User network traffic cannot reach admin management interfaces
- [ ] Split tunnelling is disabled or controlled — all traffic routes through managed gateway

### Monitoring

- [ ] All sign-ins from PAW are logged to unified audit log
- [ ] Alerts configured for sign-ins from non-PAW devices to admin roles
- [ ] Device health is checked at sign-in via Conditional Access compliance policy

---

## Common PAW Mistakes

### 1. Using the PAW for email and browsing

The most common mistake. An environment used for privileged work and normal productivity is not a PAW — it is a privileged machine with a large attack surface. Email and web browsing are primary phishing vectors.

### 2. No network restriction on the PAW

A PAW that can browse the internet or reach user resources provides limited isolation. Outbound traffic from PAW environments should be restricted to admin management endpoints.

### 3. Sharing PAW environments

PAWs should be per-administrator. Shared environments mean a compromise of one admin session can affect others.

### 4. Not enforcing PAW use via Conditional Access

Without a Conditional Access policy that requires a compliant PAW device for admin role activation, administrators can bypass the PAW entirely and log in from a standard device. The PAW only provides security if it is the only permitted path to privileged access.

### 5. PAW deployed but PIM not used

A PAW without PIM means standing access is still present. The PAW controls the execution environment — PIM controls when and how access is activated. Both are required.

### 6. PAW never tested after deployment

PAW configurations drift. Intune policies change. Conditional Access gets modified. Without regular testing — attempting to sign in to privileged roles from non-PAW devices and confirming access is blocked — there is no assurance the control is working.

---

## Related Resources

- [Framework — Isolation Pillar](framework.md#pillar-3--isolation) — How PAWs fit into the wider isolation strategy
- [Quick Assessment](quick-assess.md) — Score your current PAW and execution environment posture
- [PAW Deployment Checklist](https://paw.andykemp.com/downloads/paw-deployment-checklist/) — Step-by-step checklist for all four PAW models

[:material-web: PAW Guidance at paw.andykemp.com](https://paw.andykemp.com/paw/){ .md-button }
[:material-arrow-right: Run the Quick Assessment](https://paw.andykemp.com/quickassess){ .md-button .md-button--primary }
