---
name: lakeflow-pipeline-builder
description: Use when designing, generating, reviewing, or debugging Lakeflow Spark Declarative Pipeline code for Databricks workshops.
---

# Lakeflow Pipeline Builder

Use this skill for Lakeflow Spark Declarative Pipelines.

## Steps

1. Identify source tables, target tables, and target catalog/schema.
2. Decide which outputs should be streaming tables, materialized views, or temporary views.
3. Add data quality expectations for keys, statuses, amounts, dates, and business rules.
4. Generate Python or SQL pipeline source code.
5. Keep pipeline functions focused on returning DataFrames.
6. Add validation queries and a debugging plan.
7. Explain assumptions before running or deploying.

## Python Pattern

Use the current Databricks Lakeflow Spark Declarative Pipelines style:

```python
from pyspark import pipelines as dp
from pyspark.sql import functions as F
```

## Avoid

- collecting data to the driver in pipeline definitions
- writing tables manually inside dataset functions
- mixing unrelated business logic into the same dataset
- creating broad pipelines that are hard to teach

## Review Checklist

- Dataset names are clear.
- Expectations are meaningful.
- The code matches the configured catalog and schema.
- The output layer is useful for Genie spaces or downstream ML.

