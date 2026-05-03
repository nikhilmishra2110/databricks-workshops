# Prompt

```text
Use Genie Code Agent mode.

Optional skill if available: @lakebase-app-builder. If the skill is unavailable, continue with this prompt without blocking.

You are in step 08 of the workshop: create Lakebase operational state.

Goal:
Use Lakebase Postgres for app state and human feedback. Do not use Lakebase as the analytical source of record.

Create or guide me through creating:
- Lakebase Autoscaling project: beverage-account-actions
- branch: production
- database: beverage-app-state
- schema: account_actions

Preferred implementation pattern:
1. Use Databricks Python SDK for Lakebase control-plane setup if supported in the workspace:
   - import `WorkspaceClient` from `databricks.sdk`
   - inspect or create the Lakebase Autoscaling project
   - inspect branch `production`
   - inspect database `beverage-app-state`
2. Use Postgres SQL to create the schema and tables.
3. For the app runtime, do not use SDK as the primary data path. The app should connect to Lakebase through Databricks Apps database resource environment variables:
   - PGHOST
   - PGPORT
   - PGDATABASE
   - PGUSER
   - PGSSLMODE
   - PGAPPNAME
4. Do not hardcode Lakebase credentials or connection strings.
5. Mention that the Lakebase Data API is optional and not required for this workshop app.

Use the SQL in:
08-create-lakebase/lakebase_schema.sql

Create tables for:
- account_action_plan
- recommendation_feedback
- rep_follow_up_status
- prompt_test_case

Return:
1. Lakebase creation plan.
2. Required permissions.
3. Whether this workspace uses Lakebase Autoscaling or an existing provisioned database.
4. Exact SQL to run.
5. Validation SQL:
   - list schemas
   - list tables
   - insert one synthetic action plan
   - insert one synthetic feedback record
   - select records back
6. Explanation of what belongs in Lakebase vs Unity Catalog.
7. How step 09 should add Lakebase as a Databricks App resource.
8. Cleanup instructions.

Wait for approval before creating resources or running SQL.

If Lakebase is unavailable, use `99-backup/fallback-lakebase-sqlite.md` and keep the workshop moving.
```
