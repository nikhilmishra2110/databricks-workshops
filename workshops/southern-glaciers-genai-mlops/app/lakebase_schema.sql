CREATE SCHEMA IF NOT EXISTS account_actions;

CREATE TABLE IF NOT EXISTS account_actions.account_action_plan (
  action_plan_id BIGSERIAL PRIMARY KEY,
  account_id TEXT NOT NULL,
  recommendation TEXT NOT NULL,
  rationale TEXT,
  confidence NUMERIC(4, 3),
  follow_up_action TEXT NOT NULL,
  status TEXT NOT NULL DEFAULT 'open',
  created_by TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS account_actions.recommendation_feedback (
  feedback_id BIGSERIAL PRIMARY KEY,
  action_plan_id BIGINT REFERENCES account_actions.account_action_plan(action_plan_id),
  account_id TEXT NOT NULL,
  accepted BOOLEAN NOT NULL,
  edited_recommendation TEXT,
  reason_rejected TEXT,
  rep_notes TEXT,
  created_by TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS account_actions.prompt_test_case (
  test_case_id BIGSERIAL PRIMARY KEY,
  account_id TEXT NOT NULL,
  input_context JSONB NOT NULL,
  expected_behavior TEXT,
  tags TEXT[],
  created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS account_actions.rep_follow_up_status (
  follow_up_id BIGSERIAL PRIMARY KEY,
  account_id TEXT NOT NULL,
  sales_rep_id TEXT,
  next_step TEXT NOT NULL,
  due_date DATE,
  status TEXT NOT NULL DEFAULT 'not_started',
  notes TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_action_plan_account
  ON account_actions.account_action_plan (account_id);

CREATE INDEX IF NOT EXISTS idx_feedback_account
  ON account_actions.recommendation_feedback (account_id);

