# Contributing to RailSahayak

Thank you for your interest in contributing to **RailSahayak**! This document outlines our contribution workflow, code standards, and verification guidelines.

---

## 1. Project Mission & Boundaries

RailSahayak is an independent passenger-assistance and service-support prototype designed for exploratory technical review. All contributions must respect these fundamental principles:

1. **Independent Status:** Never add code that claims official railway partnership, live ticketing, live PNR checking, or production financial settlements unless authorized by the Ministry of Railways, IRCTC, or CRIS.
2. **Defensive Security & Privacy:** All incoming requests must adhere to zero-trust principles. Sensitive financial credentials (card numbers, PINs, CVVs, OTPs) must never be logged or stored.
3. **Evidence-Based Rules:** Any procedural rules (e.g. waitlist confirmation rules, refund timelines) must be verified against official statutory documentation (e.g. Indian Railways Commercial Manual, RBI circulars).

---

## 2. Development Workflow

1. **Fork the Repository:** Create a personal fork on GitHub.
2. **Clone & Branch:**
   ```bash
   git clone https://github.com/rajivsharma8757/RailSahayak.git
   cd RailSahayak
   git checkout -b feature/your-feature-name
   ```
3. **Environment Setup:** Ensure Java 21 LTS and PostgreSQL 16 are installed and running.
4. **Make Changes:** Keep commits focused, well-documented, and atomic.
5. **Run Automated Tests:**
   ```bash
   mvn clean test
   ```
   Ensure all 29 existing integration tests pass without failures or errors.
6. **Submit a Pull Request:** Open a PR against the `main` branch with a clear description of the problem solved and test evidence.

---

## 3. Code Standards & Quality Requirements

- **Java Version:** Java 21 LTS syntax and features.
- **Framework:** Spring Boot 3.4.5 standards (REST controllers, Spring Data JPA, Spring Security).
- **Database Migrations:** Schema changes must be added as versioned Flyway SQL migration scripts under `src/main/resources/db/migration/` (e.g. `V3__your_change.sql`). Never modify existing migrations (`V1` or `V2`).
- **Input Validation:** Use Jakarta Validation annotations (`@NotBlank`, `@Size`, etc.) on all request DTOs.
- **Error Handling:** Emit sanitized error responses via `GlobalExceptionHandler`. Never expose internal stack traces or database errors in API responses.

---

## 4. Reporting Issues

Please use GitHub Issues to report bugs or suggest enhancements. When reporting bugs, please provide:
- Operating system and Java runtime version.
- Step-by-step reproduction instructions.
- Relevant log output (with any personal data or credentials redacted).
