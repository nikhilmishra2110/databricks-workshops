# Prompt

```text
Use Genie Code Agent mode in a Databricks App workspace or app folder.

Use skills: @databricks-app-builder, @lakebase-app-builder, and @genie-space-optimizer

You are in step 09 of the workshop: build the Databricks App.

Use the app architecture in:
09-build-app/app-architecture.md

Build a minimal Streamlit Databricks App named:
Beverage Account Intelligence App

The app should:
1. Read account intelligence from Unity Catalog:
   - workshop.beverage_distribution.gold_account_intelligence
   - workshop.beverage_distribution.beverage_account_metrics
2. Use the Genie space resource if available:
   - Beverage Account Intelligence
3. Connect to Lakebase when the app has a database resource.
4. Show a clear fallback message if Lakebase environment variables are missing.
5. Let a business user:
   - select an account
   - view account health
   - view reorder risk
   - view latest rep note
   - generate or display a next-best-action recommendation
   - accept, edit, or reject the recommendation
   - save feedback to Lakebase
6. Create these files if they do not exist:
   - app.py
   - app.yaml
   - requirements.txt
   - README.md
7. Use simple, readable code suitable for a workshop.
8. Do not hardcode secrets.
9. Use environment variables injected by Databricks Apps resources.
10. Include a demo mode that uses in-memory synthetic rows if Unity Catalog or Lakebase are unavailable.

First return:
- app plan
- expected Databricks App resources
- file list
- environment variables
- security assumptions
- fallback behavior

Wait for approval before creating or editing files.

If Databricks Apps are unavailable, use demo mode and explain how the same pattern maps to Databricks Apps.
```
