# Prompt

```text
Use Genie Code Agent mode in the Lakeflow Pipelines Editor.

Use skills: @beverage-distribution-domain and @lakeflow-pipeline-builder

You are in step 03 of the workshop: build a Lakeflow Spark Declarative Pipeline.

Source tables are in `workshop.beverage_distribution`:
- bronze_accounts
- bronze_products
- bronze_orders
- bronze_inventory
- bronze_promotions
- bronze_rep_notes

Create a pipeline that produces:
- silver_account_orders: joined order lines with account and product context
- silver_inventory_position: inventory status by product and region
- gold_account_intelligence: one row per account with account health, reorder risk, sales metrics, promotion context, and latest rep note context

Requirements:
1. Use current Lakeflow Spark Declarative Pipelines patterns available in this workspace.
2. Prefer Python. If this workspace expects `from pyspark import pipelines as dp`, use that. If it expects `import dlt`, adapt and explain the difference.
3. Add data quality expectations for:
   - non-null account_id
   - non-null product_id
   - valid order_status values: paid, pending, cancelled, returned
   - gross_amount >= 0
   - net_amount >= 0
   - net_amount <= gross_amount
   - available_units = on_hand_units - reserved_units
4. Make the output useful for business questions:
   - last paid order date
   - days since last paid order
   - paid order count
   - paid net amount
   - top or recent product category
   - reorder risk: low, medium, high, hold
   - latest rep note text
   - recommended_action_seed field with a deterministic placeholder recommendation
5. Include validation queries after the pipeline design.
6. Save generated source code as `03-build-lakeflow-pipeline/generated_pipeline.py` if file editing is available.

First provide:
- pipeline design
- dataset definitions
- expectation list
- assumptions
- what will be created

Wait for approval before creating or running the pipeline.

If Lakeflow fails because of permissions or preview availability, use `99-backup/fallback-pipeline.py` as a notebook-based fallback.
```
