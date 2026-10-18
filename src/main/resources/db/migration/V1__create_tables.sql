CREATE TABLE support_cases (
 id BIGSERIAL PRIMARY KEY,
 public_id VARCHAR(24) NOT NULL UNIQUE,
 owner_username VARCHAR(100) NOT NULL,
 category VARCHAR(80) NOT NULL,
 description VARCHAR(500) NOT NULL,
 status VARCHAR(24) NOT NULL,
 created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX idx_cases_owner ON support_cases(owner_username, created_at DESC);
CREATE TABLE case_events (
 id BIGSERIAL PRIMARY KEY,
 case_id BIGINT NOT NULL REFERENCES support_cases(id) ON DELETE CASCADE,
 actor_username VARCHAR(100) NOT NULL,
 event_type VARCHAR(40) NOT NULL,
 note VARCHAR(500),
 created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE TABLE audit_logs (
 id BIGSERIAL PRIMARY KEY,
 actor_username VARCHAR(100) NOT NULL,
 action VARCHAR(80) NOT NULL,
 resource_type VARCHAR(80) NOT NULL,
 resource_id VARCHAR(80),
 detail VARCHAR(500),
 created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
