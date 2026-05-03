# Prompt: Databricks Genie Code Dataset Builder

## Purpose

Generate synthetic Databricks workshop datasets and Unity Catalog tables from a domain contract.

## Prompt

```text
You are helping build a Databricks workshop dataset.

Domain:
{{domain_contract}}

Unity Catalog target:
- catalog: {{catalog}}
- schema: {{schema}}

Rules:
- Use synthetic data only.
- Keep data small enough for a live workshop.
- Include edge cases that teach the target concepts.
- Add table and column comments.
- Generate validation queries.

First propose a plan. Then generate Databricks Python or SQL code. Wait for approval before running anything.
```

