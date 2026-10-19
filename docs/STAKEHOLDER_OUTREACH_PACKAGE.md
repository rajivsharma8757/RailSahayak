# RailSahayak — Master Stakeholder Outreach Package & Strategy

> **Project Identity:** RailSahayak (Independent Passenger Assistance & Service Support Prototype)  
> **Maintainer / Developer:** Rajiv Sharma (`rajivkumarsharma200@gmail.com`)  
> **Academic Affiliation:** Third-year B.Tech Computer Science and Engineering student at Maharishi Markandeshwar (Deemed to be University), Mullana, Ambala, Haryana  
> **Live Web Application:** [https://railsahayak-backend.onrender.com](https://railsahayak-backend.onrender.com)  
> **Public GitHub Repository:** [https://github.com/rajivsharma8757/RailSahayak](https://github.com/rajivsharma8757/RailSahayak)  
> **Package Date:** October 2026 | Prepared for Explicit User Review and Authorization

---

## 1. Executive Notice & Compliance Guardrails

> [!IMPORTANT]
> **GATEWAY NOTICE — DO NOT SEND WITHOUT EXPLICIT APPROVAL:**  
> The drafts below are prepared for the project owner's review. No emails are transmitted automatically, and no government portal submissions are executed. All outreach must be initiated manually by the project owner from `rajivkumarsharma200@gmail.com`.

### Ethical Principles & Disclosure Standards:
1. **Authentic Student Perspective:** Accurately reflects Rajiv Sharma as a solo third-year undergraduate engineering student at MMDU Mullana who designed and built the entire working prototype with personal hardware and free-tier cloud resources.
2. **Resource Constraints Disclosed with Dignity:** Frankly acknowledges financial and infrastructure limits (e.g. inability to fund enterprise cloud servers or formal certification audits independently) while emphasizing the high engineering rigor achieved (29 automated tests, zero-trust regex security filters, Flyway migrations, Docker packaging).
3. **Strict Boundary Adherence:** Zero claims of official endorsement, live PRS integration, or commercial transaction processing. Outbound handoffs to `irctc.co.in`, `indianrail.gov.in`, and `railmadad.indianrailways.gov.in` are explicitly preserved.
4. **Credential Privacy:** Administrator evaluation passwords are not broadcast; evaluators are invited to request them via private email.

---

## 2. Attachment Specifications & Delivery Budget

| Deliverable Asset | Format | File Size | Recommended Delivery Method |
| :--- | :--- | :--- | :--- |
| **Comprehensive Proposal** | PDF (Vector, 31 Pages) | ~4.83 MB | Direct Email Attachment |
| **Stakeholder Presentation** | PDF (Vector, 11 Pages) | ~5.23 MB | Direct Email Attachment |
| **Presentation Deck (Editable)** | PPTX (11 Slides) | ~4.19 MB | Available via GitHub link or on request |
| **Total Attachment Payload** | **2 PDF Files** | **~10.06 MB** | **Well below 25 MB standard mail gateway limits** |

---

## 3. Tailored Outreach Email Drafts

### DRAFT 1: Railway Technical & Operations Leadership (CRIS & IRCTC)

* **Target Recipients:**
  * Centre for Railway Information Systems (CRIS): `contactus@cris.org.in`
  * IRCTC Corporate & IT: `corporate@irctc.com`, `cmd@irctc.co.in`
  * IRCTC Public Relations: `pr@irctc.com`
* **Subject Line:**
  `Technical Review & Architectural Guidance: RailSahayak (Independent Passenger Advisory Pre-Triage Prototype)`

```text
To: contactus@cris.org.in, corporate@irctc.com, pr@irctc.com, cmd@irctc.co.in
From: Rajiv Sharma <rajivkumarsharma200@gmail.com>
Subject: Technical Review & Architectural Guidance: RailSahayak (Independent Passenger Advisory Pre-Triage Prototype)

Respected Sir / Ma'am,

I hope this email finds you well.

My name is Rajiv Sharma, and I am currently a third-year B.Tech Computer Science and Engineering student at Maharishi Markandeshwar (Deemed to be University), Mullana, Ambala, Haryana.

Over the past several months, I have been studying the immense scale of Indian Railways digital passenger systems—specifically the 1.5 to 2.0 million daily reserved ticket transactions processed by the CRIS Passenger Reservation System (PRS) and the IRCTC Internet Ticketing portal. In analyzing public traveler interactions on social channels and consumer portals, I observed that a substantial volume of repetitive inquiries revolves around procedural confusion: interpreting waitlist categories (GNWL vs. RLWL vs. PQWL), chart preparation timelines, Section 138 travel restrictions on waitlisted e-tickets, and understanding bank settlement turnaround times (RBI T+1 framework) following failed digital transactions.

To explore how these routine informational burdens could be addressed upstream without impacting core transactional systems, I independently engineered an architectural prototype named RailSahayak.

Key Technical Properties of the RailSahayak Prototype:
1. Upstream Pre-Triage Advisory Layer: Provides plain-language explanations of ticketing and cancellation rules, routing passengers authoritatively to irctc.co.in for bookings and RailMadad for grievances.
2. Zero-Trust Payment Defense: Implements server-side regex interception that immediately blocks credit/debit card 16-digit PANs and sensitive keywords (CVV, PIN, OTP) from entering systems or logs, masking transaction references (e.g. UPI****210) to protect citizen privacy.
3. Deterministic PNR Rule Explainer: Validates 10-digit PNR syntax offline and derives Northern Zone PRS cluster conventions heuristically without issuing queries to live production databases.
4. Robust Production-Ready Stack: Built with Spring Boot 3.4.5, Java 21 LTS, and PostgreSQL 16, backed by a 29-test automated integration suite (100% passing), in-memory sliding-window rate limiting, and an append-only dual audit trail.

Live Cloud Demonstration & Codebase:
- Live Interactive Demo: https://railsahayak-backend.onrender.com
  (Evaluators can immediately test the passenger interface using username: "passenger" / password: "PassengerDemo123!". If dormant, the free cloud service takes ~25 seconds to spin up.)
- Public Open-Source Repository: https://github.com/rajivsharma8757/RailSahayak (MIT License)

As an undergraduate student developing this project independently with limited personal hardware and resources, I have strictly maintained non-invasive boundaries: RailSahayak maintains zero live connections to railway PRS/NTES production systems and claims no official endorsement.

I respectfully request your guidance and critique on:
1. Whether this pre-triage architectural approach aligns with railway technical standards and data security expectations.
2. The procedural accuracy of the rule explainer and payment diagnostic models.
3. The technical prerequisites or institutional frameworks required for an academic project to explore non-production, simulated test sandbox access in the future.

If an authorized evaluator wishes to inspect the administrative triage console and audit trail, I will gladly furnish dedicated administrative credentials upon request.

Attached to this email, please find:
1. The Comprehensive Stakeholder Proposal & Technical Report (31 Pages, PDF)
2. The Executive Stakeholder Presentation (11 Pages, PDF)

Thank you very much for your time, consideration, and dedication to India's railway infrastructure.

Yours sincerely,

Rajiv Sharma
Third-Year Undergraduate Student, B.Tech Computer Science and Engineering
Maharishi Markandeshwar (Deemed to be University), Mullana, Ambala, Haryana - 133207
Email: rajivkumarsharma200@gmail.com
Phone: +91 87579 73523
Live Demo: https://railsahayak-backend.onrender.com
GitHub: https://github.com/rajivsharma8757/RailSahayak
```

---

### DRAFT 2: Railway Innovation & Startup Programs (Railway Board & RDSO)

* **Target Recipients:**
  * Railway Board Transformation Cell: `trans_cell@rb.railnet.gov.in`
  * Railway Board Computerisation & Information Systems: `edcis@rb.railnet.gov.in`
  * RDSO Director General / Startups for Railways: `dg@rdso.railnet.gov.in`
* **Subject Line:**
  `Exploratory Submission: RailSahayak Prototype for "Startups for Railways" & Innovation Policy Review`

```text
To: trans_cell@rb.railnet.gov.in, edcis@rb.railnet.gov.in, dg@rdso.railnet.gov.in
From: Rajiv Sharma <rajivkumarsharma200@gmail.com>
Subject: Exploratory Submission: RailSahayak Prototype for "Startups for Railways" & Innovation Policy Review

Respected Sir / Ma'am,

Greetings.

I am writing to respectfully introduce RailSahayak, an independent passenger assistance and service pre-triage software prototype, and to seek exploratory evaluation under the framework of the Indian Railways Innovation Policy ("Startups for Railways") and Digital Railway initiatives.

I am a third-year B.Tech Computer Science and Engineering student at Maharishi Markandeshwar (Deemed to be University), Mullana, Ambala, Haryana. As a young engineer passionate about public transportation technology, I developed RailSahayak to investigate how software architecture can alleviate passenger friction and reduce the operational burden of routine inquiries on railway helplines.

The Problem Context:
During peak travel seasons and Tatkal windows, hundreds of thousands of passengers experience confusion regarding waitlist progression (GNWL, RLWL, PQWL), Section 138 statutory penalties, and payment auto-reversal timelines when bank accounts are debited during gateway timeouts. When unassisted, passengers frequently turn to social media or the RailMadad 139 helpline with basic procedural questions, inadvertently saturating grievance channels that are vital for onboard cleanliness, safety, and medical emergencies.

What RailSahayak Implements:
- Upstream Advisory Buffer: Provides plain-language explanations of railway reservation rules, charting milestones (4-hour advance window), and RBI T+1 refund turnaround standards.
- Zero-Trust Privacy Shield: Server-side filters prevent sensitive citizen payment credentials (16-digit card numbers, CVVs, PINs) from being saved, mitigating the widespread risk of passengers sharing banking screenshots online.
- Verifiable Engineering Rigor: Built on Java 21 LTS, Spring Boot 3.4.5, and PostgreSQL 16, with 29 automated integration tests, role-based access control (RBAC), and an append-only audit ledger.
- Strict Scope Boundaries: Operates deterministically without live PRS database access or commercial booking capability; all bookings and official grievances are explicitly directed to IRCTC and RailMadad.

Project Links for Evaluation:
- Live Cloud Application: https://railsahayak-backend.onrender.com
  (Instant public passenger review via username: "passenger" / password: "PassengerDemo123!")
- Open Source Repository: https://github.com/rajivsharma8757/RailSahayak (MIT License)

As a solo student developer working within personal financial and infrastructure limits, I am seeking:
1. Mentorship from railway operational and innovation officers on aligning this prototype with active problem statements under "Startups for Railways".
2. Guidance on eligibility criteria and formal submission procedures for student innovators under the Indian Railways Innovation Policy grant scheme.
3. Constructive evaluation of whether this pre-triage architectural pattern could be piloted on a bounded, non-commercial trial basis.

I have attached our complete 31-page Comprehensive Stakeholder Proposal & Technical Report along with the 11-page Executive Stakeholder Presentation for your review.

Thank you for your leadership in modernizing Indian Railways and for fostering grassroots technology innovation.

With highest regards,

Rajiv Sharma
Third-Year B.Tech Student (Computer Science & Engineering)
Maharishi Markandeshwar (Deemed to be University), Mullana, Ambala, Haryana - 133207
Email: rajivkumarsharma200@gmail.com
Phone: +91 87579 73523
Live Demo: https://railsahayak-backend.onrender.com
GitHub: https://github.com/rajivsharma8757/RailSahayak
```

---

### DRAFT 3: National Startup Ecosystem & Seed Grants (Startup India & AIM)

* **Target Recipients:**
  * Startup India Hub (DPIIT): `dipp-startups@nic.in`
  * Startup India Incubator Team: `sui.incubators@investindia.org.in`
  * Atal Innovation Mission (NITI Aayog): `md-aim@gov.in`, `acic-aim@gov.in`
* **Subject Line:**
  `Student Innovation Submission: RailSahayak — Seeking Incubation, Mentorship & Seed Fund (SISFS) Guidance`

```text
To: dipp-startups@nic.in, sui.incubators@investindia.org.in, md-aim@gov.in, acic-aim@gov.in
From: Rajiv Sharma <rajivkumarsharma200@gmail.com>
Subject: Student Innovation Submission: RailSahayak — Seeking Incubation, Mentorship & Seed Fund (SISFS) Guidance

Respected Program Directors and Innovation Leaders,

I hope this message finds you in high spirits.

My name is Rajiv Sharma, and I am a third-year undergraduate student pursuing B.Tech in Computer Science and Engineering at Maharishi Markandeshwar (Deemed to be University), Mullana, Ambala, Haryana.

I am writing to introduce RailSahayak—a public-service technology prototype engineered to provide structured, privacy-preserving assistance for railway passengers—and to seek mentorship, incubator affiliation, and guidance on eligibility for the Startup India Seed Fund Scheme (SISFS) or Atal Incubation Centre (AIC/ACIC) support.

About RailSahayak:
RailSahayak is designed to address a critical friction point in public transit: helping millions of everyday citizens understand complex ticketing rules, waitlist confirmation probabilities, and failed digital payment auto-reversals (under RBI frameworks) without clogging official railway grievance helplines.

Key Prototype Achievements:
1. Fully Working Full-Stack System: Developed with enterprise-grade technologies (Java 21 LTS, Spring Boot 3.4.5, PostgreSQL 16, Docker).
2. Defensive Privacy Architecture: Implements server-side zero-trust filters to intercept and block payment card numbers and security credentials, protecting citizens from digital fraud.
3. Verified Code Quality: Backed by 29 automated end-to-end integration tests, role-based access control, and live deployment on cloud infrastructure.
4. Independent & Ethical: Contains zero unverified claims, no fake live data integrations, and full compliance with public service disclaimers.

Verification & Codebase Links:
- Live Prototype Demo: https://railsahayak-backend.onrender.com
  (Public evaluation account: username "passenger" / password "PassengerDemo123!")
- Open Source Repository: https://github.com/rajivsharma8757/RailSahayak (MIT License)

Current Stage & Student Developer Context:
I have built this entire project single-handedly while managing my undergraduate coursework, relying on open-source tools, student developer credits, and personal computing hardware. However, transitioning from a verified standalone prototype into an incubator-backed venture with formal cybersecurity audits (CERT-In), high-availability cloud hosting, and institutional stakeholder engagement requires institutional backing that exceeds my personal financial capacity.

I am seeking:
1. Guidance on securing DPIIT Startup Recognition for a student-led public-utility software initiative.
2. Introduction or recommendation to partner Atal Incubation Centres (AICs) or DPIIT-approved incubators specializing in mobility, governance tech, or smart infrastructure.
3. Mentorship regarding application pathways for prototype-stage grants under the Startup India Seed Fund Scheme (SISFS).

Attached are our detailed 31-page Technical Proposal and 11-page Executive Presentation.

Thank you for your tireless commitment to nurturing student innovators across India's tier-2 and tier-3 academic institutions.

Warm regards,

Rajiv Sharma
B.Tech CSE, 3rd Year | Maharishi Markandeshwar (Deemed to be University), Mullana, Haryana
Contact: rajivkumarsharma200@gmail.com | +91 87579 73523
Live Demo: https://railsahayak-backend.onrender.com
GitHub: https://github.com/rajivsharma8757/RailSahayak
```

---

### DRAFT 4: Academic & State Innovation Ecosystem (MMDU Mullana & Startup Haryana)

* **Target Recipients:**
  * Principal / Dean, MMEC, MMDU Mullana: `principal.mmec@mmumullana.org`
  * Central University Administration / IIC: `info@mmumullana.org`
  * Startup Haryana Cell (DITECH, Govt. of Haryana): `startupharyanacell@gmail.com`
  * HARTRON Managing Director: `mdhartron@gmail.com`
* **Subject Line:**
  `Student Project Demonstration: RailSahayak — Request for College Incubation, Server Sponsorship & Haryana Startup Grant Support`

```text
To: principal.mmec@mmumullana.org, info@mmumullana.org, startupharyanacell@gmail.com, mdhartron@gmail.com
From: Rajiv Sharma <rajivkumarsharma200@gmail.com>
Subject: Student Project Demonstration: RailSahayak — Request for College Incubation, Server Sponsorship & Haryana Startup Grant Support

Respected Authorities and Faculty Mentors,

Respected Sir / Ma'am,

I am Rajiv Sharma, a proud third-year B.Tech student in the Department of Computer Science and Engineering at Maharishi Markandeshwar Engineering College (MMEC), MMDU, Mullana.

I am writing to present RailSahayak, an independent software engineering prototype I have developed to solve real-world passenger assistance and grievance pre-triage challenges in Indian Railways. I would like to request institutional endorsement, guidance from our Institution's Innovation Council (IIC), campus server resources, and support in applying for seed funding under the Haryana Startup Policy 2022.

Project Summary:
RailSahayak acts as an intelligent, pre-triage advisory buffer that helps railway travelers understand waitlist confirmation rules (GNWL, RLWL, PQWL), Section 138 statutory regulations, and banking turnaround times (RBI T+1 framework) for failed online ticket payments. It incorporates server-side security to block citizens from inadvertently sharing sensitive debit/credit card details or OTPs in support requests.

Technical Highlights:
- Built with Java 21, Spring Boot 3.4.5, and PostgreSQL 16.
- 29 automated JUnit integration tests covering security, RBAC, and rate limiting (100% pass rate).
- Live cloud deployment accessible to any evaluator over HTTPS.
- Full code repository and technical documentation published under MIT License.

Links to Evaluate My Work:
- Live Demo: https://railsahayak-backend.onrender.com
  (Login: username "passenger" / password "PassengerDemo123!")
- Code Repository: https://github.com/rajivsharma8757/RailSahayak

Why I am Reaching Out to MMDU & Startup Haryana:
Developing this project as a student has been an immense learning experience, but taking it to the next stage requires institutional resources:
1. MMDU Incubation & Server Support: I would be deeply grateful for the opportunity to demonstrate RailSahayak to our respected faculty and IIC coordinators, and to request access to campus server/lab infrastructure to run staging benchmarks beyond free-tier cloud limits.
2. University Endorsement: Support and nomination from MMDU for state and national hackathons, innovation challenges, and student enterprise exhibitions.
3. Startup Haryana Seed Capital Assistance: Guidance from the Startup Haryana Cell on registering under the Haryana Startup Policy 2022 to seek student entrepreneurship assistance and seed capital grant support for prototype validation and CERT-In security audits.

I have attached my comprehensive 31-page Technical Proposal and the 11-slide Executive Presentation for your kind review. I am available at your convenience for an in-person or virtual demonstration.

Thank you very much for encouraging innovation and entrepreneurship at MMDU and across Haryana.

Respectfully yours,

Rajiv Sharma
Roll No. / Student ID: 3rd Year, B.Tech Computer Science & Engineering
Maharishi Markandeshwar Engineering College (MMEC)
Maharishi Markandeshwar (Deemed to be University), Mullana, Ambala, Haryana - 133207
Email: rajivkumarsharma200@gmail.com
Phone: +91 87579 73523
Live Demo: https://railsahayak-backend.onrender.com
GitHub: https://github.com/rajivsharma8757/RailSahayak
```

---

## 4. Phased Outreach Schedule & Cadence Plan

```mermaid
flowchart TD
    subgraph Phase 1 [Days 1–3: Academic & State Foundation]
        A1[MMDU Mullana IIC & Leadership] --> A2[In-person / internal email]
        B1[Startup Haryana Cell & HARTRON] --> B2[State portal registration & email]
    end

    subgraph Phase 2 [Days 4–7: National Startup Programs]
        C1[Startup India Hub / DPIIT] --> C2[DPIIT recognition filing & SISFS inquiry]
        D1[Atal Innovation Mission NITI Aayog] --> D2[AIC/ACIC matchmaking inquiry]
    end

    subgraph Phase 3 [Days 8–12: Railway Innovation Cells]
        E1[RDSO Startups for Railways Portal] --> E2[Innovation challenge alignment]
        F1[Railway Board Transformation Cell] --> F3[Formal proposal submission]
    end

    subgraph Phase 4 [Days 13–16: Railway Technical Systems]
        G1[CRIS Software Architecture Group] --> G2[Technical architecture review request]
        H1[IRCTC E-Ticketing & Grievance Group] --> H2[Payment diagnostic pre-triage review]
    end

    Phase 1 --> Phase 2 --> Phase 3 --> Phase 4
```

### Outreach Rules & Cadence Table:

| Stage | Target Stakeholder Group | Objective | Follow-up Window |
| :--- | :--- | :--- | :--- |
| **Stage 1 (Days 1–3)** | MMDU Mullana (MMEC) & Startup Haryana | Secure internal faculty endorsement, campus test servers, and state student entrepreneurship registration. | 3–5 working days (in person on campus) |
| **Stage 2 (Days 4–7)** | Startup India (DPIIT) & Atal Innovation Mission (NITI Aayog) | Apply for DPIIT recognition, request incubator matchmaking, and explore SISFS prototype grant eligibility. | 10–14 working days |
| **Stage 3 (Days 8–12)** | Railway Board Transformation Cell & RDSO ("Startups for Railways") | Submit proposal under the Railway Innovation Policy; map to passenger service problem statements. | 14 working days |
| **Stage 4 (Days 13–16)** | CRIS & IRCTC IT Systems Leadership | Request software architecture walkthrough and explore prerequisites for non-production sandbox data feeds. | 14 working days |

### Follow-up Protocol:
- **Maximum 1 polite follow-up per organization**, sent exactly 10–14 business days after initial contact if no acknowledgment is received.
- **Do not send automated reminders.**
- **If an organization replies requesting a live demo or administrative access**, respond within 24 hours with dedicated reviewer credentials and availability for a Google Meet / Zoom walkthrough.
