# RailSahayak — 12-Slide Enterprise Stakeholder Briefing: Presenter Delivery Guide

**Document Reference:** RS-NOTES-2026-V2.0  
**Product Name:** RailSahayak (Strict Product Name: **RailSahayak** only)  
**Author / Presenter:** Senior Systems Architecture & Engineering Briefing Team  
**Target Duration:** 7 to 10 minutes total delivery (allowing 3 to 5 minutes for Evaluator Q&A)  
**Accompanying Visual Artifacts:**
- PowerPoint Slide Deck: `docs/RailSahayak_Stakeholder_Presentation.pptx` (12 Widescreen Slides, 16:9)
- High-Resolution PDF Deck: `docs/RailSahayak_Stakeholder_Presentation.pdf` (12 Matching Widescreen Pages)
- Comprehensive Word Proposal: `docs/RailSahayak_Stakeholder_Proposal.docx` (A4 Word Document, 20 Sections)
- Comprehensive PDF Proposal: `docs/RailSahayak_Stakeholder_Proposal.pdf` (20 Matching A4 Pages)
**Target Stakeholders:** Ministry of Railways (MoR), Center for Railway Information Systems (CRIS), Indian Railway Catering and Tourism Corporation (IRCTC), Railway Innovation Program Evaluators

---

## 1. Executive Presentation Agenda & Delivery Plan (7–10 Minutes)

| Slide # | Slide Category & Topic | Target Duration | Running Time | Core Operational Focus |
| :---: | :--- | :---: | :---: | :--- |
| **Slide 1** | Executive Editorial Cover: Platform Identity & Boundaries | 0:35 | 0:35 | Editorial identity, first-line advisory role, independent prototype notice. |
| **Slide 2** | Why RailSahayak Matters: The Passenger Journey Friction Reality | 0:45 | 1:20 | 4-stage horizontal friction flow (Booking, Post-Booking, Travel, Post-Travel). |
| **Slide 3** | The Problem, Evidence & Open Questions: Root Causes of Distress | 0:45 | 2:05 | 4-column Problem Validation Matrix (Tatkal, waitlists, inquiries, panic). |
| **Slide 4** | The RailSahayak Solution: A Pre-Triage Advisory Layer | 0:45 | 2:50 | 4 functional pillars: Need $\rightarrow$ Advisory Guidance $\rightarrow$ Official Handoff. |
| **Slide 5** | See the Product: Verified Working Prototype | 0:45 | 3:35 | 4 live interface panels, execution commands, and verified local features. |
| **Slide 6** | Proof: What Works Today? Verifiable Implementation Evidence | 0:45 | 4:20 | 29/29 automated integration tests, PostgreSQL 16 persistence, DR automation. |
| **Slide 7** | Architecture & System Boundaries: Current vs Future State | 0:40 | 5:00 | Decoupled interface architecture, 6-layer comparison, zero external calls. |
| **Slide 8** | Security, Risks & Honest Limitations: Defense-in-Depth & Readiness | 0:45 | 5:45 | Verified safeguards (trusted proxy limiter, secret filter) vs production gaps. |
| **Slide 9** | Complementing Official Services: An Ecosystem Handoff Model | 0:45 | 6:30 | Core official systems vs advisory buffer; 3 non-disruption commitments. |
| **Slide 10** | A Realistic Evaluation Plan: Phased Gates & Stop Conditions | 0:45 | 7:15 | Conditional 5-stage timeline with explicit, mandatory stop conditions. |
| **Slide 11** | How Success Would Be Measured: Objective Pilot KPI Framework | 0:45 | 8:00 | Objective 5-dimension KPI matrix with prospective targets & governance note. |
| **Slide 12** | The Request: Constructive Dialogue & Collaborative Next Steps | 0:45 | 8:45 | 4 collaborative requests, verbatim mandatory fallback clause, closing vision. |
| **Q&A** | Interactive Evaluator Questions & Defensible Answers | 3:00 – 5:00 | 11:45 – 13:45 | 7 tough architectural, operational, and regulatory evaluator Q&As. |

