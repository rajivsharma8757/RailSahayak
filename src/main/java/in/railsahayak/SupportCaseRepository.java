package in.railsahayak;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;
import java.util.Optional;
public interface SupportCaseRepository extends JpaRepository<SupportCase,Long> {
 List<SupportCase> findByOwnerUsernameOrderByCreatedAtDesc(String owner);
 Optional<SupportCase> findByPublicId(String publicId);
}
