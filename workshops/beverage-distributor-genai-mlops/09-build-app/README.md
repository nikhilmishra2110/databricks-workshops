# 09 - Build App

## Goal

Build a simple Databricks App that demonstrates the platform power end to end.

## App Pattern

- Read curated account intelligence from Unity Catalog.
- Let business users ask or select account questions.
- Show a next-best-action recommendation.
- Write accepted, edited, or rejected feedback to Lakebase.
- Link the evaluation mindset back to MLflow.

## Correct Implementation Pattern

- Use `app.yaml` for Databricks App runtime configuration.
- Add Lakebase as a Databricks App database resource in the app configuration UI or supported deployment flow.
- Use injected `PG*` environment variables in app code with `psycopg` or SQLAlchemy.
- Use the Databricks SDK inside the app only for workspace APIs such as Genie conversation calls, not for writing Lakebase app-state rows.
- Use the Databricks SQL connector or SDK/SQL APIs to read curated Unity Catalog data.
- Keep a demo mode for constrained environments.

## Done When

- App files are generated.
- App can read from Unity Catalog or use fallback sample data.
- App can write to Lakebase or use backup mode.
- Participants can explain the end-to-end architecture.

## Backup

If Databricks Apps are unavailable, run the Streamlit app locally or use `../99-backup/manual-runbook.md`.
