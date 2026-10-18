# RailSahayak — Stakeholder Submission & Presentation Checklist

**Document Reference:** RS-CHECKLIST-2026-V2.1  
**Project Name:** RailSahayak  
**Purpose:** Pre-submission audit, evidence verification, data security compliance, and stakeholder readiness checklist.  
**Auditor / Engineering Team:** RailSahayak Senior Engineering & Documentation Team  
**Evaluation Date:** October 2026  

---

## 1. Important Legal & Operational Disclaimer

> [!IMPORTANT]
> **No Formal Affiliation or Endorsement:**  
> RailSahayak is an independent engineering software project developed for passenger assistance, academic research, and technical evaluation.  
> **No endorsement, partnership, data agreement, or production integration exists with the Ministry of Railways, Center for Railway Information Systems (CRIS), or Indian Railway Catering and Tourism Corporation (IRCTC) unless formally executed and confirmed in writing.**  
> Under no circumstances should this project be represented as an officially approved railway application or live ticketing channel.

---

## 2. Core Submission Deliverables Inventory

The following core deliverables constitute the complete RailSahayak Enterprise Stakeholder Submission Pack. All files have been generated, verified, and checksum-validated:

| # | Deliverable | File Path | Format & Extent | Byte Size | SHA-256 Checksum | Verification Status |
| :-: | :--- | :--- | :--- | :-: | :--- | :-: |
| **1** | **Executive Presentation (PPTX)** | [`docs/RailSahayak_Stakeholder_Presentation.pptx`](RailSahayak_Stakeholder_Presentation.pptx) | PPTX (12 slides, 16:9 widescreen) | 63,733 B | `700872f209f7ff34f5fca617c2fd824936bfe3ddc702beacb767c217799c69f7` | **Verified** |
| **2** | **Executive Presentation (PDF)** | [`docs/RailSahayak_Stakeholder_Presentation.pdf`](RailSahayak_Stakeholder_Presentation.pdf) | PDF (12 pages, 16:9 widescreen) | 30,621 B | `2862f43d3b4ba9d635910de31c3aecea7d7814def5397ee24fe5dffb25cc2d61` | **Verified** |
| **3** | **Stakeholder Proposal (Word)** | [`docs/RailSahayak_Stakeholder_Proposal.docx`](RailSahayak_Stakeholder_Proposal.docx) | DOCX (20 sections, A4) | 63,434 B | `2e96fd8b28243c44f07492b4982d74de0a295e623d9444e08af934a3ddd7fe21` | **Verified** |
| **4** | **Stakeholder Proposal (PDF)** | [`docs/RailSahayak_Stakeholder_Proposal.pdf`](RailSahayak_Stakeholder_Proposal.pdf) | PDF (20 pages, 20 sections) | 57,230 B | `718225bcc0b26a497b3586f94e8bf4aee9bc05de17892f48403eed47e8153f19` | **Verified** |
| **5** | **Presentation Notes & Pitch Guide** | [`docs/PRESENTATION_NOTES.md`](PRESENTATION_NOTES.md) | Markdown (12 slides, delivery cues, 7 Q&As) | 28,446 B | `f85ddd28fb75382cbecdae62449cb964f86bda429a8a34561e3047fed07d619e` | **Verified** |
| **6** | **Submission & Verification Checklist** | [`docs/STAKEHOLDER_SUBMISSION_CHECKLIST.md`](STAKEHOLDER_SUBMISSION_CHECKLIST.md) | Markdown (pre-submission audit & protocols) | Synchronized | See Checklist | **Verified** |
| **7** | **Proposal Evidence Register** | [`docs/PROPOSAL_EVIDENCE_REGISTER.md`](PROPOSAL_EVIDENCE_REGISTER.md) | Markdown (5 tiers, statutory citations, checksums) | Synchronized | See Register | **Verified** |
| **8** | **Final Proposal QA Report** | [`docs/FINAL_PROPOSAL_QA_REPORT.md`](FINAL_PROPOSAL_QA_REPORT.md) | Markdown (authoritative multidisciplinary audit) | Synchronized | Master Release | **Verified** |

