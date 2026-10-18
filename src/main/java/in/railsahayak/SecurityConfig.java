package in.railsahayak;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.Customizer;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.provisioning.InMemoryUserDetailsManager;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.security.web.header.writers.ReferrerPolicyHeaderWriter;

@Configuration
public class SecurityConfig {

    private static final Logger log = LoggerFactory.getLogger(SecurityConfig.class);

    @Value("${DEMO_PASSENGER_PASSWORD:PassengerDemo123!}")
    private String demoPassengerPassword;

    @Value("${DEMO_ADMIN_PASSWORD:AdminDemo123!}")
    private String demoAdminPassword;

    // Local-demo accounts only. Clearly marked for demonstration and evaluation.
    // Replace with approved persistent identity management before production railway deployment.
    @Bean
    UserDetailsService users(PasswordEncoder encoder) {
        String passengerPass = (demoPassengerPassword != null && !demoPassengerPassword.trim().isEmpty())
                ? demoPassengerPassword.trim()
                : "PassengerDemo123!";
        String adminPass = (demoAdminPassword != null && !demoAdminPassword.trim().isEmpty())
                ? demoAdminPassword.trim()
                : "AdminDemo123!";

        if ("PassengerDemo123!".equals(passengerPass) || "AdminDemo123!".equals(adminPass)) {
            log.warn("================================================================================");
            log.warn("SECURITY WARNING: Using default evaluation demo passwords.");
            log.warn("For any isolated multi-user evaluation, override via environment variables:");
            log.warn("  - DEMO_PASSENGER_PASSWORD=<secure_password>");
            log.warn("  - DEMO_ADMIN_PASSWORD=<secure_password>");
            log.warn("================================================================================");
        } else {
            log.info("Demo authentication initialized with custom environment variable credentials.");
        }

        log.warn("================================================================================");
        log.warn("SECURITY NOTICE: Running with in-memory DEMO authentication accounts.");
        log.warn("Do NOT deploy to production or connect to external railway networks with this setup.");
        log.warn("Production deployment requires database-backed auth, OAuth2/OIDC or SSO integration.");
        log.warn("================================================================================");

        return new InMemoryUserDetailsManager(
                User.withUsername("passenger")
                        .password(encoder.encode(passengerPass))
                        .roles("PASSENGER")
                        .build(),
                User.withUsername("admin")
                        .password(encoder.encode(adminPass))
                        .roles("ADMIN")
                        .build()
        );
    }

    @Bean
    PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }

    @Bean
    SecurityFilterChain filter(HttpSecurity h) throws Exception {
        return h.csrf(c -> c.disable())
                .headers(headers -> headers
                        .contentTypeOptions(Customizer.withDefaults())
                        .frameOptions(frame -> frame.sameOrigin())
                        .referrerPolicy(ref -> ref.policy(ReferrerPolicyHeaderWriter.ReferrerPolicy.STRICT_ORIGIN_WHEN_CROSS_ORIGIN))
                        .permissionsPolicy(perm -> perm.policy("camera=(), microphone=(), geolocation=()"))
                )
                .authorizeHttpRequests(a -> a
                        .requestMatchers("/", "/index.html", "/favicon.ico", "/static/**", "/api/v1/health").permitAll()
                        .requestMatchers("/api/v1/admin/**").hasRole("ADMIN")
                        .anyRequest().authenticated())
                .httpBasic(b -> b.authenticationEntryPoint((request, response, authException) -> {
                    response.setStatus(org.springframework.http.HttpStatus.UNAUTHORIZED.value());
                    response.setContentType("application/json");
                    response.getWriter().write("{\"error\":\"UNAUTHORIZED\",\"message\":\"" + authException.getMessage() + "\"}");
                }))
                .build();
    }
}

