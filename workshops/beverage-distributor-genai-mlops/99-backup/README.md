# 99 - Backup

Use this folder when a Databricks feature, preview, or permission is unavailable during the workshop.

## Backup Philosophy

Keep momentum. The participant should still understand the platform pattern even if one resource cannot be created live.

## Common Fallbacks

| Failure | Use |
| --- | --- |
| Missing Unity Catalog create permissions | Ask admin for catalog/schema or use an existing schema. |
| Synthetic data generation fails | `fallback-synthetic-data-prompt.md` |
| Lakeflow unavailable | `fallback-pipeline.py` |
| Metric views unavailable | `fallback-standard-view.sql` |
| Genie unavailable | `fallback-genie-questions.md` |
| MLflow GenAI unavailable | `fallback-manual-evaluation.md` |
| Lakebase unavailable | `fallback-lakebase-sqlite.md` |
| Databricks Apps unavailable | Use app demo mode from step 09. |

## Backup Notebooks

The `notebooks/` folder contains notebook-style Python files for facilitator fallback:

| Notebook | Purpose |
| --- | --- |
| `00_run_all_backup.py` | Orchestrates the backup flow. |
| `01_create_lakehouse_assets.py` | Creates synthetic data, curated tables, and a metric view or standard view fallback. |
| `02_create_mlflow_evaluation.py` | Creates a deterministic MLflow evaluation run. |
| `03_create_lakebase_with_sdk.py` | Uses Databricks Python SDK for Lakebase control-plane setup when available and outputs SQL for app-state tables. |
| `04_generate_app_files.py` | Generates Streamlit Databricks App files with Lakebase/App resource patterns. |

These notebooks are designed for Databricks, not local execution.
