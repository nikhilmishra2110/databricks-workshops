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

