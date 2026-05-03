# Fallback Manual Evaluation

If MLflow GenAI evaluation APIs are unavailable, create a manual evaluation table.

Columns:

- account_id
- input_context
- recommendation
- rationale
- groundedness_score
- actionability_score
- business_relevance_score
- safety_pass
- concision_score
- reviewer_notes

Use a 1 to 5 score for numeric dimensions and pass/fail for safety.

The teaching point remains the same: GenAI recommendations must be evaluated, compared, logged, and improved.

