# RailSahayak — 5 to 10 Minute Live Demonstration Script

**Document Reference:** RS-DEMO-2026-V1  
**Target Audience:** Railway Stakeholders, Hackathon Evaluators, Technical Reviewers  
**Prerequisites:** Backend running on `http://localhost:8081`, PostgreSQL running via Docker  
**Estimated Run Time:** 7 minutes  

> [!WARNING]
> **Privacy and Zero-Trust Compliance Notice:**
> - Perform this demonstration strictly using the provided synthetic sample data.
> - Never enter real passenger PNRs, Aadhaar numbers, real UPI references, debit/credit card numbers, PINs, or OTPs.

---

## Demonstration Timeline Overview

| Step | Time | Segment | Focus Area |
| :--- | :--- | :--- | :--- |
| **1** | 0:00 - 1:00 | System Architecture & Passenger Sign-In | Role-based authentication & clean landing view |
| **2** | 1:00 - 2:15 | Smart Train Finder | Route search, prototype boundary, booking links |
| **3** | 2:15 - 3:30 | Zero-Trust Payment Help | Immediate diagnostic, settlement advice, secret rejection |
| **4** | 3:30 - 4:30 | Regulatory PNR Guide | PRS zone derivation, charting logic, Section 138 rules |
| **5** | 4:30 - 5:30 | Passenger Complaint Submission | Case registration, unique `RS-XXXXXX` reference, timeline |
| **6** | 5:30 - 6:30 | Admin Operations Console | Role transition, status patch, investigation note & audit trail |
| **7** | 6:30 - 7:00 | Security Controls & Wrap-Up | Rate limiting, correlation IDs, disaster recovery scripts |

---

## Step-by-Step Script

### Step 1: System Overview & Passenger Sign-In (0:00 – 1:00)

**Presenter Talking Points:**
> *"Welcome to RailSahayak, an intelligent railway passenger assistance platform engineered to complement Indian Railways services. The platform is designed to resolve passenger anxiety surrounding payment failures, waitlist regulations, and grievance tracking before they escalate to crowded helpdesks."*

**Action:**
1. Open web browser to: **`http://localhost:8081/`**.
2. Point out the clean **RailSahayak** branding (strictly no third-party branding).
3. Scroll to the authentication bar.
4. Click the pre-filled **"Passenger Sign In"** button (Username: `passenger`, Password: `PassengerDemo123!`).
5. Click **"Sign In"**.

**Expected Result:**
- Authentication banner displays: `Authenticated as: passenger (ROLE_PASSENGER)`.
- Passenger interface features become accessible: Smart Train Finder, Payment Help, PNR Guide, and My Complaints.
- Admin dashboard tab remains hidden, preserving strict role-based separation.

---

### Step 2: Smart Train Finder (1:00 – 2:15)

**Presenter Talking Points:**
> *"Let's examine how a passenger plans a journey. Notice our prominent boundary declaration: RailSahayak explicitly marks seat availability as prototype sample data and directs passengers to book exclusively on official IRCTC portals."*

**Action:**
1. Click the **"Smart Train Finder"** tab.
2. Select or enter:
   - **From Station:** `New Delhi`
   - **To Station:** `Patna Junction`
   - **Journey Date:** Select any upcoming date (e.g. `2026-10-25`)
   - **Travel Class:** `3A`
3. Click **"Search Trains"**.

**Expected Result:**
- Loading indicator appears briefly, followed by the train schedule card:
  - Train: `Sample Howrah Rajdhani Express (via PNBE) (DEMO-12302)`
  - Departure: `16:50`, Arrival: `03:50` (11h duration)
  - Class: `3A`
  - Prominent badge: `PROTOTYPE / DEMO DATA`
- Button links directly to official Indian Railways booking portal: `Book on Official IRCTC Portal (irctc.co.in)`.
- Attempting to search with identical source and destination (`New Delhi` to `New Delhi`) triggers a client-side and server-side validation error: *"Source and destination stations cannot be identical."*

---

### Step 3: Zero-Trust Payment Help (2:15 – 3:30)

**Presenter Talking Points:**
> *"One of the highest sources of passenger distress during peak booking windows (like Tatkal) is when an account is debited but no ticket is confirmed. Passengers often panic and make duplicate bookings. RailSahayak's Payment Help module delivers instant, structured reassurance grounded in standard banking settlement rules."*

**Action:**
1. Click the **"Payment Help"** tab.
2. Fill out the diagnostic form:
   - **Payment Issue:** `Money deducted, ticket not confirmed`
   - **Payment Method:** `UPI`
   - **Purpose:** `Ticket booking`
   - **Transaction Reference (Optional):** `UPI987654321098`
3. Click **"Diagnose Payment Issue"**.

**Expected Result:**
- Instant structured diagnostic card displays:
  - **Issue Diagnosis:** `Money deducted, ticket not confirmed`
  - **Action Recommendation:** `WAIT_FOR_SETTLEMENT`
  - **Reference Masking:** `Ref recorded for guidance context only: UPI****098` (strictly masked!)
  - **Actionable Steps:** Detailed bilingual checklist (e.g. check IRCTC Failed Transactions tab, allow 3-5 bank working days for auto-reversal, avoid duplicate attempts).
