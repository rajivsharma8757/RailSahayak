package in.railsahayak;

import com.fasterxml.jackson.annotation.JsonAlias;
import com.fasterxml.jackson.annotation.JsonProperty;
import jakarta.validation.Valid;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Size;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpStatus;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.server.ResponseStatusException;

import java.time.Instant;
import java.util.*;

@RestController
@RequestMapping("/api/v1")
public class CaseController {

    private static final Logger log = LoggerFactory.getLogger(CaseController.class);

    private final SupportCaseRepository cases;
    private final CaseEventRepository events;
    private final AuditLogRepository audit;

    public CaseController(
            SupportCaseRepository cases,
            CaseEventRepository events,
            AuditLogRepository audit) {
        this.cases = cases;
        this.events = events;
        this.audit = audit;
    }

    public record CreateRequest(
            @NotBlank @Size(max = 80) String category,
            @NotBlank @Size(max = 500) String description) {
    }

    public record StatusRequest(
            @NotBlank String status,
            @Size(max = 500) String note) {
    }

    public record CaseView(
            String id,
            String owner,
            String category,
            String description,
            String status,
            Instant createdAt,
            Instant updatedAt) {
    }

    public record EventView(
            Long id,
            Long caseId,
            String actor,
            String eventType,
            String note,
            Instant createdAt) {
    }

    public record AuditLogView(
            Long id,
            String actor,
            String action,
            String resourceType,
            String resourceId,
            String detail,
            Instant createdAt) {
    }

    public record TrainSearchRequest(
            @NotBlank(message = "Source station ('from') is required")
            @Size(max = 100, message = "Source station must not exceed 100 characters")
            String from,

            @NotBlank(message = "Destination station ('to') is required")
            @Size(max = 100, message = "Destination station must not exceed 100 characters")
            String to,

            @NotBlank(message = "Journey date ('date') is required")
            String date,

            @JsonAlias({"class", "travelClass", "classPreference"})
            @Size(max = 20)
            String travelClass
    ) {}

    public record TrainOption(
            String trainName,
            String trainCode,
            String departure,
            String arrival,
            String duration,
            @JsonProperty("class") String travelClass,
            Integer sampleSeats,
            String type,
            String departureStation,
            String arrivalStation,
            String statusNote
    ) {
        @JsonProperty("travelClass")
        public String getTravelClass() {
            return travelClass;
        }
    }

    public record TrainSearchResponse(
            String mode,
            String notice,
            boolean liveRailwayIntegration,
            String from,
            String to,
            String date,
            @JsonProperty("class") String travelClass,
            List<TrainOption> results
    ) {
        @JsonProperty("travelClass")
        public String getTravelClass() {
            return travelClass;
        }
    }

    public record PaymentDiagnoseRequest(
            @NotBlank(message = "Payment issue category ('issue') is required")
            @Size(max = 50, message = "Payment issue category must not exceed 50 characters")
            String issue,

            @NotBlank(message = "Payment method ('method') is required")
            @Size(max = 50, message = "Payment method must not exceed 50 characters")
            String method,

            @Size(max = 50, message = "Payment purpose must not exceed 50 characters")
            String purpose,

            @Size(max = 100, message = "Reference must not exceed 100 characters")
            String reference,

            @Size(max = 30, message = "Transaction date must not exceed 30 characters")
            String transactionDate
    ) {}

    public record PaymentDiagnoseResponse(
            String mode,
            String issue,
            String paymentMethod,
            String purpose,
            String transactionDate,
            String title,
            String titleHindi,
            String advice,
            String adviceHindi,
            List<String> steps,
            List<String> stepsHindi,
            String actionRecommendation,
            String referenceAcknowledged,
            String maskedReference,
            boolean transactionVerified,
            boolean liveReconciliationEnabled,
            String warning,
            String disclaimer
    ) {}

    public record PnrGuideRequest(
            @Size(max = 20, message = "PNR number must not exceed 20 characters")
            String pnr,

            @Size(max = 20, message = "Status code must not exceed 20 characters")
            String statusCode,

            @Size(max = 200, message = "Query must not exceed 200 characters")
            String query
    ) {}

    public record PnrGuideResponse(
            String mode,
            String notice,
            boolean liveRailwayIntegration,
            String inputPnr,
            String maskedPnr,
            String prsZone,
            String statusCategory,
            String statusTitle,
            String statusTitleHindi,
            String statusExplanation,
            String statusExplanationHindi,
            String travelEligibility,
            String travelEligibilityHindi,
            String chartPreparationRule,
            String chartPreparationRuleHindi,
            List<String> officialVerificationChannels,
            List<String> importantGuidelines,
            List<String> importantGuidelinesHindi
    ) {
        @JsonProperty("chartRule")
        public String getChartRule() {
            return chartPreparationRule;
        }

        @JsonProperty("chartRuleHindi")
        public String getChartRuleHindi() {
            return chartPreparationRuleHindi;
        }

        @JsonProperty("officialChannels")
        public List<String> getOfficialChannels() {
            return officialVerificationChannels;
        }

        @JsonProperty("guidelines")
        public List<String> getGuidelines() {
            return importantGuidelines;
        }

        @JsonProperty("guidelinesHindi")
        public List<String> getGuidelinesHindi() {
            return importantGuidelinesHindi;
        }
    }

    private CaseView view(SupportCase c) {
        return new CaseView(
                c.getPublicId(),
                c.getOwnerUsername(),
                c.getCategory(),
                c.getDescription(),
                c.getStatus(),
                c.getCreatedAt(),
                c.getUpdatedAt());
    }

    private EventView viewEvent(CaseEvent e) {
        return new EventView(
                e.getId(),
                e.getCaseId(),
                e.getActor(),
                e.getEventType(),
                e.getNote(),
                e.getCreatedAt());
    }

