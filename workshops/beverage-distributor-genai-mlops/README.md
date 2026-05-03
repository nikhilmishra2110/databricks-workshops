# Beverage Distribution GenAI MLOps Workshop

This is a sequenced, prompt-driven Databricks workshop.

Use one folder at a time. Each folder contains a `PROMPT.md` that should be pasted into Databricks Genie Code Agent mode. Genie Code should plan first, then execute only after approval.

## Use Case

Field Sales Account Intelligence Copilot.

The business goal is to help sales leaders and field reps ask account-level questions, understand reorder risk, see inventory and promotion context, get recommended next actions, and save follow-up state in an app.

## Sequence

| Step | Folder | Outcome |
| --- | --- | --- |
| 00 | `00-before-workshop` | Check workspace permissions, skills, and feature readiness. |
| 01 | `01-use-case` | Create the one-page use case brief and target architecture. |
| 02 | `02-generate-synthetic-data` | Generate synthetic beverage distribution data in Unity Catalog. |
| 03 | `03-build-lakeflow-pipeline` | Build bronze to silver to gold Lakeflow pipeline logic. |
| 04 | `04-create-metric-view` | Create a governed Unity Catalog metric view for business metrics. |
| 05 | `05-create-optimize-genie-space` | Create and tune a Genie space for trusted Q&A. |
| 06 | `06-business-scenarios` | Run realistic business-user questions against the Genie space. |
| 07 | `07-mlflow-genai-evaluation` | Evaluate recommendation quality with MLflow GenAI. |
| 08 | `08-create-lakebase` | Create Lakebase operational state for actions and feedback. |
| 09 | `09-build-app` | Build a Databricks App that ties Genie, Unity Catalog, MLflow, and Lakebase together. |
| 99 | `99-backup` | Fallback prompts and manual assets if a step fails. |

## Default Resource Names

```text
catalog: workshop
schema: beverage_distribution
genie_space: Beverage Account Intelligence
metric_view: beverage_account_metrics
mlflow_experiment: /Shared/beverage_account_intelligence
lakebase_project: beverage-account-actions
```

## Run Style

For every step:

1. Open the numbered folder.
2. Open `PROMPT.md`.
3. Paste the prompt into Genie Code Agent mode.
4. Ask for the plan.
5. Review the plan and generated code.
6. Approve execution.
7. Confirm the "Done When" checklist in that folder's `README.md`.

If a permission or preview feature is missing, go to `99-backup`.
