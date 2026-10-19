# RailSahayak — REST API Reference Specification

All endpoints are hosted under the base URI `/api/v1`.  
Default development base URL: `http://localhost:8081/api/v1`

---

## 1. Authentication & Security Headers

| Requirement | Description |
| :--- | :--- |
| **Authentication Scheme** | HTTP Basic Authentication (`Authorization: Basic <base64-credentials>`) |
| **Public Endpoints** | `/api/v1/health`, `/`, `/index.html`, `/static/**` |
| **Passenger Endpoints** | Require `ROLE_PASSENGER` or `ROLE_ADMIN` (e.g. `passenger:PassengerDemo123!`) |
| **Admin Endpoints** | Require `ROLE_ADMIN` (credentials provided privately to authorized evaluators) |
| **Correlation Tracking** | Clients may send `X-Correlation-ID`. The service propagates this identifier across all logs and response headers. |

---

## 2. API Endpoints Catalog

### 2.1 Public Health Probe

- **Endpoint:** `GET /api/v1/health`
- **Access:** Public (No authentication required)
- **Description:** Returns service status, UTC timestamp, database migration health, and rate-limiting configuration.

#### Request Example
```bash
curl -X GET http://localhost:8081/api/v1/health
```

#### Response Example (HTTP 200 OK)
```json
{
  "status": "UP",
  "service": "railsahayak-backend",
  "version": "0.1.0",
  "timestamp": "2026-10-18T17:35:10Z",
  "database": "CONNECTED",
  "rateLimiter": {
    "enabled": true,
    "limitPerMinute": 300
  }
}
```

---

### 2.2 Smart Train Search

- **Endpoint:** `POST /api/v1/train-search`
- **Access:** Authenticated (`ROLE_PASSENGER` or `ROLE_ADMIN`)
- **Description:** Deterministic route search across high-density Indian Railways trunk routes. Rejects identical source/destination pairs with HTTP 400.

#### Request Payload
```json
{
  "from": "NDLS",
  "to": "PNBE",
  "date": "2026-10-25",
  "travelClass": "3A"
}
```

#### Response Example (HTTP 200 OK)
```json
{
  "source": "NDLS",
  "destination": "PNBE",
  "journeyDate": "2026-10-25",
  "requestedClass": "3A",
  "trains": [
    {
      "trainName": "Patna Tejas Rajdhani Express",
      "trainCode": "12310",
      "departure": "17:10",
      "arrival": "05:15",
      "duration": "12h 05m",
      "availableClasses": ["1A", "2A", "3A"]
    },
    {
      "trainName": "Sampoorna Kranti Express",
      "trainCode": "12394",
      "departure": "17:30",
      "arrival": "06:50",
      "duration": "13h 20m",
      "availableClasses": ["1A", "2A", "3A", "SL"]
    }
  ],
  "disclaimer": "Advisory schedules only. For live seat booking, visit official IRCTC portal: https://www.irctc.co.in/"
}
```

---

### 2.3 PNR Procedural Explainer

- **Endpoint:** `POST /api/v1/pnr-guide/explain`
- **Access:** Authenticated (`ROLE_PASSENGER` or `ROLE_ADMIN`)
- **Description:** Validates 10-digit numeric PNR, derives originating PRS server zone heuristic, and explains status codes and Section 138 rules.

#### Request Payload
```json
{
  "pnrNumber": "2418901234"
}
```

#### Response Example (HTTP 200 OK)
```json
{
  "pnr": "2418901234",
  "firstDigit": "2",
  "derivedZone": "Northern Zone (Delhi / NR / NCR PRS Cluster)",
  "heuristicNotice": "Offline PRS server routing convention heuristic; not a live query to CRIS PRS.",
  "statusExplanations": {
    "RAC": "Reservation Against Cancellation: Legally permitted to board the train with a shared seat. Upgrades to full confirmed berth if vacancies arise post-charting.",
    "GNWL": "General Waitlist: Highest confirmation priority among all waitlist types.",
    "PQWL": "Pooled Quota Waitlist: Shared quota for intermediate stations; lower confirmation priority.",
    "RLWL": "Remote Location Waitlist: Originates between intermediate stations; lower priority than GNWL."
  },
  "statutoryWarning": "IMPORTANT: Under Section 138 of The Railways Act, 1989, fully waitlisted e-tickets cancel automatically upon chart preparation. Boarding with a cancelled e-ticket is strictly prohibited and subject to penalty fares and eviction."
}
```

