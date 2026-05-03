# 04 - Create Metric View

## Goal

Create a governed Unity Catalog metric view that business tools and Genie can use consistently.

## Metric View

```text
workshop.beverage_distribution.beverage_account_metrics
```

## Done When

- Metric view exists.
- Measures and dimensions have business-friendly names.
- The metric view can be queried from SQL.
- It is ready to include in the Genie space.

## Backup

If metric views are unavailable, create a standard SQL view using `../99-backup/fallback-standard-view.sql`.

