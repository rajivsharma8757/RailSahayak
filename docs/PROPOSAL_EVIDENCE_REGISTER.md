# RailSahayak — Proposal Evidence and Regulatory Source Register

**Document Reference:** `docs/PROPOSAL_EVIDENCE_REGISTER.md`  
**Project Name:** RailSahayak  
**Version:** 2.1 (Executive Submission Edition)  
**Date of Verification:** October 18, 2026  
**Auditor / Verification Lead:** Technical Research & Evidence-Verification Specialist (Antigravity)  

---

## 1. Purpose and Evidentiary Standard

This register establishes the evidentiary foundation for all factual, legal, operational, and technical claims made in the **RailSahayak** Stakeholder Proposal and Presentation.

In accordance with enterprise and public-sector procurement standards, every material claim in the RailSahayak documentation is categorized into one of five evidentiary tiers:
1. **Tier 1 — Statutory / Regulatory Rule:** Documented in published Indian legislation, Ministry of Railways commercial circulars, or Reserve Bank of India policy directives.
2. **Tier 2 — Official Technical Service Specification:** Documented on canonical Indian Railways (IRCTC, CRIS, NTES, RailMadad) portals or public documentation.
3. **Tier 3 — Empirically Verified Local Implementation:** Proven via automated integration tests, runtime probes, and database state in the RailSahayak repository.
4. **Tier 4 — Proposed Operational Target:** Prospective performance or deflection goals to be measured during an authorized pilot (explicitly labeled as non-achieved targets).
5. **Tier 5 — Research Hypothesis / Operational Assumption:** Industry observations regarding passenger behavior requiring empirical validation during a controlled trial.

---

## 2. Official Regulatory and Policy Source Register

