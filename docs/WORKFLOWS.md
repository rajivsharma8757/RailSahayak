# RailSahayak — End-to-End User Journeys & Workflows

## 1. Passenger Journey Workflow

RailSahayak guides travelers through routine railway inquiries using transparent procedural workflows that minimize friction while maintaining authoritative external boundaries.

```mermaid
flowchart TD
    Start([Passenger Visits RailSahayak]) --> Intent{Identify Intent}
    
    Intent -->|Find Trains| Search[Smart Train Finder]
    Search --> InputStations[Enter Source & Destination]
    InputStations --> ValidateStations{Source != Destination?}
    ValidateStations -->|No| ErrStation[Display HTTP 400 Bad Request]
    ValidateStations -->|Yes| FilterClass[Select Travel Class]
    FilterClass --> QuerySchedules[Retrieve Trunk Route Schedules]
    QuerySchedules --> ShowResults[Display Train Details & Departure Times]
    ShowResults --> OfficialBooking[Click Authoritative Booking Link: irctc.co.in]

    Intent -->|Explain PNR| PNR[PNR Explainer Engine]
    PNR --> EnterPNR[Enter 10-Digit PNR]
    EnterPNR --> CheckPNR{10 Digits & Numeric?}
    CheckPNR -->|No| ErrPNR[Display HTTP 400 Bad Request]
    CheckPNR -->|Yes| DecodeZone[Derive PRS Cluster Heuristic]
    DecodeZone --> ExplainStatus[Translate CNF / RAC / GNWL / PQWL Rules]
    ExplainStatus --> WarnSec138[Display Section 138 Cancellation Warning]

    Intent -->|Payment Issue| PayHelp[Payment Help Diagnoser]
    PayHelp --> InputPay[Select Payment Method & Enter Reference]
    InputPay --> SecretCheck{Regex Detects Card / PIN / OTP?}
    SecretCheck -->|Yes| RejectSecret[HTTP 400 Bad Request: Secrets Blocked]
    SecretCheck -->|No| MaskRef[Sanitize & Mask Reference: UPI****098]
    MaskRef --> ExplainTAT[Provide RBI TAT Reversal Windows & Next Steps]

    Intent -->|Need Assistance| SupportCase[Support Case Engine]
    SupportCase --> AuthCheck{Authenticated?}
    AuthCheck -->|No| BasicAuthPrompt[HTTP Basic Login]
    AuthCheck -->|Yes| SubmitCase[Enter Category & Description]
    SubmitCase --> GenID[Assign RS-XXXXXX Tracking ID]
    GenID --> TrackTimeline[Track Progress via Event Timeline]
```

---

## 2. Complaint & Case Lifecycle State Machine

Support cases in RailSahayak follow a strictly governed lifecycle. Status transitions are restricted to staff holding `ROLE_ADMIN` and generate immutable audit log records.

```mermaid
stateDiagram-v2
    [*] --> OPEN: Passenger Creates Support Case (POST /api/v1/cases)
    
    OPEN --> IN_PROGRESS: Admin Assigns & Initiates Investigation (PATCH /api/v1/admin/cases/{id}/status)
    note right of IN_PROGRESS
        Atomic CaseEvent appended
        AuditLog entry recorded with actor & timestamp
    end note

    IN_PROGRESS --> RESOLVED: Admin Completes Advisory / Resolution (PATCH /api/v1/admin/cases/{id}/status)
    note right of RESOLVED
        Resolution notes captured
        Passenger views final outcome
    end note

    OPEN --> RESOLVED: Direct Resolution (Procedural Clarification Provided)
    
    RESOLVED --> [*]
```

---

## 3. Administrative Triage & Dual Audit Workflow

```mermaid
sequenceDiagram
    autonumber
    actor Admin as Railway Support Officer (ROLE_ADMIN)
    participant API as RailSahayak Admin API
    participant DB as PostgreSQL 16
    actor Passenger as Passenger (ROLE_PASSENGER)

    Admin->>API: GET /api/v1/admin/cases (Optional Status Filter)
    API->>DB: Query support_cases by status
    DB-->>API: List of Support Cases
    API-->>Admin: Display Case Triage Queue

    Admin->>API: PATCH /api/v1/admin/cases/{id}/status (status="RESOLVED", note="Advisement completed")
    API->>API: Validate ROLE_ADMIN & Status Enum
    API->>DB: Update support_cases.status = "RESOLVED"
    API->>DB: INSERT into case_events (case_id, actor, event_type, note)
    API->>DB: INSERT into audit_logs (actor, action, resource_id, detail)
    DB-->>API: Transaction Committed (Atomic)
    API-->>Admin: HTTP 200 OK (Updated Case View)

    Passenger->>API: GET /api/v1/cases/{id}
    API->>DB: Query case matching id AND owner = authenticated_user
    DB-->>API: Case Details + Event Timeline
    API-->>Passenger: HTTP 200 OK (Status: RESOLVED, Timeline with notes)
```

---

## 4. Payment Diagnostic & Settlement Guidance Workflow

When a passenger experiences a failed transaction or payment deduction without ticket confirmation:

1. **Input Submission:** Passenger selects the payment mode (UPI, Debit/Credit Card, Net Banking) and issue type (`deducted`, `pending`, `failed`), providing a transaction reference.
2. **Defensive Scrubbing:** The system evaluates the reference string with regex. If card PANs, PINs, OTPs, or passwords are detected, the request is immediately aborted with HTTP 400, protecting citizen financial secrets.
3. **Reference Masking:** Safe reference strings are masked (e.g. `UPI****098`).
4. **Regulatory Advice:** The system returns tailored advice based on Reserve Bank of India (RBI) Circular `DPSS.CO.PD No.629/02.01.014/2019-20`:
   - **UPI:** Auto-reversal within **T+1 business day**.
   - **Wallets / PPIs:** Auto-reversal within **T+1 calendar day**.
   - **E-Commerce / Card Transactions:** Auto-reversal within **T+5 calendar days**.
   - **Compensation:** ₹100 per day payable to customer if reversal exceeds TAT.
   - **Duplicate Booking Warning:** Passengers are explicitly cautioned against immediate re-booking attempts during Tatkal surge windows to prevent repeated bank deductions.
