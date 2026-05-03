# App Architecture

## Reads

Unity Catalog:

- `workshop.beverage_distribution.gold_account_intelligence`
- `workshop.beverage_distribution.beverage_account_metrics`

Genie space resource:

- `Beverage Account Intelligence`

## Writes

Lakebase:

- `account_actions.account_action_plan`
- `account_actions.recommendation_feedback`
- `account_actions.rep_follow_up_status`

## Runtime Connections

Lakebase:

- Add Lakebase as a Databricks App database resource.
- Use injected Postgres environment variables:
  - `PGHOST`
  - `PGPORT`
  - `PGDATABASE`
  - `PGUSER`
  - `PGSSLMODE`
  - `PGAPPNAME`
- Use `psycopg` or SQLAlchemy for reads/writes to Lakebase app-state tables.

Genie:

- Add the Genie space as an app resource if available.
- Use the injected Genie space ID environment variable with `databricks.sdk.WorkspaceClient().genie`.

Unity Catalog:

- Read curated analytics through Databricks SQL connector, SDK SQL APIs, or a warehouse-backed query path.

Do not hardcode secrets or connection strings.

## User Flow

1. Select an account or region.
2. Review account health and reorder risk.
3. Ask a business question through Genie or a prepared question button.
4. See a generated next-best-action recommendation.
5. Accept, edit, or reject the recommendation.
6. Save feedback to Lakebase.
7. Use feedback later for MLflow evaluation and prompt improvement.
