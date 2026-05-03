# Prompt

```text
Use Genie Code Agent mode while viewing or creating an MLflow experiment.

Use skill: @mlflow-genai-evaluator

You are in step 07 of the workshop: evaluate GenAI recommendations with MLflow.

Create an MLflow GenAI evaluation workflow for:
Field Sales Account Intelligence Copilot

Experiment:
/Shared/beverage_account_intelligence

Use data from:
workshop.beverage_distribution.gold_account_intelligence

Use the rubric in:
07-mlflow-genai-evaluation/evaluation-rubric.yml

Build a notebook that:
1. Loads 10 synthetic account scenarios from the gold table or creates 10 synthetic evaluation examples if the table is not available.
2. Defines two prompt variants:
   - Variant A: short recommendation prompt
   - Variant B: grounded recommendation prompt that cites account signals
3. Defines a local deterministic recommendation function if external model calls are not approved.
4. Tracks inputs, outputs, prompt version, and metrics in MLflow.
5. Uses MLflow GenAI evaluation if available in the workspace.
6. If MLflow GenAI scorers are unavailable, creates a manual scoring DataFrame with groundedness, actionability, business relevance, safety, and concision.
7. Logs artifacts:
   - evaluation examples
   - prompt variants
   - scored results
   - failure analysis
8. Produces a short recommendation for which prompt variant should move forward.

First return:
- experiment design
- evaluation dataset schema
- prompt variants
- scoring approach
- exact notebook cells to create

Wait for approval before running code.

If MLflow GenAI evaluation fails, use `99-backup/fallback-manual-evaluation.md`.
```
