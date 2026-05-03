# Beverage Distribution GenAI MLOps Workshop

This folder is the full workshop. Run it from top to bottom.

Every numbered folder contains:

- `README.md`: what the step means and how to know it is complete
- `PROMPT.md`: the one-shot prompt to paste into Databricks Genie Code Agent mode

Custom skills are optional. If a prompt mentions a skill and the skill is not available, continue with the prompt text.

## Workshop Story

You are building a **Field Sales Account Intelligence Copilot** for a synthetic beverage distribution business.

The business user wants to answer questions like:

- Which accounts need attention this week?
- Why are they at risk?
- Are inventory or promotions affecting the recommendation?
- What action should the sales rep take next?
- How do we capture feedback after the rep accepts, edits, or rejects the recommendation?

The Databricks platform pattern is:

```text
synthetic data
  -> Lakeflow
  -> metric view
  -> Genie space
  -> business Q&A
  -> MLflow evaluation
  -> Lakebase
  -> Databricks App
```

## How To Run Each Step

1. Open the numbered folder.
2. Read the folder's `README.md`.
3. Copy the entire `PROMPT.md`.
4. Paste it into Genie Code Agent mode.
5. Tell Genie Code: "Give me the plan first."
6. Review the plan and generated code.
7. Approve execution.
8. Confirm the folder's "Done When" checklist.
9. Move to the next folder.

## Sequence

| Step | Folder | Goal | Output |
| --- | --- | --- | --- |
| 00 | `00-before-workshop` | Confirm the workspace can run the workshop. | Readiness report. |
| 01 | `01-use-case` | Explain the business problem and architecture. | Use case brief. |
| 02 | `02-generate-synthetic-data` | Generate synthetic source data. | Bronze Unity Catalog tables. |
| 03 | `03-build-lakeflow-pipeline` | Curate data with Lakeflow. | Silver and gold tables. |
| 04 | `04-create-metric-view` | Create governed metrics. | Unity Catalog metric view. |
| 05 | `05-create-optimize-genie-space` | Create business Q&A surface. | Genie space with curated context. |
| 06 | `06-business-scenarios` | Ask realistic business questions. | Scenario results and improvements. |
| 07 | `07-mlflow-genai-evaluation` | Evaluate recommendation quality. | MLflow evaluation run. |
| 08 | `08-create-lakebase` | Create app-state database. | Lakebase schema and tables. |
| 09 | `09-build-app` | Build user-facing app. | Streamlit Databricks App files. |
| 99 | `99-backup` | Recover when blocked. | Backup prompts, SQL, and notebooks. |

## Default Resource Names

```text
catalog: workshop
schema: beverage_distribution
metric_view: beverage_account_metrics
genie_space: Beverage Account Intelligence
mlflow_experiment: /Shared/beverage_account_intelligence
lakebase_project: beverage-account-actions
lakebase_database: beverage-app-state
```

## What Each Step Teaches

`00-before-workshop`  
How to check whether the workspace has the required Databricks features and permissions.

`01-use-case`  
How to start from a concrete business workflow instead of a generic technology demo.

`02-generate-synthetic-data`  
How to use a data contract to generate predictable, safe, synthetic data.

`03-build-lakeflow-pipeline`  
How to use prompt-driven development for curated data pipelines.

`04-create-metric-view`  
How to centralize business definitions before exposing them to business users.

`05-create-optimize-genie-space`  
How to make natural-language analytics more reliable with curated assets, comments, and business terms.

`06-business-scenarios`  
How business users would actually ask questions and where Genie needs better context.

`07-mlflow-genai-evaluation`  
How to evaluate GenAI recommendations instead of trusting generated answers blindly.

`08-create-lakebase`  
How to separate analytical data from operational app state.

`09-build-app`  
How Unity Catalog, Genie, MLflow, Lakebase, and Databricks Apps come together in one workflow.

## If Something Fails

Use `99-backup`.

Most common fallback paths:

```text
Lakeflow blocked       -> 99-backup/fallback-pipeline.py
Metric views blocked   -> 99-backup/fallback-standard-view.sql
Genie blocked          -> 99-backup/fallback-genie-questions.md
MLflow GenAI blocked   -> 99-backup/fallback-manual-evaluation.md
Lakebase blocked       -> 99-backup/fallback-lakebase-sqlite.md
Need run-all fallback  -> 99-backup/notebooks/00_run_all_backup.py
```

The backup notebooks are designed for Databricks notebooks:

```text
99-backup/notebooks/
```

## Important Rules

- Use synthetic data only.
- Ask Genie Code for a plan before execution.
- Review generated code before running it.
- Do not hardcode secrets.
- Treat skills as optional.
- Use Lakebase for app state, not as the analytical source of record.