    private AuditLogView viewAudit(AuditLog a) {
        return new AuditLogView(
                a.getId(),
                a.getActor(),
                a.getAction(),
                a.getResourceType(),
                a.getResourceId(),
                a.getDetail(),
                a.getCreatedAt());
    }

    private SupportCase find(String id) {
        return cases.findByPublicId(id)
                .orElseThrow(() -> new ResponseStatusException(
                        HttpStatus.NOT_FOUND, "Case not found"));
    }

    private boolean admin(Authentication authentication) {
        return authentication.getAuthorities().stream()
                .map(GrantedAuthority::getAuthority)
                .anyMatch("ROLE_ADMIN"::equals);
    }

    @PostMapping("/cases")
    @Transactional
    public CaseView create(
            @Valid @RequestBody CreateRequest request,
            Authentication authentication) {

        String id = "RS-" + UUID.randomUUID()
                .toString().substring(0, 8).toUpperCase(Locale.ROOT);

        SupportCase supportCase = cases.save(new SupportCase(
                id,
                authentication.getName(),
                request.category().trim(),
                request.description().trim()));

        events.save(new CaseEvent(
                supportCase.getId(),
                authentication.getName(),
                "CASE_CREATED",
                "Support case created."));

        audit.save(new AuditLog(
                authentication.getName(),
                "CASE_CREATED",
                "SUPPORT_CASE",
                id,
                "New support case"));

        log.info("Support case created successfully: publicId={}, owner={}, category={}", id, authentication.getName(), request.category().trim());

        return view(supportCase);
    }

    @GetMapping("/auth/me")
    public Map<String, Object> me(Authentication authentication) {
        if (authentication == null || !authentication.isAuthenticated()) {
            throw new ResponseStatusException(HttpStatus.UNAUTHORIZED, "Not authenticated");
        }
        List<String> roles = authentication.getAuthorities().stream()
                .map(GrantedAuthority::getAuthority)
                .toList();
        return Map.of(
                "authenticated", true,
                "username", authentication.getName(),
                "roles", roles);
    }

    @GetMapping("/cases")
    public List<CaseView> mine(Authentication authentication) {
        return cases.findByOwnerUsernameOrderByCreatedAtDesc(
                        authentication.getName())
                .stream()
                .map(this::view)
                .toList();
    }

    @GetMapping("/cases/{id}")
    public Map<String, Object> detail(
            @PathVariable String id,
            Authentication authentication) {

        SupportCase supportCase = find(id);

        if (!admin(authentication)
                && !supportCase.getOwnerUsername()
                        .equals(authentication.getName())) {
            throw new ResponseStatusException(
                    HttpStatus.NOT_FOUND, "Case not found");
        }

        List<EventView> history =
                events.findByCaseIdOrderByCreatedAtAsc(supportCase.getId())
                        .stream()
                        .map(this::viewEvent)
                        .toList();

        return Map.of(
                "supportCase", view(supportCase),
                "events", history);
    }

    @GetMapping("/admin/cases")
    public List<CaseView> all() {
        return cases.findAll()
                .stream()
                .sorted(Comparator.comparing(
                        SupportCase::getCreatedAt).reversed())
                .map(this::view)
                .toList();
    }

    @PatchMapping("/admin/cases/{id}/status")
    @Transactional
    public CaseView update(
            @PathVariable String id,
            @Valid @RequestBody StatusRequest request,
            Authentication authentication) {

        String status = request.status().trim()
                .toUpperCase(Locale.ROOT);

        if (!Set.of("OPEN", "IN_PROGRESS", "RESOLVED").contains(status)) {
            throw new ResponseStatusException(
                    HttpStatus.BAD_REQUEST,
                    "status must be OPEN, IN_PROGRESS, or RESOLVED");
        }

        SupportCase supportCase = find(id);
        String oldStatus = supportCase.getStatus();

        supportCase.setStatus(status);
        cases.save(supportCase);

        String note = (request.note() == null
                || request.note().isBlank())
                ? oldStatus + " -> " + status
                : request.note().trim();

        events.save(new CaseEvent(
                supportCase.getId(),
                authentication.getName(),
                "STATUS_CHANGED",
                note));

        String auditDetail = (request.note() == null || request.note().isBlank())
                ? oldStatus + " -> " + status
                : oldStatus + " -> " + status + ": " + request.note().trim();

        audit.save(new AuditLog(
                authentication.getName(),
                "STATUS_CHANGED",
                "SUPPORT_CASE",
                id,
                auditDetail));

        log.info("Support case status updated: publicId={}, newStatus={}, actor={}", id, status, authentication.getName());

        return view(supportCase);
    }

    @GetMapping("/admin/audit-logs")
    public List<AuditLogView> logs() {
        return audit.findTop100ByOrderByCreatedAtDesc()
                .stream()
                .map(this::viewAudit)
                .toList();
    }

    @GetMapping("/health")
    public Map<String, Object> health() {
        return Map.of(
                "status", "UP",
                "mode", "PROTOTYPE",
                "liveRailwayIntegration", false);
    }

    @PostMapping("/train-search")
    public TrainSearchResponse trainSearch(@Valid @RequestBody TrainSearchRequest request) {
        String from = request.from().trim();
        String to = request.to().trim();
        String date = request.date().trim();
        String travelClass = (request.travelClass() != null && !request.travelClass().isBlank())
                ? request.travelClass().trim()
                : "Any class";

        if (from.equalsIgnoreCase(to)) {
            throw new ResponseStatusException(
                    HttpStatus.BAD_REQUEST,
                    "Source and destination stations cannot be identical.");
        }

        List<TrainOption> results = generateSampleTrains(from, to, travelClass);

        log.info("Train search requested: from='{}', to='{}', date='{}', class='{}', resultsCount={}",
                from, to, date, travelClass, results.size());

        return new TrainSearchResponse(
                "SAMPLE_DATA_ONLY",
                "Sample demonstration data only. Not connected to live IRCTC or NTES seat inventory. Confirm availability and book only via official Indian Railways portals (irctc.co.in).",
                false,
                from,
                to,
                date,
                travelClass,
                results);
    }

