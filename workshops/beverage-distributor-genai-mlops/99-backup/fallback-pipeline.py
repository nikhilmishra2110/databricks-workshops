# Notebook fallback when Lakeflow is unavailable.
# Run this in a Databricks notebook after step 02 creates bronze tables.

from pyspark.sql import functions as F

catalog = "workshop"
schema = "beverage_distribution"
spark.sql(f"USE CATALOG {catalog}")
spark.sql(f"USE SCHEMA {schema}")

orders = spark.read.table("bronze_orders")
accounts = spark.read.table("bronze_accounts")
products = spark.read.table("bronze_products")
inventory = spark.read.table("bronze_inventory")
rep_notes = spark.read.table("bronze_rep_notes")

silver_account_orders = (
    orders.alias("o")
    .join(accounts.alias("a"), "account_id", "left")
    .join(products.alias("p"), "product_id", "left")
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
    inventory.alias("i")
    .join(products.alias("p"), "product_id", "left")
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
    paid_orders.groupBy(
        "account_id",
        "account_name",
        "account_segment",
        "region",
        "sales_rep_id",
        "license_status",
    )
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
    rep_notes.withColumn("note_date", F.to_date("note_date"))
    .groupBy("account_id")
    .agg(
        F.max("note_date").alias("latest_note_date"),
        F.max_by("note_text", "note_date").alias("latest_note_text"),
    )
)

gold_account_intelligence = order_metrics.join(latest_notes, "account_id", "left")
gold_account_intelligence.write.mode("overwrite").saveAsTable("gold_account_intelligence")

display(spark.table("gold_account_intelligence"))

