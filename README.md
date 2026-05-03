# Databricks GenAI MLOps Workshop

This repository contains a sequential, prompt-driven Databricks workshop. It is designed so a facilitator or participant can open the repo, start at step `00`, and move through the full workflow without needing to understand the repo structure in advance.

The workshop is intentionally low effort:

- no custom skills are required
- every build step has a self-contained `PROMPT.md`
- Genie Code Agent mode should plan first, then act only after approval
- backup notebooks exist if a feature, permission, or workspace setup blocks the live path

## What You Build

The workshop builds a single end-to-end Databricks pattern:

```text
Use case
  -> synthetic data
  -> Lakeflow pipeline
  -> metric view
  -> Genie space
  -> business Q&A scenarios
  -> MLflow GenAI evaluation
  -> Lakebase operational state
  -> Databricks App
```

The use case is **Field Sales Account Intelligence Copilot** for a synthetic beverage distribution business. The app helps a sales leader or field rep understand which accounts need attention, why they need attention, what action should happen next, and how feedback should be captured.

## Who This Is For

You do not need to be a beverage industry expert to follow this repo.

The workshop is useful for:

- data engineers learning prompt-driven Databricks development
- ML engineers learning GenAI evaluation and app-state patterns
- solution architects demonstrating the Databricks platform end to end
- sales engineers or workshop facilitators preparing customer demos
- business stakeholders who want to understand what the platform can do

If you are non-technical, read each step's `README.md` first. It explains the business outcome before the prompt asks Genie Code to create anything.

## Repository Map

