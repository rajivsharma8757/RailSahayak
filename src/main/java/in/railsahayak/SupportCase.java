package in.railsahayak;
import jakarta.persistence.*;
import java.time.Instant;
@Entity @Table(name="support_cases")
public class SupportCase {
 @Id @GeneratedValue(strategy=GenerationType.IDENTITY) private Long id;
 @Column(name="public_id",nullable=false,unique=true) private String publicId;
 @Column(name="owner_username",nullable=false) private String ownerUsername;
 @Column(nullable=false,length=80) private String category;
 @Column(nullable=false,length=500) private String description;
 @Column(nullable=false,length=24) private String status;
 @Column(name="created_at",nullable=false) private Instant createdAt;
 @Column(name="updated_at",nullable=false) private Instant updatedAt;
 protected SupportCase() {}
 public SupportCase(String id,String owner,String category,String description) {
  this.publicId=id; this.ownerUsername=owner; this.category=category; this.description=description;
  this.status="OPEN"; this.createdAt=Instant.now(); this.updatedAt=this.createdAt;
 }
 @PreUpdate void touch(){updatedAt=Instant.now();}
 public Long getId(){return id;} public String getPublicId(){return publicId;}
 public String getOwnerUsername(){return ownerUsername;} public String getCategory(){return category;}
 public String getDescription(){return description;} public String getStatus(){return status;}
 public Instant getCreatedAt(){return createdAt;} public Instant getUpdatedAt(){return updatedAt;}
 public void setStatus(String s){status=s;}
}
