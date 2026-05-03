# Databricks notebook source
# MAGIC %md
# MAGIC # Backup 03 - Lakebase With Databricks SDK
# MAGIC
# MAGIC Uses the Databricks Python SDK for Lakebase control-plane setup when available.
# MAGIC This notebook does not hardcode database credentials.

# COMMAND ----------

dbutils.widgets.text("lakebase_project", "beverage-account-actions")
dbutils.widgets.text("branch", "production")
dbutils.widgets.text("database", "beverage-app-state")
dbutils.widgets.dropdown("attempt_create", "false", ["false", "true"])

project_id = dbutils.widgets.get("lakebase_project")
branch_id = dbutils.widgets.get("branch")
database_id = dbutils.widgets.get("database")
attempt_create = dbutils.widgets.get("attempt_create") == "true"

project_name = f"projects/{project_id}"
branch_name = f"{project_name}/branches/{branch_id}"
database_name = f"{branch_name}/databases/{database_id}"

print(f"project_name={project_name}")
print(f"branch_name={branch_name}")
print(f"database_name={database_name}")

# COMMAND ----------

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

try:
    me = w.current_user.me()
    print(f"Current user: {me.user_name}")
except Exception as exc:
    print(f"Could not resolve current user: {exc}")

# COMMAND ----------

postgres_api = getattr(w, "postgres", None)

if postgres_api is None:
    print("This Databricks SDK version does not expose w.postgres. Use the Lakebase UI or SQL editor fallback.")


def exists(getter, name):
    try:
        return getter(name)
    except Exception as exc:
        print(f"Not found or no permission for {name}: {exc}")
        return None


project = exists(postgres_api.get_project, project_name) if postgres_api else None
branch = exists(postgres_api.get_branch, branch_name) if postgres_api and project else None
database = exists(postgres_api.get_database, database_name) if postgres_api and branch else None

print(f"project_exists={project is not None}")
print(f"branch_exists={branch is not None}")
print(f"database_exists={database is not None}")

# COMMAND ----------

if attempt_create and postgres_api:
    from databricks.sdk.service import postgres

    if project is None:
        print("Attempting to create Lakebase project.")
        operation = postgres_api.create_project(
            project=postgres.Project(),
            project_id=project_id,
        )
        project = operation.wait()

    if branch is None:
        print("Attempting to create production branch.")
        operation = postgres_api.create_branch(
            parent=project_name,
            branch=postgres.Branch(),
            branch_id=branch_id,
            replace_existing=False,
        )
        branch = operation.wait()

    if database is None:
        print("Attempting to create database.")
        operation = postgres_api.create_database(
            parent=branch_name,
            database=postgres.Database(),
            database_id=database_id,
        )
        database = operation.wait()
elif attempt_create and not postgres_api:
    print("Cannot create Lakebase resources because this SDK does not expose w.postgres.")
else:
    print("Dry run only. Set attempt_create=true to create Lakebase resources.")

# COMMAND ----------

# MAGIC %md
# MAGIC ## App-State DDL
# MAGIC Run this SQL in the Lakebase SQL editor or through a secure Postgres connection.

# COMMAND ----------

lakebase_sql = """
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
"""

print(lakebase_sql)

# COMMAND ----------

# MAGIC %md
# MAGIC ## App Runtime Guidance
# MAGIC
# MAGIC In the Databricks App, add this Lakebase database as an App resource.
# MAGIC The app should connect through injected `PG*` environment variables using `psycopg` or SQLAlchemy.
# MAGIC Do not use Databricks SDK as the app runtime path for inserting app-state rows.
