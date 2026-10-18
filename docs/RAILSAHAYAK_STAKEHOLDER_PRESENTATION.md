# RailSahayak — Railway Stakeholder Presentation Pack

**Document Reference:** RS-PRES-2026-V1  
**Project Name:** RailSahayak  
**Subtitle:** Intelligent Railway Passenger Assistance & Complaint Resolution Platform  
**Target Audience:** Ministry of Railways, Center for Railway Information Systems (CRIS), IRCTC Technical Leadership, Innovation & Hackathon Juries  
**Date:** October 2026  
**Auditor / Presenter:** RailSahayak Engineering Team  

---

## Slide 1: Title & Project Overview

```
========================================================================================
                                      RAILSAHAYAK
             Intelligent Railway Passenger Assistance & Complaint Resolution
========================================================================================
```

### Executive Summary
- **What is RailSahayak?** A lightweight, secure, and intelligent passenger assistance web platform engineered to eliminate friction in the Indian Railways passenger journey.
- **Role in Railway Ecosystem:** Operates strictly as a **first-line advisory and guidance terminal**. It complements—rather than replaces—core transaction systems (CRIS PRS, IRCTC E-Ticketing, and RailMadad).
- **Core Value Proposition:**
  1. Instant, structured diagnostic advice for failed and deducted payments, preventing panic repeat bookings.
  2. Clear, bilingual explanations of complex reservation rules (RAC entitlements, waitlist priority codes, and Section 138 charting rules).
  3. Transparent, auditable passenger support ticketing with real-time operational status updates.
  4. Zero load on live railway reservation engines; directs all live ticketing and emergency grievances to official government channels.

---

## Slide 2: Passenger Problems Being Targeted

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        INDIAN RAILWAYS PASSENGER JOURNEY FRICTION                      │
├──────────────────────────┬─────────────────────────────┬───────────────────────────────┤
│    Payment Uncertainty   │    Regulatory Complexity    │    Support Fragmentation      │
├──────────────────────────┼─────────────────────────────┼───────────────────────────────┤
│ • Money deducted during  │ • Confusion between GNWL,   │ • Casual passengers unsure    │
│   Tatkal peak windows    │   RLWL, PQWL, and TQWL      │   whether to call bank,       │
│ • Panic duplicate book-  │ • Misunderstanding RAC      │   IRCTC, or RailMadad         │
│   ings & bank disputes   │   rights vs full waitlist   │ • Lack of visibility into     │
│ • Unclear auto-reversal  │ • Chart preparation rules   │   ticket investigation        │
│   settlement timelines   │   (4h vs 30m 2nd chart)     │   status and resolution notes │
└──────────────────────────┴─────────────────────────────┴───────────────────────────────┘
```

1. **Payment Distress:** High transaction volume during peak booking windows can lead to payment gateway drop-offs. Passengers whose accounts are debited often make duplicate bookings out of anxiety or file premature chargebacks.
2. **Reservation Rule Ambiguity:** Many travelers are unaware that traveling on a dropped waitlisted e-ticket in reserved coaches constitutes ticketless travel under Section 138 of the Railways Act, 1989, or that RAC provides legal boarding rights with shared seating.
3. **Grievance Inaccessibility:** Non-emergency inquiries (refund follow-ups, station amenities, general policy questions) frequently clutter emergency helplines like 139 and RailMadad desks.

---

## Slide 3: RailSahayak's Proposed Solution

```
[ Passenger Inquiries ] ──► [ RailSahayak Advisory Layer ]
                                   │
         ┌─────────────────────────┼─────────────────────────┐
         ▼                         ▼                         ▼
  [ Payment Diagnoser ]   [ PNR & Rules Guide ]    [ Support Case Engine ]
  • Heuristic checklist   • Heuristic PRS zone     • Trackable RS-XXXXXX ID
  • RBI TAT alignment     • RAC & WL explanation   • Chronological timeline
  • Secret rejection      • Official channel links • Tamper-evident audit
         │                         │                         │
         └─────────────────────────┼─────────────────────────┘
                                   ▼
              [ Official Indian Railways Portals ]
              • Bookings: irctc.co.in
              • Live PNR: indianrail.gov.in
              • Emergency Help: RailMadad 139
