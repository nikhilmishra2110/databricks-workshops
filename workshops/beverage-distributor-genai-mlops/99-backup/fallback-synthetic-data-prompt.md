# Fallback Synthetic Data Prompt

```text
Use Genie Code Agent mode.

The main synthetic data generation failed. Keep the workshop moving.

Create a smaller synthetic dataset directly in a Databricks notebook:
- 5 accounts
- 5 products
- 12 orders
- 6 inventory rows
- 3 promotions
- 6 rep notes

Write to the same target if possible:
workshop.beverage_distribution

If Unity Catalog write permissions are unavailable, create temporary Spark views with the same names and explain that downstream steps are demo-only.

Return the code, validation queries, and limitations before running anything.
```

