# Databricks notebook source
# MAGIC %md
# MAGIC # Synthetic Data Setup
# MAGIC
# MAGIC Creates small synthetic tables for the Beverage Distribution GenAI MLOps workshop.
# MAGIC Use synthetic data only.

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
]

products = [
    ("P-2001", "North Ridge Pinot", "wine", "North Ridge", "12x750ml", 18.50),
    ("P-2002", "Silver Creek Lager", "beer", "Silver Creek", "24x12oz", 22.00),
    ("P-2003", "Blue Mesa Vodka", "spirits", "Blue Mesa", "6x1L", 31.00),
    ("P-2004", "Valley Sparkling Rose", "wine", "Valley", "12x750ml", 16.25),
]

orders = [
    ("O-3001", "2026-03-01", "A-1001", "P-2001", 10, 185.00, 166.50, "paid"),
    ("O-3002", "2026-03-18", "A-1001", "P-2004", 8, 130.00, 117.00, "paid"),
    ("O-3003", "2026-03-22", "A-1002", "P-2002", 20, 440.00, 396.00, "paid"),
    ("O-3004", "2026-04-01", "A-1003", "P-2003", 6, 186.00, 186.00, "pending"),
    ("O-3005", "2026-04-08", "A-1004", "P-2001", 4, 74.00, 66.60, "returned"),
    ("O-3006", "2026-04-12", "A-1005", "P-2002", 18, 396.00, 356.40, "paid"),
    ("O-3007", "2026-04-21", "A-1001", "P-2002", 12, 264.00, 237.60, "paid"),
]

inventory = [
    ("2026-04-30", "P-2001", "West", 120, 30, 90),
    ("2026-04-30", "P-2002", "West", 24, 20, 4),
    ("2026-04-30", "P-2003", "East", 70, 10, 60),
    ("2026-04-30", "P-2004", "West", 35, 5, 30),
]

promotions = [
    ("PR-4001", "P-2001", "West", "2026-03-01", "2026-03-31", 0.10, "spring_wine"),
    ("PR-4002", "P-2002", "West", "2026-04-01", "2026-04-30", 0.10, "seasonal_beer"),
    ("PR-4003", "P-2004", "West", "2026-03-15", "2026-04-15", 0.10, "rose_launch"),
]

rep_notes = [
    ("N-5001", "A-1001", "2026-04-24", "Manager asked about lager availability before weekend events.", "inventory"),
    ("N-5002", "A-1002", "2026-04-25", "Interested in expanding premium wine shelf space.", "opportunity"),
    ("N-5003", "A-1004", "2026-04-26", "License review pending; avoid new spirits order until cleared.", "compliance"),
]

spark.createDataFrame(accounts, "account_id string, account_name string, account_segment string, region string, sales_rep_id string, license_status string, account_since_date string").write.mode("overwrite").saveAsTable("bronze_accounts")
spark.createDataFrame(products, "product_id string, product_name string, category string, brand_family string, package_size string, unit_price double").write.mode("overwrite").saveAsTable("bronze_products")
spark.createDataFrame(orders, "order_id string, order_date string, account_id string, product_id string, quantity int, gross_amount double, net_amount double, order_status string").write.mode("overwrite").saveAsTable("bronze_orders")
spark.createDataFrame(inventory, "inventory_date string, product_id string, region string, on_hand_units int, reserved_units int, available_units int").write.mode("overwrite").saveAsTable("bronze_inventory")
spark.createDataFrame(promotions, "promotion_id string, product_id string, region string, start_date string, end_date string, discount_pct double, promotion_type string").write.mode("overwrite").saveAsTable("bronze_promotions")
spark.createDataFrame(rep_notes, "note_id string, account_id string, note_date string, note_text string, note_type string").write.mode("overwrite").saveAsTable("bronze_rep_notes")

# COMMAND ----------

comments = {
    "bronze_accounts": "Synthetic beverage distribution accounts for the workshop.",
    "bronze_products": "Synthetic beverage product catalog for the workshop.",
    "bronze_orders": "Synthetic order lines by account and product.",
    "bronze_inventory": "Synthetic inventory position by product and region.",
    "bronze_promotions": "Synthetic promotions by product and region.",
    "bronze_rep_notes": "Synthetic sales rep notes for GenAI summarization exercises.",
}

for table_name, comment in comments.items():
    spark.sql(f"COMMENT ON TABLE {table_name} IS '{comment}'")

for table_name in comments:
    display(spark.sql(f"SELECT '{table_name}' AS table_name, COUNT(*) AS rows FROM {table_name}"))
