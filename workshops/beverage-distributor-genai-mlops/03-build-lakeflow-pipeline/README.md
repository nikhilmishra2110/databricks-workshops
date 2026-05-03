# 03 - Build Lakeflow Pipeline

## Goal

Use Genie Code Agent mode in the Lakeflow Pipelines Editor to generate the curated pipeline.

## Inputs

Bronze tables from step 02.

## Outputs

- `silver_account_orders`
- `silver_inventory_position`
- `gold_account_intelligence`

## Done When

- Lakeflow pipeline code is generated and reviewed.
- Expectations cover IDs, order statuses, amounts, and inventory math.
- Gold table supports metric views, Genie, MLflow, and the app.

## Backup

If Lakeflow Agent mode or pipeline permissions are unavailable, use `../99-backup/fallback-pipeline.py` in a Databricks notebook as a non-Lakeflow fallback.

