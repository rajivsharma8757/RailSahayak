# RailSahayak — Railway Stakeholder Pilot Proposal & Technical Integration Pack

**Document Reference:** RS-PROP-2026-V1  
**Project:** RailSahayak (Intelligent Railway Passenger Assistance Platform)  
**Target Stakeholders:** Ministry of Railways, Center for Railway Information Systems (CRIS), Indian Railway Catering and Tourism Corporation (IRCTC)  
**Author:** RailSahayak Engineering Team  
**Date:** October 2026  

---

## 1. Executive Summary

Indian Railways operates one of the world's most intricate transportation networks, serving over 24 million passengers daily. While core transaction systems (such as the CRIS Passenger Reservation System and IRCTC E-Ticketing) handle booking volumes at extraordinary scale, millions of passengers routinely experience friction surrounding **payment ambiguity, refund timelines, waitlist regulations, and grievance submission**.

**RailSahayak** is designed as a focused, lightweight, and modern **passenger assistance layer** to complement existing railway infrastructure. Rather than replacing or competing with IRCTC, CRIS, or RailMadad, RailSahayak acts as an intelligent first-line guidance terminal that:
1. Educates passengers on complex railway operational rules (charting timelines, waitlist categories, Section 138 travel regulations).
2. Provides immediate, automated diagnostic checklists for failed or deducted payments before passengers initiate duplicate charges or flood bank grievance desks.
3. Consolidates passenger support cases into a transparent, auditable timeline with real-time operator updates.
4. Seamlessly routes passengers to official Ministry of Railways portals for live transactions, live PNR confirmation, and emergency assistance.

This proposal outlines a phased, risk-mitigated **limited-scope pilot** in partnership with railway authorities to validate passenger satisfaction, operational load reduction, and grievance resolution times.

---

