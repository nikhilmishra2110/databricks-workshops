# Prompt

```text
Use Genie Code Agent mode.

Use skills: @beverage-distribution-domain and @lakehouse-data-generator

You are in step 02 of the workshop: generate synthetic data.

Use the data contract in `02-generate-synthetic-data/data-contract.yml`.

Create Databricks notebook code that creates small synthetic Delta tables in Unity Catalog:
- catalog: workshop
- schema: beverage_distribution

Tables to create:
- bronze_accounts
- bronze_products
- bronze_orders
- bronze_inventory
- bronze_promotions
- bronze_rep_notes

Requirements:
1. Use synthetic data only.
2. Do not use real customer names, people, emails, addresses, contracts, credentials, or private data.
3. Keep the dataset workshop-sized: roughly 12 accounts, 12 products, 80 order rows, 24 inventory rows, 8 promotions, and 24 rep notes.
4. Include these edge cases:
   - low available inventory for at least one high-demand product
   - account with overdue reorder behavior
   - account under license review
   - pending order
   - returned order
   - promotion that overlaps recent orders
   - rep note that explains a recommended action
5. Create catalog and schema if permissions allow. If not, stop and tell me the exact SQL permissions needed.
6. Write managed Delta tables.
7. Add table comments and column comments using SQL.
8. Run validation queries:
   - row count per table
   - null key checks
   - valid order status check
   - inventory math check: available_units = on_hand_units - reserved_units
   - revenue math check: net_amount <= gross_amount
9. Save the generated notebook or SQL in this folder as `generated_synthetic_data_setup.py` if file editing is available.

First return a plan with:
- tables to be created
- edge cases to include
- exact Databricks objects that will be created
- validation queries

Wait for my approval before running code.

If execution fails, diagnose the issue and use `99-backup/fallback-synthetic-data-prompt.md`.
```
