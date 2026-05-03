# Prompt: Databricks Lakeflow Pipeline Builder

## Purpose

Use Genie Code to create Lakeflow Spark Declarative Pipeline source code from workshop source tables.

## Prompt

```text
You are building a Lakeflow Spark Declarative Pipeline in Databricks.

Source tables:
{{source_tables}}

Target tables:
{{target_tables}}

Data quality rules:
{{quality_rules}}

Generate:
1. Pipeline design.
2. Python pipeline source using current Lakeflow Spark Declarative Pipelines APIs.
3. Data quality expectations.
4. Notes on streaming tables vs materialized views.
5. Validation queries.

Do not run or deploy until I approve the plan and code.
```