```text
.
|-- AGENTS.md                         # Instructions for Genie Code / coding agents
|-- SKILLS.md                         # Optional skills guidance
|-- .assistant/skills/                # Optional local Genie Code skills
|-- docs/databricks/                  # Product notes and links
|-- scripts/check_structure.sh        # Local repo validation
|-- workshops/
|   `-- beverage-distributor-genai-mlops/
|       |-- 00-before-workshop/
|       |-- 01-use-case/
|       |-- 02-generate-synthetic-data/
|       |-- 03-build-lakeflow-pipeline/
|       |-- 04-create-metric-view/
|       |-- 05-create-optimize-genie-space/
|       |-- 06-business-scenarios/
|       |-- 07-mlflow-genai-evaluation/
|       |-- 08-create-lakebase/
|       |-- 09-build-app/
|       `-- 99-backup/
`-- .github/                          # GitHub issue and PR templates
```

Start here:

[workshops/beverage-distributor-genai-mlops](workshops/beverage-distributor-genai-mlops)

## Prerequisites

For the full hands-on workshop, use a Databricks workspace with:

- Unity Catalog
- SQL warehouse access
- Genie Code Agent mode
- Lakeflow Spark Declarative Pipelines
- Metric views
- Genie spaces
- MLflow experiment access
- Lakebase Autoscaling or Lakebase database access
- Databricks Apps

You can still run a partial workshop if some features are missing. Use:

[workshops/beverage-distributor-genai-mlops/99-backup](workshops/beverage-distributor-genai-mlops/99-backup)

## How To Run The Workshop

Use this exact loop for every numbered folder:

1. Open the folder.
2. Read `README.md`.
3. Open `PROMPT.md`.
4. Paste the full prompt into Genie Code Agent mode.
5. Ask Genie Code to return a plan first.
6. Review the plan, resources, and code.
7. Approve execution only when it looks right.
8. Confirm the step's "Done When" checklist.
9. Move to the next numbered folder.

Do not skip the plan/review step. The point of the workshop is prompt-driven engineering with human control, not blind code generation.

## Step-By-Step Sequence

| Step | Folder | What Happens | Output |
| --- | --- | --- | --- |
| 00 | [before workshop](workshops/beverage-distributor-genai-mlops/00-before-workshop) | Check workspace readiness. | Readiness report and fallback plan. |
| 01 | [use case](workshops/beverage-distributor-genai-mlops/01-use-case) | Define the one business workflow. | Use case brief and target architecture. |
| 02 | [generate synthetic data](workshops/beverage-distributor-genai-mlops/02-generate-synthetic-data) | Create workshop data from a data contract. | Bronze Unity Catalog tables. |
| 03 | [build Lakeflow pipeline](workshops/beverage-distributor-genai-mlops/03-build-lakeflow-pipeline) | Curate bronze data into silver and gold. | `silver_*` and `gold_account_intelligence` tables. |
| 04 | [create metric view](workshops/beverage-distributor-genai-mlops/04-create-metric-view) | Define governed business metrics. | `beverage_account_metrics` metric view. |
| 05 | [create and optimize Genie space](workshops/beverage-distributor-genai-mlops/05-create-optimize-genie-space) | Add curated assets and business context. | `Beverage Account Intelligence` Genie space. |
| 06 | [business scenarios](workshops/beverage-distributor-genai-mlops/06-business-scenarios) | Ask realistic business questions. | Scenario results and Genie improvement backlog. |
| 07 | [MLflow GenAI evaluation](workshops/beverage-distributor-genai-mlops/07-mlflow-genai-evaluation) | Compare recommendation quality. | MLflow experiment, evaluation examples, scored outputs. |
| 08 | [create Lakebase](workshops/beverage-distributor-genai-mlops/08-create-lakebase) | Create operational app-state schema. | Lakebase tables for actions and feedback. |
| 09 | [build app](workshops/beverage-distributor-genai-mlops/09-build-app) | Build a simple Databricks App. | App files and demo workflow. |
| 99 | [backup](workshops/beverage-distributor-genai-mlops/99-backup) | Keep moving if something fails. | Fallback prompts, SQL, and notebooks. |

## Default Resource Names

The prompts use these defaults:

```text
catalog: workshop
schema: beverage_distribution
metric_view: beverage_account_metrics
genie_space: Beverage Account Intelligence
mlflow_experiment: /Shared/beverage_account_intelligence
lakebase_project: beverage-account-actions
lakebase_database: beverage-app-state
```

Change these names if your workspace requires a different catalog, schema, or naming convention.

## What The Main Artifacts Mean

`PROMPT.md`  
The instruction you paste into Genie Code Agent mode. It is intentionally detailed and should work without loading custom skills.

`README.md` inside each step  
Explains the business goal, expected output, and "Done When" criteria.

`data-contract.yml`  
Defines the synthetic data structure for step 02. It tells Genie Code what entities, grains, columns, and edge cases the data must include.

`metric-view.sql`  
Starter SQL for a Unity Catalog metric view. This centralizes business metrics before the Genie space is created.

`evaluation-rubric.yml`  
Defines how MLflow should evaluate GenAI recommendations.

`lakebase_schema.sql`  
Defines app-state tables for saved recommendations, feedback, follow-up status, and prompt test cases.

`99-backup/notebooks`  
Notebook-style Python files for facilitator fallback when a live prompt-driven path is blocked.

## Skills Are Optional

The workshop does not depend on custom skill loading.

Why: customer environments can vary across Windows, macOS, managed desktops, restricted networks, and Databricks workspace permissions. Making skills mandatory creates avoidable setup risk.

Preferred path:

```text
Use the numbered PROMPT.md files directly.
```

Optional path:

- use local skills in [.assistant/skills](.assistant/skills)
- use Databricks or AI Dev Kit skills if a facilitator installs them ahead of time

See [SKILLS.md](SKILLS.md).

## Lakebase And App Pattern

The intended architecture is:

- Unity Catalog stores governed analytical data.
- Genie space answers natural-language questions over curated assets.
- MLflow tracks and evaluates GenAI recommendations.
- Lakebase stores operational app state, such as action plans and feedback.
- Databricks App connects everything into one business workflow.

For the app:

- add Lakebase as a Databricks App database resource
- use injected `PG*` environment variables for Postgres connections
- use `psycopg` or SQLAlchemy for Lakebase reads/writes
- use Databricks SDK for workspace APIs, such as Genie calls
- do not hardcode credentials or connection strings

## Backup Path

If a live step fails, use [99-backup](workshops/beverage-distributor-genai-mlops/99-backup).

The backup notebooks are:

```text
00_run_all_backup.py
01_create_lakehouse_assets.py
02_create_mlflow_evaluation.py
03_create_lakebase_with_sdk.py
04_generate_app_files.py
```

They are Databricks notebook-source Python files. They are meant to run inside Databricks, not on a local laptop.

## Common Failure Modes

| Problem | What To Do |
| --- | --- |
| Genie Code Agent mode is unavailable | Use the prompt as manual instructions, or use backup notebooks. |
| Cannot create catalog or schema | Use an existing catalog/schema and update the prompts. |
| Lakeflow permissions are missing | Use `99-backup/fallback-pipeline.py`. |
| Metric views are unavailable | Use `99-backup/fallback-standard-view.sql`. |
| Genie spaces are unavailable | Use `99-backup/fallback-genie-questions.md`. |
| MLflow GenAI APIs are unavailable | Use `99-backup/fallback-manual-evaluation.md`. |
| Lakebase is unavailable | Use `99-backup/fallback-lakebase-sqlite.md` or skip to app demo mode. |
| App resources are not available | Generate app files and explain the resource wiring as a design walkthrough. |

## Local Validation

From the repo root:

```bash
./scripts/check_structure.sh
```

This only validates that the repo structure is intact. It does not create Databricks resources.

## Safety Rules

- Use synthetic data only.
- Do not paste customer PII, private account data, contracts, credentials, or production connection strings into prompts.
- Review all generated code before running it.
- Prefer least-privilege access for Genie spaces, Apps, Lakebase, and SQL warehouses.

