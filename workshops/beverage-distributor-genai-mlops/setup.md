# Setup

## Required Databricks Capabilities

- Unity Catalog enabled
- SQL warehouse with required permissions
- Workspace access to Genie Code
- Permission to create or edit Lakeflow pipelines
- MLflow experiment access
- Databricks Apps access if running the app exercise
- Lakebase enabled if running the Lakebase exercise

## Recommended Permissions

- `USE CATALOG` and `USE SCHEMA` on the workshop catalog/schema
- `CREATE TABLE`, `CREATE VOLUME`, and `CREATE FUNCTION` where applicable
- SQL warehouse `CAN USE`
- permission to create Lakeflow pipelines
- permission to create MLflow experiments
- permission to create Databricks Apps
- Lakebase project `CAN MANAGE` for app resource setup

## Naming

Use the placeholders in `assets/resource-names.yml`.

Suggested values:

```text
catalog: workshop
schema: beverage_distribution
pipeline: beverage_account_intelligence_pipeline
genie_space: Beverage Account Intelligence
mlflow_experiment: /Shared/beverage_account_intelligence
lakebase_project: beverage-account-actions
```

## Skills Setup

Copy or sync the repo skills into Databricks:

```text
Workspace/.assistant/skills/
```

or:

```text
/Users/{username}/.assistant/skills/
```

Then open Genie Code Agent mode and mention the relevant skill when needed:

```text
@lakehouse-data-generator
@lakeflow-pipeline-builder
@genie-space-optimizer
@mlflow-genai-evaluator
@lakebase-app-builder
```

## Data Safety

This workshop uses synthetic data. Do not paste customer PII, private account data, contracts, or credentials into prompts.

