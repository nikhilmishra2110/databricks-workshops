---
name: databricks-app-builder
description: Use when designing, generating, debugging, or explaining Databricks Apps that connect to Unity Catalog, Genie spaces, MLflow, and Lakebase resources.
---

# Databricks App Builder

Use this skill when creating a Databricks App for a workshop.

## Steps

1. Identify the app user and workflow.
2. Identify Unity Catalog assets the app reads.
3. Identify Genie space resources the app uses.
4. Identify Lakebase resources the app writes to.
5. Generate a minimal app plan before code.
6. Create `app.py`, `app.yaml`, `requirements.txt`, and `README.md`.
7. Use environment variables for Databricks App resources.
8. Add demo mode for missing resources.
9. Explain deployment steps and permission assumptions.

## Standards

- Do not hardcode secrets.
- Keep the app simple enough for a workshop.
- Read governed analytics from Unity Catalog.
- Write operational state to Lakebase.
- Include clear fallback behavior when resources are missing.