---

## 2. Slide-by-Slide Presenter Script, Visual Cues & Verbal Transitions

### Slide 1: Executive Cover
- **Slide Title:** RailSahayak — Intelligent Railway Passenger Advisory Platform
- **Category:** Executive Briefing
- **Target Duration:** 0:35 (Running Time: 0:35)
- **Presenter Speaking Points:**
  > *"Respected members of the Railway Board, technical evaluators, and leadership teams from CRIS and IRCTC, good morning. Today, we present **RailSahayak**, an intelligent passenger advisory and non-emergency complaint pre-triage platform engineered specifically for Indian Railways commuters.*
  >
  > *Every day, Indian Railways serves over 24 million citizens. While core transaction systems like CRIS PRS and IRCTC process bookings at unparalleled national scale, millions of passengers face acute anxiety during high-traffic booking windows, waitlist charting, and interbank refund turnaround cycles.*
  >
  > *RailSahayak is designed strictly as an **informational pre-triage advisory layer**. It does not replace or compete with existing railway systems; rather, it acts as an intelligent digital buffer that reassures passengers, clarifies operating rules, and deflects routine inquiries before they reach crowded helpdesks—all with zero load on live reservation servers."*
- **Visual Focus Cues:** Point to the subtitle highlighting the pre-triage role, and note the prominent independent engineering prototype notice at the bottom.
- **Verbal Transition to Slide 2:**
  > *"To understand the operational necessity of this advisory layer, let us examine the reality of passenger friction across the travel journey."*

---

### Slide 2: Why RailSahayak Matters
- **Slide Title:** Why RailSahayak Matters: The Passenger Journey Friction Reality
- **Category:** Operational Need & Friction Analysis
- **Target Duration:** 0:45 (Running Time: 1:20)
- **Presenter Speaking Points:**
  > *"Passenger distress does not occur in a vacuum; it concentrates across four chronological journey stages:*
  >
  > *First, **Booking Window Friction**: During the 10:00 AM and 11:00 AM Tatkal rush, multi-party distributed payment sessions timeout. Bank accounts are debited without ticket confirmation, causing panic and duplicate bookings.*
  >
  > *Second, **Post-Booking Ambiguity**: Travelers struggle to interpret complex waitlist taxonomies—GNWL, RLWL, PQWL—and misunderstand RAC shared seating entitlements.*
  >
  > *Third, **Travel Readiness & Charting**: Unaware of 4-hour chart release deadlines, passengers occasionally board with dropped waitlisted e-tickets, inadvertently incurring Section 138 penalties.*
  >
  > *Fourth, **Post-Travel Refund Anxiety**: Travelers misunderstand interbank T+3 to T+5 settlement cycles, overwhelming emergency helplines like 139 with routine refund status checks.*
  >
  > *As highlighted in the blue takeaway banner below: Core transaction engines must process bookings; an intelligent pre-triage layer is needed to manage edge passenger anxiety."*
- **Visual Focus Cues:** Guide the audience along the 4 horizontal journey cards across the slide, finishing on the key takeaway banner at the bottom.
- **Verbal Transition to Slide 3:**
  > *"Let us look closer at the underlying root causes and empirical evidence behind these friction points."*

---

### Slide 3: The Problem, Evidence & Open Questions
- **Slide Title:** The Problem, Evidence & Open Questions: Root Causes of Commuter Distress
- **Category:** Problem Validation Matrix
- **Target Duration:** 0:45 (Running Time: 2:05)
- **Presenter Speaking Points:**
  > *"Our Problem Validation Matrix categorizes these friction points with evidentiary discipline:*
  >
  > *For Tatkal Payment Drop-Offs, bank debits without instant PNRs cause commuter panic, resulting in duplicate debits of Rs. 1,800 to Rs. 4,500 and merchant disputes.*
  >
  > *For Waitlist Rule Misinterpretation, commuters misunderstand RAC accommodation rights and legal restrictions on cancelled waitlisted e-tickets, leading to inadvertent ticketless travel under Section 138.*
  >
  > *For Non-Emergency Inquiry Load, routine refund queries flood emergency 139 queues, cluttering emergency response.*
  >
  > *And for Tatkal Booking Panic, high-speed UI competition triggers irrational repeated payments.*
  >
  > *Crucially, as noted at the bottom, all operational friction is grounded in public helpdesk evidence and regulatory circulars, while quantitative deflection metrics represent prospective research hypotheses to be empirically validated during an authorized pilot."*
