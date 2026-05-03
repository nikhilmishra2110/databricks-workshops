# Prompt

```text
Use Genie Code Agent mode.

Use skill: @beverage-distribution-domain

You are helping me run a Databricks workshop. Start with exactly one use case:

Field Sales Account Intelligence Copilot for a synthetic beverage distribution business.

Do not ask me to pick between multiple use cases. Use this one.

Create a concise use case brief in the current folder named `use-case-brief.md`.

The brief must include:
1. Business user: sales leader and field sales rep.
2. Business decision: which accounts need follow-up this week and why.
3. Data needed: accounts, products, orders, inventory, promotions, rep notes.
4. Databricks platform path:
   - synthetic data in Unity Catalog
   - Lakeflow pipeline
   - Unity Catalog metric view
   - Genie space for natural-language questions
   - MLflow GenAI evaluation
   - Lakebase for app state and feedback
   - Databricks App for the field workflow
5. Success criteria:
   - business user can ask trusted questions
   - recommendations are grounded in curated data
   - human feedback is captured
   - the workflow is reusable for another customer
6. A simple ASCII architecture diagram.
7. Three stakeholder sound bites that make the use case feel realistic.

Before writing the file, show me the plan and wait for approval.
```
