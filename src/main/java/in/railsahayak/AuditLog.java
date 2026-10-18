package in.railsahayak;
import jakarta.persistence.*;
import java.time.Instant;
@Entity @Table(name="audit_logs")
public class AuditLog {
 @Id @GeneratedValue(strategy=GenerationType.IDENTITY) private Long id;
 @Column(name="actor_username",nullable=false) private String actor;
 @Column(nullable=false) private String action;
 @Column(name="resource_type",nullable=false) private String resourceType;
 @Column(name="resource_id") private String resourceId;
 @Column(length=500) private String detail;
 @Column(name="created_at",nullable=false) private Instant createdAt;
 protected AuditLog(){}
 public AuditLog(String actor,String action,String type,String id,String detail){this.actor=actor;this.action=action;this.resourceType=type;this.resourceId=id;this.detail=detail;this.createdAt=Instant.now();}
 public Long getId(){return id;}
 public String getActor(){return actor;}
 public String getAction(){return action;}
 public String getResourceType(){return resourceType;}
 public String getResourceId(){return resourceId;}
 public String getDetail(){return detail;}
 public Instant getCreatedAt(){return createdAt;}
}

