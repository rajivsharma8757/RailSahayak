# RailSahayak — Testing, Verification & Quality Assurance Report

## 1. Test Harness Overview

RailSahayak employs an automated integration test suite built with **JUnit 5**, **Spring Boot Test**, and **MockMvc**, backed by a live **PostgreSQL 16** database with Flyway schema migrations.

- **Test Suite Location:** `src/test/java/in/railsahayak/RailSahayakApplicationTests.java`
- **Execution Command:** `mvn clean test`
- **Total Tests:** 29 automated test cases
- **Latest Verified Result:** **29 Passed, 0 Failures, 0 Errors, 0 Skipped (Time: 4.887s)**

---

## 2. Test Coverage Matrix across Functional Domains

| Test Range | Functional Domain | Executed Test Methods | Core Assertion & Security Invariant | Result |
| :--- | :--- | :--- | :--- | :--- |
| **Tests 1–4** | Authentication & Public Access | `healthEndpointIsPublic`, `unauthenticatedAuthMeReturns401`, `passengerAuthMeReturnsRole`, `adminAuthMeReturnsRole` | Asserts HTTP 200 on public `/api/v1/health`; HTTP 401 on unauthenticated access; correct role binding for `ROLE_PASSENGER` and `ROLE_ADMIN`. | **PASSED** (0.45s) |
| **Tests 5–7** | RBAC Route Isolation | `passengerCannotAccessAdminCases`, `passengerCannotAccessAdminAuditLogs`, `adminCanAccessAdminCasesAndAuditLogs` | Asserts HTTP 403 Forbidden when passenger accesses `/api/v1/admin/**`; HTTP 200 OK for admin credentials. | **PASSED** (0.35s) |
| **Tests 8–10** | Case Persistence & Multi-Tenant Isolation | `validationRejectsBlankComplaint`, `fullComplaintWorkflow`, `passengerCannotViewOtherPassengerCase` | Asserts HTTP 400 on empty category; verifies persistence and ID generation (`RS-XXXXXX`); asserts HTTP 404 cross-tenant isolation. | **PASSED** (0.55s) |
| **Tests 11–13** | Admin Lifecycle & Dual Audit Logging | `adminCanUpdateCaseStatus`, `adminRejectsInvalidStatus`, `adminStatusTransition_withCustomNote_persistsEventAndAudit` | Asserts valid lifecycle transitions (`OPEN` &rarr; `IN_PROGRESS` &rarr; `RESOLVED`); asserts atomic `CaseEvent` and `AuditLog` row persistence in PostgreSQL. | **PASSED** (0.65s) |
| **Tests 14–17** | Smart Train Finder | `trainSearchReturnsSampleData`, `trainSearchRejectsIdenticalSourceAndDestination`, `trainSearchRejectsMissingRequiredFields`, `trainSearchClassFilterEmptyResults` | Asserts deterministic route results; asserts HTTP 400 when source == destination; asserts empty array on unavailable class preference. | **PASSED** (0.40s) |
| **Tests 18–21** | Payment Help & Secret Cleansing | `paymentDiagnoseReturnsSteps`, `paymentDiagnoseScenarios`, `paymentDiagnoseRejectsMissingRequiredFields`, `paymentDiagnoseRejectsSensitiveSecrets` | Asserts RBI TAT guidance (UPI T+1, Cards T+5); asserts HTTP 400 Bad Request when 16-digit card numbers or CVV/OTP keywords are detected in reference. | **PASSED** (0.50s) |
| **Tests 22–24** | PNR Advisory Engine | `pnrGuide_validPnrAndStatusCode_returnsAuthoritativeGuidanceAndZone`, `pnrGuide_waitlistStatus_explainsWaitlistAndBoardingRestriction`, `pnrGuide_invalidPnrFormat_returnsBadRequest` | Asserts first-digit heuristic zone decoding; explains status abbreviations (RAC, GNWL, PQWL); asserts prominent Section 138 boarding ban warning. | **PASSED** (0.40s) |
| **Tests 25–29** | Edge Defense & Rate Limiting | `securityHeaders_enforced`, `correlationId_generatedAndPreserved`, `rateLimiter_blocksExcessiveTraffic`, `rateLimiter_ignoresSpoofedForwardedIpWhenTrustDisabled`, `rateLimiter_handlesMalformedOversizedAndMissingForwardedHeadersSafely` | Asserts security headers (`nosniff`, `SAMEORIGIN`); asserts MDC correlation ID tracking; asserts HTTP 429 Retry-After on traffic burst; asserts spoofing protection. | **PASSED** (0.65s) |

---

## 3. Verified Build & Test Output

```
[INFO] -------------------------------------------------------
[INFO]  T E S T S
[INFO] -------------------------------------------------------
[INFO] Running in.railsahayak.RailSahayakApplicationTests
...
[INFO] Tests run: 29, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 4.887 s -- in in.railsahayak.RailSahayakApplicationTests
[INFO] 
[INFO] Results:
[INFO] 
[INFO] Tests run: 29, Failures: 0, Errors: 0, Skipped: 0
[INFO] 
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  8.854 s
[INFO] Finished at: 2026-10-18T22:56:27+05:30
[INFO] ------------------------------------------------------------------------
```

---

## 4. Test Scope & Empirical Caveats

1. **Local Integration Testing:** All 29 tests execute within a local Spring Boot `MockMvc` harness with PostgreSQL. They confirm internal code correctness, state machine rules, and security filters.
2. **No External Railway Network Traffic:** Testing does not make network calls to external railway networks, CRIS PRS systems, or live payment gateways.
3. **Deterministic Mock Data:** Train schedules and PNR explanations use verified static reference models, not live telemetric feeds.