## 2. Core Passenger Problems Addressed

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        INDIAN RAILWAYS PASSENGER JOURNEY FRICTION                      │
├──────────────────────────┬─────────────────────────────┬───────────────────────────────┤
│    Payment Ambiguity     │   Regulatory Complexity     │   Grievance Fragmentation     │
├──────────────────────────┼─────────────────────────────┼───────────────────────────────┤
│ - Account debited but    │ - Confusion between GNWL,   │ - Unclear whether to contact  │
│   ticket not confirmed   │   RLWL, PQWL, and TQWL      │   bank, IRCTC, or RailMadad   │
│ - Duplicate bookings out │ - Misunderstanding of RAC   │ - Lack of visibility into     │
│   of fear / uncertainty  │   rights vs full waitlist   │   investigation timelines     │
│ - Unclear refund windows │ - Chart preparation rules   │ - Inaccessible grievance      │
│   (T+3 to T+5 days)      │   (4h vs 30m 2nd chart)     │   interfaces for casual users │
└──────────────────────────┴─────────────────────────────┴───────────────────────────────┘
```

1. **Payment Failures & Double Deductions:** High-traffic booking periods (e.g. 10:00 AM / 11:00 AM Tatkal windows) occasionally experience payment gateway timeouts. Passengers whose accounts are debited frequently make duplicate booking attempts or submit premature disputes. RailSahayak's zero-trust Payment Help module immediately diagnoses the scenario, explains the automatic settlement cycle, and outlines step-by-step instructions.
2. **PNR Rule Confusion:** Many passengers do not know that travelling on a waitlisted e-ticket is illegal under Section 138 of the Railways Act, or how RAC allocation functions. RailSahayak provides clear, bilingual regulatory explanations without exposing passengers to untrusted third-party apps that scrape personal data.
3. **Transparent Case Tracking:** When passengers submit complaints regarding station amenities, booking issues, or accessibility, they receive a trackable case reference (`RS-XXXXXX`) backed by a persistent audit trail.

---

## 3. How RailSahayak Complements Existing Systems

RailSahayak is architected as an **informational and operational complement**, not an alternative system:

| Railway System | Primary Authority | Existing Role | How RailSahayak Complements |
| :--- | :--- | :--- | :--- |
| **IRCTC E-Ticketing** | IRCTC | Commercial ticketing, transactions, and passenger profile management. | Reduces helpdesk ticket volume by handling pre-booking inquiries, payment diagnostic guidance, and directing passengers to official booking flows. |
| **CRIS PRS** | CRIS | Master database for seat reservations, quotas, charting, and coach allocations. | Interprets PRS status codes (CNF, RAC, WL) and explains charting logic in simple language; does not query or burden PRS core databases directly during prototype phase. |
| **NTES** | CRIS | Real-time train running information and delay schedules. | Provides station route planning guidance and links passengers directly to verified NTES live tracking. |
| **RailMadad** | MoR | Official integrated grievance redressal mechanism (Helpline 139). | Acts as a friendly intake portal for local and non-emergency feedback, directing active on-train passengers directly to RailMadad for immediate physical intervention. |

---

## 4. Current Working Prototype Capabilities

The RailSahayak software package is fully functional in a localized sandbox environment with the following verified capabilities:

- **Full-Stack Implementation:** Responsive Single-Page Application (HTML5, CSS3, JavaScript) served by Spring Boot 3.4.5 (Java 24) with PostgreSQL 16 persistence via Flyway.
- **Role-Based Access Control:** Separate authenticated workflows for passengers (`ROLE_PASSENGER`) and railway administrators (`ROLE_ADMIN`).
- **Support Case Engine:** Passenger submission wizard generating unique `RS-XXXXXX` references, real-time case timeline tracking, and administrative status transitions (`OPEN` -> `IN_PROGRESS` -> `RESOLVED`) with custom operator notes.
- **Tamper-Evident Audit Logging:** Dual-persistence architecture capturing every operational action in `audit_logs` and `case_events`.
- **Zero-Trust Payment Guidance:** Intelligent heuristic troubleshooter for UPI, Net Banking, and Card failures that masks transaction IDs and actively rejects card numbers, PINs, OTPs, or passwords.
- **Regulatory PNR Explainer:** Heuristic zone derivation from first digit, detailed breakdown of waitlist priority rules, and chart preparation timelines.
- **Enterprise Security Hardening:** Sliding-window rate limiting (300 req/min/IP), HTTP security headers (`nosniff`, `SAMEORIGIN`, strict referrer policy), request correlation ID tracing (`X-Correlation-ID`), sanitized error bodies, and zero stack trace leakage.
- **Automated Test Suite:** 29 integration tests executing with 100% pass rate in CI/CD pipeline.
- **Operational Automation:** Disaster recovery automation (`backup-db.ps1`, `restore-db.ps1`) and load testing benchmark suite (`load-test.ps1`).

---

## 5. Proposed Pilot Architecture & Integration Roadmap

During the proposed pilot, RailSahayak will operate in a controlled, read-only hybrid model:

```
[ Passenger Mobile / Web Browser ]
                 │
                 ▼
       [ NGINX Reverse Proxy ] ── TLS 1.3 / HSTS Termination
                 │
                 ▼
      [ RailSahayak Core Backend ]
      ├── Spring Security + Sliding-Window Rate Limiter
      ├── Request Correlation ID Filter (MDC Tracing)
      └── Support Case & Diagnostic Services
                 │
        ┌────────┴──────────────────────────┐
        ▼                                   ▼
 [ Local PostgreSQL 16 ]            [ Railway Integration Boundary ]
 (Cases, Timelines, Audits)                         │
                                    ┌───────────────┼───────────────┐
                                    ▼               ▼               ▼
                            [ CRIS Read-Only ] [ RailMadad ] [ Bank Gateway ]
                            (API Gateway)      (Webhook)     (Webhook Reconciliation)
```

### Required Railway / CRIS / IRCTC Authorizations
1. **CRIS Passenger Data Access:** Authorized, read-only API gateway credentials to query PNR status codes over secure TLS/mTLS, avoiding web scraping.
2. **NTES Train Schedule API:** Access to official Indian Railways train schedule and station directory feeds.
3. **RailMadad Webhook Bridge:** Authorized REST endpoint to forward unresolved passenger complaints directly into the zonal railway officer queue.
4. **IRCTC Single Sign-On (SSO):** Technical approval to allow passengers to log in via IRCTC credentials using OAuth2 / OpenID Connect.

---

## 6. Privacy, Cybersecurity & Operational Safeguards

| Domain | Safeguard Standard | Implementation in RailSahayak |
| :--- | :--- | :--- |
| **Data Protection** | Digital Personal Data Protection (DPDP) Act, 2023 | Zero persistent storage of unmasked financial credentials; explicit user consent on case submission; data minimization principle strictly applied. |
| **Zero-Trust Payments** | RBI Cyber Security Framework | RailSahayak does NOT handle card numbers, CVVs, or UPI PINs. Inputs matching sensitive credential patterns are immediately rejected with HTTP 400 Bad Request. |
| **Transport Security** | Ministry of Electronics and IT (MeitY) Guidelines | TLS 1.3 encryption across all communication; strict HTTP headers (`X-Content-Type-Options: nosniff`, `X-Frame-Options: SAMEORIGIN`); HSTS enforcement. |
| **Denial of Service** | CERT-In Web Application Guidelines | Sliding-window IP rate limiting (300 req/min/IP) preventing credential stuffing, scraping, and brute force; input length sanitization on all payload fields. |
| **Audit Integrity** | ISO/IEC 27001 Compliance | Immutable timestamped audit records (`audit_logs`) capturing user IDs, timestamps, transition notes, and correlation IDs. |

---

## 7. Phased Pilot Proposal

```
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│     Phase 1     │       │     Phase 2     │       │     Phase 3     │
│ Sandboxed Trial │ ────► │ Zonal Pilot     │ ────► │ Full Evaluation │
│  (Weeks 1 - 4)  │       │ (Weeks 5 - 12)  │       │ (Weeks 13 - 16) │
└─────────────────┘       └─────────────────┘       └─────────────────┘
  • Staging environment     • 1 Major Railway Zone    • Final KPI Audit
  • Security audit review   • Northern Railway (NR)   • Stakeholder Review
  • CRIS testbed access     • RailMadad sync active   • Rollout roadmap
