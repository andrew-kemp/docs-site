# The Framework

The Privileged Path Framework is a five-pillar model for securing privileged access. It is practical, opinionated, and designed to be implemented — not just read.

Each pillar addresses a distinct layer of privileged access risk. The pillars are designed to be implemented in order, but they are not mutually exclusive — work across multiple pillars simultaneously where resources allow.

---

## Pillar 1 — Foundation

**Identity, governance, and baseline hygiene**

The Foundation pillar covers the prerequisites for everything else. Without clean identity hygiene and basic governance, controls built on top are unreliable.

### What Foundation Covers

- **Identity separation** — Admin accounts are separate from user accounts. No shared credentials. No hybrid admin/user accounts.
- **Cloud-only admin identities** — Privileged accounts are cloud-only where possible, removing dependency on on-premises identity infrastructure for Tier 0 administration.
- **Account lifecycle governance** — Stale admin accounts are identified and removed. Joiners, movers, and leavers processes include privileged account handling.
- **Naming and visibility** — Admin accounts follow a consistent naming convention and are visible in identity governance tooling.
- **Licence and entitlement hygiene** — Privileged accounts are not assigned user-facing licences (E3, E5) that expand their attack surface unnecessarily.

### Foundation Maturity Indicators

| Level | Description |
|---|---|
| **Initial** | Admin accounts share credentials with user accounts or are untracked |
| **Developing** | Admin accounts are separate but governance is informal |
| **Defined** | Formal process for admin account creation, review, and removal |
| **Managed** | Automated lifecycle management with regular access reviews |
| **Optimised** | Continuous governance with identity risk scoring and anomaly detection |

---

## Pillar 2 — Control

**Just-in-time access, approval workflows, and policy enforcement**

The Control pillar governs how and when privileged access is activated. The goal is to eliminate standing access — the persistent assignment of powerful roles that exist whether or not they are being used.

### What Control Covers

- **Privileged Identity Management (PIM)** — Eligible role assignments replace permanent assignments. Roles are activated on demand for a defined window.
- **Approval workflows** — High-impact role activations require approval from a second party before access is granted.
- **Justification and audit trail** — Every activation requires a business justification that is logged and reviewable.
- **Just-in-time (JIT) access** — Access exists only for the duration of a defined task, then automatically expires.
- **Conditional Access enforcement** — Admin sign-ins are subject to strict Conditional Access policies — phishing-resistant MFA, compliant device requirements, named locations.
- **Access reviews** — Regular, scheduled reviews of privileged role assignments to confirm continued necessity.

### Control Maturity Indicators

| Level | Description |
|---|---|
| **Initial** | Permanent role assignments, no activation workflow |
| **Developing** | PIM deployed but not consistently enforced |
| **Defined** | PIM with approval workflows for critical roles |
| **Managed** | Full JIT model with Conditional Access and regular access reviews |
| **Optimised** | Risk-adaptive access controls with continuous access evaluation |

---

## Pillar 3 — Isolation

**PAWs, tiering, network segmentation, and boundary enforcement**

The Isolation pillar addresses the execution environment — where privileged work actually happens. Identity controls alone are insufficient if privileged sessions run on compromised or unmanaged devices connected to flat networks.

### What Isolation Covers

- **Privileged Access Workstations (PAWs)** — Dedicated devices or environments used exclusively for privileged administration. No email, web browsing, or productivity tools on PAW environments.
- **Tiering model** — Administration of Tier 0 (identity infrastructure), Tier 1 (servers and services), and Tier 2 (user devices and data) is performed from appropriately isolated environments.
- **Device compliance enforcement** — Conditional Access policies block privileged sign-ins from non-compliant or unmanaged devices.
- **Network segmentation** — Admin traffic is isolated from user traffic. Privileged management interfaces (Azure Portal, M365 Admin Center, domain controllers) are accessible only from defined admin network segments.
- **Outbound restriction on PAWs** — PAW environments restrict outbound internet access. Admin tools are the only permitted use case.

### PAW Deployment Options

| Option | Isolation Level | Best For |
|---|---|---|
| **Physical PAW** | Highest | Tier 0 administration, highest security environments |
| **Virtual PAW** | High | Organisations with existing virtualisation capability |
| **Windows 365 PAW** | High | Cloud-first organisations, distributed admin teams |
| **AVD PAW** | High | Scalable, session-based privileged access |

[Read the full PAW documentation →](paw.md)

### Isolation Maturity Indicators

