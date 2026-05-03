# Databricks notebook source
# MAGIC %md
# MAGIC # Backup 01 - Create Lakehouse Assets
# MAGIC
# MAGIC Creates synthetic data, curated tables, and a metric view or standard-view fallback.

# COMMAND ----------

dbutils.widgets.text("catalog", "workshop")
dbutils.widgets.text("schema", "beverage_distribution")

catalog = dbutils.widgets.get("catalog")
schema = dbutils.widgets.get("schema")

spark.sql(f"CREATE CATALOG IF NOT EXISTS {catalog}")
spark.sql(f"CREATE SCHEMA IF NOT EXISTS {catalog}.{schema}")
spark.sql(f"USE CATALOG {catalog}")
spark.sql(f"USE SCHEMA {schema}")

# COMMAND ----------

from pyspark.sql import functions as F

accounts = [
    ("A-1001", "Alpine Cellars", "restaurant", "West", "R-10", "active", "2024-01-12"),
    ("A-1002", "Canyon Market", "grocery", "West", "R-10", "active", "2024-02-18"),
    ("A-1003", "Harbor Bistro", "restaurant", "East", "R-20", "active", "2024-04-01"),
    ("A-1004", "Mesa Spirits", "retail", "South", "R-30", "review", "2024-05-20"),
    ("A-1005", "Summit Hotel", "hospitality", "West", "R-10", "active", "2024-06-02"),
    ("A-1006", "Pine Social", "bar", "East", "R-20", "active", "2024-07-14"),
    ("A-1007", "River Grill", "restaurant", "South", "R-30", "active", "2024-08-21"),
    ("A-1008", "Crest Grocers", "grocery", "Midwest", "R-40", "active", "2024-09-03"),
]

products = [
    ("P-2001", "North Ridge Pinot", "wine", "North Ridge", "12x750ml", 18.50),
    ("P-2002", "Silver Creek Lager", "beer", "Silver Creek", "24x12oz", 22.00),
    ("P-2003", "Blue Mesa Vodka", "spirits", "Blue Mesa", "6x1L", 31.00),
    ("P-2004", "Valley Sparkling Rose", "wine", "Valley", "12x750ml", 16.25),
    ("P-2005", "Summit IPA", "beer", "Summit", "24x12oz", 25.00),
    ("P-2006", "Canyon Tequila", "spirits", "Canyon", "6x750ml", 42.00),
]

orders = [
    ("O-3001", "2026-03-01", "A-1001", "P-2001", 10, 185.00, 166.50, "paid"),
    ("O-3002", "2026-03-18", "A-1001", "P-2004", 8, 130.00, 117.00, "paid"),
    ("O-3003", "2026-03-22", "A-1002", "P-2002", 20, 440.00, 396.00, "paid"),
    ("O-3004", "2026-04-01", "A-1003", "P-2003", 6, 186.00, 186.00, "pending"),
    ("O-3005", "2026-04-08", "A-1004", "P-2001", 4, 74.00, 66.60, "returned"),
    ("O-3006", "2026-04-12", "A-1005", "P-2002", 18, 396.00, 356.40, "paid"),
    ("O-3007", "2026-04-21", "A-1001", "P-2002", 12, 264.00, 237.60, "paid"),
    ("O-3008", "2026-04-25", "A-1006", "P-2005", 14, 350.00, 315.00, "paid"),
    ("O-3009", "2026-03-05", "A-1007", "P-2006", 5, 210.00, 210.00, "paid"),
    ("O-3010", "2026-04-29", "A-1008", "P-2002", 25, 550.00, 495.00, "paid"),
]

inventory = [
    ("2026-04-30", "P-2001", "West", 120, 30, 90),
    ("2026-04-30", "P-2002", "West", 24, 20, 4),
    ("2026-04-30", "P-2003", "East", 70, 10, 60),
    ("2026-04-30", "P-2004", "West", 35, 5, 30),
    ("2026-04-30", "P-2005", "East", 40, 12, 28),
    ("2026-04-30", "P-2006", "South", 15, 12, 3),
]