- **Visual Focus Cues:** Walk through the 4-column matrix, emphasizing the *Observed Friction Point*, *Passenger Impact*, and *Evidence Tier* for each column.
- **Verbal Transition to Slide 4:**
  > *"To resolve these root causes without placing load on core railway systems, let us examine RailSahayak's solution architecture."*

---

### Slide 4: The RailSahayak Solution
- **Slide Title:** The RailSahayak Solution: A Pre-Triage Architecture
- **Category:** Functional Solution Architecture
- **Target Duration:** 0:45 (Running Time: 2:50)
- **Presenter Speaking Points:**
  > *"RailSahayak delivers targeted guidance across four specialized advisory pillars:*
  >
  > *1. **Smart Train Search**: Provides trunk route discovery between distinct stations and delivers deterministic schedule guidance, before performing a clean handoff to the official IRCTC portal for booking.*
  >
  > *2. **Payment Help Troubleshooter**: Grounded in RBI Circular RBI/2019-20/67, it diagnoses transaction states and explains the T+1 to T+5 auto-reversal cycle, with zero collection of financial secrets.*
  >
  > *3. **Regulatory PNR Guide**: Decodes PRS codes, explains 1st chart (~4h) and 2nd chart (30-50m) preparation timelines, and prominently displays statutory warnings regarding Section 138.*
  >
  > *4. **Grievance Intake & Audit**: Registers non-emergency inquiries with unique RS-XXXXXX reference IDs and interactive chronological timeline tracking, directing urgent on-train emergencies immediately to Helpline 139.*
  >
  > *As summarized at the bottom, RailSahayak acts as an intelligent informational filter: resolving questions locally and routing structured cases to official channels."*
- **Visual Focus Cues:** Follow the 3-step vertical progression (*Passenger Need $\rightarrow$ RailSahayak Advisory Guidance $\rightarrow$ Official System Handoff*) across the 4 pillar cards.
- **Verbal Transition to Slide 5:**
  > *"This platform is not a conceptual wireframe; it is an active, running prototype that you can test today."*

---

### Slide 5: See the Product
- **Slide Title:** See the Product: Verified Working Prototype
- **Category:** Interactive Interface Walkthrough
- **Target Duration:** 0:45 (Running Time: 3:35)
- **Presenter Speaking Points:**
  > *"RailSahayak is a lightweight, responsive web application served on localhost port 8081.*
  >
  > *On this slide, you see four verified interface panels:*
  >
  > *Panel 1: The **Smart Train Finder**, validating station pairs, filtering classes, and providing direct deep-links to IRCTC.*
  >
  > *Panel 2: The **Payment Help Diagnostic Form**, guiding commuters through payment mode selection and generating RBI turnaround checklists with zero-trust PAN/CVV filtering.*
  >
  > *Panel 3: The **Regulatory PNR Guide**, validating 10-digit formats, deriving PRS zones heuristically, and issuing Section 138 legal warnings.*
  >
  > *Panel 4: The **Case Timeline & Operations Console**, where passengers inspect status updates, and authenticated administrators execute status transitions with mandatory investigation notes.*
  >
  > *The complete application can be launched in seconds using the exact Maven, PowerShell, or Docker commands listed in the green banner below."*
- **Visual Focus Cues:** Point to the 4 interface cards, then reference the command bar at the bottom showing `mvn spring-boot:run` and `./scripts/verify-runtime.ps1`.
- **Verbal Transition to Slide 6:**
  > *"Let us examine the concrete technical evidence verifying these capabilities."*

---

