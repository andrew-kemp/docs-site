# The Privileged Path Framework

A practical, opinionated model for securing privileged access in Microsoft environments — covering identity, access, isolation, operations, and continuous validation.

## What It Is

The Privileged Path Framework is a structured approach to securing privileged access across your organisation. It moves beyond point controls like MFA or PIM and treats privileged access as a cohesive discipline — with five interlocking pillars that work together.

The framework is built from real-world implementation experience and maps directly to regulatory guidance from NCSC, NIS2, NIST, ISO 27001, and the CIS Controls.

## Why Most Organisations Are Exposed

Most organisations believe their admin access is secured. In practice, the gaps are significant:

| Common Gap | Why It Matters |
|---|---|
| **Controls without isolation** | PIM, MFA, and Conditional Access are essential — but don't prevent admins working from compromised devices |
| **Paper compliance** | Policies exist but admins still operate from shared, unmanaged endpoints on flat networks |
| **Operational shortcuts** | Break glass accounts never tested, admin exclusions in Conditional Access, missing operational process |
| **Missing boundary enforcement** | Without dedicated admin environments and network segmentation, identity controls alone leave exploitable gaps |

## The Five Pillars

| # | Pillar | Focus |
|---|---|---|
| 1 | **Foundation** | Identity separation, governance, and baseline hygiene |
| 2 | **Control** | Just-in-time access, approval workflows, and policy enforcement |
| 3 | **Isolation** | PAWs, tiering, network segmentation, and boundary enforcement |
| 4 | **Operations** | Secure admin processes, break glass design, and operational discipline |
| 5 | **Validation** | Continuous monitoring, audit, and evidence-based assurance |

[Read the full framework breakdown →](framework.md)

## Tools & Resources

### Quick Assessment

The [Privileged Access Quick Assessment](quick-assess.md) is a free, interactive tool that scores your current privileged access posture across six control areas:

- Identity separation and constraint
- Authentication strength and consistency
- Standing access and privilege governance
- Execution environment isolation
- Role design and least privilege
- Monitoring and investigative capability

[:material-arrow-right: Run the Quick Assessment](https://paw.andykemp.com/quickassess){ .md-button .md-button--primary }

### Privileged Access Workstations

The [PAW section](paw.md) covers Privileged Access Workstations in depth — covering what they are, when each deployment model makes sense, and the most common implementation mistakes.

## Regulatory Alignment

The framework maps to the following regulatory and standards bodies:

| Region | Frameworks |
|---|---|
| **United Kingdom** | NCSC, ICO, FCA, PRA |
| **European Union** | NIS2, GDPR, DORA, ENISA |
| **United States** | NIST, CISA, CMMC, HIPAA, SOX |
| **Global** | ISO 27001, CIS Controls |

## Downloads & Templates

Free resources available at [paw.andykemp.com/downloads](https://paw.andykemp.com/downloads/):

| Resource | Description |
|---|---|
| **Privileged Access Checklist** | Comprehensive checklist across identity, access, isolation, operations, and validation |
| **30-Day Privileged Access Reset** | Structured 30-day plan prioritised by impact |
| **PAW Deployment Checklist** | Step-by-step checklist for physical, virtual, Windows 365, and AVD PAW deployments |
| **Break Glass Review Template** | Template for validating break glass account design, storage, monitoring, and testing |

## Quick Links

- [Quick Assessment](quick-assess.md) — Score your privileged access posture in minutes
- [Framework](framework.md) — The five pillars in detail
- [Privileged Access Workstations](paw.md) — PAW concepts, deployment options, and common mistakes

[:material-web: Visit paw.andykemp.com](https://paw.andykemp.com){ .md-button }