    private List<TrainOption> generateSampleTrains(String from, String to, String requestedClass) {
        String f = from.toLowerCase(Locale.ROOT);
        String t = to.toLowerCase(Locale.ROOT);
        String reqCls = (requestedClass == null || requestedClass.equalsIgnoreCase("ANY") || requestedClass.equalsIgnoreCase("ANY CLASS")) ? "ALL" : requestedClass.toUpperCase(Locale.ROOT);

        List<TrainOption> candidates = new ArrayList<>();

        boolean isDelhiPatna = (f.contains("delhi") && t.contains("patna")) || (f.contains("patna") && t.contains("delhi"));
        boolean isDelhiMumbai = (f.contains("delhi") && t.contains("mumbai")) || (f.contains("mumbai") && t.contains("delhi"));
        boolean isDelhiHowrah = (f.contains("delhi") && (t.contains("howrah") || t.contains("kolkata"))) || ((f.contains("howrah") || f.contains("kolkata")) && t.contains("delhi"));
        boolean isBlrChennai = ((f.contains("bengaluru") || f.contains("bangalore")) && t.contains("chennai")) || (f.contains("chennai") && (t.contains("bengaluru") || t.contains("bangalore")));

        if (isDelhiPatna) {
            candidates.add(new TrainOption(
                    "Sample Howrah Rajdhani Express (via PNBE)",
                    "DEMO-12302",
                    "16:50",
                    "03:50",
                    "11h 00m",
                    "3A",
                    18,
                    "Rajdhani Express",
                    from,
                    to,
                    "Sample: 18 seats available (GNWL)"));
            candidates.add(new TrainOption(
                    "Sample Sampoorna Kranti Superfast Express",
                    "DEMO-12394",
                    "17:30",
                    "06:50",
                    "13h 20m",
                    "SL",
                    42,
                    "Superfast Express",
                    from,
                    to,
                    "Sample: 42 seats available (GNWL)"));
            candidates.add(new TrainOption(
                    "Sample Vande Bharat Express",
                    "DEMO-22348",
                    "06:35",
                    "18:05",
                    "11h 30m",
                    "CC",
                    24,
                    "Vande Bharat",
                    from,
                    to,
                    "Sample: 24 seats available (Chair Car)"));
            candidates.add(new TrainOption(
                    "Sample Shramjeevi Express",
                    "DEMO-12392",
                    "13:10",
                    "07:05",
                    "17h 55m",
                    "2A",
                    6,
                    "Mail/Express",
                    from,
                    to,
                    "Sample: 6 seats available"));
        } else if (isDelhiMumbai) {
            candidates.add(new TrainOption(
                    "Sample Mumbai Rajdhani Express",
                    "DEMO-12952",
                    "16:55",
                    "08:35",
                    "15h 40m",
                    "3A",
                    26,
                    "Rajdhani Express",
                    from,
                    to,
                    "Sample: 26 seats available (GNWL)"));
            candidates.add(new TrainOption(
                    "Sample August Kranti Tejas Rajdhani",
                    "DEMO-12954",
                    "17:15",
                    "10:05",
                    "16h 50m",
                    "2A",
                    8,
                    "Tejas Rajdhani",
                    from,
                    to,
                    "Sample: 8 seats available"));
            candidates.add(new TrainOption(
                    "Sample Paschim Superfast Express",
                    "DEMO-12926",
                    "16:35",
                    "14:55",
                    "22h 20m",
                    "SL",
                    55,
                    "Superfast Express",
                    from,
                    to,
                    "Sample: 55 seats available"));
        } else if (isDelhiHowrah) {
            candidates.add(new TrainOption(
                    "Sample Kolkata Rajdhani Express",
                    "DEMO-12306",
                    "16:50",
                    "12:15",
                    "19h 25m",
                    "3A",
                    14,
                    "Rajdhani Express",
                    from,
                    to,
                    "Sample: 14 seats available"));
            candidates.add(new TrainOption(
                    "Sample Sealdah Rajdhani Express",
                    "DEMO-12314",
                    "16:30",
                    "10:10",
                    "17h 40m",
                    "2A",
                    5,
                    "Rajdhani Express",
                    from,
                    to,
                    "Sample: 5 seats available"));
            candidates.add(new TrainOption(
                    "Sample Poorva Express",
                    "DEMO-12382",
                    "17:40",
                    "17:00",
                    "23h 20m",
                    "SL",
                    30,
                    "Superfast Express",
                    from,
                    to,
                    "Sample: 30 seats available"));
        } else if (isBlrChennai) {
            candidates.add(new TrainOption(
                    "Sample Vande Bharat Express",
                    "DEMO-20608",
                    "05:45",
                    "10:10",
                    "4h 25m",
                    "CC",
                    38,
                    "Vande Bharat",
                    from,
                    to,
                    "Sample: 38 seats available"));
            candidates.add(new TrainOption(
                    "Sample Shatabdi Express",
                    "DEMO-12028",
                    "06:00",
                    "11:00",
                    "5h 00m",
                    "CC",
                    20,
                    "Shatabdi Express",
                    from,
                    to,
                    "Sample: 20 seats available"));
            candidates.add(new TrainOption(
                    "Sample Chennai Mail",
                    "DEMO-12658",
                    "22:40",
                    "04:20",
                    "5h 40m",
                    "3A",
                    12,
                    "Mail/Express",
                    from,
                    to,
                    "Sample: 12 seats available"));
        } else {
            candidates.add(new TrainOption(
                    "Sample " + from + " - " + to + " Superfast",
                    "DEMO-12015",
                    "07:15",
                    "15:45",
                    "8h 30m",
                    "3A",
                    15,
                    "Superfast Express",
                    from,
                    to,
                    "Sample: 15 seats available (GNWL)"));
            candidates.add(new TrainOption(
                    "Sample " + from + " - " + to + " Intercity",
                    "DEMO-22018",
                    "14:00",
                    "21:30",
                    "7h 30m",
                    "CC",
                    28,
                    "Intercity Express",
                    from,
                    to,
                    "Sample: 28 seats available"));
            candidates.add(new TrainOption(
                    "Sample " + from + " - " + to + " Overnight Express",
                    "DEMO-12040",
                    "22:15",
                    "07:45",
                    "9h 30m",
                    "SL",
                    40,
                    "Mail/Express",
                    from,
                    to,
                    "Sample: 40 seats available"));
        }

        if (!"ALL".equals(reqCls)) {
            return candidates.stream()
                    .filter(opt -> opt.travelClass().equalsIgnoreCase(reqCls))
                    .toList();
        }
        return candidates;
    }

