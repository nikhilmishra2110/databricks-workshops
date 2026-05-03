# 02 - Generate Synthetic Data

## Goal

Use Genie Code to create workshop-sized synthetic data and write it to Unity Catalog.

## Output Tables

Target namespace:

```text
workshop.beverage_distribution
```

Bronze tables:

- `bronze_accounts`
- `bronze_products`
- `bronze_orders`
- `bronze_inventory`
- `bronze_promotions`
- `bronze_rep_notes`

## Done When

- Tables exist in Unity Catalog.
- Data is synthetic and small.
- Tables and columns have comments.
- Validation queries pass.
- Edge cases exist for low inventory, pending orders, returned orders, license review, and overdue reorder behavior.

## Backup

If data generation fails, use `../99-backup/fallback-synthetic-data-prompt.md`.

