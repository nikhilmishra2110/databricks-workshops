# Fallback Genie Questions

If Genie is unavailable, run these as SQL or dashboard questions.

1. Which accounts need attention this week?
2. Which sales reps have the most high-risk accounts?
3. Which regions have the highest paid net amount?
4. Which accounts are high risk but have recent promotion activity?
5. Which products have low available inventory?
6. Why should a rep contact the highest-risk account?

Use SQL against:

```text
workshop.beverage_distribution.gold_account_intelligence
workshop.beverage_distribution.silver_account_orders
workshop.beverage_distribution.silver_inventory_position
```