### Supporting Repository Documentation & Operational Scripts

| Document / Tool | Location | Purpose & Audience | Readiness Status |
| :--- | :--- | :--- | :--- |
| **Final Readiness Report** | [`docs/FINAL_READINESS_REPORT.md`](FINAL_READINESS_REPORT.md) | Authoritative 8-section audit report with security fixes, test logs, and verdict. | **Ready** |
| **Feature & Integration Matrix** | [`docs/FEATURE_AND_INTEGRATION_MATRIX.md`](FEATURE_AND_INTEGRATION_MATRIX.md) | Exhaustive breakdown of all 14 features, tests, live vs prototype boundaries, and dependencies. | **Ready** |
| **Live Demonstration Script** | [`docs/DEMO_SCRIPT.md`](DEMO_SCRIPT.md) | Step-by-step 5–10 minute live walkthrough guide with actions and expected outcomes. | **Ready** |
| **System README** | [`README.md`](../README.md) | Architecture overview, prerequisites, quickstart, API reference, and security roadmap. | **Ready** |
| **Runtime Verification Script** | [`scripts/verify-runtime.ps1`](../scripts/verify-runtime.ps1) | Automated live health, header, RBAC, API, and branding verification tool. | **Ready** |
| **Local Load Benchmark** | [`scripts/load-test.ps1`](../scripts/load-test.ps1) | Automated performance and latency benchmark suite. | **Ready** |
| **Database Backup & Restore** | [`scripts/backup-db.ps1`](../scripts/backup-db.ps1) / [`scripts/restore-db.ps1`](../scripts/restore-db.ps1) | Idempotent disaster recovery automation for PostgreSQL 16. | **Ready** |

---

## 3. Technical Evidence Package (Attached in Submission)

When preparing an evaluation submission or pitch deck, attach the following verified technical evidence:

- [x] **Full Maven Integration Test Log:**
  - Command: `mvn test` (using Java 24 / Maven 3.10)
  - Result: **Tests run: 29, Failures: 0, Errors: 0, Skipped: 0 (BUILD SUCCESS)**
  - Coverage: Security headers, RBAC 403, 401 unauthorized, input validation, case lifecycle, dual audit persistence, train search, zero-trust payment diagnosis, PNR rules, DoS rate limiting, trusted proxy protection, and error sanitization.
- [x] **Runtime Verification Audit Output:**
  - Script: `scripts/verify-runtime.ps1` executed against `http://localhost:8081/`
  - Result: **8 out of 8 categories passed** (Health, Passenger Auth, Admin Auth, RBAC isolation, Smart Train Finder, Payment Help, PNR Guide, and Clean Branding).
- [x] **Relational Persistence & Migration Proof:**
  - PostgreSQL 16 container with Flyway migrations (`V1__create_tables.sql`, `V2__add_performance_indexes.sql`).
  - Active record counts: **25 support cases, 49 case events, 49 audit records** fully preserved across application restarts.
- [x] **Performance & Latency Benchmark Data:**
  - 240 requests across 8 endpoints with **0.00% error rate**.
  - P50 latency $< 80\text{ ms}$ on local JVM; health check throughput $> 90\text{ req/sec}$.
- [x] **Disaster Recovery Proof:**
  - Verified idempotent backup and restore cycle with zero data loss using `backup-db.ps1` and `restore-db.ps1`.

---

## 4. Presentation & Proposal Structure Alignment