```

- **Defensive Self-Service:** Provides passengers with immediate structured guidance before frustration leads to redundant bookings or escalated disputes.
- **Zero-Trust Information Model:** RailSahayak never handles banking credentials, never stores unmasked payment references, and never claims to execute live bookings or direct financial debits.
- **Clean Handoff:** Clearly delineates general guidance from live railway operations, directing travelers to official railway endpoints for live verification.

---

## Slide 4: Current Working Prototype & Interface Walkthrough

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  RAILSAHAYAK — Web Interface Architecture                                              │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  [ Header Bar: RailSahayak Brand | Bilingual Switch (EN / HI) | Role-Based Sign In ]   │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  [ Navigation Tabs: Train Finder | Payment Help | PNR Guide | File Case | Admin ]      │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  • Smart Train Finder: Form (From/To/Date/Class) -> Sample Train Cards + IRCTC Link    │
│  • Payment Help: Issue Selector + Method -> Instant Diagnostic Steps + Reversal Range  │
│  • PNR Guide: 10-digit Input -> Heuristic PRS Zone + Boarding Eligibility + Chart Rule │
│  • Complaint Wizard: Category + Description -> RS-XXXXXX Confirmation + Timeline Modal │
│  • Admin Console: Metrics Dashboard + Case Queue + Status Update Modal + Audit Table   │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

- **Technology Stack:** Single-Page Web Application (HTML5, responsive CSS3, modular JavaScript) served by Spring Boot 3.4.5 (Java 24) with PostgreSQL 16 relational persistence.
- **Strict Role-Based UI Rendering:** UI elements dynamically adapt based on server-verified session roles (`/api/v1/auth/me`). The administrative console remains completely hidden from passengers.
- **Bilingual Accessibility:** Instant toggle between English and Hindi for all diagnostic advice and reservation explanations.

---

## Slide 5: Passenger Complaint Workflow & Admin Audit Trail

```
[ Passenger Submits Case ] ──► Assigned ID: RS-F4273733 (Status: OPEN)
                                        │
                                        ▼
                  [ Atomically Recorded in PostgreSQL 16 ]
                  ├── support_cases: Primary case record
                  └── case_events: Event type CASE_CREATED (Actor: passenger)
                                        │
                                        ▼
[ Admin Reviews in Console ] ──► Selects Case -> Opens Status Modal
                                        │
                                        ▼
[ Admin Updates Status ] ────► New Status: IN_PROGRESS
                               Investigation Note: "Verified refund queued with bank PG"
                                        │
                                        ▼
                  [ Dual-Persistence Atomic Transaction ]
                  ├── case_events: STATUS_CHANGED (Visible in Passenger Timeline)
                  └── audit_logs: Server-Side Audit Entry (Actor, Note, Correlation ID)
```

- **Passenger Timeline Modal:** Passengers inspect a chronological event log of their case, viewing exactly when it was created, reviewed, and updated.
- **Administrative Accountability:** Operators cannot update case status without a transaction boundary; all status transitions record the actor, timestamp in `Asia/Kolkata` timezone, and investigation notes.
- **Verified Persistence:** 25 cases, 49 timeline events, and 49 audit records verified persistent in local PostgreSQL database across restarts.

---

## Slide 6: Core Modules & Explicit Prototype Limitations

| Module | Implemented Capabilities | Explicit Prototype Limitations (Boundaries) |
| :--- | :--- | :--- |
| **Smart Train Finder** | • Input validation (source, destination, date, class).<br>• Blocks identical source/destination.<br>• Deterministic sample schedules on trunk corridors.<br>• Direct links to official IRCTC booking portal. | • **Not connected to live CRIS/NTES seat inventory**.<br>• Seat availability numbers are simulated sample data.<br>• Does not calculate live dynamic fares or train delays.<br>• All bookings must occur on [irctc.co.in](https://www.irctc.co.in/). |
| **Payment Help Diagnoser** | • Evaluates issue codes (`deducted`, `pending`, `failed`).<br>• Masks payment reference (`UPI****654`).<br>• Actively rejects card PANs, PINs, OTPs, CVVs.<br>• References RBI TAT framework (RBI/2019-20/67). | • **Does not query banking switches or initiate refunds**.<br>• Settlement timelines (3–7 bank working days) are typical ranges, not guarantees.<br>• Cannot resolve bank chargeback disputes directly. |
| **PNR Guide Explainer** | • Validates 10-digit numeric format.<br>• Identifies originating PRS server routing cluster.<br>• Explains status codes (CNF, RAC, GNWL, RLWL, etc.).<br>• Outlines charting rules and Section 138 waitlist law. | • **Does not query live CRIS PRS databases**.<br>• PRS server zone is an **offline heuristic routing convention**, not a live query.<br>• Does not display personal passenger names or berth allocations. |

---

## Slide 7: Architecture & Security Safeguards

```
[ Client Browser ]
        │
        ▼ (HTTP / Port 8081; TLS 1.3 / HTTPS via Reverse Proxy in Production)
