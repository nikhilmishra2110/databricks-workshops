# Lakeflow Spark Declarative Pipelines source example.
# Place this file in the Lakeflow Pipelines Editor or adapt it with Genie Code.

from pyspark import pipelines as dp
from pyspark.sql import functions as F


@dp.materialized_view(
    name="silver_account_orders",
    comment="Curated account order lines with account and product context.",
)
@dp.expect_or_drop("valid_account_id", "account_id IS NOT NULL")
@dp.expect_or_drop("valid_product_id", "product_id IS NOT NULL")
@dp.expect("valid_order_status", "order_status IN ('paid', 'pending', 'cancelled', 'returned')")
@dp.expect("valid_amounts", "gross_amount >= 0 AND net_amount >= 0 AND net_amount <= gross_amount")
def silver_account_orders():
    orders = spark.read.table("bronze_orders")
    accounts = spark.read.table("bronze_accounts")
    products = spark.read.table("bronze_products")

    return (
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
            "p.brand_family",
            "o.quantity",
            "o.gross_amount",
            "o.net_amount",
            "o.order_status",
        )
    )


@dp.materialized_view(
    name="silver_inventory_position",
    comment="Curated inventory availability by product and region.",
)
@dp.expect_or_drop("valid_product_id", "product_id IS NOT NULL")
@dp.expect("available_units_math", "available_units = on_hand_units - reserved_units")
def silver_inventory_position():
    inventory = spark.read.table("bronze_inventory")
    products = spark.read.table("bronze_products")

    return (
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
            F.when(F.col("i.available_units") <= 10, F.lit("low"))
            .when(F.col("i.available_units") <= 50, F.lit("medium"))
            .otherwise(F.lit("healthy"))
            .alias("inventory_status"),
        )
    )


@dp.materialized_view(
    name="gold_account_intelligence",
    comment="Account-level metrics for sales prioritization and Genie questions.",
)
def gold_account_intelligence():
    account_orders = spark.read.table("silver_account_orders")
    rep_notes = spark.read.table("bronze_rep_notes")

    paid_orders = account_orders.where(F.col("order_status") == "paid")

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
            F.countDistinct("category").alias("category_count"),
        )
        .withColumn(
            "days_since_last_paid_order",
            F.datediff(F.current_date(), F.col("last_paid_order_date")),
        )
        .withColumn(
            "reorder_risk",
            F.when(F.col("license_status") != "active", F.lit("hold"))
            .when(F.col("days_since_last_paid_order") >= 30, F.lit("high"))
            .when(F.col("days_since_last_paid_order") >= 14, F.lit("medium"))
            .otherwise(F.lit("low")),
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

    return order_metrics.join(latest_notes, "account_id", "left")

