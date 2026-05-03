# Backup Notebooks

Use these only when the prompt-driven workshop path is blocked.

Recommended order:

1. `00_run_all_backup.py`
2. `01_create_lakehouse_assets.py`
3. `02_create_mlflow_evaluation.py`
4. `03_create_lakebase_with_sdk.py`
5. `04_generate_app_files.py`

The notebooks prefer Databricks-native APIs:

- Spark SQL for Unity Catalog objects and tables.
- MLflow for experiment tracking.
- Databricks Python SDK for control-plane checks and Lakebase project setup where available.
- Postgres SQL for Lakebase app-state schema creation.

The Lakebase notebook intentionally separates control-plane setup from app runtime access. Databricks Apps should connect to Lakebase through App resources and injected `PG*` environment variables.

