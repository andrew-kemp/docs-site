# Privileged Access Quick Assessment

A free, interactive assessment that scores your privileged access posture across six control areas and produces a practical scorecard with targeted next steps.

[:material-arrow-right: Start the Assessment](https://paw.andykemp.com/quickassess){ .md-button .md-button--primary }

---

## What It Assesses

The Quick Assessment covers 29 questions across six domains. Each domain maps to a specific control area within the [Privileged Path Framework](framework.md).

### 1. Identity — 5 questions

Assesses how privileged identities are separated, constrained, and kept out of standard user workflows.

Key areas examined:

- Separation of admin accounts from user accounts
- Cloud-only or hybrid admin identity design
- Admin account naming and visibility conventions
- Privileged account lifecycle management
- Identity governance controls for admin accounts

### 2. Authentication — 5 questions

Measures the strength and consistency of authentication controls protecting privileged access.

Key areas examined:

- Phishing-resistant MFA enforcement for admin accounts
- Authentication method consistency across all privileged roles
- Conditional Access policy coverage for admin sign-ins
- Session lifetime and re-authentication requirements
- Exclusions and bypass paths in authentication policy

### 3. Privilege — 5 questions

Reviews how standing access, role activation, and high-impact privileges are governed.

Key areas examined:

- Use of Privileged Identity Management (PIM) for eligible assignments
- Global Administrator account count and justification
- Standing access vs just-in-time activation model
- Approval workflows and justification requirements
- Regular access reviews for privileged role assignments

### 4. Execution — 4 questions

Tests whether privileged work is carried out in isolated, controlled execution environments.

Key areas examined:

- Use of dedicated Privileged Access Workstations (PAWs)
- Device compliance enforcement for admin sign-ins
- Network segmentation and admin network access controls
- Whether admin tasks are performed from standard user devices

### 5. Capability — 5 questions

Measures how well role design and assignment scope align with least privilege principles.

Key areas examined:

- Use of custom roles vs broad built-in roles
- Scope limitation for privileged role assignments
- Service account privilege design
- Third-party and vendor access controls
- Emergency access (break glass) account design

### 6. Validation — 5 questions

Checks whether privileged access can be monitored, correlated, and investigated with confidence.

Key areas examined:

- Unified audit log coverage for privileged operations
- Alerting on high-risk privileged activity
- Microsoft Sentinel or equivalent SIEM integration
- Privileged Identity Management audit log retention
- Regular review and testing of break glass account access

---

## Assessment Output

On completion, the assessment produces a **scorecard** with:

- An overall privileged access posture score
- A per-domain score and rating for each of the six areas
- Colour-coded risk indicators (Critical / High / Medium / Low)
- Targeted next steps based on your lowest-scoring areas
- A print-friendly report suitable for internal review or saving as PDF

---

## How to Use the Results

The scorecard is designed to drive prioritised action:

| Score Range | Posture | Recommended Action |
|---|---|---|
| **0–40%** | Critical | Immediate remediation required — focus on Foundation and Control pillars first |
| **41–60%** | Poor | Significant gaps — prioritise the lowest-scoring domains |
| **61–75%** | Developing | Core controls present but isolation and validation are typically weak |
| **76–90%** | Good | Strong posture with targeted improvement areas |
| **91–100%** | Strong | Mature privileged access programme — focus on continuous validation |

!!! tip "Use alongside the 30-Day Reset"
    The Quick Assessment pairs well with the [30-Day Privileged Access Reset](https://paw.andykemp.com/downloads/30-day-reset/) — run the assessment first, then use the reset plan to address the gaps in a structured way.

---

## Frequently Asked Questions

**Does the assessment connect to my tenant?**

No. The Quick Assessment is entirely self-reported — it asks questions about your environment and you provide answers. Nothing connects to Microsoft 365, Azure AD, or any external system.

**How long does it take?**

Most assessments complete in 10–15 minutes. There are 29 questions across six sections.

**Can I save my results?**

The results page is print-friendly and can be saved as a PDF directly from your browser (File → Print → Save as PDF).

**Is it free?**

Yes — the Quick Assessment is completely free with no registration required.

**What happens after the assessment?**

The scorecard identifies your weakest areas. From there, use the [framework guidance](framework.md), [PAW documentation](paw.md), and [downloadable resources](https://paw.andykemp.com/downloads/) to drive remediation.

---

[:material-arrow-right: Run the Quick Assessment](https://paw.andykemp.com/quickassess){ .md-button .md-button--primary }
[:material-web: View the Full Framework](https://paw.andykemp.com/framework/){ .md-button }
