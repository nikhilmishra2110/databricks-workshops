# Prompt

```text
Use Genie Code Agent mode.

Optional skills if available: @genie-space-optimizer and @metric-view-builder. If skills are unavailable, continue with this prompt without blocking.

You are in step 05 of the workshop: create and optimize a Genie space.

Create or guide me through creating a Genie space named:
Beverage Account Intelligence

Use the business context in:
05-create-optimize-genie-space/business-context.yml

Include only curated and governed assets:
- workshop.beverage_distribution.beverage_account_metrics
- workshop.beverage_distribution.gold_account_intelligence
- workshop.beverage_distribution.silver_account_orders
- workshop.beverage_distribution.silver_inventory_position

Do not include raw bronze tables.

Return a complete Genie space optimization package:
1. Creation steps for the UI if direct creation is not available.
2. Assets to include and why.
3. Assets to exclude and why.
4. Table comments to improve answer quality.
5. Column comments to improve answer quality.
6. Business terms to define.
7. Sample questions to seed the space.
8. Five weak-answer tests that might expose ambiguity.
9. Fixes for each weak-answer risk.
10. A short facilitator script that explains why governed metrics and curated tables make Genie more reliable.

First give me the plan and wait for approval before making any metadata changes.

If Genie space creation fails, use `99-backup/fallback-genie-questions.md`.
```
