# Prompt: Databricks MLflow GenAI Evaluator

## Purpose

Create an MLflow tracking and evaluation workflow for GenAI app or agent outputs.

## Prompt

```text
You are designing an MLflow GenAI evaluation workflow in Databricks.

Application:
{{application_description}}

Inputs:
{{inputs}}

Outputs:
{{outputs}}

Quality rubric:
{{quality_rubric}}

Return:
1. Experiment structure.
2. Evaluation dataset schema.
3. Prompt/model versioning strategy.
4. Metrics and scorers.
5. Human feedback fields.
6. Databricks notebook code to compare two prompt variants.
7. Failure analysis checklist.

Do not call external services unless approved.
```

