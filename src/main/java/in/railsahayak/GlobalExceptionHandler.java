package in.railsahayak;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.slf4j.MDC;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;

import java.time.Instant;
import java.util.Map;

@ControllerAdvice
public class GlobalExceptionHandler {

    private static final Logger log = LoggerFactory.getLogger(GlobalExceptionHandler.class);

    // Only catch general unexpected exceptions to prevent internal stack traces leaking to client.
    // ResponseStatusException, MethodArgumentNotValidException, and AccessDeniedException
    // are re-thrown so Spring MVC handles them with proper HTTP status codes, reasons, and validation messages.
    @ExceptionHandler(Exception.class)
    public ResponseEntity<Map<String, Object>> handleUnexpectedException(Exception ex) throws Exception {
        if (ex instanceof org.springframework.web.server.ResponseStatusException
                || ex instanceof org.springframework.web.bind.MethodArgumentNotValidException
                || ex instanceof org.springframework.security.access.AccessDeniedException) {
            throw ex;
        }

        String correlationId = MDC.get(CorrelationIdFilter.MDC_KEY);
        log.error("Unhandled server exception [correlationId: {}]: {}", correlationId, ex.getMessage(), ex);

        Map<String, Object> body = Map.of(
                "timestamp", Instant.now().toString(),
                "status", HttpStatus.INTERNAL_SERVER_ERROR.value(),
                "error", "Internal Server Error",
                "message", "An unexpected server error occurred. Please quote reference '" +
                        (correlationId != null ? correlationId : "N/A") + "' when contacting passenger support.",
                "correlationId", correlationId != null ? correlationId : ""
        );

        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(body);
    }
}