    private static final java.util.regex.Pattern SENSITIVE_PAYMENT_SECRET_PATTERN =
            java.util.regex.Pattern.compile("(?i)\\b(\\d{4}[- ]?){3}\\d{4}\\b|\\b(cvv|otp|pin|password)\\b");

    @PostMapping("/payment-help/diagnose")
    public PaymentDiagnoseResponse payment(@Valid @RequestBody PaymentDiagnoseRequest request) {
        String issue = request.issue().trim().toLowerCase(Locale.ROOT);
        String method = request.method().trim().toUpperCase(Locale.ROOT);
        String purpose = (request.purpose() != null && !request.purpose().isBlank())
                ? request.purpose().trim()
                : "TICKET_BOOKING";
        String date = (request.transactionDate() != null && !request.transactionDate().isBlank())
                ? request.transactionDate().trim()
                : "Not specified";
        String rawRef = request.reference() != null ? request.reference().trim() : "";

        if (!rawRef.isEmpty() && SENSITIVE_PAYMENT_SECRET_PATTERN.matcher(rawRef).find()) {
            throw new ResponseStatusException(
                    HttpStatus.BAD_REQUEST,
                    "Sensitive payment secret detected in reference. Never enter card numbers, PINs, OTPs, CVVs, or passwords.");
        }

        String maskedRef = maskReference(rawRef);
        String refAck = (maskedRef != null)
                ? "Ref recorded for guidance context only: " + maskedRef
                : null;

        log.info("Payment help diagnose requested: method={}, issue={}, purpose={}, maskedRef={}",
                method, issue, purpose, maskedRef != null ? maskedRef : "NONE");

        String title;
        String titleHindi;
        String advice;
        String adviceHindi;
        List<String> steps;
        List<String> stepsHindi;
        String actionRecommendation;

        switch (issue) {
            case "deducted" -> {
                title = "Money deducted, ticket not confirmed";
                titleHindi = "खाते से पैसे कटे, लेकिन टिकट कन्फर्म नहीं हुआ";
                advice = "Check official booking history and payment provider status; do not repeat payment until status is clear.";
                adviceHindi = "आधिकारिक बुकिंग इतिहास और बैंक स्थिति की जांच करें; स्थिति स्पष्ट होने तक दोबारा भुगतान न करें।";
                actionRecommendation = "WAIT_FOR_SETTLEMENT";
                steps = List.of(
                        "Check your official IRCTC 'Failed Transactions' or 'Booking History' tab before attempting a new booking.",
                        "Save the payment provider reference, UPI transaction ID (RRN), and exact timestamp.",
                        "If no ticket was generated, payment gateways initiate an auto-reversal per RBI turnaround time (TAT) guidelines; typical bank settlement cycles range from 3 to 7 working days depending on your bank and payment method. RailSahayak cannot guarantee refund processing or timeframes; verify directly with your bank and IRCTC.",
                        "Avoid making repeated booking attempts until the status of this transaction is verified by your bank or IRCTC.");
                stepsHindi = List.of(
                        "नया टिकट बुक करने से पहले IRCTC के 'बुकिंग इतिहास' या 'विफल लेनदेन' टैब की जांच करें।",
                        "पेमेंट गेटवे संदर्भ संख्या, UPI रेफरेंस (RRN) और सटीक समय नोट कर लें।",
                        "यदि टिकट नहीं बना, तो पेमेंट गेटवे RBI के नियमों के अनुसार ऑटो-रिवर्सल प्रक्रिया शुरू करता है; बैंक के आधार पर इसमें आमतौर पर 3 से 7 कार्यदिवस लग सकते हैं। रेलसहायक रिफंड या समयसीमा की गारंटी नहीं देता; अपने बैंक और IRCTC से पुष्टि करें।",
                        "लेनदेन की स्थिति स्पष्ट होने तक बार-बार भुगतान करने का प्रयास न करें।");
            }
            case "pending" -> {
                title = "Payment is pending";
                titleHindi = "भुगतान प्रक्रिया अभी लंबित (Pending) है";
                advice = "Wait 15 to 30 minutes for settlement confirmation before taking further action.";
                adviceHindi = "आगे की कार्रवाई करने से पहले निपटान पुष्टि के लिए 15 से 30 मिनट प्रतीक्षा करें।";
                actionRecommendation = "WAIT_AND_MONITOR";
                steps = List.of(
                        "Wait 15-30 minutes for your bank or payment gateway switch to confirm the settlement status.",
                        "Verify the transaction in your bank statement or UPI app before initiating a duplicate attempt.",
                        "Do NOT share OTPs, UPI PINs, or confidential credentials with anyone claiming to expedite verification.",
                        "If the transaction status remains pending beyond 2 hours, contact your bank citing the transaction reference.");
                stepsHindi = List.of(
                        "बैंक या पेमेंट गेटवे द्वारा स्थिति अपडेट करने के लिए 15-30 मिनट प्रतीक्षा करें।",
                        "दोबारा भुगतान करने से पहले अपने बैंक स्टेटमेंट या UPI ऐप में जांचें कि राशि कटी है या नहीं।",
                        "किसी भी अनधिकृत व्यक्ति के साथ OTP या UPI पिन साझा न करें।",
                        "यदि 2 घंटे बाद भी स्थिति लंबित रहती है, तो संदर्भ संख्या के साथ अपने बैंक से संपर्क करें।");
            }
            case "failed" -> {
                title = "Payment failed";
                titleHindi = "गेटवे पर भुगतान विफल (Failed) हो गया";
                advice = "Check whether the provider shows a completed debit and use official support if needed.";
                adviceHindi = "जांचें कि बैंक खाते से राशि कटी है या नहीं; यदि कटी है तो ऑटो-रिफंड की प्रतीक्षा करें।";
                actionRecommendation = "RETRY_OR_DISPUTE";
                steps = List.of(
                        "Check whether your account balance was actually debited.",
                        "If not debited, check your network connection and retry the booking using an alternative payment method.",
                        "If money was debited despite failure, the auto-reversal process will initiate credit back to your account per bank settlement cycles (typically 3 to 7 business days, though exact timing is determined by your bank). RailSahayak does not process refunds.",
                        "For unresolved debits after standard banking settlement windows, submit a formal dispute with your bank citing the transaction reference.");
                stepsHindi = List.of(
                        "जांचें कि आपके खाते से वास्तव में पैसे कटे हैं या नहीं।",
                        "यदि पैसे नहीं कटे हैं, तो नेटवर्क जांचें और किसी अन्य भुगतान विधि से पुनः प्रयास करें।",
                        "यदि विफलता के बावजूद पैसे कट गए हैं, तो ऑटो-रिवर्सल प्रक्रिया बैंक निपटान चक्र के अनुसार राशि वापस करेगी (आमतौर पर 3 से 7 कार्यदिवस, जो बैंक पर निर्भर करता है)। रेलसहायक रिफंड प्रोसेस नहीं करता।",
                        "मानक बैंक निपटान अवधि के बाद भी राशि वापस न आने पर संदर्भ संख्या के साथ अपने बैंक में औपचारिक विवाद दर्ज करें।");
            }
            case "refund" -> {
                title = "Refund status unclear";
                titleHindi = "रिफंड स्थिति अस्पष्ट या विलंबित है";
                advice = "Review official refund history and contact official support if unclear.";
                adviceHindi = "IRCTC टिकट रद्दीकरण इतिहास देखें और मानक समय सीमा के बाद eQuery पर शिकायत दर्ज करें।";
                actionRecommendation = "CHECK_IRCTC_EQUERY";
                steps = List.of(
                        "Check the IRCTC Ticket Cancellation / Refund history tab for the refund reference number.",
                        "Standard refund timelines: UPI (2-3 working days), Net Banking/Debit Card (5-7 working days).",
                        "Keep your PNR and transaction reference ready.",
                        "Raise a query on IRCTC eQuery portal (equery.irctc.co.in) if the refund period has elapsed.");
                stepsHindi = List.of(
                        "IRCTC के 'टिकट रद्दीकरण / रिफंड इतिहास' टैब में रिफंड रेफरेंस नंबर की जांच करें।",
                        "मानक रिफंड समय: UPI (2-3 कार्यदिवस), नेट बैंकिंग/डेबिट कार्ड (5-7 कार्यदिवस)।",
                        "अपना PNR और बैंक संदर्भ संख्या तैयार रखें।",
                        "यदि निर्धारित समय सीमा समाप्त हो गई है, तो आधिकारिक IRCTC eQuery पोर्टल (equery.irctc.co.in) पर शिकायत दर्ज करें।");
            }
            case "wallet" -> {
                title = "eWallet balance / withdrawal query";
                titleHindi = "IRCTC ई-वॉलेट बैलेंस या लेनदेन संबंधी समस्या";
                advice = "Review current official eWallet terms; wallet rules may differ from bank/card refunds.";
                adviceHindi = "आधिकारिक ई-वॉलेट नियमों की समीक्षा करें; वॉलेट रिफंड बैंक खातों से भिन्न नियमों का पालन करते हैं।";
                actionRecommendation = "VERIFY_WALLET_TERMS";
                steps = List.of(
                        "IRCTC eWallet refunds are usually credited faster directly to the eWallet balance.",
                        "Note that promotional or specific eWallet balances may have non-withdrawable restrictions per IRCTC terms.",
                        "Check your eWallet transaction statement for credit entries.",
                        "Contact IRCTC customer care if the balance does not reflect within the stipulated turnaround time.");
                stepsHindi = List.of(
                        "IRCTC ई-वॉलेट से किए गए भुगतानों का रिफंड सीधे ई-वॉलेट बैलेंस में तेजी से जमा होता है।",
                        "IRCTC नियमों के अनुसार टॉप-अप राशि बैंक खाते में वापस नहीं निकाली जा सकती।",
                        "क्रेडिट प्रविष्टियों के लिए अपने ई-वॉलेट लेनदेन विवरण की जांच करें।",
                        "यदि समय पर बैलेंस नहीं दिखता है, तो IRCTC कस्टमर केयर से संपर्क करें।");
            }
            case "successful" -> {
                title = "Payment successful, booking verification";
                titleHindi = "भुगतान सफल रहा, टिकट पुष्टि की जांच करें";
                advice = "Verify booked ticket in My Bookings; download SMS / PDF confirmation.";
                adviceHindi = "बुकिंग इतिहास में टिकट की जांच करें; SMS या ईमेल पुष्टि की पुष्टि करें।";
                actionRecommendation = "CHECK_BOOKING_HISTORY";
                steps = List.of(
                        "Log in to your IRCTC account and open 'Booked Ticket History' to confirm your PNR status.",
                        "Check your registered email and mobile SMS for booking confirmation and coach/berth details.",
                        "If payment succeeded but no PNR appears in Booked Ticket History, the booking failed during settlement and the amount will auto-reverse in 3-5 working days.",
                        "Do not travel without a confirmed PNR or valid reservation against cancellation (RAC).");
                stepsHindi = List.of(
                        "अपने IRCTC खाते में लॉगिन करें और PNR स्थिति जांचने के लिए 'बुक्ड टिकट हिस्ट्री' खोलें।",
                        "टिकट पुष्टि और कोच/बर्थ विवरण के लिए अपने पंजीकृत ईमेल और मोबाइल SMS की जांच करें।",
                        "यदि भुगतान सफल हुआ लेकिन PNR नहीं बना, तो राशि 3-5 कार्यदिवसों में स्वतः वापस आ जाएगी।",
                        "वैध PNR या अधिकृत RAC स्थिति के बिना यात्रा न करें।");
            }
            default -> {
                title = "General payment inquiry";
                titleHindi = "सामान्य रेलवे भुगतान पूछताछ";
                advice = "Review official booking and payment history, then contact official support.";
                adviceHindi = "आधिकारिक बुकिंग और भुगतान इतिहास की समीक्षा करें, आवश्यकतानुसार आधिकारिक सहायता से संपर्क करें।";
                actionRecommendation = "GENERAL_RECONCILIATION";
                steps = List.of(
                        "Review transaction entries in both your banking app and IRCTC account.",
                        "Keep transaction time, amount, and reference details documented.",
                        "Contact official customer support for specific reconciliation.");
                stepsHindi = List.of(
                        "अपने बैंकिंग ऐप और IRCTC खाते दोनों में लेनदेन प्रविष्टियों की समीक्षा करें।",
                        "लेनदेन का समय, राशि और संदर्भ विवरण सुरक्षित रखें।",
                        "यदि समस्या बनी रहती है, तो आधिकारिक सहायता से संपर्क करें।");
            }
        }

        return new PaymentDiagnoseResponse(
                "GENERAL_GUIDANCE_ONLY",
                issue,
                method,
                purpose,
                date,
                title,
                titleHindi,
                advice,
                adviceHindi,
                steps,
                stepsHindi,
                actionRecommendation,
                refAck,
                maskedRef,
                false,
                false,
                "Zero-Trust Payment Security: RailSahayak does NOT initiate, process, or verify financial transactions. Never share PINs, CVVs, or OTPs.",
                "Advisory guidance only based on general banking turnaround principles. RailSahayak does not verify transactions, process refunds, or guarantee settlement timeframes. For live dispute resolution, contact your bank and IRCTC eQuery (equery.irctc.co.in).");
    }

