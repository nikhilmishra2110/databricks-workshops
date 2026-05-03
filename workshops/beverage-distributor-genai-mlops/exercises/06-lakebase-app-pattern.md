# Exercise 6: Lakebase App Pattern

## Goal

Design or create a Lakebase-backed Databricks App pattern for operational state.

## Steps

1. Use prompt 5 from `../prompts/prompt-pack.md`.
2. Confirm whether Lakebase is enabled in the workspace.
3. Create or design a Lakebase project, branch, and database.
4. Define PostgreSQL tables for saved actions and feedback.
5. Sketch a Streamlit app flow.
6. Decide what reads from Unity Catalog and what writes to Lakebase.

## Done When

- Lakebase is positioned for app state, not analytical source-of-record data.
- App tables are defined.
- Required permissions are known.
- Participants understand how Databricks Apps receive Lakebase resource connection details.

## App State Tables

- `account_action_plan`
- `recommendation_feedback`
- `prompt_test_case`
- `rep_follow_up_status`

