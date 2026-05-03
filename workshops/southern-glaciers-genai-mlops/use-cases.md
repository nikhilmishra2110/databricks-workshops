# Use Cases For Southern Glaciers

These use cases are framed for a beverage distribution customer. Keep all workshop data synthetic unless the customer explicitly provides approved workshop data.

## Use Case Menu

| Use Case | Business Question | Databricks Pattern | Workshop Fit |
| --- | --- | --- | --- |
| Field Sales Account Intelligence Copilot | Which accounts need attention this week and why? | Lakeflow + Genie space + MLflow + Lakebase app state | Best fit |
| Promotion Performance Assistant | Which promotions are working by region, segment, and product category? | Lakeflow + AI/BI dashboard + Genie space | Strong fit |
| Reorder And Stockout Risk | Which accounts are likely to miss reorder windows? | Feature engineering + MLflow model + recommendations | Strong fit |
| Product Substitution Advisor | What product should a rep suggest when inventory is constrained? | Vector/semantic search + rules + feedback capture | Good fit |
| Route And Visit Prioritization | Which accounts should a rep visit first? | Forecasting + optimization + app workflow | Good but more complex |
| Contract And Compliance Knowledge Assistant | What restrictions apply to this account, product, or region? | RAG + evaluation + governance | Good if docs are available |
| Customer Service Case Summarizer | What happened with this account and what should happen next? | GenAI summarization + MLflow traces | Good if text data exists |

## Recommended Workshop Story

Use Field Sales Account Intelligence Copilot as the main storyline.

Participant prompt:

```text
Build an account intelligence workflow for a beverage distributor. Use synthetic data for accounts, products, orders, inventory, promotions, and rep notes. Create curated tables, a Lakeflow pipeline, a Genie space for natural-language account questions, MLflow tracking for recommendation quality, and a Lakebase-backed app workflow for saving rep actions and feedback.
```

## Why This Story Works

It connects technical capabilities to a concrete field workflow:

1. Data teams curate account, order, inventory, and promotion data.
2. Analysts ask business questions in a Genie space.
3. ML engineers create reorder-risk and next-best-action logic.
4. Facilitators show MLflow traces and evaluation for GenAI quality.
5. Business users save action plans and feedback into Lakebase.

## Example Business Questions

- Which West region accounts are below their usual reorder cadence?
- Which products are growing fastest by account segment?
- Which promotions drove paid orders but low repeat purchase?
- What are the top reasons a rep should contact an account this week?
- Which accounts have pending orders and low inventory availability?
- What action should a sales rep take next for a high-value account?

## Scope Control

Keep the workshop focused on one end-to-end slice:

- one synthetic customer domain
- six to eight Unity Catalog tables
- one Lakeflow pipeline
- one Genie space
- one recommendation/evaluation notebook
- one Lakebase-backed app state model

Do not try to build a full production sales system in the workshop.

