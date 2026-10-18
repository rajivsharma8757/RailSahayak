package in.railsahayak;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.MvcResult;

import java.nio.charset.StandardCharsets;
import java.util.Base64;

import static org.hamcrest.Matchers.*;
import static org.junit.jupiter.api.Assertions.*;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

@SpringBootTest
@AutoConfigureMockMvc
class RailSahayakApplicationTests {

    static {
        System.setProperty("user.timezone", "Asia/Kolkata");
        java.util.TimeZone.setDefault(java.util.TimeZone.getTimeZone("Asia/Kolkata"));
    }

    @Autowired
    private MockMvc mockMvc;

    @Autowired
    private ObjectMapper objectMapper;

    @Autowired
    private SupportCaseRepository caseRepository;

    @Autowired
    private AuditLogRepository auditLogRepository;

    @Autowired(required = false)
    private RateLimitingFilter rateLimitingFilter;

    private String basicAuth(String username, String password) {
        String token = username + ":" + password;
        return "Basic " + Base64.getEncoder().encodeToString(token.getBytes(StandardCharsets.UTF_8));
    }

    @Test
    @DisplayName("Context loads successfully")
    void contextLoads() {
        assertNotNull(mockMvc);
    }

    @Test
    @DisplayName("Health endpoint is public and returns PROTOTYPE mode")
    void healthEndpointIsPublic() throws Exception {
        mockMvc.perform(get("/api/v1/health"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.status", is("UP")))
                .andExpect(jsonPath("$.mode", is("PROTOTYPE")))
                .andExpect(jsonPath("$.liveRailwayIntegration", is(false)));
    }

    @Test
    @DisplayName("Unauthenticated request to /auth/me returns 401 Unauthorized")
    void unauthenticatedAuthMeReturns401() throws Exception {
        mockMvc.perform(get("/api/v1/auth/me"))
                .andExpect(status().isUnauthorized());
    }

    @Test
    @DisplayName("Passenger credentials return PASSENGER role on /auth/me")
    void passengerAuthMeReturnsRole() throws Exception {
        mockMvc.perform(get("/api/v1/auth/me")
                        .header("Authorization", basicAuth("passenger", "PassengerDemo123!")))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.authenticated", is(true)))
                .andExpect(jsonPath("$.username", is("passenger")))
                .andExpect(jsonPath("$.roles", hasItem("ROLE_PASSENGER")));
    }

    @Test
    @DisplayName("Admin credentials return ADMIN role on /auth/me")
    void adminAuthMeReturnsRole() throws Exception {
        mockMvc.perform(get("/api/v1/auth/me")
                        .header("Authorization", basicAuth("admin", "AdminDemo123!")))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.authenticated", is(true)))
                .andExpect(jsonPath("$.username", is("admin")))
                .andExpect(jsonPath("$.roles", hasItem("ROLE_ADMIN")));
    }

    @Test
    @DisplayName("Passenger cannot access admin cases (403 Forbidden)")
    void passengerCannotAccessAdminCases() throws Exception {
        mockMvc.perform(get("/api/v1/admin/cases")
                        .header("Authorization", basicAuth("passenger", "PassengerDemo123!")))
                .andExpect(status().isForbidden());
    }

    @Test
    @DisplayName("Passenger cannot access admin audit logs (403 Forbidden)")
    void passengerCannotAccessAdminAuditLogs() throws Exception {
        mockMvc.perform(get("/api/v1/admin/audit-logs")
                        .header("Authorization", basicAuth("passenger", "PassengerDemo123!")))
                .andExpect(status().isForbidden());
    }

    @Test
    @DisplayName("Admin can view admin cases and audit logs")
    void adminCanAccessAdminCasesAndAuditLogs() throws Exception {
        mockMvc.perform(get("/api/v1/admin/cases")
                        .header("Authorization", basicAuth("admin", "AdminDemo123!")))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$", isA(Iterable.class)));

        mockMvc.perform(get("/api/v1/admin/audit-logs")
                        .header("Authorization", basicAuth("admin", "AdminDemo123!")))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$", isA(Iterable.class)));
    }

    @Test
    @DisplayName("Validation fails when submitting complaint with blank fields (400 Bad Request)")
    void validationRejectsBlankComplaint() throws Exception {
        String invalidJson = """
                {
                    "category": "",
                    "description": ""
                }
                """;

        mockMvc.perform(post("/api/v1/cases")
                        .header("Authorization", basicAuth("passenger", "PassengerDemo123!"))
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(invalidJson))
                .andExpect(status().isBadRequest());
    }

    @Test
    @DisplayName("Complete complaint workflow: create, detail, list, update status, audit log")
    void fullComplaintWorkflow() throws Exception {
        // 1. Submit complaint as passenger
        String requestJson = """
                {
                    "category": "Refund follow-up",
                    "description": "Auto-test: Refund pending for failed booking attempt"
                }
                """;

        MvcResult createResult = mockMvc.perform(post("/api/v1/cases")
                        .header("Authorization", basicAuth("passenger", "PassengerDemo123!"))
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(requestJson))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.id", startsWith("RS-")))
                .andExpect(jsonPath("$.status", is("OPEN")))
                .andExpect(jsonPath("$.owner", is("passenger")))
                .andExpect(jsonPath("$.category", is("Refund follow-up")))
                .andReturn();

        JsonNode createdNode = objectMapper.readTree(createResult.getResponse().getContentAsString());
        String caseId = createdNode.get("id").asText();

        // 2. Passenger can retrieve own complaint detail with real events
        mockMvc.perform(get("/api/v1/cases/" + caseId)
                        .header("Authorization", basicAuth("passenger", "PassengerDemo123!")))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.supportCase.id", is(caseId)))
                .andExpect(jsonPath("$.events", hasSize(greaterThanOrEqualTo(1))))
                .andExpect(jsonPath("$.events[0].eventType", is("CASE_CREATED")));

        // 3. Passenger can list own complaints
        mockMvc.perform(get("/api/v1/cases")
                        .header("Authorization", basicAuth("passenger", "PassengerDemo123!")))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$[*].id", hasItem(caseId)));

        // 4. Admin updates status to RESOLVED
        String statusUpdateJson = """
                {
                    "status": "RESOLVED",
                    "note": "Verified refund credited by bank"
                }
                """;

        mockMvc.perform(patch("/api/v1/admin/cases/" + caseId + "/status")
                        .header("Authorization", basicAuth("admin", "AdminDemo123!"))
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(statusUpdateJson))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.id", is(caseId)))
                .andExpect(jsonPath("$.status", is("RESOLVED")));

        // 5. Passenger view reflects the RESOLVED status
        mockMvc.perform(get("/api/v1/cases/" + caseId)
                        .header("Authorization", basicAuth("passenger", "PassengerDemo123!")))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.supportCase.status", is("RESOLVED")))
                .andExpect(jsonPath("$.events", hasSize(greaterThanOrEqualTo(2))));

        // 6. Admin audit logs contain the STATUS_CHANGED event
        mockMvc.perform(get("/api/v1/admin/audit-logs")
                        .header("Authorization", basicAuth("admin", "AdminDemo123!")))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$[*].resourceId", hasItem(caseId)))
                .andExpect(jsonPath("$[*].action", hasItem("STATUS_CHANGED")));
    }

    @Test
    @DisplayName("Admin rejecting invalid status update (400 Bad Request)")
    void adminRejectsInvalidStatus() throws Exception {
        String invalidStatusJson = """
                {
                    "status": "INVALID_STATE",
                    "note": "test"
                }
                """;

        mockMvc.perform(patch("/api/v1/admin/cases/RS-TESTING/status")
                        .header("Authorization", basicAuth("admin", "AdminDemo123!"))
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(invalidStatusJson))
                .andExpect(status().isBadRequest());
    }

    @Test
    @DisplayName("Train search endpoint returns sample options with clear prototype notice")
    void trainSearchReturnsSampleData() throws Exception {
        String trainQuery = """
                {
                    "from": "New Delhi",
                    "to": "Patna Junction",
                    "date": "2026-10-25",
                    "class": "3A"
                }
                """;

        mockMvc.perform(post("/api/v1/train-search")
                        .header("Authorization", basicAuth("passenger", "PassengerDemo123!"))
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(trainQuery))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.mode", is("SAMPLE_DATA_ONLY")))
                .andExpect(jsonPath("$.liveRailwayIntegration", is(false)))
                .andExpect(jsonPath("$.from", is("New Delhi")))
                .andExpect(jsonPath("$.to", is("Patna Junction")))
                .andExpect(jsonPath("$.results", hasSize(greaterThan(0))))
                .andExpect(jsonPath("$.results[0].trainName", notNullValue()))
                .andExpect(jsonPath("$.results[0].trainCode", notNullValue()))
                .andExpect(jsonPath("$.results[0].class", is("3A")))
                .andExpect(jsonPath("$.results[0].travelClass", is("3A")));
    }

    @Test
    @DisplayName("Train search rejects identical source and destination with 400 Bad Request")
    void trainSearchRejectsIdenticalSourceAndDestination() throws Exception {
        String trainQuery = """
                {
                    "from": "New Delhi",
                    "to": "new delhi",
                    "date": "2026-10-25",
                    "class": "3A"
                }
                """;

        mockMvc.perform(post("/api/v1/train-search")
                        .header("Authorization", basicAuth("passenger", "PassengerDemo123!"))
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(trainQuery))
                .andExpect(status().isBadRequest())
                .andExpect(status().reason(containsString("Source and destination stations cannot be identical")));
    }

    @Test
    @DisplayName("Train search rejects missing or blank required fields with 400 Bad Request")
    void trainSearchRejectsMissingRequiredFields() throws Exception {
        // Blank from
        mockMvc.perform(post("/api/v1/train-search")
                        .header("Authorization", basicAuth("passenger", "PassengerDemo123!"))
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{\"from\":\"\",\"to\":\"Patna Junction\",\"date\":\"2026-10-25\"}"))
                .andExpect(status().isBadRequest());

        // Blank to
        mockMvc.perform(post("/api/v1/train-search")
                        .header("Authorization", basicAuth("passenger", "PassengerDemo123!"))
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{\"from\":\"New Delhi\",\"to\":\"\",\"date\":\"2026-10-25\"}"))
                .andExpect(status().isBadRequest());

        // Blank date
        mockMvc.perform(post("/api/v1/train-search")
                        .header("Authorization", basicAuth("passenger", "PassengerDemo123!"))
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{\"from\":\"New Delhi\",\"to\":\"Patna Junction\",\"date\":\"\"}"))
                .andExpect(status().isBadRequest());
    }

    @Test
    @DisplayName("Train search class filter returns empty results when class is not available")
    void trainSearchClassFilterEmptyResults() throws Exception {
        // Class 1A on route where sample trains have only 3A, 2A, SL, CC
        String trainQuery = """
                {
                    "from": "New Delhi",
                    "to": "Patna Junction",
                    "date": "2026-10-25",
                    "class": "1A"
                }
                """;

        mockMvc.perform(post("/api/v1/train-search")
                        .header("Authorization", basicAuth("passenger", "PassengerDemo123!"))
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(trainQuery))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.results", hasSize(0)));
    }

    @Test
    @DisplayName("Train search handles arbitrary valid routes with realistic sample trains")
    void trainSearchHandlesGeneralRoute() throws Exception {
        String trainQuery = """
                {
                    "from": "Jaipur",
                    "to": "Varanasi",
                    "date": "2026-10-28",
                    "class": "Any class"
                }
                """;

        mockMvc.perform(post("/api/v1/train-search")
                        .header("Authorization", basicAuth("passenger", "PassengerDemo123!"))
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(trainQuery))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.mode", is("SAMPLE_DATA_ONLY")))
                .andExpect(jsonPath("$.from", is("Jaipur")))
                .andExpect(jsonPath("$.to", is("Varanasi")))
                .andExpect(jsonPath("$.results", hasSize(greaterThanOrEqualTo(3))));
    }


    @Test
    @DisplayName("Payment help diagnosis endpoint returns structured steps and advice")
    void paymentDiagnoseReturnsSteps() throws Exception {
        String diagQuery = """
                {
                    "issue": "deducted",
                    "method": "UPI",
                    "reference": "UPI-DEMO-987654"
                }
                """;

        mockMvc.perform(post("/api/v1/payment-help/diagnose")
                        .header("Authorization", basicAuth("passenger", "PassengerDemo123!"))
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(diagQuery))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.mode", is("GENERAL_GUIDANCE_ONLY")))
                .andExpect(jsonPath("$.title", containsString("Money deducted")))
                .andExpect(jsonPath("$.steps", hasSize(greaterThan(1))))
                .andExpect(jsonPath("$.transactionVerified", is(false)))
                .andExpect(jsonPath("$.maskedReference", is("UPI****654")))
                .andExpect(jsonPath("$.titleHindi", notNullValue()))
                .andExpect(jsonPath("$.actionRecommendation", is("WAIT_FOR_SETTLEMENT")));
    }

    @Test
    @DisplayName("Payment help diagnoses pending and failed payment scenarios")
    void paymentDiagnoseScenarios() throws Exception {
        // Pending scenario
        mockMvc.perform(post("/api/v1/payment-help/diagnose")
                        .header("Authorization", basicAuth("passenger", "PassengerDemo123!"))
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("""
                                {
                                    "issue": "pending",
                                    "method": "NETBANKING",
                                    "purpose": "TICKET_BOOKING"
                                }
                                """))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.title", containsString("pending")))
                .andExpect(jsonPath("$.actionRecommendation", is("WAIT_AND_MONITOR")));

        // Failed scenario
        mockMvc.perform(post("/api/v1/payment-help/diagnose")
                        .header("Authorization", basicAuth("passenger", "PassengerDemo123!"))
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("""
                                {
                                    "issue": "failed",
                                    "method": "CARD",
                                    "purpose": "TICKET_BOOKING"
                                }
                                """))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.title", containsString("failed")))
                .andExpect(jsonPath("$.actionRecommendation", is("RETRY_OR_DISPUTE")));
    }

    @Test
    @DisplayName("Payment help rejects missing required issue or method with 400 Bad Request")
    void paymentDiagnoseRejectsMissingRequiredFields() throws Exception {
        // Missing issue
        mockMvc.perform(post("/api/v1/payment-help/diagnose")
                        .header("Authorization", basicAuth("passenger", "PassengerDemo123!"))
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{\"issue\":\"\",\"method\":\"UPI\"}"))
                .andExpect(status().isBadRequest());

        // Missing method
        mockMvc.perform(post("/api/v1/payment-help/diagnose")
                        .header("Authorization", basicAuth("passenger", "PassengerDemo123!"))
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{\"issue\":\"deducted\",\"method\":\"\"}"))
                .andExpect(status().isBadRequest());
    }

    @Test
    @DisplayName("Payment help rejects sensitive financial secrets like card numbers or CVVs with 400 Bad Request")
    void paymentDiagnoseRejectsSensitiveSecrets() throws Exception {
        // Reference containing 16-digit card number
        mockMvc.perform(post("/api/v1/payment-help/diagnose")
                        .header("Authorization", basicAuth("passenger", "PassengerDemo123!"))
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("""
                                {
                                    "issue": "deducted",
                                    "method": "CARD",
                                    "reference": "Card 4111-2222-3333-4444"
                                }
                                """))
                .andExpect(status().isBadRequest())
                .andExpect(status().reason(containsString("Sensitive payment secret detected")));

        // Reference containing CVV keyword
        mockMvc.perform(post("/api/v1/payment-help/diagnose")
                        .header("Authorization", basicAuth("passenger", "PassengerDemo123!"))
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("""
                                {
                                    "issue": "deducted",
                                    "method": "CARD",
                                    "reference": "CVV 123"
                                }
                                """))
                .andExpect(status().isBadRequest())
                .andExpect(status().reason(containsString("Sensitive payment secret detected")));
    }

    @Test
    @DisplayName("PNR guide returns authoritative guidance, masked PNR, and derived PRS zone for valid 10-digit PNR")
    void pnrGuide_validPnrAndStatusCode_returnsAuthoritativeGuidanceAndZone() throws Exception {
        String pnrQuery = """
                {
                    "pnr": "2345678901",
                    "statusCode": "RAC",
                    "query": "Can I board the train with RAC?"
                }
                """;

        mockMvc.perform(post("/api/v1/pnr-guide/explain")
                        .header("Authorization", basicAuth("passenger", "PassengerDemo123!"))
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(pnrQuery))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.mode", is("GUIDANCE_ONLY")))
                .andExpect(jsonPath("$.liveRailwayIntegration", is(false)))
                .andExpect(jsonPath("$.maskedPnr", is("234****901")))
                .andExpect(jsonPath("$.prsZone", containsString("Northern Zone")))
                .andExpect(jsonPath("$.statusCategory", is("RAC")))
                .andExpect(jsonPath("$.statusTitle", containsString("Reservation Against Cancellation")))
                .andExpect(jsonPath("$.statusTitleHindi", notNullValue()))
                .andExpect(jsonPath("$.travelEligibility", containsString("shared sitting accommodation")))
                .andExpect(jsonPath("$.chartRule", containsString("4 hours")))
                .andExpect(jsonPath("$.officialChannels", hasSize(greaterThanOrEqualTo(3))))
                .andExpect(jsonPath("$.guidelines", hasSize(greaterThanOrEqualTo(2))));
    }

    @Test
    @DisplayName("PNR guide clarifies that waitlisted e-tickets are barred from boarding under Section 138")
    void pnrGuide_waitlistStatus_explainsWaitlistAndBoardingRestriction() throws Exception {
        String pnrQuery = """
                {
                    "pnr": "4567890123",
                    "statusCode": "GNWL"
                }
                """;

        mockMvc.perform(post("/api/v1/pnr-guide/explain")
                        .header("Authorization", basicAuth("passenger", "PassengerDemo123!"))
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(pnrQuery))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.maskedPnr", is("456****123")))
                .andExpect(jsonPath("$.prsZone", containsString("Western Zone")))
                .andExpect(jsonPath("$.statusCategory", is("GNWL")))
                .andExpect(jsonPath("$.travelEligibility", containsString("Boarding NOT permitted")))
                .andExpect(jsonPath("$.guidelines[0]", containsString("Section 138")));
    }

    @Test
    @DisplayName("PNR guide rejects invalid PNR format with 400 Bad Request")
    void pnrGuide_invalidPnrFormat_returnsBadRequest() throws Exception {
        // Less than 10 digits
        mockMvc.perform(post("/api/v1/pnr-guide/explain")
                        .header("Authorization", basicAuth("passenger", "PassengerDemo123!"))
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{\"pnr\":\"12345\"}"))
                .andExpect(status().isBadRequest())
                .andExpect(status().reason(containsString("valid Indian Railways PNR")));

        // Non-numeric characters
        mockMvc.perform(post("/api/v1/pnr-guide/explain")
                        .header("Authorization", basicAuth("passenger", "PassengerDemo123!"))
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{\"pnr\":\"2345ABC901\"}"))
                .andExpect(status().isBadRequest())
                .andExpect(status().reason(containsString("valid Indian Railways PNR")));
    }

    @Test
    @DisplayName("Admin status transition with custom note persists event and audit log details")
    void adminStatusTransition_withCustomNote_persistsEventAndAudit() throws Exception {
        // 1. Create case as passenger
        String requestJson = """
                {
                    "category": "Accessibility assistance",
                    "description": "Need wheelchair assistance at New Delhi railway station platform 1"
                }
                """;

        MvcResult createResult = mockMvc.perform(post("/api/v1/cases")
                        .header("Authorization", basicAuth("passenger", "PassengerDemo123!"))
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(requestJson))
                .andExpect(status().isOk())
                .andReturn();

        JsonNode createdNode = objectMapper.readTree(createResult.getResponse().getContentAsString());
        String caseId = createdNode.get("id").asText();

        // 2. Admin updates status to IN_PROGRESS with custom note
        String updateJson = """
                {
                    "status": "IN_PROGRESS",
                    "note": "Assigned station porter assistance team at NDLS"
                }
                """;

        mockMvc.perform(patch("/api/v1/admin/cases/" + caseId + "/status")
                        .header("Authorization", basicAuth("admin", "AdminDemo123!"))
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(updateJson))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.id", is(caseId)))
                .andExpect(jsonPath("$.status", is("IN_PROGRESS")));

        // 3. Verify event timeline contains the note
        mockMvc.perform(get("/api/v1/cases/" + caseId)
                        .header("Authorization", basicAuth("passenger", "PassengerDemo123!")))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.supportCase.status", is("IN_PROGRESS")))
                .andExpect(jsonPath("$.events[1].eventType", is("STATUS_CHANGED")))
                .andExpect(jsonPath("$.events[1].note", is("Assigned station porter assistance team at NDLS")));

        // 4. Verify audit log contains the note
        mockMvc.perform(get("/api/v1/admin/audit-logs")
                        .header("Authorization", basicAuth("admin", "AdminDemo123!")))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$[*].detail", hasItem(containsString("OPEN -> IN_PROGRESS: Assigned station porter assistance team at NDLS"))));
    }

    @Test
    @DisplayName("Security response headers are properly enforced")
    void securityHeaders_enforced() throws Exception {
        mockMvc.perform(get("/api/v1/health"))
                .andExpect(status().isOk())
                .andExpect(header().string("X-Content-Type-Options", "nosniff"))
                .andExpect(header().string("X-Frame-Options", "SAMEORIGIN"))
                .andExpect(header().exists("X-Correlation-ID"));
    }

    @Test
    @DisplayName("Correlation ID is generated when omitted and preserved when provided")
    void correlationId_generatedAndPreserved() throws Exception {
        // Auto-generation
        MvcResult res1 = mockMvc.perform(get("/api/v1/health"))
                .andExpect(status().isOk())
                .andExpect(header().exists("X-Correlation-ID"))
                .andReturn();
        String corr1 = res1.getResponse().getHeader("X-Correlation-ID");
        assertNotNull(corr1);
        assertTrue(corr1.startsWith("rs-"));

        // Preservation of client-supplied correlation ID
        mockMvc.perform(get("/api/v1/health")
                        .header("X-Correlation-ID", "custom-trace-999"))
                .andExpect(status().isOk())
                .andExpect(header().string("X-Correlation-ID", "custom-trace-999"));
    }

    @Test
    @DisplayName("Rate limiting filter enforces limits and returns 429 Too Many Requests")
    void rateLimiter_blocksExcessiveTraffic() throws Exception {
        if (rateLimitingFilter != null) {
            int originalLimit = 300;
            try {
                RateLimitingFilter.clearRateLimits();
                rateLimitingFilter.setLimitPerMinute(3);
                rateLimitingFilter.setTrustForwardedFor(true);
                rateLimitingFilter.setTrustedProxies("127.0.0.1,::1");

                // First 3 requests with custom IP should succeed
                for (int i = 0; i < 3; i++) {
                    mockMvc.perform(get("/api/v1/cases")
                                    .header("Authorization", basicAuth("passenger", "PassengerDemo123!"))
                                    .header("X-Forwarded-For", "203.0.113.42"))
                            .andExpect(status().isOk());
                }

                // 4th request from same IP should get 429
                mockMvc.perform(get("/api/v1/cases")
                                .header("Authorization", basicAuth("passenger", "PassengerDemo123!"))
                                .header("X-Forwarded-For", "203.0.113.42"))
                        .andExpect(status().isTooManyRequests())
                        .andExpect(header().string("Retry-After", "60"))
                        .andExpect(jsonPath("$.status", is(429)))
                        .andExpect(jsonPath("$.error", is("TOO_MANY_REQUESTS")));
            } finally {
                rateLimitingFilter.setLimitPerMinute(originalLimit);
                rateLimitingFilter.setTrustForwardedFor(false);
                RateLimitingFilter.clearRateLimits();
            }
        }
    }

    @Test
    @DisplayName("Rate limiter ignores spoofed X-Forwarded-For headers when trust is disabled")
    void rateLimiter_ignoresSpoofedForwardedIpWhenTrustDisabled() throws Exception {
        if (rateLimitingFilter != null) {
            int originalLimit = 300;
            try {
                RateLimitingFilter.clearRateLimits();
                rateLimitingFilter.setLimitPerMinute(3);
                // Ensure forwarded trust is explicitly disabled (default posture)
                rateLimitingFilter.setTrustForwardedFor(false);

                // Attacker attempts to bypass rate limiting by rotating X-Forwarded-For headers
                for (int i = 1; i <= 3; i++) {
                    mockMvc.perform(get("/api/v1/cases")
                                    .header("Authorization", basicAuth("passenger", "PassengerDemo123!"))
                                    .header("X-Forwarded-For", "198.51.100." + i))
                            .andExpect(status().isOk());
                }

                // 4th request rotates header again, but server maps to real remote IP (127.0.0.1) and rejects
                mockMvc.perform(get("/api/v1/cases")
                                .header("Authorization", basicAuth("passenger", "PassengerDemo123!"))
                                .header("X-Forwarded-For", "198.51.100.99"))
                        .andExpect(status().isTooManyRequests())
                        .andExpect(header().string("Retry-After", "60"));
            } finally {
                rateLimitingFilter.setLimitPerMinute(originalLimit);
                RateLimitingFilter.clearRateLimits();
            }
        }
    }

    @Test
    @DisplayName("Rate limiter handles malformed, oversized, and missing forwarded-IP headers safely")
    void rateLimiter_handlesMalformedOversizedAndMissingForwardedHeadersSafely() throws Exception {
        if (rateLimitingFilter != null) {
            int originalLimit = 300;
            try {
                RateLimitingFilter.clearRateLimits();
                rateLimitingFilter.setLimitPerMinute(10);
                rateLimitingFilter.setTrustForwardedFor(true);
                rateLimitingFilter.setTrustedProxies("127.0.0.1,::1");

                // 1. Malformed header containing special symbols
                mockMvc.perform(get("/api/v1/cases")
                                .header("Authorization", basicAuth("passenger", "PassengerDemo123!"))
                                .header("X-Forwarded-For", "INVALID_IP_$$<SCRIPT>"))
                        .andExpect(status().isOk());

                // 2. Oversized header (e.g. 500 characters)
                String oversizedHeader = "2001:db8::1,".repeat(40);
                mockMvc.perform(get("/api/v1/cases")
                                .header("Authorization", basicAuth("passenger", "PassengerDemo123!"))
                                .header("X-Forwarded-For", oversizedHeader))
                        .andExpect(status().isOk());

                // 3. Blank / whitespace header
                mockMvc.perform(get("/api/v1/cases")
                                .header("Authorization", basicAuth("passenger", "PassengerDemo123!"))
                                .header("X-Forwarded-For", "   "))
                        .andExpect(status().isOk());

                // 4. Missing header entirely
                mockMvc.perform(get("/api/v1/cases")
                                .header("Authorization", basicAuth("passenger", "PassengerDemo123!")))
                        .andExpect(status().isOk());
            } finally {
                rateLimitingFilter.setLimitPerMinute(originalLimit);
                rateLimitingFilter.setTrustForwardedFor(false);
                RateLimitingFilter.clearRateLimits();
            }
        }
    }
}

