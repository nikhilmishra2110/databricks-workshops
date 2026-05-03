# Prompt: Databricks Genie Space Optimizer

## Purpose

Improve a Genie space by tightening table scope, metadata, business definitions, and sample questions.

## Prompt

```text
You are optimizing a Databricks Genie space for business users.

Space name:
{{space_name}}

Audience:
{{audience}}

Trusted tables:
{{trusted_tables}}

Business terms:
{{business_terms}}

Return:
1. Recommended included tables and excluded tables.
2. Table comments.
3. Column comments.
4. Sample questions.
5. Known ambiguity risks.
6. Test plan for answer quality.
7. Improvement backlog.

Use business-friendly language and avoid exposing sensitive columns.
```

