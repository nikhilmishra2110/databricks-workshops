# Databricks notebook source
# MAGIC %md
# MAGIC # Backup Run-All
# MAGIC
# MAGIC This notebook orchestrates the fallback path when the live Genie Code workshop flow is blocked.
# MAGIC It is intended for Databricks notebooks, not local execution.

# COMMAND ----------

dbutils.widgets.text("catalog", "workshop")
dbutils.widgets.text("schema", "beverage_distribution")
dbutils.widgets.text("mlflow_experiment", "/Shared/beverage_account_intelligence")
dbutils.widgets.text("lakebase_project", "beverage-account-actions")
dbutils.widgets.dropdown("run_lakebase_sdk", "false", ["false", "true"])
dbutils.widgets.dropdown("generate_app_files", "true", ["true", "false"])

catalog = dbutils.widgets.get("catalog")
schema = dbutils.widgets.get("schema")
mlflow_experiment = dbutils.widgets.get("mlflow_experiment")
lakebase_project = dbutils.widgets.get("lakebase_project")

print("Backup workshop run configuration")
print(f"catalog={catalog}")
print(f"schema={schema}")
print(f"mlflow_experiment={mlflow_experiment}")
print(f"lakebase_project={lakebase_project}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 1: Lakehouse Assets

# COMMAND ----------

dbutils.notebook.run(
    "./01_create_lakehouse_assets",
    timeout_seconds=1800,
    arguments={"catalog": catalog, "schema": schema},
)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 2: MLflow Evaluation

# COMMAND ----------

dbutils.notebook.run(
    "./02_create_mlflow_evaluation",
    timeout_seconds=1200,
    arguments={"catalog": catalog, "schema": schema, "mlflow_experiment": mlflow_experiment},
)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 3: Lakebase Control Plane
# MAGIC Set `run_lakebase_sdk=true` only if the workspace has Lakebase enabled and the user has permissions.

# COMMAND ----------

if dbutils.widgets.get("run_lakebase_sdk") == "true":
    dbutils.notebook.run(
        "./03_create_lakebase_with_sdk",
        timeout_seconds=1200,
        arguments={"lakebase_project": lakebase_project},
    )
else:
    print("Skipping Lakebase SDK setup. Use 03_create_lakebase_with_sdk when ready.")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 4: App Files

# COMMAND ----------

if dbutils.widgets.get("generate_app_files") == "true":
    dbutils.notebook.run(
        "./04_generate_app_files",
        timeout_seconds=600,
        arguments={"catalog": catalog, "schema": schema},
    )
else:
    print("Skipping app file generation.")