### 12-Slide Executive Presentation Structure
- **Slide 1:** Executive Editorial Cover: Intelligent Railway Passenger Advisory Platform (Platform Identity & Boundaries)
- **Slide 2:** Why RailSahayak Matters: The Passenger Journey Friction Reality (4-stage friction flow)
- **Slide 3:** The Problem, Evidence & Open Questions: Root Causes of Commuter Distress (Problem Validation Matrix)
- **Slide 4:** The RailSahayak Solution: A Pre-Triage Architecture (4 Pillars: Need $\rightarrow$ Advisory $\rightarrow$ Handoff)
- **Slide 5:** See the Product: Verified Working Prototype (4 Live Panels & Execution Commands)
- **Slide 6:** Proof: What Works Today? Verifiable Implementation Evidence (29 Tests, PostgreSQL 16, Automation)
- **Slide 7:** Architecture & System Boundaries: Local Prototype vs Future Enterprise State (6 Layers & Transition)
- **Slide 8:** Security, Risks & Honest Limitations: Defense-in-Depth & Readiness Gaps (Controls vs Gaps)
- **Slide 9:** Complementing Official Services: An Ecosystem Handoff Model (Synergy & 3 Non-Disruption Commitments)
- **Slide 10:** A Realistic Evaluation Plan: Phased Gates & Stop Conditions (5 Stages & Mandatory Stop Conditions)
- **Slide 11:** How Success Would Be Measured: Objective Pilot KPI Framework (KPI Matrix & Measurement Commitment)
- **Slide 12:** The Request: Constructive Dialogue & Collaborative Next Steps (4 Requests & Mandatory Fallback Clause)

### 20-Section Enterprise Proposal Structure
1. Cover Page
2. Document Control, Metadata & Independent Prototype Disclaimer
3. Executive Summary (Strategic Intent & Core Principles)
4. Project Background & Scope Boundaries (Scope Matrix: In-Scope vs Out-of-Scope)
5. Passenger Problem Statement & Evidence Gaps (3 Domains, Validation Matrix, Evidence Qualification)
6. Proposed Solution, Architectural Principles & Target User Personas (5 Personas)
7. Detailed Feature & Workflow Specifications (5 Core Modules, Zero-Trust Defense, Section 138 Advisory)
8. Current Implementation & Verifiable Technical Evidence (Stack, 29/29 tests, DB proof)
9. Current Architecture vs Proposed Future Production Architecture (Comparison Matrix & Decoupled Adapters)
10. Security, Privacy & Data Governance (DPDP Act 2023, RBI TAT, Trusted Proxy Limiting, Sanitized Errors)
11. Existing Railway Systems & Integration Boundaries (IRCTC, CRIS PRS, NTES, RailMadad 139)
12. Proposed Limited Pilot, Staging Prerequisites & Approval Gates (4 Phased Gates)
13. Proposed KPIs, Baseline Requirements & Measurement Governance (7 Prospective Target Metrics)
14. Comprehensive Risk Register & Mitigation Controls (6 Key Operational/Technical Risks)
15. Implementation Roadmap & Estimated Workstreams (24-Week Phased Execution)
16. Operational Readiness, Incident Response, Backup Automation & 60-Second Rollback Protocol
17. Assumptions, External Dependencies & Current Prototype Limitations
18. Specific Stakeholder Requests, Mentorship & Next Steps (including Verbatim Fallback Proposal Clause)
19. Authoritative Official Source & Regulatory Citation Register (8 Regulatory Citations)
20. Technical Evidence Appendix (Integration Test Suite Log, PostgreSQL Schema DDL, REST API Specs)

---

## 5. Security, Credential & Data Protection Checklist

Review this checklist before every demonstration or code distribution to ensure no sensitive credentials or private passenger data are exposed:

- [x] **Zero Hardcoded Production Credentials:**
  - In-memory demo credentials are strictly externalized to environment variables (`DEMO_PASSENGER_PASSWORD`, `DEMO_ADMIN_PASSWORD`).
  - Safe local fallbacks exist for development only, triggering high-visibility startup warning logs.
  - No database passwords, JWT private keys, or API tokens are hardcoded in Java classes or configuration files.
- [x] **Version Control Cleanliness (`.gitignore`):**
  - `.gitignore` explicitly excludes `backups/`, `*.sql`, `*.dump`, `*.log`, and all `.env*` files.
  - Verified that local database dumps containing synthetic support cases are not committed.
