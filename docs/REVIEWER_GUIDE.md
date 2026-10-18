# RailSahayak — Technical Reviewer Guide & Evaluation Handbook

> **Project Identity:** RailSahayak (Independent Passenger Assistance & Service Support Prototype)  
> **Repository:** [https://github.com/rajivsharma8757/RailSahayak](https://github.com/rajivsharma8757/RailSahayak)  
> **Contact / Maintainer:** Rajiv Sharma (`rajivkumarsharma200@gmail.com`)  
> **Evidentiary Standard:** Evaluator Guidance Document (October 2026)

---

## 1. Executive Notice & Boundary Disclaimers

**RailSahayak** is an independent, proof-of-concept software prototype engineered to demonstrate modern pre-triage architectural patterns for railway passenger assistance.

- **Independent Initiative:** RailSahayak has **not** been commissioned, endorsed, or approved by the Ministry of Railways, IRCTC, or the Centre for Railway Information Systems (CRIS).
- **No Live Production Connections:** The prototype maintains **no live network access** to the Passenger Reservation System (PRS), National Train Enquiry System (NTES), or official payment gateways.
- **No Financial Execution:** No live payment card transactions, banking settlements, ticket bookings, or cancellations are executed. All train schedules, PNR routing zones, and refund timelines represent deterministic sample fixtures and regulatory turnaround frameworks.

---

## 2. Reviewer Testing Paths Overview

The application implements strict Role-Based Access Control (RBAC) via Spring Security 6.4.5. Reviewers can evaluate the application through two distinct interfaces:

| Property | Passenger Dashboard | Administrator Dashboard |
| :--- | :--- | :--- |
| **Target Role** | Railway passenger seeking advisory support | Railway customer service / station operations staff |
| **Access URL** | `/` (Overview, Train Finder, PNR, Payment, Cases) | `/#admin` (Admin Case Console & Audit Logs) |
| **Demo Username** | `passenger` | `admin` |
| **Demo Password** | `PassengerDemo123!` | `AdminDemo123!` |
| **Assigned Authority** | `ROLE_PASSENGER` | `ROLE_ADMIN` |
| **Data Scope** | User's own submitted support cases only | System-wide case queue, status mutator, and audit trail |
| **Admin Route Access** | **Blocked (HTTP 403 Forbidden)** | **Granted (HTTP 200 OK)** |

> [!SECURITY]
> **Demo Account Safety:** These demo accounts are restricted in-memory identities configured strictly for evaluation. They do not access production databases or external networks. In production, authentication must be replaced with an enterprise OAuth2/OIDC or railway SSO provider.

---

## 3. Evaluation Setup & Access Methods

### Option A: Local Standalone Evaluation (Recommended / Instant)

The application includes an embedded in-memory database fallback (PostgreSQL compatibility mode) allowing complete evaluation in under 30 seconds with zero external database setup:

1. **Prerequisites:** Java 21 LTS (or higher) and Apache Maven 3.9+.
2. **Clone the Repository:**
   ```bash
   git clone https://github.com/rajivsharma8757/RailSahayak.git
   cd RailSahayak
   ```
3. **Run the Application:**
   ```bash
   mvn clean spring-boot:run
   ```
   *Alternative with packaged JAR:*
   ```bash
   mvn package -DskipTests
   java -jar target/railsahayak-backend-0.1.0.jar --spring.datasource.url="jdbc:h2:mem:railsahayak;MODE=PostgreSQL;DATABASE_TO_LOWER=TRUE;DEFAULT_NULL_ORDERING=HIGH;DB_CLOSE_DELAY=-1;INIT=CREATE DOMAIN IF NOT EXISTS TIMESTAMPTZ AS TIMESTAMP WITH TIME ZONE" --spring.datasource.driver-class-name=org.h2.Driver --spring.datasource.username=sa --spring.datasource.password=""
   ```
4. **Access the Web Interface:** Open `http://localhost:8081` in any modern web browser.

### Option B: Local Docker Compose Evaluation

For testing with full container orchestration and native PostgreSQL 16:
```bash
docker compose up --build
```
The backend starts on `http://localhost:8081` connected to the PostgreSQL container on port `5432`.

### Option C: 1-Click Cloud Deployment via Render Blueprint

The repository contains a declarative [`render.yaml`](../render.yaml) blueprint:
* **Deploy Link:** [https://render.com/deploy?repo=https://github.com/rajivsharma8757/RailSahayak](https://render.com/deploy?repo=https://github.com/rajivsharma8757/RailSahayak)
* **Status:** The blueprint is ready for instant cloud deployment. When an authorized reviewer connects a Render account, Render automatically provisions the managed PostgreSQL database and Eclipse Temurin Java 21 runtime container.

---

## 4. Testing Path 1: Passenger Dashboard Walkthrough

### Step 1: Sign in as Passenger
1. Navigate to `http://localhost:8081/` (or public URL).
2. In the demo sign-in card, enter:
   * **Username:** `passenger`
   * **Password:** `PassengerDemo123!`
3. Click **Connect to backend**. The top navigation bar confirms: `passenger · Passenger`.

### Step 2: Smart Train Finder
* **Navigation:** Click **Smart Train Finder** in the sidebar.
* **Input:**
  * **From Station:** `New Delhi`
  * **To Station:** `Patna Junction`
  * **Journey Date:** Select any future date (e.g. `2026-10-25`).
  * **Class:** `3A`
* **Click:** **Find trains**.
* **Expected Result:** Renders sample train cards (e.g., *Sample Howrah Rajdhani Express*) with departure times, platform estimates, and an immutable advisory banner directing passengers to `irctc.co.in` for live seat availability and official booking.

### Step 3: PNR Guide & Rule Explainer
* **Navigation:** Click **PNR Guide** in the sidebar.
* **Input:**
  * **10-Digit PNR:** `2418901234`
  * **Status Code:** `GNWL` (or select `RAC`, `CNF`)
* **Click:** **Explain Status & Rules**.
* **Expected Result:**
  * Displays derived PRS server cluster: `Northern Zone (New Delhi PRS Server)`.
  * Clarifies General Waitlist operational rules, charting deadlines (4 hours prior to scheduled departure), and the Section 138 statutory warning regarding fully waitlisted e-tickets.

### Step 4: Payment Help & Zero-Trust Secret Defense
* **Navigation:** Click **Payment Help** in the sidebar.
* **Security Test (Sensitive Data Rejection):**
  * **Issue Category:** `Money debited, no ticket`
  * **Payment Method:** `Debit / Credit Card`
  * **Transaction Reference:** Enter `My card number is 4111 2222 3333 4444 please refund`
  * **Click:** **Diagnose Issue**.
  * **Expected Result:** The server immediately intercepts the 16-digit card pattern and rejects the submission with **HTTP 400 Bad Request**: *Sensitive payment credentials detected and blocked*.
* **Valid Diagnostic Test:**
  * Replace the reference with `UPI9876543210`.
  * Click **Diagnose Issue**.
  * **Expected Result:** Returns RBI turnaround time guidance (**T + 1 business day** auto-reversal framework) and masks the reference string as `UPI****210`.

### Step 5: Submit a Test Passenger Support Case
* **Navigation:** Click **Complaint Help** in the sidebar.
* **Form Entry:**
  * **Category:** Select `Payment confirmation delay`.
  * **Description:** Enter `Payment debited via UPI, PNR generation failed. Seeking guidance.`
* **Click:** **Submit Complaint**.
* **Expected Result:** Server persists the record and returns a unique public case identifier (e.g., `RS-EE26BD1A`) with initial status `OPEN`. The case appears in the passenger's personal history list.

---

## 5. Testing Path 2: Administrator Dashboard Walkthrough

### Step 1: Sign in as Administrator
1. Click **Sign out** in the top bar.
2. Enter the administrator credentials:
   * **Username:** `admin`
   * **Password:** `AdminDemo123!`
3. Click **Connect to backend**.
4. The top bar updates to `admin · Admin`, and the **Admin Dashboard** navigation item unlocks in the sidebar.

### Step 2: Verify RBAC Route Isolation (Security Verification)
* When authenticated as `passenger`, any direct HTTP request to `/api/v1/admin/cases` or `/api/v1/admin/audit-logs` returns **HTTP 403 Forbidden**.
* When authenticated as `admin`, the administrative endpoints return **HTTP 200 OK**.

### Step 3: Manage Case Lifecycle
1. Click **Admin Dashboard** in the sidebar.
2. The central table displays all submitted cases across the system.
3. Locate the case created in Path 1 (e.g., `RS-EE26BD1A`).
4. Click on the case row to inspect the detail modal.
5. In the status dropdown, change status from `Open` to `In progress`.
6. Add staff note: `Verifying payment transaction reference with acquiring bank switch.`
7. Click **Update case**.
8. **Expected Result:** The case status badge transitions to `In progress`, and a timestamped `CaseEvent` is permanently appended to the case timeline.

### Step 4: Inspect System Audit Trail
1. Scroll down to the **System Audit Log** section on the Admin Dashboard (or query `GET /api/v1/admin/audit-logs`).
2. **Expected Result:** Displays the append-only audit trail logging the action (`STATUS_CHANGED`), actor (`admin`), resource type (`CASE`), case public ID, and timestamp.

---

## 6. Automated Test Suite Verification (29 Passing Tests)

Reviewers can independently verify the automated integration test suite by executing:
```bash
mvn test
```
The test suite in [`RailSahayakApplicationTests.java`](../src/test/java/in/railsahayak/RailSahayakApplicationTests.java) executes 29 automated assertions across 7 core functional areas:

```text
[INFO] Running in.railsahayak.RailSahayakApplicationTests
[INFO] Tests run: 29, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 17.51 s
[INFO] BUILD SUCCESS
```

### Coverage Matrix
1. **Public Ingress & Security (Tests 1–4):** Public health check (`/api/v1/health`), unauthenticated request rejection (HTTP 401), passenger authentication.
2. **RBAC Route Isolation (Tests 5–7):** Rejection of passenger requests to `/api/v1/admin/**` (HTTP 403), admin authorization verification.
3. **Persistence & Data Isolation (Tests 8–10):** Validation of required fields, multi-turn case creation, cross-user case isolation.
4. **Case Lifecycle State Machine (Tests 11–13):** Transition validation (`OPEN` $\to$ `IN_PROGRESS` $\to$ `RESOLVED`), rejection of invalid transitions.
5. **Train Finder Route Matching (Tests 14–17):** Deterministic route filtering, identical source-destination rejection, date format enforcement.
6. **Payment Help & Zero-Trust Secret Cleansing (Tests 18–21):** Rejection of 16-digit card numbers, rejection of security keywords (`cvv`, `otp`, `pin`), reference masking.
7. **Edge Defense & Rate Limiter (Tests 22–29):** Sliding-window rate limiter (HTTP 429 after 300 req/min), proxy header (`X-Forwarded-For`) validation, security headers (`X-Content-Type-Options: nosniff`, `X-Frame-Options: SAMEORIGIN`).

---

## 7. Known Prototype Limitations & Future Roadmap

| Capability | Current Prototype Implementation | Proposed Production Pathway |
| :--- | :--- | :--- |
| **Authentication** | In-memory demo credentials (`passenger` / `admin`) | OAuth2 / OIDC, IRCTC SSO, or Indian Railways enterprise IAM |
| **Train Schedules** | Static sample fixtures for demonstration | Authoritative CRIS NTES real-time API integration |
| **PNR Status** | Heuristic PRS cluster deduction from first digit | CRIS PRS read-only sandbox / production API integration |
| **Payment Triage** | Regulatory advisory based on RBI TAT framework | IRCTC merchant payment gateway reconciliation callbacks |
| **Case Escalation** | Local PostgreSQL database persistence | Official RailMadad CRM integration via authorized API |

---

## 8. Evidentiary Inquiries & Technical Review Feedback

For questions regarding this architecture, security specifications, or scheduling an exploratory technical review:
* **Lead Engineer:** Rajiv Sharma
* **Contact Email:** [rajivkumarsharma200@gmail.com](mailto:rajivkumarsharma200@gmail.com)
* **GitHub Repository:** [https://github.com/rajivsharma8757/RailSahayak](https://github.com/rajivsharma8757/RailSahayak)
