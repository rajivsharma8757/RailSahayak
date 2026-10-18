package in.railsahayak;

import jakarta.annotation.PostConstruct;
import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.core.Ordered;
import org.springframework.core.annotation.Order;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Component;
import org.springframework.web.filter.OncePerRequestFilter;

import java.io.IOException;
import java.util.Arrays;
import java.util.Collections;
import java.util.Set;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.Collectors;

@Component
@Order(Ordered.HIGHEST_PRECEDENCE + 1)
public class RateLimitingFilter extends OncePerRequestFilter {

    private static final Logger log = LoggerFactory.getLogger(RateLimitingFilter.class);

    @Value("${railsahayak.rate-limit.enabled:true}")
    private boolean enabled = true;

    @Value("${railsahayak.rate-limit.limit-per-minute:300}")
    private int limitPerMinute = 300;

    // Default forwarded-header trust to disabled (false) unless explicitly enabled behind a verified reverse proxy
    @Value("${railsahayak.rate-limit.trust-forwarded-for:false}")
    private boolean trustForwardedFor = false;

    // Documented trusted reverse-proxy IP addresses (defaults to loopback interfaces)
    @Value("${railsahayak.rate-limit.trusted-proxies:127.0.0.1,::1,0:0:0:0:0:0:0:1}")
    private String trustedProxiesConfig = "127.0.0.1,::1,0:0:0:0:0:0:0:1";

    private Set<String> trustedProxies = Set.of("127.0.0.1", "::1", "0:0:0:0:0:0:0:1");

    private static final java.util.regex.Pattern IP_PATTERN =
            java.util.regex.Pattern.compile("^[a-fA-F0-9:.]+$");

    private static final ConcurrentHashMap<String, RequestCounter> requestCounts = new ConcurrentHashMap<>();

    private static class RequestCounter {
        final long windowStartMs;
        final AtomicInteger count;

        RequestCounter(long windowStartMs) {
            this.windowStartMs = windowStartMs;
            this.count = new AtomicInteger(1);
        }
    }

    @PostConstruct
    public void init() {
        parseTrustedProxies(this.trustedProxiesConfig);
    }

    public void parseTrustedProxies(String config) {
        if (config != null && !config.isBlank()) {
            this.trustedProxies = Arrays.stream(config.split(","))
                    .map(String::trim)
                    .filter(s -> !s.isEmpty())
                    .collect(Collectors.toSet());
        } else {
            this.trustedProxies = Collections.emptySet();
        }
    }

    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain)
            throws ServletException, IOException {

        if (!enabled) {
            filterChain.doFilter(request, response);
            return;
        }

        String path = request.getRequestURI();
        // Do not rate limit static resources or public health probes
        if (path == null || path.equals("/") || path.equals("/index.html") || path.equals("/favicon.ico")
                || path.startsWith("/static/") || path.equals("/api/v1/health")) {
            filterChain.doFilter(request, response);
            return;
        }

        String clientIp = getClientIp(request);
        long now = System.currentTimeMillis();

        RequestCounter counter = requestCounts.compute(clientIp, (key, existing) -> {
            if (existing == null || (now - existing.windowStartMs) > 60_000) {
                return new RequestCounter(now);
            }
            existing.count.incrementAndGet();
            return existing;
        });

        if (counter.count.get() > limitPerMinute) {
            log.warn("Rate limit exceeded for IP: {} on URI: {} (count: {})", clientIp, path, counter.count.get());
            response.setStatus(HttpStatus.TOO_MANY_REQUESTS.value());
            response.setContentType("application/json");
            response.setHeader("Retry-After", "60");
            response.getWriter().write("{\"status\":429,\"error\":\"TOO_MANY_REQUESTS\",\"message\":\"Rate limit exceeded. Please wait before retrying.\",\"retryAfterSeconds\":60}");
            return;
        }

        // Periodic opportunistic cleanup
        if (requestCounts.size() > 5000) {
            requestCounts.entrySet().removeIf(entry -> (now - entry.getValue().windowStartMs) > 120_000);
        }

        filterChain.doFilter(request, response);
    }

    private String getClientIp(HttpServletRequest request) {
        String remoteAddr = request.getRemoteAddr() != null ? request.getRemoteAddr().trim() : "127.0.0.1";

        // Security check: Only inspect X-Forwarded-For if forwarded-header trust is explicitly enabled
        // AND the direct remote connection originates from a documented, trusted reverse proxy.
        // IP pattern matching alone does not prevent spoofing; proxy origin verification is mandatory.
        if (trustForwardedFor && isTrustedProxy(remoteAddr)) {
            String xForwardedFor = request.getHeader("X-Forwarded-For");
            if (xForwardedFor != null && !xForwardedFor.isBlank()) {
                String candidate = xForwardedFor.split(",")[0].trim();
                // Reject malformed, oversized (>45 chars for standard IPv6), or non-IP characters
                if (candidate.length() <= 45 && IP_PATTERN.matcher(candidate).matches()) {
                    return candidate;
                } else {
                    log.warn("Ignored malformed or oversized X-Forwarded-For header from trusted proxy [{}]: '{}'",
                            remoteAddr, candidate.length() > 50 ? candidate.substring(0, 50) + "..." : candidate);
                }
            }
        }

        return remoteAddr;
    }

    private boolean isTrustedProxy(String remoteAddr) {
        if (trustedProxies == null || trustedProxies.isEmpty()) {
            return false;
        }
        return trustedProxies.contains(remoteAddr);
    }

    public void setLimitPerMinute(int limit) {
        this.limitPerMinute = limit;
    }

    public void setEnabled(boolean enabled) {
        this.enabled = enabled;
    }

    public void setTrustForwardedFor(boolean trustForwardedFor) {
        this.trustForwardedFor = trustForwardedFor;
    }

    public void setTrustedProxies(String proxiesCommaSeparated) {
        parseTrustedProxies(proxiesCommaSeparated);
    }

    public static void clearRateLimits() {
        requestCounts.clear();
    }
}