- [x] **Zero Personal Passenger Data:**
  - All support cases, references, and timeline events in the database use synthetic sample data (`passenger`, `admin`, generic station names, simulated issues).
  - No real passenger names, personal phone numbers, Aadhaar numbers, or valid ticket PNRs exist in the repository.
- [x] **Zero-Trust Sensitive Payment Masking & Rejection:**
  - Payment references are strictly masked (`UPI****654`) in API responses and database records.
  - Input validator actively detects and rejects credit/debit card numbers (13–19 digits), CVVs, PINs, OTPs, and passwords with HTTP 400 Bad Request.
- [x] **Rate Limiting & Anti-Spoofing Protection:**
  - `RateLimitingFilter` defaults `trust-forwarded-for` to `false`.
  - When enabled, only accepts forwarded IP headers from an explicitly configured `trusted-proxies` whitelist.
  - Malformed or oversized forwarded headers safely fall back to the direct socket IP address.

---

## 6. Official Submission Channel Protocols

To maintain professional credibility and comply with government communication standards:

1. **Use Only Official Application Channels:**
   - Submit materials strictly through recognized, published government channels (e.g., official innovation challenge portals, verified institutional email addresses of nominated challenge coordinators, or formal university-sponsored liaison channels).
   - Never send unsolicited proposal attachments or cold emails to personal staff addresses found online.
2. **Verify Submission Requirements in Real Time:**
   - Check the active portal or program terms directly on the official host website on the day of submission.
   - Do not rely on assumed deadlines, expired challenge rules, or third-party blog summaries.
3. **Preserve Prototype Identity:**
   - Clearly state in cover letters and submission abstracts that RailSahayak is a **functional software engineering prototype** with clear operating boundaries and zero live integration with CRIS/IRCTC master databases.
   - Never claim existing pilot authorization or nationwide scale.

---

## 7. Comprehensive Source Reference Verification

The following table documents all official regulatory, legal, and operational references incorporated into RailSahayak's procedural guidance, verified against authoritative sources:

| # | Rule / Assertion in RailSahayak | Authoritative Source Document | Verification Date | Canonical URL Checked | Verification Status & Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | **Dropped Waitlisted E-Tickets & Section 138**<br>Fully waitlisted e-tickets that do not confirm upon chart preparation are automatically cancelled; travelling in reserved coaches on a dropped waitlisted e-ticket is illegal. | Ministry of Railways Commercial Circular No. 64 of 2015;<br>IRCTC E-Ticketing Terms & Conditions;<br>The Railways Act, 1989 (Section 138: Levy of excess charge for travelling without proper pass or ticket). | 2026-10-18 | [https://www.irctc.co.in/nget/enquiry/terms-and-conditions](https://www.irctc.co.in/nget/enquiry/terms-and-conditions)<br>[https://indianrailways.gov.in/](https://indianrailways.gov.in/) | **VERIFIED FACT**<br>Confirmed in official IRCTC terms and Indian Railways Commercial rules. Section 138 applies because a dropped e-ticket is invalid for travel. |
| **2** | **Reservation Chart Preparation Timelines**<br>1st chart prepared ~4 hours before departure (or by 20:00 previous evening for morning departures); 2nd chart prepared 30 to 50 minutes before departure for last-minute allocations. | Ministry of Railways Press Release (PIB Delhi, Nov 2015: "Preparation of Reservation Charts");<br>Indian Railways Commercial Manual. | 2026-10-18 | [https://pib.gov.in/newsite/PrintRelease.aspx?relid=130424](https://pib.gov.in/newsite/PrintRelease.aspx?relid=130424)<br>[https://www.indianrail.gov.in/](https://www.indianrail.gov.in/) | **VERIFIED FACT**<br>Established nationwide policy introduced by Railway Board in November 2015 to streamline berth allocation and enable second charting. |
| **3** | **RAC Entitlement & Boarding Rights**<br>RAC (Reservation Against Cancellation) passengers possess legal entitlement to board the train with shared sitting accommodation (side-lower berth) and automatically upgrade to full berth on cancellations. | Indian Railways Passenger Coaching Tariff & Commercial Rules;<br>Indian Railways Official Passenger Information Manual. | 2026-10-18 | [https://www.indianrail.gov.in/enquiry/StaticPages/StaticEnquiry.jsp?StaticPage=index.html](https://www.indianrail.gov.in/enquiry/StaticPages/StaticEnquiry.jsp?StaticPage=index.html) | **VERIFIED FACT**<br>RAC provides confirmed travel authorization with sitting accommodation; distinguished from waitlisted tickets which grant no boarding entitlement. |
| **4** | **Failed Transaction Auto-Reversal (TAT)**<br>Failed online payment transactions are subject to auto-reversal; typical banking settlement cycles take 3 to 7 working days depending on payment channel and acquiring switch. | Reserve Bank of India (RBI) Circular RBI/2019-20/67 (DPSS.CO.PD No.629/02.01.014/2019-20): "Harmonisation of Turn Around Time (TAT) and customer compensation for failed transactions using authorised Payment Systems". | 2026-10-18 | [https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11693&Mode=0](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11693&Mode=0) | **VERIFIED REGULATORY STANDARD**<br>RBI mandate establishes T+1 to T+5 turnaround frameworks for failed merchant transactions. RailSahayak explicitly provides typical ranges without guaranteeing fixed outcomes. |
| **5** | **Grievance Redressal & Helpline 139**<br>RailMadad is the official integrated grievance redressal portal and app; active on-train passengers requiring urgent physical intervention should contact Helpline 139. | Ministry of Railways Press Information Bureau; RailMadad Operational Framework. | 2026-10-18 | [https://railmadad.indianrailways.gov.in/](https://railmadad.indianrailways.gov.in/) | **VERIFIED FACT**<br>RailMadad consolidates passenger complaints, clean-train requests, and medical emergencies across all railway zones. |
| **6** | **First-Digit PNR PRS Zone Routing**<br>First digit of 10-digit PNR historically designates regional PRS zone server (1: CR/CRIS, 2-3: NR, 4-5: WR, 6-7: SR, 8-9: ER). | Indian Railways Passenger Reservation System (PRS) Networking Architecture Convention. | 2026-10-18 | [https://www.indianrail.gov.in/enquiry/PNR/PnrEnquiry.html](https://www.indianrail.gov.in/enquiry/PNR/PnrEnquiry.html) | **HEURISTIC / ROUTING CONVENTION (CAUTION)**<br>⚠️ *Note:* While historically grounded in PRS regional partitioning, modern CRIS infrastructure utilizes centralized data center virtualization and dynamic routing. RailSahayak **strictly and explicitly labels this as an offline heuristic routing convention**, and never presents it as a live PRS lookup. |

---

## 8. Final Pre-Submission Sign-Off Checklist

Before presenting or packaging RailSahayak:

- [x] Product name is strictly **RailSahayak** everywhere (zero occurrences of legacy or modified names).
- [x] No demo passwords, API keys, or private passenger details are present in slides, proposal documents, or submission files.
- [x] All 29 automated integration tests run green (`BUILD SUCCESS`).
- [x] Runtime probe passes 8 out of 8 checks on `http://localhost:8081/`.
- [x] Database records in PostgreSQL 16 (25 cases, 49 events, 49 audit records) are intact and persistent.
- [x] Boundary disclaimers are prominent on Smart Train Finder, Payment Help, and PNR Guide.
- [x] Pilot KPIs are clearly designated as **proposed prospective evaluation targets**, not achieved metrics.
- [x] No live CRIS/NTES/IRCTC integration or nationwide Tatkal capacity is claimed.
- [x] Clear statement included that no formal railway partnership exists unless formally confirmed in writing.
- [x] All primary deliverables and supporting documentation are complete, synchronized, and archived.