[ Spring Security Filter Chain ]
        ├── Security Headers: nosniff | SAMEORIGIN | Strict-Referrer
        ├── CorrelationIdFilter: Assigns / Propagates X-Correlation-ID (MDC Tracing)
        ├── RateLimitingFilter: 300 req/min/IP Sliding Window (Trusted-Proxy Whitelist)
        └── Custom JSON 401/403 Authentication Entry Points
        │
        ▼
[ REST Controllers & Validation Layer ]
        ├── Strict DTO Bean Validation (@NotBlank, @Pattern, Regex)
        ├── Zero-Trust Secret Filter (Blocks Card Numbers, CVVs, OTPs, Passwords)
        └── GlobalExceptionHandler (Sanitized JSON responses; zero stack trace leakage)
        │
        ▼
[ Spring Data JPA & PostgreSQL 16 Persistence ]
        ├── Flyway Versioned Migrations (V1 Tables, V2 Performance B-Tree Indexes)
        └── Atomic Multi-Entity Transactions (support_cases + case_events + audit_logs)
```

- **Automated Verification:** 29 automated integration tests executing with 100% pass rate.
- **IP Spoofing Defense:** `RateLimitingFilter` defaults `trust-forwarded-for` to `false` and validates client socket IPs against a trusted proxy whitelist before inspecting forwarded headers.
- **Disaster Recovery Automation:** Idempotent backup and restore scripts (`backup-db.ps1`, `restore-db.ps1`) verified functional against PostgreSQL 16.

---

## Slide 8: Relationship with Existing Railway Services

RailSahayak is engineered to **strengthen and protect** existing railway systems, not compete with them:

| Existing System | Managing Authority | Traditional Challenge | RailSahayak Complementary Role |
| :--- | :--- | :--- | :--- |
| **IRCTC E-Ticketing** | IRCTC | High volume of payment status and refund inquiries during peak Tatkal booking hours. | Filters and deflects pre-complaint payment questions; educates users on auto-reversal cycles; routes ready travelers directly to IRCTC. |
| **CRIS PRS** | CRIS | High query loads from third-party scrapers checking static PNR rules and waitlist codes. | Offloads procedural education (explaining RAC, GNWL, RLWL, charting rules) locally without querying master reservation databases. |
| **NTES** | CRIS | Casual users checking station connectivity and general train availability. | Provides station route planning guidance and directs travelers to official NTES live running status. |
| **RailMadad** | Ministry of Railways | Emergency grievance desks burdened by routine informational inquiries and payment status questions. | Resolves informational questions locally; clearly directs active train travelers with urgent on-board grievances to Helpline 139 / RailMadad. |

---

## Slide 9: Phased Limited Pilot Proposal

```
┌───────────────────────────────────┐
│     Phase 1: Staging & Audit      │  • Deploy in railway-controlled staging environment
│          (Weeks 1 - 4)            │  • Third-party CERT-In empaneled VAPT security audit
└─────────────────┬─────────────────┘  • Non-production CRIS testbed API connectivity
                  │
                  ▼
┌───────────────────────────────────┐
│     Phase 2: Zonal Beta Pilot     │  • Limited deployment for 1 division (e.g. NR / Delhi)
│          (Weeks 5 - 12)           │  • Non-emergency booking inquiry link on IRCTC help tab
└─────────────────┬─────────────────┘  • Bi-directional webhook bridge to zonal RailMadad
                  │
                  ▼
