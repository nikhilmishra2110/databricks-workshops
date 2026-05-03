# Prompt: Databricks Lakebase App Builder

## Purpose

Design a Databricks App that uses Lakebase Postgres for operational state.

## Prompt

```text
You are designing a Databricks App with a Lakebase Postgres resource.

Application:
{{application_description}}

Lakebase state to persist:
{{state_entities}}

Analytics sources:
{{unity_catalog_tables}}

Return:
1. Lakebase project, branch, database, and schema naming.
2. PostgreSQL DDL.
3. Databricks Apps resource checklist.
4. Environment variables the app should expect.
5. Minimal Streamlit or Flask architecture.
6. Security and permission checks.
7. What belongs in Lakebase vs Unity Catalog.

First produce a plan. Do not create resources until approved.
```

