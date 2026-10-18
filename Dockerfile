# ==============================================================================
# RailSahayak Multi-Stage Production Dockerfile
# Base: Eclipse Temurin OpenJDK 21 LTS
# ==============================================================================

# Stage 1: Build stage
FROM maven:3.9.9-eclipse-temurin-21-alpine AS builder

WORKDIR /build

# Cache dependencies
COPY pom.xml .
RUN mvn dependency:go-offline -B

# Copy source code and build application jar
COPY src ./src
RUN mvn clean package -DskipTests -B

# Stage 2: Runtime stage
FROM eclipse-temurin:21-jre-alpine AS runner

WORKDIR /app

# Create unprivileged application user
RUN addgroup -S railsahayak && adduser -S railsahayak -G railsahayak

# Copy compiled jar from build stage
COPY --from=builder /build/target/railsahayak-backend-0.1.0.jar /app/app.jar

# Expose default HTTP port
EXPOSE 8081

# Set ownership to unprivileged user
USER railsahayak

# Environment defaults
ENV PORT=8081 \
    SPRING_PROFILES_ACTIVE=default \
    TZ=Asia/Kolkata

# Health check probe against public health endpoint
HEALTHCHECK --interval=30s --timeout=5s --start-period=40s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost:${PORT}/api/v1/health || exit 1

ENTRYPOINT ["java", "-Duser.timezone=Asia/Kolkata", "-jar", "/app/app.jar"]
