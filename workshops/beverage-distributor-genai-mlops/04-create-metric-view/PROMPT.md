# Prompt

```text
Use Genie Code Agent mode in a Databricks SQL editor or notebook.

Optional skill if available: @metric-view-builder. If the skill is unavailable, continue with this prompt without blocking.

You are in step 04 of the workshop: create a Unity Catalog metric view.

Create this metric view:
workshop.beverage_distribution.beverage_account_metrics

Source:
workshop.beverage_distribution.gold_account_intelligence

Use Databricks metric view syntax:
CREATE OR REPLACE VIEW <name> WITH METRICS LANGUAGE YAML AS $$ ... $$;

Measures to include:
- account_count
- paid_net_amount
- avg_days_since_last_order
- high_risk_accounts
- hold_accounts

Dimensions to include:
- account_id
- account_name
- region
- account_segment
- license_status
- reorder_risk
- sales_rep_id

Requirements:
1. Use business-friendly display names, comments, and synonyms where useful.
2. Make the metric view useful for Genie and dashboards.
3. Run SQL validation queries that show:
   - total account count
   - paid net amount by region
   - high risk accounts by sales rep
   - average days since last order by segment
4. Save the final SQL as `04-create-metric-view/generated_metric_view.sql` if file editing is available.

First return:
- the YAML metric definition
- the CREATE VIEW SQL
- the validation queries
- permission assumptions

Wait for approval before running SQL.

If metric views are unavailable, use `99-backup/fallback-standard-view.sql` to create a standard SQL view and explain what capability is missing.
```
