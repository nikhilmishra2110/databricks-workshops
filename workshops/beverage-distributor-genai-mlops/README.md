# Beverage Distribution GenAI MLOps Workshop

Domain: Beverage distribution

Status: draft workshop package using synthetic data only.

## Workshop Thesis

Give a customer team a hands-on path for building governed GenAI and MLOps workflows in Databricks using prompts and Genie Code. Participants should leave with a working pattern they can reuse for their own account, product, inventory, promotion, and sales operations data.

## Recommended Anchor Use Case

Field Sales Account Intelligence Copilot.

The copilot helps a sales rep or regional manager ask account-level questions, identify reorder risk, recommend next actions, and capture follow-up actions in an operational app.

Why this is the right anchor:

- It is familiar to beverage distribution teams.
- It touches analytical data, ML features, business-friendly natural language, and operational state.
- It creates a natural path through Lakehouse data, Lakeflow, Genie spaces, MLflow, Databricks Apps, and Lakebase.
- It can run on synthetic data without exposing customer information.

## What Participants Build

1. Synthetic customer-like datasets for accounts, products, orders, inventory, promotions, and rep notes.
2. Unity Catalog tables and views.
3. A Lakeflow pipeline that cleans, joins, and curates bronze/silver/gold tables.
4. A Genie space for natural-language business questions.
5. A lightweight ML/GenAI workflow tracked and evaluated with MLflow.
6. A Lakebase-backed app concept that stores recommended actions and human feedback.
7. A reusable Genie Code skill pack for customer-specific development tasks.

## Primary Databricks Capabilities

- Genie Code Agent mode
- Genie Code skills
- Unity Catalog
- Lakeflow Spark Declarative Pipelines
- Genie spaces
- MLflow 3 for GenAI
- Databricks Apps
- Lakebase Postgres
- Git-backed workshop assets

## Workshop Assets

- `use-cases.md`: use case menu and recommendation
- `workshop-plan.md`: learning outcomes and flow
- `agenda.md`: time-boxed agenda
- `setup.md`: prerequisites and setup
- `prompts/prompt-pack.md`: prompts to paste into Genie Code
- `exercises/`: participant exercises
- `assets/`: data contracts, table descriptions, sample Genie questions, and evaluation rubrics
- `notebooks/`: optional starter notebooks for synthetic data and baseline modeling