- **Security Check:** Try entering `1234-5678-9012-3456` or the word `otp` into the reference box. Notice the application actively rejects the input: *"Sensitive payment secret detected in reference. Never enter card numbers, PINs, OTPs, CVVs, or passwords."*

---

### Step 4: Regulatory PNR Guide (3:30 – 4:30)

**Presenter Talking Points:**
> *"Passengers often struggle to understand waitlist abbreviations or charting timelines. Rather than scraping CRIS databases without permission, RailSahayak provides an educational explainer and links passengers to verified government resources."*

**Action:**
1. Click the **"PNR Guide"** tab.
2. Enter synthetic sample PNR: `2345678901` (First digit `2` indicates Northern Zone).
3. Select status code: `RAC (Reservation Against Cancellation)`.
4. Click **"Explain PNR & Rules"**.

**Expected Result:**
- Diagnostic result card displays:
  - **Masked PNR:** `234****901`
  - **Derived PRS Server:** `Heuristic cluster: Northern Zone (NDLS PRS) [Derived from first-digit routing convention, not live PRS lookup]`
  - **Travel Eligibility:** `Permitted to board reserved coach with shared sitting accommodation.`
  - **Charting Rules:** Clearly explains the 1st chart (~4 hours before departure) and 2nd chart (30-50 minutes before departure).
  - **Legal Reminder:** Emphasizes that fully waitlisted e-tickets are automatically cancelled and boarding reserved coaches on waitlisted e-tickets violates Section 138 of the Railways Act.
  - **Official Verification Links:** Direct links to `indianrail.gov.in`, `irctc.co.in`, SMS `139`, and `railmadad.indianrailways.gov.in`.

---

### Step 5: Passenger Complaint Submission (4:30 – 5:30)

**Presenter Talking Points:**
> *"When a passenger requires assistance, they can file a complaint directly in the application. Let's register a sample complaint and observe the audit trail."*

**Action:**
1. Click the **"File Complaint"** tab.
2. Select:
   - **Category:** `Refund follow-up`
   - **Description:** `Payment debited via UPI on 15-Oct during Tatkal window. Need status update on auto-refund reversal.`
3. Click **"Submit Complaint"**.

**Expected Result:**
- Immediate confirmation banner: `Complaint registered successfully! Case Reference: RS-XXXXXX`.
- The case appears immediately in the passenger's **"My Complaints"** list with status `OPEN`.
- Click **"View Timeline"**: Opens an interactive modal showing the initial event:
  - Event: `CASE_CREATED`
  - Actor: `passenger`
  - Timestamp: Current Indian Standard Time (`Asia/Kolkata`)

---

### Step 6: Admin Operations & Audit Trail (5:30 – 6:30)

**Presenter Talking Points:**
> *"Now let's switch roles to a railway operations administrator. Notice how the UI and backend dynamically enforce role-based access control."*

**Action:**
1. Scroll up and click **"Sign Out"**.
2. Click **"Admin Sign In"** (Username: `admin`, Password: Enter the private evaluation credential provided by the maintainer).
3. Click **"Sign In"**.
4. Observe that the navigation bar now displays the **"Admin Operations Console"** with active metric counters (Total Cases, Open, In Progress, Resolved).
5. Locate the newly created complaint in the Admin Cases queue.
6. Click **"Update Status"**.
7. In the status modal:
   - Select New Status: `IN_PROGRESS`
   - Enter Investigation Note: `Verified transaction reference with payment gateway switch; auto-refund settlement queued.`
   - Click **"Save Status Update"**.
8. Scroll to the **"System Audit Trail"** table at the bottom of the page.

**Expected Result:**
- Case status updates immediately to `IN_PROGRESS`.
- Case Timeline modal reflects the transition with the admin's custom investigation note.
- System Audit Log records the event atomically:
  - Timestamp, Actor: `admin`, Action: `STATUS_CHANGED`, Public ID: `RS-XXXXXX`, Detail: `OPEN -> IN_PROGRESS: Verified transaction reference with payment gateway switch; auto-refund settlement queued.`

---

### Step 7: Security Controls & Summary (6:30 – 7:00)

**Presenter Talking Points:**
> *"To conclude, RailSahayak is engineered with production-ready defensive security:"*
> 1. *Defensive HTTP Headers: `X-Content-Type-Options: nosniff`, `X-Frame-Options: SAMEORIGIN`, and strict referrer policy.*
> 2. *Sliding-Window Rate Limiting: 300 requests/minute per IP returning HTTP 429 with trusted proxy verification.*
> 3. *End-to-End Tracing: Every request receives a unique `X-Correlation-ID` (`rs-xxxxxxxx`) traced across logs and HTTP headers.*
> 4. *Zero Data Loss: 100% of data is stored in PostgreSQL and backed up using automated idempotent backup/restore scripts.*
> 5. *Comprehensive Testing: 29 automated integration tests running with 100% pass rate.*

**Closing Statement:**
> *"RailSahayak is ready for a controlled, sandboxed pilot in collaboration with the Center for Railway Information Systems and the Ministry of Railways. Thank you."*
