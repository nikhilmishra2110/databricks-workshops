# Databricks notebook source
# MAGIC %md
# MAGIC # Backup 04 - Generate App Files
# MAGIC
# MAGIC Generates a minimal Streamlit Databricks App with Lakebase and Genie resource hooks.

# COMMAND ----------

dbutils.widgets.text("catalog", "workshop")
dbutils.widgets.text("schema", "beverage_distribution")
dbutils.widgets.text("app_dir", "")

catalog = dbutils.widgets.get("catalog")
schema = dbutils.widgets.get("schema")
app_dir = dbutils.widgets.get("app_dir")

if not app_dir:
    user = spark.sql("SELECT current_user() AS user").collect()[0]["user"]
    app_dir = f"/Workspace/Users/{user}/beverage-account-intelligence-app"

print(f"Generating app files in {app_dir}")

# COMMAND ----------

import os
from textwrap import dedent

os.makedirs(app_dir, exist_ok=True)

app_py = f'''
import os

import pandas as pd
import streamlit as st

try:
    import psycopg
except Exception:
    psycopg = None

try:
    from databricks import sql
except Exception:
    sql = None

try:
    from databricks.sdk import WorkspaceClient
except Exception:
    WorkspaceClient = None


CATALOG = "{catalog}"
SCHEMA = "{schema}"
GOLD_TABLE = f"{{CATALOG}}.{{SCHEMA}}.gold_account_intelligence"


def lakebase_ready():
    required = ["PGHOST", "PGPORT", "PGDATABASE", "PGUSER", "PGSSLMODE"]
    return all(os.getenv(key) for key in required) and psycopg is not None


def get_lakebase_connection():
    if not lakebase_ready():
        return None
    return psycopg.connect(
        host=os.getenv("PGHOST"),
        port=os.getenv("PGPORT"),
        dbname=os.getenv("PGDATABASE"),
        user=os.getenv("PGUSER"),
        sslmode=os.getenv("PGSSLMODE", "require"),
    )


def load_demo_accounts():
    return pd.DataFrame(
        [
            {{
                "account_id": "A-1001",
                "account_name": "Alpine Cellars",
                "region": "West",
                "reorder_risk": "high",
                "paid_net_amount": 521.10,
                "latest_note_text": "Manager asked about lager availability before weekend events.",
                "recommended_action_seed": "Contact this account this week with reorder and inventory context.",
            }},
            {{
                "account_id": "A-1004",
                "account_name": "Mesa Spirits",
                "region": "South",
                "reorder_risk": "hold",
                "paid_net_amount": 66.60,
                "latest_note_text": "License review pending; avoid new spirits order until cleared.",
                "recommended_action_seed": "Resolve account status before recommending an order.",
            }},
        ]
    )


def load_accounts():
    # Workshop fallback: use demo data unless a SQL warehouse connection is configured.
    # Facilitators can replace this with Databricks SQL connector connection settings.
    return load_demo_accounts()


def save_feedback(account_id, recommendation, accepted, notes):
    if not lakebase_ready():
        return False, "Lakebase resource is not configured. Running in demo mode."
    with get_lakebase_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO account_actions.account_action_plan
                  (account_id, recommendation, rationale, confidence, follow_up_action, status, created_by)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                RETURNING action_plan_id
                """,
                (account_id, recommendation, "Generated from app demo", 0.80, recommendation, "open", os.getenv("PGUSER")),
            )
            action_plan_id = cur.fetchone()[0]
            cur.execute(
                """
                INSERT INTO account_actions.recommendation_feedback
                  (action_plan_id, account_id, accepted, rep_notes, created_by)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (action_plan_id, account_id, accepted, notes, os.getenv("PGUSER")),
            )
        conn.commit()
    return True, "Saved feedback to Lakebase."


st.title("Beverage Account Intelligence")
st.caption("Workshop app: Unity Catalog analytics + Genie questions + Lakebase feedback state")

accounts = load_accounts()
selected = st.selectbox("Account", accounts["account_name"].tolist())
row = accounts[accounts["account_name"] == selected].iloc[0].to_dict()

st.subheader("Account Health")
st.write(row)

recommendation = row.get("recommended_action_seed", "Review account before next route cycle.")
st.subheader("Next Best Action")
edited = st.text_area("Recommendation", value=recommendation)
accepted = st.checkbox("Accept recommendation", value=True)
notes = st.text_area("Rep feedback notes")

if st.button("Save feedback"):
    ok, message = save_feedback(row["account_id"], edited, accepted, notes)
    if ok:
        st.success(message)
    else:
        st.warning(message)

if os.getenv("GENIE_SPACE_ID"):
    st.info("Genie space resource detected. Add WorkspaceClient Genie calls here for live Q&A.")
else:
    st.info("No Genie space resource detected. Running prepared-question demo mode.")
'''

app_yaml = """
command:
  - streamlit
  - run
  - app.py
"""

requirements = """
streamlit
databricks-sdk
databricks-sql-connector
psycopg[binary]
pandas
"""

readme = """
# Beverage Account Intelligence App

This app is generated by the workshop backup notebook.

Add Databricks App resources before deploying:

- Lakebase database resource with Can connect and create
- Genie space resource for Beverage Account Intelligence
- SQL warehouse configuration if you replace demo data with live Unity Catalog queries

Lakebase writes use injected `PG*` environment variables and `psycopg`.
Databricks SDK is reserved for workspace APIs such as Genie calls.
"""

files = {
    "app.py": app_py,
    "app.yaml": app_yaml,
    "requirements.txt": requirements,
    "README.md": readme,
}

for name, contents in files.items():
    path = os.path.join(app_dir, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(dedent(contents).strip() + "\n")
    print(f"Wrote {path}")

# COMMAND ----------

display(spark.createDataFrame([(app_dir,)], "app_dir string"))