### Slide 6: Proof: What Works Today?
- **Slide Title:** Proof: What Works Today? Verifiable Implementation Evidence
- **Category:** Technical Verification & Proof
- **Target Duration:** 0:45 (Running Time: 4:20)
- **Presenter Speaking Points:**
  > *"We substantiate all technical claims with verifiable repository artifacts across three core areas:*
  >
  > *First, **29 Automated Integration Tests**: Our JUnit 5 and MockMvc test suite in `RailSahayakApplicationTests.java` executes with a 100% pass rate in ~14.2 seconds, validating role-based authorization, rate limiting, trusted proxy headers, payment secret rejection, and exception sanitization.*
  >
  > *Second, **PostgreSQL 16 Relational Persistence**: Managed via Flyway migrations V1 and V2, persisting support cases, timeline events, and immutable audit logs with verified performance indexing and zero data loss.*
  >
  > *Third, **Operational Automation & DR**: Fully automated PowerShell scripts—`verify-runtime.ps1` passing 8 of 8 live API audits, `backup-db.ps1` producing compressed dumps with MD5 hashes, and `restore-db.ps1` providing idempotent disaster recovery.*
  >
  > *As highlighted in the green banner: Everything shown today runs autonomously in a local sandbox with zero external dependencies."*
- **Visual Focus Cues:** Direct attention to the 3 proof panels (*29 Integration Tests*, *PostgreSQL Persistence*, *Operational Scripts*), then highlight the green *Local Verification Status* bar.
- **Verbal Transition to Slide 7:**
  > *"Now, let us examine the system architecture and its strict operational boundaries."*

---

### Slide 7: Architecture & System Boundaries
- **Slide Title:** Architecture & System Boundaries: Local Prototype vs Future Enterprise State
- **Category:** Technical Architecture & Boundaries
- **Target Duration:** 0:40 (Running Time: 5:00)
- **Presenter Speaking Points:**
  > *"Architectural transparency is essential for mission-critical railway systems. On this slide, we clearly distinguish our current sandbox baseline from our planned enterprise production architecture:*
  >
  > *Across Client, Ingress, Rate Limiting, IAM, Persistence, and Gateways, our current prototype is built with clean interface abstractions.*
  >
  > *For example, our train search and PNR services implement decoupled contracts. Today, they execute offline heuristic logic. Transitioning to production requires zero changes to core business logic; it merely involves injecting production adapters that communicate with CRIS PRS and NTES testbeds over mutual TLS.*
  >
  > *And as stated in the red boundary banner: RailSahayak makes zero unauthorized network calls to live railway infrastructure today."*
- **Visual Focus Cues:** Contrast the *Current Local Sandbox* column with the *Future Production Architecture* column, emphasizing the bottom red *Non-Intrusive Integration Principle* banner.
- **Verbal Transition to Slide 8:**
  > *"Let us examine our security posture, risks, and honest prototype limitations."*

---

### Slide 8: Security, Risks & Honest Limitations
- **Slide Title:** Security, Risks & Honest Limitations: Defense-in-Depth & Readiness Gaps
- **Category:** Cybersecurity & Risk Management
- **Target Duration:** 0:45 (Running Time: 5:45)
- **Presenter Speaking Points:**
  > *"RailSahayak implements rigorous defense-in-depth security:*
  >
  > *On the left are our verified safeguards: Sliding-window rate limiting at 300 req/min/IP with strict trusted proxy validation; zero-trust payment secret defense rejecting card PANs and CVVs; DPDP Act 2023 data minimization and consent; and MDC correlation tracing with sanitized JSON error responses.*
  >
  > *On the right, we openly document current prototype gaps and our production remediation roadmap: Migrating in-memory test users to PostgreSQL Argon2id or IRCTC/Parichay OAuth2 SSO; scaling the single-node rate limiter to a distributed Redis Lua cluster; deploying TLS 1.3 reverse proxies; and undergoing an independent CERT-In empaneled VAPT audit.*
  >
  > *As stated in our engineering disclosure below: We make no false claims of being production-ready until formal VAPT and enterprise controls are completed."*
