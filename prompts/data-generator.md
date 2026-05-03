# Prompt: Data Generator

## Purpose

Create small, synthetic datasets for database exercises.

## Best Used When

- building sample tables
- avoiding sensitive or real customer data
- creating edge cases for joins, filters, grouping, and null handling

## Inputs

- `{{scenario}}`
- `{{tables}}`
- `{{row_count}}`
- `{{database_dialect}}`
- `{{concepts_to_teach}}`

## Prompt

```text
You create small synthetic datasets for database workshops.

Scenario:
{{scenario}}

Tables needed:
{{tables}}

Target row count:
{{row_count}}

Database dialect:
{{database_dialect}}

Concepts to teach:
{{concepts_to_teach}}

Return:

1. Table definitions.
2. Insert statements or CSV data.
3. At least five intentional edge cases.
4. Three exercise ideas that use the data.

Rules:

- Do not use real people, companies, emails, or addresses.
- Keep values realistic enough for learning.
- Include nulls and boundary values only when they support the concept.
```

## Expected Output

Runnable sample data or CSV content with known teaching edge cases.

## Human Review Checklist

- [ ] Data is synthetic
- [ ] Edge cases are intentional and documented
- [ ] Row counts are small enough for a live workshop

