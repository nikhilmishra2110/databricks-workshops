---
name: mlflow-genai-evaluator
description: Use when designing MLflow tracking, evaluation, observability, feedback, and prompt iteration workflows for GenAI apps or agents.
---

# MLflow GenAI Evaluator

Use this skill to build MLOps workflows for GenAI recommendations, copilots, or agents.

## Steps

1. Define the app input and output schema.
2. Define quality dimensions before coding.
3. Create a small evaluation dataset with normal and edge cases.
4. Track prompt versions, model choices, inputs, outputs, and artifacts.
5. Add metrics or scorers for groundedness, actionability, safety, and concision.
6. Capture human feedback fields.
7. Compare at least two prompt or model variants.
8. Summarize failures and propose the next iteration.

## Output Standards

- Make evaluation reproducible.
- Log enough context to debug failures.
- Keep synthetic examples separate from production data.
- Make human review part of the loop.

## Review Checklist

- Metrics match the business workflow.
- Test cases include edge cases.
- Results can be compared across versions.
- Feedback can be written to Lakebase or Delta for future analysis.