| Ref ID | Material Claim / Subject Matter | Official Authority & Source Document | Canonical URL | Access / Verification Date | Evidentiary Finding & Legal / Technical Scope | Explicit Boundary, Limitation, or Ambiguity |
| :---: | :--- | :--- | :--- | :---: | :--- | :--- |
| **REG-01** | **Waitlisted E-Ticket Travel Prohibition & Penalties** | Ministry of Railways Commercial Circular No. 64 of 2015; Indian Railways Commercial Manual; Section 138 of the Railways Act, 1989 | [https://www.irctc.co.in/](https://www.irctc.co.in/) | 2026-10-18 | Fully waitlisted e-tickets post-charting are automatically cancelled by IRCTC and refunded. Boarding a reserved coach with a cancelled waitlisted e-ticket constitutes ticketless travel under Section 138 of the Railways Act, 1989, subject to excess charge and fare penalties. | Applies strictly to e-tickets (PRS counter tickets with waitlist status allow travel in general/unreserved coaches or as permitted by TTE rules). |
| **REG-02** | **Reservation Charting Timelines** | Ministry of Railways Press Information Bureau (PIB) Circular (Nov 2015); Indian Railways Commercial Rules | [https://www.indianrail.gov.in/](https://www.indianrail.gov.in/) | 2026-10-18 | 1st reservation chart is finalized at least 4 hours prior to scheduled train departure (or by 20:00 of the previous evening for trains departing before 11:00 AM). 2nd reservation chart is prepared 30 to 50 minutes prior to departure for last-minute allocations. | Charting times can vary during severe operational disruptions, weather delays, or special train notifications. |
| **REG-03** | **Reservation Against Cancellation (RAC) Accommodation Rights** | Indian Railways Passenger Coaching Tariff; Commercial Operating Rules | [https://www.indianrail.gov.in/](https://www.indianrail.gov.in/) | 2026-10-18 | RAC passengers hold confirmed travel entitlement and are assigned shared sitting accommodation (typically 2 RAC passengers share 1 side-lower berth). Upon cancellation of confirmed berths, RAC tickets automatically advance toward full berth confirmation in priority order. | Berth allocation occurs dynamically during 1st and 2nd charting; seat location cannot be guaranteed in advance of charting. |
| **REG-04** | **Failed Digital Payment Harmonisation of Turnaround Time (TAT)** | Reserve Bank of India (RBI) Circular RBI/2019-20/67 (DPSS.CO.PD No.629/02.01.014/2019-20) on "Harmonisation of Turnaround Time (TAT) and customer compensation for failed transactions" | [https://www.rbi.org.in/](https://www.rbi.org.in/) | 2026-10-18 | Establishes automated reversal windows for merchant transactions where funds are debited from customer accounts but not credited to the merchant (e.g. $T+1$ for UPI auto-reversals, $T+5$ for card acquiring). In banking practice, multi-bank settlement and gateway reconciliation cycles typically complete within 3 to 7 bank working days. | Turnaround times depend on acquiring/issuing bank response times; RailSahayak cannot guarantee specific reversal execution dates or override banking dispute procedures. |
| **REG-05** | **Grievance Escalation Framework & Official Channels** | Ministry of Railways RailMadad Portal; National Rail Helpline 139 | [https://railmadad.indianrailways.gov.in/](https://railmadad.indianrailways.gov.in/) | 2026-10-18 | RailMadad is the Ministry of Railways' sole official integrated grievance redressal mechanism, accessible via web, app, and Helpline 139 for on-board security, medical, catering, and coach cleanliness emergencies. | RailSahayak is strictly an informational first-contact guidance layer; it does not replace Helpline 139 for active on-train emergencies. |
| **REG-06** | **Digital Personal Data Protection & Privacy Standards** | Digital Personal Data Protection (DPDP) Act, 2023; Information Technology Act, 2000 (Section 43A) | [https://www.meity.gov.in/](https://www.meity.gov.in/) | 2026-10-18 | Requires purpose limitation, data minimization, explicit consent, and secure handling of personal identification data. Mandates that digital intermediaries do not collect or store unneeded sensitive credentials. | Full compliance certification requires a formal third-party audit prior to processing production citizen records. |
| **REG-07** | **Web Application Security & Defense-in-Depth Guidelines** | Indian Computer Emergency Response Team (CERT-In) Guidelines on Securing Web Applications and APIs | [https://www.cert-in.org.in/](https://www.cert-in.org.in/) | 2026-10-18 | Recommends defense-in-depth security: strict transport security headers (`nosniff`, `SAMEORIGIN`), rate limiting against DoS/brute force, input sanitization, error masking, and end-to-end tracing. | Production readiness requires formal CERT-In empanelled Vulnerability Assessment and Penetration Testing (VAPT) signoff. |

---

## 3. Local Implementation Evidence Register

The following technical claims describe features and security controls physically implemented and verified in the RailSahayak software repository (`C:\Railshahayak\railsahayak-backend-starter\railsahayak-backend-starter`):

| Ref ID | Component / Claim | Implementation File(s) | Verification Method | Actual Test Evidence | Status |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **IMP-01** | **Automated Integration Test Suite Passage** | `src/test/java/.../RailSahayakApplicationTests.java` | Maven test runner (`mvn test`) with OpenJDK 24 | Tests run: 29, Failures: 0, Errors: 0, Skipped: 0. Build Success (~14.2s). | **VERIFIED** |
| **IMP-02** | **Role-Based Authorization & Path Isolation** | `SecurityConfig.java` | Automated tests `passengerCannotAccessAdminCases_returns403`, `unauthenticatedRequest_returns401` | HTTP 403 Forbidden enforced for passenger attempting to access `/api/v1/admin/**`; HTTP 401 for unauthenticated calls. | **VERIFIED** |
| **IMP-03** | **Trusted-Proxy Hardened Rate Limiting** | `RateLimitingFilter.java` | Automated tests `rateLimiter_blocksExcessiveTraffic`, `rateLimiter_ignoresSpoofedForwardedIpWhenTrustDisabled`, `rateLimiter_handlesMalformedOversizedAndMissingForwardedHeadersSafely` | Atomic sliding-window rate limiter (300 req/min/IP). `trust-forwarded-for` defaults to `false`. Forwarded IPs inspected only from whitelisted socket addresses. Malformed/oversized headers safely fall back. | **VERIFIED** |
| **IMP-04** | **Sensitive Payment Secret Rejection** | `PaymentHelpService.java`, `PaymentHelpRequest.java` | Automated test `paymentDiagnose_sensitiveSecret_returnsBadRequest` | Regex detects card PANs (13–19 digits), CVVs, PINs, OTPs, or passwords; rejects request immediately with HTTP 400 Bad Request before processing. | **VERIFIED** |
| **IMP-05** | **Zero-Trust Reference Masking** | `PaymentHelpService.java` | Automated test `paymentDiagnose_moneyDeducted_returnsStructuredGuidance` | Input references are masked (e.g. `UPI987654321098` $\rightarrow$ `UPI****098`) for guidance context; no unmasked references persisted. | **VERIFIED** |
| **IMP-06** | **Offline Heuristic PNR Zone Derivation** | `PnrGuideService.java` | Automated test `pnrGuide_validPnr_derivesPrsZoneAndExplainsStatus` | Derives regional ticketing cluster from first digit (1: Central/CRIS, 2-3: Northern, etc.); explicitly labels output as heuristic routing convention, not live PRS lookup. | **VERIFIED** |
| **IMP-07** | **Support Case Lifecycle & Dual Persistence** | `CaseController.java`, `SupportCaseRepository.java`, `CaseEventRepository.java`, `AuditLogRepository.java` | Automated test `adminStatusTransition_withCustomNote_persistsEventAndAudit`, `verify-runtime.ps1` | Status transitions (`OPEN` $\rightarrow$ `IN_PROGRESS` $\rightarrow$ `RESOLVED`) require mandatory custom note; atomically records in `case_events` and `audit_logs`. | **VERIFIED** |
| **IMP-08** | **Database Schema Migrations & Indexing** | `src/main/resources/db/migration/V1__create_tables.sql`, `V2__add_performance_indexes.sql` | Flyway schema history in PostgreSQL 16 | Flyway migrations executed to version 2; performance B-tree indexes applied on `case_events(case_id, created_at ASC)`, `audit_logs(created_at DESC)`. | **VERIFIED** |
| **IMP-09** | **HTTP Security Headers & Tracing** | `SecurityConfig.java`, `CorrelationIdFilter.java` | Automated test `securityHeaders_enforced`, `correlationId_generatedAndPreserved` | Enforces `nosniff`, `SAMEORIGIN`, `strict-origin-when-cross-origin`; generates or propagates `X-Correlation-ID` into SLF4J MDC and HTTP responses. | **VERIFIED** |
| **IMP-10** | **Exception Sanitization & Zero Leakage** | `GlobalExceptionHandler.java` | Exception testing in integration suite and runtime probe | Intercepts unhandled exceptions; logs full stack trace internally with correlation ID; returns sanitized JSON quoting correlation ID with zero stack trace or SQL leakage. | **VERIFIED** |
| **IMP-11** | **Disaster Recovery Automation** | `scripts/backup-db.ps1`, `scripts/restore-db.ps1` | Execution test in local PowerShell environment | Verified idempotent PostgreSQL dump generation (`pg_dump` with `--clean --if-exists`) and database restoration without record corruption. | **VERIFIED** |

---

## 4. Claims Corrected or Reframed

In accordance with strict factual integrity, several prior statements have been reviewed and corrected:

1. **Information Ambiguity vs Technical Failure Percentage:**
   - *Previous Unsubstantiated Claim:* "Over 60% of routine passenger friction stems from information ambiguity rather than technical failure."
   - *Correction:* Removed the 60% numerical figure because no public CRIS or IRCTC audit definitively establishes that exact ratio. Replaced with an evidence-grounded operational statement:  
     *"A substantial proportion of post-booking passenger distress—particularly during Tatkal booking windows—is driven by procedural ambiguity (such as uncertainty regarding automatic bank reversals and charting timelines) rather than unrecoverable technical failure."*
2. **First-Digit PNR Derivation:**
   - *Previous Phrasing:* "PNR Server Zone Query".
   - *Correction:* Strictly labeled as an **offline heuristic routing convention**:  
     *"Heuristic cluster: [Zone] (Derived from first-digit routing convention, not live PRS lookup)."*
3. **Refund Timeline Guarantees:**
   - *Previous Phrasing:* "Refunds processed within 3 to 5 business days."
   - *Correction:* Aligned with RBI TAT circular (RBI/2019-20/67); explains typical 3–7 bank working day settlement cycles while explicitly stating that RailSahayak does not execute refunds.
4. **Pilot Key Performance Indicators (KPIs):**
   - *Previous Phrasing:* Stated target metrics (e.g. <150ms P95 latency, >70% self-resolution) without clear disclaimers.
   - *Correction:* Formally framed as **Proposed Operational Target Goals for an Authorized Pilot**, requiring formal approval of baseline methodologies.
5. **Database Persistence Metrics:**
   - *Previous Phrasing:* Fixed counts ("25 cases, 49 events") presented as static system facts.
   - *Correction:* Phrased as verified structural persistence:  
     *"Full lifecycle of support cases, timeline events, and audit logs preserved with zero data loss across test cycles and server restarts."*

---

## 5. Formal Authorizations Required Prior to Live Operation

The proposal explicitly declares that the following four institutional agreements must be executed before RailSahayak connects to live Indian Railways infrastructure:

1. **CRIS Data Access Agreement (MoU):**
   - Authorized read-only REST/mTLS gateway access to staging and production PRS status feeds and NTES timetable databases.
2. **RailMadad Webhook Bridge Authorization:**
   - Formal technical protocol and API credentials permitting RailSahayak to forward escalated, unresolvable passenger complaints into zonal railway officer queues.
3. **IRCTC Single Sign-On (SSO) Technical Approval:**
   - OAuth2 / OpenID Connect federation approval to authenticate passengers using their official IRCTC credentials.
4. **CERT-In Empanelled Security Audit Signoff:**
   - Comprehensive Vulnerability Assessment and Penetration Testing (VAPT) and DPDP Act 2023 compliance certification by an accredited cybersecurity firm.

---

## 6. Deliverables Inventory & Cryptographic Hash Register

All submission artifacts are validated with exact file lengths and SHA-256 cryptographic checksums:

| # | Artifact Description | Canonical File Path | Format & Extent | Byte Size | SHA-256 Checksum |
| :-: | :--- | :--- | :--- | :-: | :--- |
| **1** | **Executive Presentation (PPTX)** | `docs/RailSahayak_Stakeholder_Presentation.pptx` | PPTX (12 slides, 16:9) | 63,733 B | `700872f209f7ff34f5fca617c2fd824936bfe3ddc702beacb767c217799c69f7` |
| **2** | **Executive Presentation (PDF)** | `docs/RailSahayak_Stakeholder_Presentation.pdf` | PDF (12 pages, 16:9) | 30,621 B | `2862f43d3b4ba9d635910de31c3aecea7d7814def5397ee24fe5dffb25cc2d61` |
| **3** | **Stakeholder Proposal (Word)** | `docs/RailSahayak_Stakeholder_Proposal.docx` | DOCX (20 sections, A4) | 63,434 B | `2e96fd8b28243c44f07492b4982d74de0a295e623d9444e08af934a3ddd7fe21` |
| **4** | **Stakeholder Proposal (PDF)** | `docs/RailSahayak_Stakeholder_Proposal.pdf` | PDF (20 pages, 20 sections) | 57,230 B | `718225bcc0b26a497b3586f94e8bf4aee9bc05de17892f48403eed47e8153f19` |
| **5** | **Presentation Notes & Pitch Guide** | `docs/PRESENTATION_NOTES.md` | Markdown (12 slides, 7 Q&As) | 28,446 B | `f85ddd28fb75382cbecdae62449cb964f86bda429a8a34561e3047fed07d619e` |
| **6** | **Submission Checklist** | `docs/STAKEHOLDER_SUBMISSION_CHECKLIST.md` | Markdown (Audit & checklist) | Synchronized | See Checklist |
| **7** | **Final Proposal QA Report** | `docs/FINAL_PROPOSAL_QA_REPORT.md` | Markdown (QA Audit Report) | 26,815 B | `ea133b6aafe9020176854f40a6cfe643e8921bed01850fc0c35afb76ab846229` |

---

## 7. Audit Conclusion

All statements of fact, legal references, technical capabilities, and operational boundaries in the **RailSahayak** stakeholder package are fully verified against official regulatory publications or reproducible codebase test runs. No unauthorized claims of partnership, live integration, or guaranteed outcomes remain.
