# Prompt: Schema Design Reviewer

## Purpose

Review a database schema for workshop use, with emphasis on clarity, correctness, and teachability.

## Best Used When

- creating a new sample schema
- simplifying production-like examples
- preparing schema critique exercises

## Inputs

- `{{schema_sql}}`
- `{{workshop_topic}}`
- `{{audience}}`
- `{{database_dialect}}`

## Prompt

```text
You are reviewing a database schema for a teaching workshop.

Workshop topic:
{{workshop_topic}}

Audience:
{{audience}}

Database dialect:
{{database_dialect}}

Schema:
{{schema_sql}}

Review the schema for:

1. Naming clarity.
2. Primary keys and foreign keys.
3. Data types.
4. Normalization tradeoffs.
5. Queryability for workshop exercises.
6. Anything likely to distract learners.

Return a table with columns:

- Finding
- Why it matters
- Suggested change
- Severity: low, medium, high

Then provide a revised schema only if changes are substantial.
```

## Expected Output

A prioritized review that helps improve the schema before it appears in a workshop.

## Human Review Checklist

- [ ] Review is grounded in the provided schema
- [ ] Suggestions fit the workshop audience
- [ ] Dialect-specific syntax is checked

