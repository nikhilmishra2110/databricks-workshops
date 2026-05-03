# Prompt

```text
Use Genie Code Agent mode.

Use skill: @lakebase-app-builder

You are in step 08 of the workshop: create Lakebase operational state.

Goal:
Use Lakebase Postgres for app state and human feedback. Do not use Lakebase as the analytical source of record.

Create or guide me through creating:
- Lakebase Autoscaling project: beverage-account-actions
- branch: production
- database: databricks_postgres
- schema: account_actions

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
7. Cleanup instructions.

Wait for approval before creating resources or running SQL.

If Lakebase is unavailable, use `99-backup/fallback-lakebase-sqlite.md` and keep the workshop moving.
```
