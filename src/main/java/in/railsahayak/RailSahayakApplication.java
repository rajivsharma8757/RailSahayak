package in.railsahayak;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import java.net.URI;
import java.util.TimeZone;

@SpringBootApplication
public class RailSahayakApplication {

    static {
        System.setProperty("user.timezone", "Asia/Kolkata");
        TimeZone.setDefault(TimeZone.getTimeZone("Asia/Kolkata"));

        normalizeDatabaseUrl();
    }

    private static void normalizeDatabaseUrl() {
        String dbUrl = System.getenv("DB_URL");
        if (dbUrl == null || dbUrl.isBlank()) {
            dbUrl = System.getenv("DATABASE_URL");
        }
        if (dbUrl != null && !dbUrl.isBlank()) {
            if (dbUrl.startsWith("postgres://") || dbUrl.startsWith("postgresql://")) {
                try {
                    URI uri = URI.create(dbUrl);
                    String host = uri.getHost();
                    int port = uri.getPort() > 0 ? uri.getPort() : 5432;
                    String path = uri.getPath() != null && uri.getPath().length() > 1 ? uri.getPath().substring(1) : "railsahayak";
                    String jdbcUrl = "jdbc:postgresql://" + host + ":" + port + "/" + path;
                    System.setProperty("spring.datasource.url", jdbcUrl);
                    System.setProperty("DB_URL", jdbcUrl);

                    if (uri.getUserInfo() != null && !uri.getUserInfo().isBlank()) {
                        String[] parts = uri.getUserInfo().split(":", 2);
                        if (parts.length > 0 && !parts[0].isBlank()) {
                            System.setProperty("spring.datasource.username", parts[0]);
                            System.setProperty("DB_USERNAME", parts[0]);
                        }
                        if (parts.length > 1 && !parts[1].isBlank()) {
                            System.setProperty("spring.datasource.password", parts[1]);
                            System.setProperty("DB_PASSWORD", parts[1]);
                        }
                    }
                } catch (Exception e) {
                    String converted = dbUrl.replaceFirst("^postgres(ql)?://", "jdbc:postgresql://");
                    System.setProperty("spring.datasource.url", converted);
                    System.setProperty("DB_URL", converted);
                }
            }
        }
    }

    public static void main(String[] args) {
        SpringApplication.run(RailSahayakApplication.class, args);
    }
}

