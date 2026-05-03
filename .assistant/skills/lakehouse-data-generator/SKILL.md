---
name: lakehouse-data-generator
description: Use when creating synthetic Databricks workshop datasets, Unity Catalog tables, validation queries, and metadata from a domain contract.
---

# Lakehouse Data Generator

Use this skill to create synthetic workshop data in Databricks.

## Steps

1. Ask for or infer the target catalog and schema.
2. Read the domain contract or ask for entities and grains.
3. Propose a small dataset plan before code.
4. Generate Spark DataFrames or SQL inserts.
5. Write managed Delta tables.
6. Add table and column comments.
7. Add validation queries and row counts.
8. Call out edge cases intentionally included.

## Safety

- Use synthetic data only.
- Do not create real people, real emails, real addresses, credentials, or customer records.
- Keep row counts workshop-sized unless asked otherwise.

## Example Output

- `bronze_accounts`
- `bronze_products`
- `bronze_orders`
- `bronze_inventory`
- `bronze_promotions`
- `bronze_rep_notes`

## Review Checklist

- Tables match the entity grain.
- IDs are stable and easy to join.
- Data contains useful but explainable edge cases.
- Metadata is readable by business users and useful for Genie spaces.