┌───────────────────────────────────┐
│     Phase 3: Impact Evaluation    │  • Independent audit of pilot KPIs vs baseline
│          (Weeks 13 - 16)          │  • Joint review with Railway Board, CRIS, and IRCTC
└───────────────────────────────────┘  • Formal production rollout roadmap or graceful rollback
```

### Necessary Formal Authorizations Required for Pilot
1. **CRIS Data Access MoU:** Authorized read-only REST API access to staging/mock PNR and timetable feeds.
2. **RailMadad Webhook Authorization:** Secure API bridge allowing escalated complaints to create tickets in RailMadad CRM.
3. **IRCTC Single Sign-On (SSO):** Technical approval to authenticate passengers via IRCTC OAuth2/OIDC.

---

## Slide 10: Pilot KPIs, Evaluation Method & Rollback Criteria

> [!NOTE]
> **Proposed Pilot Evaluation Targets:** The following metrics represent **proposed evaluation targets** to be measured during an authorized pilot, rather than pre-existing production results.

| Metric | Proposed Pilot Target | Evaluation & Measurement Method |
| :--- | :--- | :--- |
| **Diagnostic Advisory Latency** | $< 150\text{ ms}$ (P95) | Server-side Prometheus/MDC telemetry on `/api/v1/payment-help/diagnose` and `/api/v1/pnr-guide/explain`. |
| **Payment Issue Self-Resolution** | $> 70\%$ resolved | Percentage of diagnosed passengers who confirm understanding without opening an IRCTC support ticket. |
| **Duplicate Booking Prevention** | $> 85\%$ reduction | Self-reported post-diagnostic survey ("Did this prevent a repeat booking attempt?"). |
| **Grievance Audit Traceability** | $100\%$ compliance | Automated audit verifying every case status update contains an associated audit log entry and correlation ID. |
| **Service Availability** | $\ge 99.95\%$ uptime | Synthetic probes pinging `/api/v1/health` at 10-second intervals from external monitoring nodes. |
| **HTTP 5xx Error Rate** | $< 0.05\%$ of total | Continuous log parsing of sanitized error responses. |

### Clear Rollback Criteria
- If unhandled error rates exceed $0.5\%$ over a rolling 1-hour window, or if data discrepancy is reported with CRIS PRS records, traffic can be diverted back to standard static help pages within **60 seconds** via DNS/reverse proxy reconfiguration without data loss.

---

## Slide 11: Risks, Dependencies & Production-Readiness Gaps

| Area | Current Working Prototype State | Production Requirement / Gap | Risk Mitigation Roadmap |
| :--- | :--- | :--- | :--- |
| **Identity & Authentication** | In-memory demo credentials externalized to environment variables. | Database-backed users with Argon2id hashing or IRCTC/Parichay OAuth2 SSO. | Implement JPA `users` entity and token-based JWT sessions; enforce admin TOTP MFA. |
| **Rate Limiting** | Single-node in-memory sliding window (300 req/min/IP). | Multi-node distributed rate limiting across horizontal pods. | Migrate in-memory sliding window to Redis Lua token-bucket cluster. |
| **Transport Security** | Local HTTP on port 8081 for development. | TLS 1.3 encryption with HSTS and SSL pinning. | Terminate TLS at enterprise reverse proxy (NGINX/Cloudflare/ALB). |
| **Live Railway Feeds** | Heuristic PRS zone mapping and deterministic sample train schedules. | Authorized read-only CRIS/NTES API integration. | Operate with strict prototype disclaimer badges until formal CRIS MoU is executed. |
| **Compliance Certification** | Automated test suite and internal security hardening. | Formal CERT-In VAPT audit and DPDP Act 2023 compliance signoff. | Complete independent security assessment prior to public beta rollout. |

---

## Slide 12: Specific Request for Technical Feedback & Next Steps

```
========================================================================================
                          REQUEST FOR TECHNICAL DIALOGUE & GUIDANCE
========================================================================================
```

We respectfully submit this architectural overview to railway and innovation stakeholders with the following specific, realistic requests:

1. **Architecture & Security Review:** Technical feedback from CRIS and IRCTC software engineering teams regarding our defensive security posture, zero-trust payment masking, and database persistence model.
2. **Mentorship on Railway Data Protocols:** Guidance from railway operational specialists on standard API schemas, terminology harmonization, and preferred integration patterns.
3. **Sandbox / Testbed Access:** Exploration of eligibility to connect to non-production staging environments or developer sandboxes for CRIS PRS status inquiries and NTES schedule feeds.
4. **Feasibility Review for a Controlled Pilot:** Exploratory discussions regarding the prerequisites, compliance standards, and administrative steps required to propose a future sandboxed passenger trial.

**Contact & Repository Reference:**  
Project RailSahayak Technical Package  
Repository Root: `C:\Railshahayak\railsahayak-backend-starter\railsahayak-backend-starter`  
Local Verification Endpoint: `http://localhost:8081/`  
Automated Verification Suite: 29 Integration Tests (100% Pass Rate)