---

### 2.4 Payment Help Diagnoser

- **Endpoint:** `POST /api/v1/payment-help/diagnose`
- **Access:** Authenticated (`ROLE_PASSENGER` or `ROLE_ADMIN`)
- **Description:** Zero-trust payment issue diagnosis. Scans reference for 16-digit card patterns & secret keywords, returning HTTP 400 if detected. Masked reference and RBI TAT guidelines returned on success.

#### Request Payload
```json
{
  "issueType": "deducted",
  "method": "UPI",
  "reference": "UPI9827364123"
}
```

#### Response Example (HTTP 200 OK)
```json
{
  "status": "DIAGNOSED",
  "paymentMethod": "UPI",
  "maskedReference": "UPI****123",
  "diagnosis": "Transaction debited from bank account but ticket generation unconfirmed.",
  "regulatoryTAT": "Under Reserve Bank of India (RBI) Circular DPSS.CO.PD No.629/02.01.014/2019-20, failed UPI transactions must be auto-reversed by your bank within T+1 business day.",
  "delayCompensation": "If the refund is not credited within T+1 business day, customer compensation of Rs. 100 per calendar day of delay is mandated by RBI regulations.",
  "recommendedAction": "1. Do not attempt an immediate duplicate booking during peak windows. 2. Verify account statement after T+1 business day. 3. If funds are not auto-reversed, lodge a dispute with your issuing bank quoting reference UPI****123."
}
```

#### Malicious / Secret Payload Example
```json
{
  "issueType": "deducted",
  "method": "Card",
  "reference": "4111 2222 3333 4444"
}
```

#### Error Response (HTTP 400 Bad Request)
```json
{
  "timestamp": "2026-10-18T17:36:00Z",
  "status": 400,
  "error": "Bad Request",
  "message": "Reference contains sensitive payment secrets"
}
```

---

### 2.5 Passenger Support Case Submission

- **Endpoint:** `POST /api/v1/cases`
- **Access:** Authenticated (`ROLE_PASSENGER` or `ROLE_ADMIN`)
- **Description:** Creates a structured support case, generates tracking ID (`RS-XXXXXX`), and binds ownership.

#### Request Payload
```json
{
  "category": "REFUND_INQUIRY",
  "description": "Payment was deducted via UPI yesterday during Tatkal booking. Need guidance on bank reversal timeline."
}
```

#### Response Example (HTTP 201 Created)
```json
{
  "id": "RS-482910",
  "owner": "passenger",
  "category": "REFUND_INQUIRY",
  "description": "Payment was deducted via UPI yesterday during Tatkal booking. Need guidance on bank reversal timeline.",
  "status": "OPEN",
  "createdAt": "2026-10-18T17:36:20Z",
  "updatedAt": "2026-10-18T17:36:20Z"
}
```

---

### 2.6 Admin Case Status Transition

- **Endpoint:** `PATCH /api/v1/admin/cases/{id}/status`
- **Access:** Restricted to `ROLE_ADMIN`
- **Description:** Transitions case state, appends atomic timeline event to `case_events`, and logs governance record to `audit_logs`.

#### Request Payload
```json
{
  "status": "RESOLVED",
  "note": "Advised passenger regarding RBI T+1 business day reversal window. Case closed."
}
```

#### Response Example (HTTP 200 OK)
```json
{
  "id": "RS-482910",
  "owner": "passenger",
  "category": "REFUND_INQUIRY",
  "description": "Payment was deducted via UPI yesterday during Tatkal booking. Need guidance on bank reversal timeline.",
  "status": "RESOLVED",
  "createdAt": "2026-10-18T17:36:20Z",
  "updatedAt": "2026-10-18T17:40:00Z"
}
```