- **Visual Focus Cues:** Compare the left green verified safeguards with the right amber prototype gaps, concluding on the honest engineering disclosure note.
- **Verbal Transition to Slide 9:**
  > *"With these security controls established, how does RailSahayak complement existing Indian Railways digital services?"*

---

### Slide 9: Complementing Official Services
- **Slide Title:** Complementing Official Services: An Ecosystem Handoff Model
- **Category:** Railway Ecosystem Synergy
- **Target Duration:** 0:45 (Running Time: 6:30)
- **Presenter Speaking Points:**
  > *"RailSahayak is engineered strictly to complement official railway systems, not compete with them:*
  >
  > *Core official systems retain exclusive authority: IRCTC manages commercial ticketing, fare collection, and refund processing; CRIS operates the central PRS mainframe and train scheduling; and RailMadad 139 provides on-train emergency intervention and formal grievance redressal.*
  >
  > *RailSahayak acts as a first-contact advisory buffer: It clarifies banking settlement cycles in plain language to reduce anxiety; provides statutory rule guidance on waitlists and Section 138 compliance; and performs structured pre-triage to deflect routine informational queries away from emergency helplines.*
  >
  > *In the green banner below, we formalize three non-disruption commitments: RailSahayak NEVER books tickets, NEVER executes financial refunds, and NEVER performs unauthorized web scraping."*
- **Visual Focus Cues:** Guide evaluators between the two comparison columns (*Core Official Railway Systems* vs *RailSahayak Advisory Buffer*), then read the three bulleted non-disruption commitments.
- **Verbal Transition to Slide 10:**
  > *"To evaluate these complementary capabilities safely, we have structured a realistic evaluation plan."*

---

### Slide 10: A Realistic Evaluation Plan
- **Slide Title:** A Realistic Evaluation Plan: Phased Gates & Stop Conditions
- **Category:** Evaluation Roadmap & Safety Gates
- **Target Duration:** 0:45 (Running Time: 7:15)
- **Presenter Speaking Points:**
  > *"We propose a conditional 5-stage evaluation plan with mandatory approval gates:*
  >
  > *Stage 1, Weeks 1 to 4: Technical scoping and rule alignment with Commercial Officers.*
  >
  > *Stage 2, Weeks 5 to 8: Independent CERT-In VAPT audit and DPDP privacy review.*
  >
  > *Stage 3, Weeks 9 to 14: Controlled non-production staging sandbox testing with synthetic data and zero live commuter exposure.*
  >
  > *Stage 4, Weeks 15 to 20: A restricted pilot on designated trial routes with voluntary participants.*
  >
  > *Stage 5, Week 21: Comprehensive evaluation report and executive decision on handover or licensing.*
  >
  > *Crucially, as highlighted in the red box below, our plan includes **Mandatory Stop Conditions**: Evaluation will immediately halt upon any security incident, any inaccurate statutory guidance, system instability, or revocation of stakeholder authorization."*
- **Visual Focus Cues:** Walk through the 5 vertical phase columns (*Stage 1 to Stage 5*), noting the gate criteria on each, then emphasize the red *Mandatory Stop Conditions* banner.
- **Verbal Transition to Slide 11:**
  > *"How would success be objectively measured during this trial? Let us look at our KPI framework."*

---

### Slide 11: How Success Would Be Measured
- **Slide Title:** How Success Would Be Measured: Objective Pilot KPI Framework
- **Category:** Measurement Governance
- **Target Duration:** 0:45 (Running Time: 8:00)
- **Presenter Speaking Points:**
  > *"Our measurement framework establishes objective evaluation metrics across five operational dimensions:*
  >
  > *1. Advisory Response Latency: Baseline prototype P50 < 80 ms; proposed pilot target P95 < 200 ms under simulated load, measured via Spring Boot Actuator.*
  >
  > *2. Guidance Workflow Completion: Target > 85% session completion without aborting.*
  >
  > *3. Informational Query Deflection: Targeting 25% to 35% reduction in repetitive informational calls on trial routes, evaluated by operations analysts.*
  >
  > *4. Dual Audit Completeness: Targeting 100% event capture with zero orphan cases, audited via automated SQL queries.*
  >
  > *5. Security & Privacy: Exactly zero data exposures and zero raw card numbers stored, audited by CERT-In assessors.*
  >
  > *As stated at the bottom: We commit that no deflection or satisfaction claim will be presented as fact until validated by an authorized railway pilot."*
