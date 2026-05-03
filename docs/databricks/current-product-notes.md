# Databricks Product Notes

These notes capture the product assumptions used by the workshop assets. Validate them before a live delivery because Databricks product names and previews move quickly.

## Genie Code

Genie Code is the Databricks context-aware assistant for notebooks, SQL, jobs, dashboards, files, Lakeflow, and MLflow. Agent mode can perform multi-step work with approval.

Workshop implication: every workshop build step uses Genie Code Agent mode and asks for a plan before execution.

Reference: https://docs.databricks.com/aws/en/genie-code/

## Metric Views

Unity Catalog metric views define governed business metrics in YAML and can be created with SQL using `CREATE OR REPLACE VIEW ... WITH METRICS LANGUAGE YAML AS $$`. They can be used by SQL, dashboards, Genie spaces, and alerts.

Workshop implication: create the metric view after the Lakeflow gold table and before the Genie space so business definitions are centralized.

References:

- https://docs.databricks.com/aws/en/business-semantics/metric-views/create-edit
- https://docs.databricks.com/aws/en/business-semantics/metric-views/yaml-reference

## Genie Code Skills

Skills live in `.assistant/skills/`. Each skill has its own folder and a required `SKILL.md` file with frontmatter. Workspace skills are under `Workspace/.assistant/skills/`; user skills are under `/Users/{username}/.assistant/skills/`.

Workshop implication: this repo includes starter skills that can be copied into the Databricks workspace skill folder before the workshop.

Reference: https://docs.databricks.com/gcp/en/genie-code/skills

## Lakeflow Spark Declarative Pipelines

Lakeflow Spark Declarative Pipelines is the current Databricks framework for batch and streaming pipelines in SQL and Python. Python pipeline code uses `from pyspark import pipelines as dp` in current examples.

Workshop implication: use Genie Code Agent mode in the Lakeflow Pipelines Editor for prompt-driven pipeline creation and debugging.

Reference: https://docs.databricks.com/aws/en/ldp/

## Genie Spaces

Genie spaces let business users ask natural-language questions against curated Unity Catalog tables and views. A space needs Unity Catalog data and an appropriate SQL warehouse.

Workshop implication: optimize the space by including curated tables and the metric view, improving table comments, column comments, business definitions, and sample questions.

Reference: https://docs.databricks.com/gcp/en/genie/set-up

## MLflow 3 For GenAI

MLflow 3 for GenAI supports tracking, evaluation, observability, traces, scorers, human feedback, and version tracking for GenAI apps and agents.

Workshop implication: make the MLOps portion about instrumenting prompts, traces, evaluation sets, quality metrics, and iteration.

Reference: https://docs.databricks.com/aws/en/mlflow3/genai/

## Lakebase

Lakebase Postgres brings fully managed Postgres OLTP workloads to Databricks. As of March 12, 2026, new Lakebase databases are created as Lakebase Autoscaling projects in supported regions.

Workshop implication: use Lakebase for app state, feedback capture, prompt test cases, account action plans, or operational recommendations. Do not position Lakebase as the analytical source of record.

Reference: https://docs.databricks.com/aws/en/oltp/

## Databricks Apps With Genie And Lakebase

Databricks Apps can add Genie spaces and Lakebase databases as app resources. Lakebase-backed resources inject Postgres connection details into the app environment.

Workshop implication: the app exercise can combine a Genie space resource for natural-language analytics and a Lakebase resource for persistent workflow state.

References:

- https://docs.databricks.com/aws/en/dev-tools/databricks-apps/genie
- https://docs.databricks.com/aws/en/dev-tools/databricks-apps/lakebase
