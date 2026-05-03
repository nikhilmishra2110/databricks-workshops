# Genie Code Skills

The reusable Genie Code skills are in `.assistant/skills/`.

Copy that folder into Databricks:

```text
Workspace/.assistant/skills/
```

or:

```text
/Users/{username}/.assistant/skills/
```

## Skills In This Repo

| Skill | Use It When |
| --- | --- |
| `@beverage-distribution-domain` | You need the workshop's beverage distribution domain, entities, grains, and safety rules. |
| `@lakehouse-data-generator` | You need synthetic data and Unity Catalog tables. |
| `@lakeflow-pipeline-builder` | You need Lakeflow Spark Declarative Pipeline code or debugging. |
| `@metric-view-builder` | You need a Unity Catalog metric view for governed business metrics. |
| `@genie-space-optimizer` | You need a curated Genie space with business context and sample questions. |
| `@business-scenario-synthesizer` | You need business-user question scenarios for the Genie space. |
| `@mlflow-genai-evaluator` | You need MLflow tracking, traces, scorers, or evaluation data for GenAI. |
| `@lakebase-app-builder` | You need Lakebase app state, feedback tables, or a Databricks App pattern. |
| `@databricks-app-builder` | You need a Databricks App that connects Unity Catalog, Genie, MLflow, and Lakebase. |