- **Visual Focus Cues:** Review the 5 KPI rows, drawing attention to the distinct *Baseline Status*, *Proposed Target*, and assigned *Evaluator* roles.
- **Verbal Transition to Slide 12:**
  > *"This brings us to our specific request for constructive stakeholder dialogue."*

---

### Slide 12: The Request
- **Slide Title:** The Request: Constructive Dialogue & Collaborative Next Steps
- **Category:** Stakeholder Engagement & Collaboration
- **Target Duration:** 0:45 (Running Time: 8:45)
- **Presenter Speaking Points:**
  > *"We respectfully request four specific forms of collaboration from railway leadership:*
  >
  > *1. Technical Architecture Feedback: Critique on our stateless Spring Boot service architecture, token-bucket rate limiting, and PostgreSQL persistence design.*
  >
  > *2. Standards & Regulatory Guidance: Expert advice from Commercial Officers on reservation edge cases and exact terminology alignment.*
  >
  > *3. Mentorship & Skill Development: Opportunities for academic mentorship from CRIS and IRCTC technical leaders to build national-scale engineering capabilities.*
  >
  > *4. Sandbox Testing Prerequisites: Clarity on official compliance checklists and clearances needed to apply for non-production sandbox API evaluation.*
  >
  > *And we place our core proposition in the blue box below:*
  >
  > *'**If Indian Railways or IRCTC does not wish to replace or change its existing system, RailSahayak could still be evaluated as a complementary independent tool, subject to technical, legal and institutional review. Stakeholders may also advise on technical mentorship, skill-development opportunities, further development, or a possible handover arrangement.**'*
  >
  > *Our objective is simple: improving passenger clarity while fully respecting core railway infrastructure. Thank you for your time, and we welcome your questions."*
- **Visual Focus Cues:** Point to the 4 collaborative request cards, read the bold text in the *Exploratory Collaboration* panel, and conclude on the bottom closing statement.

---

## 3. Anticipated Evaluator Questions & Defensible, Evidence-Grounded Answers

### Q1: "Are you scraping live IRCTC or CRIS websites for train schedules and PNR status?"
- **Defensible Answer:**
  > *"No, absolutely not. Web scraping violates railway terms of service, creates security vulnerabilities, and introduces platform instability. In RailSahayak, train schedules are deterministic sample datasets on trunk corridors, and PNR status codes and charting rules are purely procedural explanations. Our first-digit PRS zone mapping is derived purely as an offline heuristic routing convention from established railway numbering patterns. Every API response explicitly returns a `liveRailwayIntegration: false` flag, and every UI card features a prominent demo badge and directs passengers to official government portals for live data."*

### Q2: "Can RailSahayak refund a passenger's money when an account is debited?"
- **Defensible Answer:**
  > *"No. RailSahayak never handles money, connects to payment switches, or executes financial refunds. The Payment Help module is an informational diagnostic engine. It reassures anxious travelers, explains the automated interbank settlement timelines mandated by the Reserve Bank of India (RBI Circular RBI/2019-20/67), masks transaction references, and actively rejects sensitive secrets like card numbers, CVVs, and PINs. All financial settlement remains strictly between the passenger's bank and the official payment aggregator."*

### Q3: "What is the legal basis for your warning regarding waitlisted e-tickets under Section 138?"
- **Defensible Answer:**
  > *"Under Ministry of Railways Commercial Circular No. 64 of 2015 and the Indian Railways Commercial Manual, an e-ticket that remains fully waitlisted after 2nd chart preparation is automatically invalidated by CRIS PRS, and the fare is credited back to the customer's account. Traveling on an Indian Railways train with an invalidated, waitlisted e-ticket is strictly prohibited and constitutes ticketless travel under Section 138 of the Railways Act, 1989, subjecting the traveler to mandatory excess fare penalties. RailSahayak clearly highlights this rule to protect travelers from inadvertent violations."*

