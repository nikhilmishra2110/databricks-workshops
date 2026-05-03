# Lakebase-Backed App Architecture

## Purpose

Show how a Databricks App can combine governed lakehouse analytics with Lakebase operational state.

## Reads From Unity Catalog

- `workshop.beverage_distribution.gold_account_intelligence`
- `workshop.beverage_distribution.silver_account_orders`
- `workshop.beverage_distribution.silver_inventory_position`

## Writes To Lakebase

- saved account action plans
- recommendation feedback
- prompt test cases
- rep follow-up status

## Minimal Flow

1. User selects an account.
2. App reads account intelligence from Unity Catalog.
3. App generates or displays a next-best-action recommendation.
4. User accepts, edits, or rejects the recommendation.
5. App writes feedback and follow-up status to Lakebase.
6. MLflow evaluation can use feedback for the next prompt/model iteration.

## Prompt For Genie Code

```text
Using the Lakebase schema in app/lakebase_schema.sql, create a minimal Streamlit Databricks App that:
1. Reads account intelligence from Unity Catalog.
2. Shows recommended next actions.
3. Lets the user accept, edit, or reject a recommendation.
4. Writes the result to Lakebase using injected Postgres environment variables.
5. Handles missing Lakebase connection settings with a clear error message.

Return a plan first. Wait for approval before editing files.
```