```

### Phase 1: Security Review & Sandboxed Integration (Weeks 1 – 4)
- Deploy RailSahayak in a railway-controlled staging environment.
- Conduct third-party CERT-In empanelled vulnerability assessment and penetration testing (VAPT).
- Connect to CRIS staging APIs for mock PNR and train schedule queries.

### Phase 2: Limited Zonal Passenger Pilot (Weeks 5 – 12)
- Deploy for a single designated zone (e.g. Northern Railway / New Delhi Division).
- Direct passengers with booking inquiries or payment questions from select IRCTC help pages to the RailSahayak diagnostic assistant.
- Activate bi-directional grievance syncing with the zonal RailMadad desk.

### Phase 3: Comprehensive KPI Evaluation & Rollout Decision (Weeks 13 – 16)
- Evaluate pilot against predefined quantitative targets.
- Present findings to Railway Board, CRIS, and IRCTC leadership.
- Formulate permanent operational roadmap or execute graceful rollback.

---

## 8. Measurable Pilot Key Performance Indicators (KPIs)

> [!NOTE]
> **Proposed Pilot Evaluation Targets (Not Pre-Existing or Achieved Metrics):**
> The following figures represent **proposed operational target goals to be measured during an authorized pilot**, rather than claims of achieved production results. RailSahayak does not claim existing production throughput or nationwide Tatkal capacity. All external integrations depend on formal written authorization.

| Metric | Proposed Pilot Target | Measurement Method |
| :--- | :--- | :--- |
| **Average Initial Diagnostic Latency** | < 150 ms (P95 target) | Server-side Prometheus request metrics on `/api/v1/payment-help/diagnose` and `/api/v1/pnr-guide/explain`. |
| **Payment Issue Resolution Rate** | > 70% resolved without human escalation | Percentage of passengers diagnosed who confirm issue understanding without opening an IRCTC support ticket. |
| **Duplicate Booking Prevention** | > 85% reduction in panic bookings | Passenger survey feedback following payment status diagnosis. |
| **Complaint Tracking Completion Rate** | 100% | Ratio of submitted cases successfully receiving assigned timeline updates from operators. |
| **System Uptime & Availability** | 99.95% (target) | Synthetic health checks pinging `/api/v1/health` at 10-second intervals. |
| **HTTP Error Rate (5xx)** | < 0.05% (target) | Continuous HTTP error monitoring via centralized log aggregation. |
| **Passenger Satisfaction Score (CSAT)**| > 4.2 / 5.0 (target) | Post-interaction single-click feedback rating in the web UI. |

---

## 9. Risk Management and Rollback Plan

| Risk Description | Probability | Impact | Mitigation Strategy |
| :--- | :--- | :--- | :--- |
| **Misinterpretation of Sample Data** | Low | Medium | Prominent, persistent visual badges ("DEMO DATA ONLY") and direct links to official booking channels on all train search cards. |
| **Backend Service Overload** | Low | High | Horizontal pod autoscaling (HPA) in Kubernetes; aggressive application-layer rate limiting; Redis caching. |
| **CRIS / External API Downtime** | Medium | Medium | Circuit breaker pattern (Resilience4j); graceful fallback to offline regulatory guidance and direct telephone helpline links. |
| **Rollback Execution** | Low | Low | Standalone deployment architecture allows immediate traffic diversion back to standard IRCTC help pages within 60 seconds by switching DNS / reverse proxy routing. |

---

## 10. Conclusion and Next Steps

RailSahayak represents an agile, passenger-centric modernization opportunity for Indian Railways. By combining strict adherence to railway operating rules with enterprise-grade application security, the platform provides immediate assistance to travelers while reducing the burden on railway helpdesks.

We welcome the opportunity to demonstrate the working prototype to the Railway Board, CRIS technical leadership, and IRCTC representatives.