### Q4: "How does RailSahayak defend against Distributed Denial of Service (DDoS) and IP spoofing?"
- **Defensible Answer:**
  > *"We implement defense-in-depth: our `RateLimitingFilter` enforces a sliding-window threshold of 300 requests per minute per IP address. Following our Step 9 security hardening, forwarded-header trust (`X-Forwarded-For`) defaults to false and is accepted only from a documented, whitelisted reverse proxy IP, preventing client IP spoofing. Furthermore, we enforce strict security headers (`nosniff`, `SAMEORIGIN`), assign unique `X-Correlation-ID`s for distributed tracing, and sanitize all runtime exceptions so that zero stack traces or internal SQL fragments are ever leaked to clients. Our full suite of 29 automated tests validates these controls with a 100% pass rate."*

### Q5: "Why build RailSahayak when RailMadad and IRCTC already exist? Isn't this duplicative?"
- **Defensible Answer:**
  > *"RailSahayak is engineered on the principle of complementary defense, not duplication. IRCTC is a commercial booking engine designed for transaction throughput; when transactions fail, its helpdesk is overwhelmed by repetitive status queries. RailMadad is an emergency grievance system designed for urgent on-train safety, security, and cleanliness dispatch. When non-emergency informational questions—such as 'Why is my refund taking 3 days?' or 'What does RLWL mean?'—hit RailMadad 139, emergency queues become congested. RailSahayak acts as an intelligent first-contact filter at the perimeter: it resolves informational questions locally and defers urgent grievances directly to RailMadad 139, thereby protecting core railway capacity."*

### Q6: "How do you guarantee that a pilot will not disrupt railway operations, and what is your rollback strategy?"
- **Defensible Answer:**
  > *"RailSahayak operates in a completely decoupled architecture. It sits behind an edge reverse proxy and does not write to CRIS PRS or modify live seat inventories. Furthermore, we have engineered an Enterprise Graceful Rollback Protocol that executes in under 60 seconds: if the pilot HTTP 5xx error rate exceeds 0.5% or a critical anomaly is detected, railway operators can divert passenger traffic back to standard static help pages within 60 seconds via reverse proxy or DNS routing. Zero data is lost: all existing support cases, audit logs, and diagnostic records remain securely persisted in PostgreSQL for forensic post-incident review."*

### Q7: "How does RailSahayak comply with the Digital Personal Data Protection (DPDP) Act, 2023?"
- **Defensible Answer:**
  > *"RailSahayak strictly adheres to the DPDP Act principles of data minimization and purpose limitation. The platform never prompts for, transmits, or persists Aadhaar numbers, unmasked payment cards, or unnecessary personal identifiers. The Payment Help module actively rejects inputs matching primary account numbers (PANs) or CVVs with an immediate HTTP 400 Bad Request. All support cases include an explicit bilingual consent notice prior to submission, and case records in PostgreSQL are tagged with retention timestamps enabling automated purging or anonymization following resolution."*

---

## 4. Presenter Self-Checklist Before Entering the Room

- [x] Verified running software on `localhost:8081` (health endpoint responds HTTP 200).
- [x] Verified 12-slide presentation deck matches `docs/RailSahayak_Stakeholder_Presentation.pptx` and `.pdf`.
- [x] Verified 20-page proposal matches `docs/RailSahayak_Stakeholder_Proposal.docx` and `.pdf`.
- [x] Prepared to demonstrate 29 passing automated integration tests via `mvn test`.
- [x] Confirmed zero live scraping or live railway server calls are claimed or executed.
- [x] Memorized the verbatim fallback proposal clause on Slide 12 and Section 18.
- [x] Checked backup and disaster recovery scripts in `scripts/backup-db.ps1` and `restore-db.ps1`.
