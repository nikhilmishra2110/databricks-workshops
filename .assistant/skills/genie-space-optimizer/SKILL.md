---
name: genie-space-optimizer
description: Use when creating or improving Databricks Genie spaces through curated table scope, metadata, business terms, and sample questions.
---

# Genie Space Optimizer

Use this skill when creating or tuning a Genie space.

## Steps

1. Confirm the audience and business questions.
2. Limit the space to curated Unity Catalog tables or views.
3. Improve table comments and column comments.
4. Define ambiguous business terms.
5. Add sample questions tied to the actual schema.
6. Identify weak or risky questions.
7. Create an answer-quality test plan.

## Good Genie Space Inputs

- Gold tables or trusted views.
- Business-friendly metadata.
- Stable KPI definitions.
- Sample questions that represent real user intent.

## Avoid

- raw bronze tables
- duplicate columns with unclear meaning
- sensitive fields
- tables that require unsupported business logic
- overloaded terms that are not defined

## Output Format

Return:

- included tables
- excluded tables
- metadata changes
- sample questions
- known risks
- testing checklist

