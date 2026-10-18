package in.railsahayak;
import jakarta.persistence.*;
import java.time.Instant;
@Entity @Table(name="case_events")
public class CaseEvent {
 @Id @GeneratedValue(strategy=GenerationType.IDENTITY) private Long id;
 @Column(name="case_id",nullable=false) private Long caseId;
 @Column(name="actor_username",nullable=false) private String actor;
 @Column(name="event_type",nullable=false) private String eventType;
 @Column(length=500) private String note;
 @Column(name="created_at",nullable=false) private Instant createdAt;
 protected CaseEvent(){}
 public CaseEvent(Long id,String actor,String type,String note){this.caseId=id;this.actor=actor;this.eventType=type;this.note=note;this.createdAt=Instant.now();}
 public Long getId(){return id;}
 public Long getCaseId(){return caseId;}
 public String getActor(){return actor;}
 public String getEventType(){return eventType;}
 public String getNote(){return note;}
 public Instant getCreatedAt(){return createdAt;}
}

