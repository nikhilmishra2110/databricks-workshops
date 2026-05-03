---
name: metric-view-builder
description: Use when designing, creating, validating, or troubleshooting Unity Catalog metric views for Databricks workshops.
---

# Metric View Builder

Use this skill when a task involves governed business metrics in Databricks.

## Steps

1. Confirm the source table or query.
2. Identify business dimensions.
3. Identify aggregate measures.
4. Add display names, comments, and synonyms for AI/BI discovery.
5. Generate `CREATE OR REPLACE VIEW ... WITH METRICS LANGUAGE YAML AS $$`.
6. Add validation SQL that queries the metric view.
7. Provide a standard SQL view fallback if metric views are unavailable.

## Standards

- Use Unity Catalog three-part names.
- Keep metric names business-friendly.
- Do not include raw bronze tables as metric view sources.
- Prefer curated gold tables or trusted semantic views.

