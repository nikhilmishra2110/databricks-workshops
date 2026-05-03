# Optional Genie Code Skills

The workshop does **not** require skill installation. Every numbered folder has a self-contained `PROMPT.md`.

Use skills only if the customer environment already supports them or the facilitator wants to install them ahead of time.

## Preferred Workshop Default

Use the numbered `PROMPT.md` files directly in Genie Code Agent mode. This avoids customer setup issues across managed desktops, Windows, macOS, restricted networks, or workspaces where users cannot write to `.assistant/skills`.

## Optional Local Skills In This Repo

The reusable local skills are in `.assistant/skills/`. If you choose to use them, copy that folder into Databricks:

```text
Workspace/.assistant/skills/
```

or:

```text
/Users/{username}/.assistant/skills/
```

## Optional Databricks And AI Dev Kit Skills

Databricks documents multiple skill repositories. AI Dev Kit skills are especially relevant because they cover SQL analytics, ML evaluation, model serving, streaming, pipelines, Unity Catalog, Lakebase, apps, and more.

Use these only as facilitator prep. Do not require participants to run installers during a customer workshop.

Databricks agent skills via Skills CLI:

```bash
npx skills add databricks/databricks-agent-skills --list
npx skills add databricks/databricks-agent-skills --skill databricks-apps --skill databricks-pipelines
```

AI Dev Kit skills via the AI Dev Kit installer, if a facilitator machine has bash, network access, and Databricks CLI configured:

```bash
curl -sSL https://raw.githubusercontent.com/databricks-solutions/ai-dev-kit/main/databricks-skills/install_skills.sh | bash -s -- --list
curl -sSL https://raw.githubusercontent.com/databricks-solutions/ai-dev-kit/main/databricks-skills/install_skills.sh | bash -s -- --install-to-genie
```

Use AI Dev Kit skills as accelerators for Databricks development patterns, not as a hard workshop dependency. The workshop `PROMPT.md` files remain the source of truth.

Reference: https://docs.databricks.com/gcp/en/agent-skills/

## Local Skills In This Repo

| Skill | Use It When |
| --- | --- |
| `@beverage-distribution-domain` | You need the workshop's beverage distribution domain, entities, grains, and safety rules. |
| `@lakehouse-data-generator` | You need synthetic data and Unity Catalog tables. |
| `@lakeflow-pipeline-builder` | You need Lakeflow Spark Declarative Pipeline code or debugging. |
| `@metric-view-builder` | You need a Unity Catalog metric view for governed business metrics. |
| `@genie-space-optimizer` | You need a curated Genie space with business context and sample questions. |
| `@business-scenario-synthesizer` | You need business-user question scenarios for the Genie space. |
| `@mlflow-genai-evaluator` | You need MLflow tracking, traces, scorers, or evaluation data for GenAI. |
| `@lakebase-app-builder` | You need Lakebase app state, feedback tables, or a Databricks App pattern. |
| `@databricks-app-builder` | You need a Databricks App that connects Unity Catalog, Genie, MLflow, and Lakebase. |