promotions = [
    ("PR-4001", "P-2001", "West", "2026-03-01", "2026-03-31", 0.10, "spring_wine"),
    ("PR-4002", "P-2002", "West", "2026-04-01", "2026-04-30", 0.10, "seasonal_beer"),
    ("PR-4003", "P-2004", "West", "2026-03-15", "2026-04-15", 0.10, "rose_launch"),
    ("PR-4004", "P-2006", "South", "2026-04-01", "2026-04-30", 0.05, "spirits_focus"),
]

rep_notes = [
    ("N-5001", "A-1001", "2026-04-24", "Manager asked about lager availability before weekend events.", "inventory"),
    ("N-5002", "A-1002", "2026-04-25", "Interested in expanding premium wine shelf space.", "opportunity"),
    ("N-5003", "A-1004", "2026-04-26", "License review pending; avoid new spirits order until cleared.", "compliance"),
    ("N-5004", "A-1007", "2026-04-27", "No reorder in several weeks; ask about tequila promotion before stock runs out.", "reorder"),
]

spark.createDataFrame(accounts, "account_id string, account_name string, account_segment string, region string, sales_rep_id string, license_status string, account_since_date string").write.mode("overwrite").saveAsTable("bronze_accounts")
spark.createDataFrame(products, "product_id string, product_name string, category string, brand_family string, package_size string, unit_price double").write.mode("overwrite").saveAsTable("bronze_products")
spark.createDataFrame(orders, "order_id string, order_date string, account_id string, product_id string, quantity int, gross_amount double, net_amount double, order_status string").write.mode("overwrite").saveAsTable("bronze_orders")
spark.createDataFrame(inventory, "inventory_date string, product_id string, region string, on_hand_units int, reserved_units int, available_units int").write.mode("overwrite").saveAsTable("bronze_inventory")
spark.createDataFrame(promotions, "promotion_id string, product_id string, region string, start_date string, end_date string, discount_pct double, promotion_type string").write.mode("overwrite").saveAsTable("bronze_promotions")
spark.createDataFrame(rep_notes, "note_id string, account_id string, note_date string, note_text string, note_type string").write.mode("overwrite").saveAsTable("bronze_rep_notes")

# COMMAND ----------

orders_df = spark.read.table("bronze_orders")
accounts_df = spark.read.table("bronze_accounts")
products_df = spark.read.table("bronze_products")
inventory_df = spark.read.table("bronze_inventory")
rep_notes_df = spark.read.table("bronze_rep_notes")

silver_account_orders = (
    orders_df.alias("o")
    .join(accounts_df.alias("a"), "account_id", "left")
    .join(products_df.alias("p"), "product_id", "left")
    .select(
        "o.order_id",
        F.to_date("o.order_date").alias("order_date"),
        "o.account_id",
        "a.account_name",
        "a.account_segment",
        "a.region",
        "a.sales_rep_id",
        "a.license_status",
        "o.product_id",
        "p.product_name",
        "p.category",
        "o.quantity",
        "o.gross_amount",
        "o.net_amount",
        "o.order_status",
    )
)
silver_account_orders.write.mode("overwrite").saveAsTable("silver_account_orders")

silver_inventory_position = (
    inventory_df.alias("i")
    .join(products_df.alias("p"), "product_id", "left")
    .select(
        F.to_date("i.inventory_date").alias("inventory_date"),
        "i.product_id",
        "p.product_name",
        "p.category",
        "i.region",
        "i.on_hand_units",
        "i.reserved_units",
        "i.available_units",
        F.when(F.col("i.available_units") <= 10, "low")
        .when(F.col("i.available_units") <= 50, "medium")
        .otherwise("healthy")
        .alias("inventory_status"),
    )
)
silver_inventory_position.write.mode("overwrite").saveAsTable("silver_inventory_position")

