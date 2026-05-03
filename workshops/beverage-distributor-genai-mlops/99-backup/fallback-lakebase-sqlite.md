# Fallback Lakebase Simulation

If Lakebase is unavailable, simulate app state with a local SQLite database or an in-memory table.

Use the same conceptual entities:

- account_action_plan
- recommendation_feedback
- rep_follow_up_status
- prompt_test_case

Explain clearly:

- Unity Catalog stores governed analytical data.
- Lakebase stores app state and feedback.
- SQLite is only a delivery fallback, not the target architecture.