| Level | Description |
|---|---|
| **Initial** | Admin tasks performed from standard user devices |
| **Developing** | Some device compliance controls, no dedicated admin environments |
| **Defined** | PAW programme initiated for Tier 0 |
| **Managed** | Full PAW coverage with device compliance enforcement and network segmentation |
| **Optimised** | Continuous device health validation, session isolation, and boundary monitoring |

---

## Pillar 4 — Operations

**Secure admin processes, break glass design, and operational discipline**

The Operations pillar governs how privileged access is used in practice — the processes, procedures, and operational habits that determine whether controls work under real-world conditions.

### What Operations Covers

- **Break glass accounts** — Emergency access accounts that bypass normal controls. Must be cloud-only, excluded from Conditional Access, stored offline, monitored for any sign-in, and tested regularly.
- **Admin operational procedures** — Documented and followed processes for common privileged tasks. Prevents ad-hoc admin work from bypassing controls.
- **Change management for privileged access** — Modifications to privileged role assignments, PAW configurations, or Conditional Access policies go through a defined approval process.
- **Vendor and third-party access** — External access to privileged systems is time-limited, monitored, and subject to the same controls as internal admin accounts.
- **Security awareness for administrators** — Admins understand the elevated risk of their accounts and the operational discipline required.

### Break Glass Account Requirements

!!! warning "Break Glass is a Critical Control"
    Break glass accounts are your last line of defence. Most organisations get them wrong — accounts that are never tested, stored insecurely, or excluded from monitoring.

| Requirement | Detail |
|---|---|
| **Cloud-only** | Not synchronised from on-premises AD |
| **Excluded from Conditional Access** | Must work when CA policies fail |
| **Phishing-resistant MFA** | FIDO2 key stored separately from account credentials |
| **Offline storage** | Credentials stored physically, not in password managers |
| **Monitored** | Any sign-in generates an immediate alert |
| **Tested** | Sign-in tested regularly (at least quarterly) to confirm access still works |
| **Minimal use** | Used only when all other admin access has failed |

### Operations Maturity Indicators

| Level | Description |
|---|---|
| **Initial** | No documented admin procedures, break glass untested |
| **Developing** | Break glass accounts exist but are not monitored or tested |
| **Defined** | Documented procedures, break glass configured and monitored |
| **Managed** | Regular operational reviews, tested break glass, vendor access controls |
| **Optimised** | Continuous operational assurance with simulation testing |

---

## Pillar 5 — Validation

**Continuous monitoring, audit, and evidence-based assurance**

The Validation pillar ensures that controls are working as intended and that privileged activity can be detected, investigated, and evidenced.

### What Validation Covers

- **Unified audit logging** — All privileged operations are captured in the Microsoft 365 Unified Audit Log with sufficient retention for investigation.
- **Privileged Identity Management audit trail** — PIM activation, approval, and denial events are logged and retained.
- **Alerting on high-risk activity** — Automated alerts fire on Global Admin sign-ins, PIM activations outside business hours, break glass account sign-ins, and bulk privilege changes.
- **SIEM integration** — Privileged access events are ingested into Microsoft Sentinel or equivalent for correlation and investigation.
- **Regular privileged access reviews** — Scheduled reviews of role assignments, PAW device health, Conditional Access policy effectiveness, and break glass account status.
- **Evidence-based reporting** — Privileged access posture can be evidenced to auditors, regulators, and internal governance bodies.

### Validation Maturity Indicators

| Level | Description |
|---|---|
| **Initial** | No consistent audit logging or alerting |
| **Developing** | Audit log enabled but not reviewed or retained adequately |
| **Defined** | Alerting on key events, regular manual review |
| **Managed** | SIEM integration, automated response, scheduled access reviews |
| **Optimised** | Continuous monitoring with risk-adaptive controls and evidence-based assurance |

---

## Maturity Model Summary

The framework uses a five-level maturity model consistent across all pillars:

| Level | Description |
|---|---|
| **1 — Initial** | Ad-hoc, undocumented, inconsistent |
| **2 — Developing** | Some controls present but not consistently applied |
| **3 — Defined** | Formal controls documented and consistently applied |
| **4 — Managed** | Controls measured, reviewed, and improved on a schedule |
| **5 — Optimised** | Continuous improvement with risk-adaptive, evidence-based assurance |

Use the [Quick Assessment](quick-assess.md) to determine your current maturity level across each pillar.

---

[:material-arrow-right: Run the Quick Assessment](https://paw.andykemp.com/quickassess){ .md-button .md-button--primary }
[:material-web: Full Framework at paw.andykemp.com](https://paw.andykemp.com/framework/){ .md-button }
