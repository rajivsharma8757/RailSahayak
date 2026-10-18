-- Flyway Migration V2: Add Performance & Concurrency Indexes
-- Improves query execution time for case timelines, audit trails, and status queues under concurrent load

CREATE INDEX IF NOT EXISTS idx_case_events_case_id ON case_events(case_id, created_at ASC);
CREATE INDEX IF NOT EXISTS idx_audit_logs_created_at ON audit_logs(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_cases_status ON support_cases(status, created_at DESC);
