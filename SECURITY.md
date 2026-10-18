# Security Policy

## 1. Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |

---

## 2. Reporting a Vulnerability

We take the security and privacy of citizen interactions seriously. If you discover a security vulnerability or potential privacy issue in RailSahayak, please report it responsibly:

- **Do NOT** open a public GitHub issue for security vulnerabilities.
- Please email the maintainer directly at: `rajivkumarsharma200@gmail.com`
- Include detailed steps to reproduce the issue, along with any relevant proof-of-concept code or network payloads.

You will receive an acknowledgment within 48 hours, followed by regular updates on triage and mitigation progress.

---

## 3. Security Design Invariants

RailSahayak implements several defensive controls by design:

1. **Edge Rate Limiting:** `RateLimitingFilter` enforces a sliding-window limit (default: 300 requests/minute per client IP) to protect against brute-force attacks and volumetric DoS.
2. **Reverse Proxy Trust Verification:** Header inspection (`X-Forwarded-For`) is disabled by default (`trust-forwarded-for: false`) and requires explicit configuration of trusted proxy IPs.
3. **Sensitive Secret Scanning:** `POST /api/v1/payment-help/diagnose` checks transaction reference strings using server-side regex (`(?i)\b(\d{4}[- ]?){3}\d{4}\b|\b(cvv|otp|pin|password)\b`), rejecting payment card numbers and security keywords with HTTP 400 Bad Request.
4. **Zero-Leakage Error Handling:** `GlobalExceptionHandler` intercepts uncaught runtime exceptions, logging stack traces internally while returning sanitized JSON responses with correlation tracking IDs to clients.
5. **Security Headers:** Spring Security filter chain enforces `X-Content-Type-Options: nosniff`, `X-Frame-Options: SAMEORIGIN`, `Referrer-Policy: strict-origin-when-cross-origin`, and `Permissions-Policy`.
6. **Demo Mode Notice:** The prototype currently utilizes in-memory authentication (`InMemoryUserDetailsManager`) for local evaluation. Production deployment requires transition to OAuth2/OIDC, IRCTC SSO, or enterprise identity providers.
