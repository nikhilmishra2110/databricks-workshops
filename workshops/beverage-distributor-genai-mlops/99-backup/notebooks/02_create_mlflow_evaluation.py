# Databricks notebook source
# MAGIC %md
# MAGIC # Backup 02 - MLflow Evaluation
# MAGIC
# MAGIC Creates a deterministic MLflow run that compares two recommendation prompt variants.

# COMMAND ----------

dbutils.widgets.text("catalog", "workshop")
dbutils.widgets.text("schema", "beverage_distribution")
dbutils.widgets.text("mlflow_experiment", "/Shared/beverage_account_intelligence")

catalog = dbutils.widgets.get("catalog")
schema = dbutils.widgets.get("schema")
mlflow_experiment = dbutils.widgets.get("mlflow_experiment")

# COMMAND ----------

import json
import tempfile

import mlflow
import pandas as pd

mlflow.set_experiment(mlflow_experiment)

source_table = f"{catalog}.{schema}.gold_account_intelligence"

try:
    eval_pdf = (
        spark.table(source_table)
        .select(
            "account_id",
            "account_segment",
            "region",
            "reorder_risk",
            "paid_net_amount",
            "days_since_last_paid_order",
            "latest_note_text",
            "recommended_action_seed",
        )
        .limit(10)
        .toPandas()
    )
except Exception as exc:
    print(f"Could not load {source_table}, using in-memory fallback examples. Reason: {exc}")
    eval_pdf = pd.DataFrame(
        [
            {
                "account_id": "A-1001",
                "account_segment": "restaurant",
                "region": "West",
                "reorder_risk": "high",
                "paid_net_amount": 166.50,
                "days_since_last_paid_order": 35,
                "latest_note_text": "Asked about lager availability before weekend events.",
                "recommended_action_seed": "Contact account this week with reorder and inventory context.",
            }
        ]
    )

# COMMAND ----------

prompt_a = "Recommend the next action for this beverage account."
prompt_b = (
    "Recommend the next action for this beverage account. "
    "Ground the answer in reorder risk, order history, inventory or notes, and include a concise rationale."
)


def recommend(row, variant):
    risk = row.get("reorder_risk", "unknown")
    note = row.get("latest_note_text") or "No note available."
    if risk == "hold":
        action = "Resolve account status before order recommendation."
    elif risk == "high":
        action = "Contact this account this week with a focused reorder plan."
    elif risk == "medium":
        action = "Review account before the next route cycle."
    else:
        action = "Maintain normal cadence and monitor."

    if variant == "B":
        rationale = f"Risk={risk}; days_since_last_order={row.get('days_since_last_paid_order')}; note={note}"
    else:
        rationale = f"Risk={risk}."

    return {
        "recommendation": action,
        "rationale": rationale,
        "confidence": 0.85 if risk in ["high", "hold"] else 0.70,
        "follow_up_action": action,
    }


def score_output(row, output):
    rationale = output["rationale"]
    groundedness = 5 if "Risk=" in rationale and str(row.get("reorder_risk")) in rationale else 3
    actionability = 5 if output["follow_up_action"] else 1
    business_relevance = 5 if row.get("reorder_risk") in ["high", "hold", "medium", "low"] else 3
    safety_pass = True
    concision = 5 if len(output["recommendation"]) < 120 else 3
    return {
        "groundedness": groundedness,
        "actionability": actionability,
        "business_relevance": business_relevance,
        "safety_pass": safety_pass,
        "concision": concision,
    }


records = []
for _, row in eval_pdf.iterrows():
    row_dict = row.to_dict()
    for variant, prompt in [("A", prompt_a), ("B", prompt_b)]:
        output = recommend(row_dict, variant)
        scores = score_output(row_dict, output)
        records.append(
            {
                **{f"input_{k}": v for k, v in row_dict.items()},
                "variant": variant,
                "prompt": prompt,
                **output,
                **scores,
            }
        )

results_pdf = pd.DataFrame(records)

# COMMAND ----------

with mlflow.start_run(run_name="backup_genai_recommendation_eval") as run:
    mlflow.log_param("source_table", source_table)
    mlflow.log_param("prompt_a", prompt_a)
    mlflow.log_param("prompt_b", prompt_b)

    for variant, group in results_pdf.groupby("variant"):
        mlflow.log_metric(f"{variant}_avg_groundedness", float(group["groundedness"].mean()))
        mlflow.log_metric(f"{variant}_avg_actionability", float(group["actionability"].mean()))
        mlflow.log_metric(f"{variant}_avg_business_relevance", float(group["business_relevance"].mean()))
        mlflow.log_metric(f"{variant}_avg_concision", float(group["concision"].mean()))

    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump(records, f, indent=2, default=str)
        artifact_path = f.name
    mlflow.log_artifact(artifact_path, artifact_path="evaluation")

display(results_pdf)
print(f"MLflow run: {run.info.run_id}")

