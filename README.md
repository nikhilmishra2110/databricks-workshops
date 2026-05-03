# Databricks GenAI MLOps Workshop

This repo contains one low-effort, prompt-driven Databricks workshop.

Participants move through numbered folders from start to finish. Every build step is driven by a detailed `PROMPT.md` intended for Databricks Genie Code Agent mode. Custom skills are optional; prompts are self-contained so the workshop can run in constrained customer environments.

Start here:

```text
workshops/beverage-distributor-genai-mlops/
```

## Repository Map

```text
.
|-- AGENTS.md                         # Instructions auto-discovered by Genie Code
|-- SKILLS.md                         # Human-readable skill index
|-- .assistant/skills/                # Genie Code skills
|-- workshops/beverage-distributor-genai-mlops/
|   |-- 00-before-workshop/
|   |-- 01-use-case/
|   |-- 02-generate-synthetic-data/
|   |-- 03-build-lakeflow-pipeline/
|   |-- 04-create-metric-view/
|   |-- 05-create-optimize-genie-space/
|   |-- 06-business-scenarios/
|   |-- 07-mlflow-genai-evaluation/
|   |-- 08-create-lakebase/
|   |-- 09-build-app/
|   `-- 99-backup/
|-- docs/databricks/                  # Product notes and links
|-- scripts/                          # Repo validation
`-- .github/                          # GitHub templates
```

## Quick Start

1. Clone this repo into Databricks Repos or a workspace Git folder.
2. Open `workshops/beverage-distributor-genai-mlops/README.md`.
3. Run the numbered folders in order.
4. Use Genie Code Agent mode for each `PROMPT.md`.
5. Optional: install local skills or AI Dev Kit skills if the customer environment supports it.

To validate the repo locally:

```bash
./scripts/check_structure.sh
```

## Optional Databricks Skill Setup

Databricks Genie Code skills live in a `.assistant/skills/` directory inside a Databricks workspace or user folder. This repo includes starter skills under `.assistant/skills/`, but the workshop does not require them.

Recommended workspace path:

```text
Workspace/.assistant/skills/
```

Recommended user path:

```text
/Users/{username}/.assistant/skills/
```

## Workshop Outcome

Participants build one end-to-end pattern:

```text
Use case -> synthetic data -> Lakeflow pipeline -> metric view -> Genie space -> business Q&A scenarios -> MLflow evaluation -> Lakebase -> Databricks App
```

If a product feature or permission is missing, use `99-backup/`.

## Backup Automation

The backup folder includes Databricks notebook-style Python files designed to create the core objects in one path when a live prompt-driven step fails:

```text
workshops/beverage-distributor-genai-mlops/99-backup/notebooks/
```
