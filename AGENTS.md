# Genie Code Workshop Instructions

These instructions are for Databricks Genie Code when this repo is opened in a Databricks Git folder or workspace file browser.

## Operating Mode

- Use Genie Code Agent mode for build steps.
- Start every build step by producing a short plan.
- Wait for explicit human approval before creating, modifying, running, or deploying resources.
- If the user asks for "plan mode", produce the plan, assumptions, required permissions, and exact next prompt without running anything.
- If a step fails, do not improvise silently. Diagnose the error, explain the likely cause, and use the matching fallback in `workshops/beverage-distributor-genai-mlops/99-backup`.
- Do not require custom skills to run the workshop. Treat skills as optional accelerators only.
- If a prompt mentions a skill that is unavailable, continue using the prompt instructions directly.

## Workshop Rules

- Follow the numbered folders in order.
- Use synthetic data only.
- Do not use real customer names, people, emails, addresses, account records, contracts, credentials, or private data.
- Use Unity Catalog three-part names.
- Prefer business-readable table, column, metric, and Genie space descriptions.
- Keep generated code workshop-sized and easy to explain.
- Prefer Databricks Python SDK for control-plane automation in backup notebooks.
- For Databricks Apps + Lakebase, use the App resource model and injected Postgres environment variables for runtime database connections. Do not hardcode Lakebase credentials.

## Default Resources

- Catalog: `workshop`
- Schema: `beverage_distribution`
- Genie space: `Beverage Account Intelligence`
- MLflow experiment: `/Shared/beverage_account_intelligence`
- Lakebase project: `beverage-account-actions`