paid_orders = silver_account_orders.where(F.col("order_status") == "paid")
order_metrics = (
    paid_orders.groupBy("account_id", "account_name", "account_segment", "region", "sales_rep_id", "license_status")
    .agg(
        F.max("order_date").alias("last_paid_order_date"),
        F.countDistinct("order_id").alias("paid_order_count"),
        F.sum("net_amount").alias("paid_net_amount"),
    )
    .withColumn("days_since_last_paid_order", F.datediff(F.current_date(), F.col("last_paid_order_date")))
    .withColumn(
        "reorder_risk",
        F.when(F.col("license_status") != "active", "hold")
        .when(F.col("days_since_last_paid_order") >= 30, "high")
        .when(F.col("days_since_last_paid_order") >= 14, "medium")
        .otherwise("low"),
    )
)

latest_notes = (
    rep_notes_df.withColumn("note_date", F.to_date("note_date"))
    .groupBy("account_id")
    .agg(
        F.max("note_date").alias("latest_note_date"),
        F.max_by("note_text", "note_date").alias("latest_note_text"),
    )
)

gold = order_metrics.join(latest_notes, "account_id", "left").withColumn(
    "recommended_action_seed",
    F.when(F.col("reorder_risk") == "hold", "Resolve account status before recommending an order.")
    .when(F.col("reorder_risk") == "high", "Contact account this week with reorder and inventory context.")
    .when(F.col("reorder_risk") == "medium", "Review account before next route cycle.")
    .otherwise("Monitor account and maintain normal cadence."),
)
gold.write.mode("overwrite").saveAsTable("gold_account_intelligence")

# COMMAND ----------

metric_view_sql = f"""
CREATE OR REPLACE VIEW {catalog}.{schema}.beverage_account_metrics
WITH METRICS
LANGUAGE YAML
AS $$
version: 1.1
comment: "Business metrics for beverage distribution account intelligence."
source: {catalog}.{schema}.gold_account_intelligence
dimensions:
  - name: region
    expr: region
    display_name: "Region"
    comment: "Sales region."
  - name: account_segment
    expr: account_segment
    display_name: "Account Segment"
    comment: "Type of account."
  - name: reorder_risk
    expr: reorder_risk
    display_name: "Reorder Risk"
    comment: "Estimated account follow-up risk."
  - name: sales_rep_id
    expr: sales_rep_id
    display_name: "Sales Rep"
    comment: "Synthetic sales representative identifier."
measures:
  - name: account_count
    expr: COUNT(DISTINCT account_id)
    display_name: "Account Count"
    comment: "Number of distinct accounts."
  - name: paid_net_amount
    expr: SUM(paid_net_amount)
    display_name: "Paid Net Amount"
    comment: "Total paid net amount."
  - name: high_risk_accounts
    expr: SUM(CASE WHEN reorder_risk = 'high' THEN 1 ELSE 0 END)
    display_name: "High Risk Accounts"
    comment: "Accounts classified as high reorder risk."
$$
"""

try:
    spark.sql(metric_view_sql)
    print("Created metric view beverage_account_metrics")
except Exception as exc:
    print(f"Metric view creation failed, creating standard view fallback. Reason: {exc}")
    spark.sql(f"""
    CREATE OR REPLACE VIEW {catalog}.{schema}.beverage_account_metrics_fallback AS
    SELECT
      region,
      account_segment,
      reorder_risk,
      sales_rep_id,
      COUNT(DISTINCT account_id) AS account_count,
      SUM(paid_net_amount) AS paid_net_amount,
      SUM(CASE WHEN reorder_risk = 'high' THEN 1 ELSE 0 END) AS high_risk_accounts
    FROM {catalog}.{schema}.gold_account_intelligence
    GROUP BY region, account_segment, reorder_risk, sales_rep_id
    """)

# COMMAND ----------

for table in [
    "bronze_accounts",
    "bronze_products",
    "bronze_orders",
    "bronze_inventory",
    "bronze_promotions",
    "bronze_rep_notes",
    "silver_account_orders",
    "silver_inventory_position",
    "gold_account_intelligence",
]:
    display(spark.sql(f"SELECT '{table}' AS table_name, COUNT(*) AS row_count FROM {catalog}.{schema}.{table}"))

display(spark.sql(f"SELECT * FROM {catalog}.{schema}.gold_account_intelligence ORDER BY reorder_risk DESC"))