    @PostMapping("/pnr-guide/explain")
    public PnrGuideResponse pnrGuide(@Valid @RequestBody PnrGuideRequest request) {
        String rawPnr = request.pnr() != null ? request.pnr().trim() : "";
        String code = request.statusCode() != null ? request.statusCode().trim().toUpperCase(Locale.ROOT) : "";

        // If PNR provided, validate 10-digit numeric format
        String maskedPnr = null;
        String prsZone = null;
        if (!rawPnr.isEmpty()) {
            if (!rawPnr.matches("^\\d{10}$")) {
                throw new ResponseStatusException(
                        HttpStatus.BAD_REQUEST,
                        "Invalid PNR format. A valid Indian Railways PNR consists of exactly 10 numeric digits.");
            }
            maskedPnr = rawPnr.substring(0, 3) + "****" + rawPnr.substring(7);
            char firstDigit = rawPnr.charAt(0);
            prsZone = switch (firstDigit) {
                case '1' -> "Heuristic cluster: CRIS / Central Railway Zone [Derived from first-digit routing convention, not live PRS lookup]";
                case '2', '3' -> "Heuristic cluster: Northern Zone (New Delhi PRS Server) [Derived from first-digit routing convention, not live PRS lookup]";
                case '4', '5' -> "Heuristic cluster: Western Zone (Mumbai PRS Server) [Derived from first-digit routing convention, not live PRS lookup]";
                case '6', '7' -> "Heuristic cluster: Southern Zone (Chennai PRS Server) [Derived from first-digit routing convention, not live PRS lookup]";
                case '8', '9' -> "Heuristic cluster: Eastern Zone (Kolkata PRS Server) [Derived from first-digit routing convention, not live PRS lookup]";
                default -> "Heuristic cluster: Indian Railways PRS [Derived from first-digit routing convention, not live PRS lookup]";
            };
        }

        log.info("PNR guide explain requested: hasPnr={}, maskedPnr={}, code='{}'",
                !rawPnr.isEmpty(), maskedPnr != null ? maskedPnr : "NONE", code);

        // Determine status code classification
        String statusCategory;
        String statusTitle;
        String statusTitleHindi;
        String statusExplanation;
        String statusExplanationHindi;
        String travelEligibility;
        String travelEligibilityHindi;

        if (code.contains("CNF") || code.contains("CONFIRM")) {
            statusCategory = "CNF";
            statusTitle = "Confirmed (CNF)";
            statusTitleHindi = "कन्फर्म टिकट (CNF)";
            statusExplanation = "Your reservation is confirmed. A full berth or seat is reserved for your journey. Specific coach and berth numbers are finalized upon chart preparation.";
            statusExplanationHindi = "आपका आरक्षण पूरी तरह से कन्फर्म है। यात्रा के लिए पूरी सीट/बर्थ आरक्षित है। कोच और सीट संख्या चार्ट बनने पर अंतिम रूप से आवंटित की जाती है।";
            travelEligibility = "Permitted to board reserved coach with confirmed berth.";
            travelEligibilityHindi = "आरक्षित कोच में कन्फर्म बर्थ के साथ यात्रा की पूर्ण अनुमति है।";
        } else if (code.contains("RAC")) {
            statusCategory = "RAC";
            statusTitle = "Reservation Against Cancellation (RAC)";
            statusTitleHindi = "रद्दीकरण के विरुद्ध आरक्षण (RAC)";
            statusExplanation = "RAC provides a legal entitlement to board the train with guaranteed sitting accommodation (shared side-lower berth). If confirmed passengers cancel before chart preparation, your ticket upgrades automatically to full CNF.";
            statusExplanationHindi = "RAC टिकट पर ट्रेन में यात्रा करने की कानूनी अनुमति होती है। यात्री को बैठने के लिए सीट (साइड लोअर) मिलती है। यदि कोई कन्फर्म टिकट रद्द होता है, तो यह टिकट पूरी तरह कन्फर्म (CNF) हो जाता है।";
            travelEligibility = "Permitted to board reserved coach with shared sitting accommodation.";
            travelEligibilityHindi = "आरक्षित कोच में साझा बैठने की सीट के साथ यात्रा की पूर्ण अनुमति है।";
        } else if (code.contains("RLWL")) {
            statusCategory = "RLWL";
            statusTitle = "Remote Location Waiting List (RLWL)";
            statusTitleHindi = "रिमोट लोकेशन वेटिंग लिस्ट (RLWL)";
            statusExplanation = "Issued for intermediate or connecting stations having a separate designated quota pool. RLWL has a lower confirmation probability compared to general waitlist (GNWL).";
            statusExplanationHindi = "यह मध्यवर्ती या महत्वपूर्ण कनेक्टिंग स्टेशनों के लिए अलग कोटा पूल होता है। सामान्य वेटलिस्ट (GNWL) की तुलना में इसके कन्फर्म होने की संभावना अपेक्षाकृत कम होती है।";
            travelEligibility = "Boarding NOT permitted if e-ticket remains waitlisted after final chart preparation.";
            travelEligibilityHindi = "चार्ट बनने के बाद यदि ई-टिकट वेटिंग में ही रहता है, तो आरक्षित कोच में यात्रा की अनुमति नहीं है।";
        } else if (code.contains("PQWL")) {
            statusCategory = "PQWL";
            statusTitle = "Pooled Quota Waiting List (PQWL)";
            statusTitleHindi = "पूल्ड कोटा वेटिंग लिस्ट (PQWL)";
            statusExplanation = "Shared across several smaller intermediate stations on a train route. Cleared only if passengers travelling from that specific pool cancel their journey.";
            statusExplanationHindi = "यह ट्रेन मार्ग के कई छोटे स्टेशनों के लिए एक साझा कोटा होता है। इसके कन्फर्म होने की प्राथमिकता सीमित होती है।";
            travelEligibility = "Boarding NOT permitted if e-ticket remains waitlisted after final chart preparation.";
            travelEligibilityHindi = "चार्ट बनने के बाद ई-टिकट वेटिंग रहने पर आरक्षित डिब्बों में चढ़ना वर्जित है।";
        } else if (code.contains("TQWL")) {
            statusCategory = "TQWL";
            statusTitle = "Tatkal Waiting List (TQWL)";
            statusTitleHindi = "तत्काल वेटिंग लिस्ट (TQWL)";
            statusExplanation = "Waitlist issued against the Tatkal reservation quota. Moves directly to CNF only if other Tatkal confirmed tickets are cancelled. Does not move into RAC or general waitlist.";
            statusExplanationHindi = "तत्काल कोटे के तहत जारी वेटिंग लिस्ट। यह केवल तभी कन्फर्म होती है जब कोई तत्काल कन्फर्म टिकट रद्द किया जाए। यह RAC से पहले नहीं जाती।";
            travelEligibility = "Boarding NOT permitted if e-ticket remains waitlisted after chart preparation.";
            travelEligibilityHindi = "अंतिम चार्ट बनने के बाद तत्काल ई-टिकट वेटलिस्ट रहने पर यात्रा की अनुमति नहीं है।";
        } else if (code.contains("WL") || code.contains("GNWL") || code.contains("WAIT")) {
            statusCategory = "GNWL";
            statusTitle = "General Waiting List (GNWL / WL)";
            statusTitleHindi = "सामान्य वेटिंग लिस्ट (GNWL / WL)";
            statusExplanation = "General waiting list is the primary waitlist issued from originating stations. It has the highest confirmation probability among all waitlist quotas as cancellations occur.";
            statusExplanationHindi = "प्रारंभिक स्टेशन से जारी की जाने वाली मुख्य वेटिंग लिस्ट। सभी वेटलिस्ट श्रेणियों में इसके कन्फर्म होने की संभावना सबसे अधिक होती है।";
            travelEligibility = "Boarding NOT permitted if e-ticket remains waitlisted after final chart preparation.";
            travelEligibilityHindi = "चार्ट बनने के बाद भी ई-टिकट वेटिंग रहने पर आरक्षित कोच में यात्रा की अनुमति नहीं है।";
        } else if (code.contains("CAN")) {
            statusCategory = "CAN";
            statusTitle = "Ticket Cancelled (CAN)";
            statusTitleHindi = "रद्द टिकट (CAN)";
            statusExplanation = "The ticket has been cancelled by passenger or automatically by IRCTC due to fully waitlisted status after charting. Refund is initiated to source account.";
            statusExplanationHindi = "टिकट यात्री द्वारा अथवा चार्ट बनने पर स्वतः रद्द कर दिया गया है। रिफंड की राशि मूल बैंक खाते में प्रेषित की जा रही है।";
            travelEligibility = "Ticket is void. Travel not permitted.";
            travelEligibilityHindi = "टिकट अमान्य है। यात्रा की अनुमति नहीं है।";
        } else if (code.contains("TDR")) {
            statusCategory = "TDR";
            statusTitle = "Ticket Deposit Receipt (TDR Filed)";
            statusTitleHindi = "टिकट डिपॉजिट रसीद (TDR)";
            statusExplanation = "A TDR has been lodged for refund claiming (e.g., train delayed >3 hours, AC failure, or passenger did not travel). IRCTC and Zonal Railways process TDR claims in 30-60 days.";
            statusExplanationHindi = "ट्रेन 3 घंटे से अधिक लेट होने, AC खराब होने या यात्रा न कर पाने की स्थिति में रिफंड के लिए TDR दर्ज किया गया है। रेलवे 30-60 दिनों में इसका निपटान करती है।";
            travelEligibility = "TDR filed. Journey cancelled.";
            travelEligibilityHindi = "TDR दर्ज किया गया है। यात्रा रद्द है।";
        } else {
            statusCategory = "GENERAL_GUIDE";
            statusTitle = "Railway PNR Status Guide";
            statusTitleHindi = "रेलवे PNR स्थिति एवं प्रक्रिया मार्गदर्शिका";
            statusExplanation = "A 10-digit Passenger Name Record (PNR) tracks your reservation status from booking through chart preparation and journey completion.";
            statusExplanationHindi = "10 अंकों का PNR नंबर बुकिंग से लेकर चार्ट बनने और यात्रा पूरी होने तक आपके टिकट की स्थिति पर नज़र रखता है।";
            travelEligibility = "Verify live status with official IRCTC portal before boarding.";
            travelEligibilityHindi = "ट्रेन में चढ़ने से पहले आधिकारिक IRCTC पोर्टल से अपनी वर्तमान स्थिति अवश्य जांचें।";
        }

        String chartRule = "1st Chart: Prepared ~4 hours before train departure from originating station (or previous evening by 20:00 for morning trains). 2nd Chart: Prepared 30 to 50 minutes before departure from the charting station for last-minute allocations.";
        String chartRuleHindi = "प्रथम चार्ट: प्रारंभिक स्टेशन से ट्रेन छूटने के लगभग 4 घंटे पहले (सुबह की ट्रेनों के लिए पिछली रात 20:00 बजे तक)। दूसरा चार्ट: ट्रेन छूटने के 30 से 50 मिनट पहले अंतिम सीट आवंटन हेतु तैयार किया जाता है।";

        List<String> officialChannels = List.of(
                "Official IRCTC Web Portal (https://www.irctc.co.in/)",
                "Indian Railways Official PNR Enquiry (https://www.indianrail.gov.in/enquiry/PNR/PnrEnquiry.html)",
                "SMS Service: Send 'PNR <10-digit PNR>' to 139",
                "RailMadad Passenger Helpline: Dial 139 or visit https://railmadad.indianrailways.gov.in/",
                "National Train Enquiry System (NTES) for running status (https://enquiry.indianrailways.gov.in/)"
        );

        List<String> guidelines = List.of(
                "CRITICAL RAILWAY RULE: Fully waitlisted e-tickets that do not confirm after final chart preparation are automatically cancelled by IRCTC with full refund. Travelling on waitlisted e-tickets in reserved coaches is illegal and treated as ticketless travel under Section 138 of the Railways Act.",
                "RAC TICKETS: RAC passengers have guaranteed boarding rights with shared sitting accommodation (side lower).",
                "COACH & BERTH ALLOCATION: Coach and berth numbers for waitlist and RAC passengers are assigned ONLY upon final chart preparation, not at the time of booking.",
                "PRIVACY PROTECTION: Never share your full PNR publicly on social media or untrusted third-party apps, as PNRs can expose your travel itinerary and partial passenger details."
        );

        List<String> guidelinesHindi = List.of(
                "महत्वपूर्ण नियम: अंतिम चार्ट बनने के बाद भी पूरी तरह वेटलिस्ट रहने वाले ई-टिकट स्वतः रद्द हो जाते हैं और पूरा रिफंड वापस आ जाता है। ऐसे ई-टिकट पर आरक्षित डिब्बों में यात्रा करना गैरकानूनी है।",
                "RAC टिकट: RAC यात्रियों को ट्रेन में यात्रा करने और बैठने के लिए सीट (साइड लोअर) की पूर्ण कानूनी गारंटी होती है।",
                "सीट व कोच आवंटन: वेटलिस्ट और RAC यात्रियों को कोच और सीट संख्या केवल अंतिम चार्ट बनने पर ही मिलती है।",
                "गोपनीयता सुरक्षा: अपना PNR कभी भी सोशल मीडिया पर सार्वजनिक न करें।"
        );

        return new PnrGuideResponse(
                "GUIDANCE_ONLY",
                "DEMO / GUIDANCE ONLY: RailSahayak is a passenger assistance guide. We do not query live CRIS/PRS databases or access personal booking records. Real-time PNR confirmation, coach/berth allocation, and chart status must be verified exclusively through official Indian Railways channels.",
                false,
                rawPnr.isEmpty() ? null : rawPnr,
                maskedPnr,
                prsZone,
                statusCategory,
                statusTitle,
                statusTitleHindi,
                statusExplanation,
                statusExplanationHindi,
                travelEligibility,
                travelEligibilityHindi,
                chartRule,
                chartRuleHindi,
                officialChannels,
                guidelines,
                guidelinesHindi
        );
    }

    private String maskReference(String ref) {
        if (ref == null || ref.isBlank()) return null;
        String trimmed = ref.trim();
        if (trimmed.length() <= 4) {
            return "****";
        }
        if (trimmed.length() <= 8) {
            return trimmed.substring(0, 2) + "****" + trimmed.substring(trimmed.length() - 2);
        }
        return trimmed.substring(0, 3) + "****" + trimmed.substring(trimmed.length() - 3);
    }
}