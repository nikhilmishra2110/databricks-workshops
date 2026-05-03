# Prompt Pack: Beverage Distribution GenAI MLOps

Use these prompts in Databricks Genie Code. Ask for a plan first, then approve code or resource changes only after review.

## 1. Create Synthetic Datasets And Tables

```text
@lakehouse-data-generator

I am building a Databricks workshop for a synthetic beverage distributor.

Use this domain:
- accounts
- products
- orders
- inventory
- promotions
- rep notes

Use Unity Catalog:
- catalog: workshop
- schema: beverage_distribution

Create synthetic data only. Do not use real customer names, people, addresses, emails, contracts, or credentials.

First propose a plan. Then generate Databricks Python code that:
1. Creates the catalog and schema if allowed.
2. Creates small Spark DataFrames for each entity.
3. Adds realistic edge cases for reorder risk and inventory constraints.
4. Writes managed Delta tables.
5. Adds table comments and column comments.
6. Shows validation queries.

Wait for my approval before running any code.
```

## 2. Build Lakeflow Pipeline

```text
@lakeflow-pipeline-builder

Build a Lakeflow Spark Declarative Pipeline for the beverage distribution account intelligence workshop.

Inputs are existing bronze tables in workshop.beverage_distribution:
- bronze_accounts
- bronze_products
- bronze_orders
- bronze_inventory
- bronze_promotions
- bronze_rep_notes

Target outputs:
- silver_account_orders
- silver_inventory_position
- gold_account_intelligence

Use Python with the current Lakeflow Spark Declarative Pipelines API. Include data quality expectations for non-null IDs, valid order statuses, positive amounts, and inventory math.

First provide the pipeline design. Then generate pipeline source code and explain where it should be placed in the Lakeflow Pipelines Editor.

Wait for approval before making changes.
```

## 3. Create And Optimize Genie Space

```text
@genie-space-optimizer

Help me create and optimize a Databricks Genie space named "Beverage Account Intelligence".

Use only curated tables:
- workshop.beverage_distribution.gold_account_intelligence
- workshop.beverage_distribution.silver_account_orders
- workshop.beverage_distribution.silver_inventory_position

Business users are sales leaders and field sales reps.

Return:
1. Recommended table and column comments.
2. Business terms to define.
3. Sample questions that should work well.
4. Questions likely to fail and why.
5. A tuning checklist for improving answer quality.
6. Any tables or columns that should be hidden from the space.

Keep the language business-friendly.
```

## 4. MLOps And GenAI Evaluation With MLflow

```text
@mlflow-genai-evaluator

Create an MLOps pattern for the beverage distribution account intelligence recommendation workflow.

The app should produce:
- recommendation
- rationale
- confidence
- follow_up_action

Use MLflow to track prompt versions, inputs, outputs, metrics, evaluation examples, and human feedback. Include an evaluation dataset with at least 10 synthetic test cases.

First propose the evaluation design. Then generate Databricks notebook code that logs an experiment and compares two prompt variants.

Do not call external services unless I explicitly approve them.
```

## 5. Create Lakebase App Pattern

```text
@lakebase-app-builder

Design a Databricks App backed by Lakebase for the beverage distribution account intelligence workflow.

Use Lakebase for operational state only:
- saved account action plans
- human feedback on recommendations
- rep follow-up status
- prompt test cases

Return:
1. Lakebase project, branch, database, and schema naming.
2. PostgreSQL DDL for app tables.
3. A Databricks Apps resource configuration checklist.
4. A minimal Streamlit app architecture.
5. How the app should read curated analytics from Unity Catalog and write state to Lakebase.
6. Security and permission checks.

First give a plan. Do not create resources until I approve.
```

## 6. Package Skills After The Workshop

```text
Create or update Genie Code skills from what worked in this workshop.

For each skill, produce:
- folder name
- SKILL.md frontmatter
- when to use it
- step-by-step instructions
- examples
- edge cases

Focus on narrow skills:
- lakehouse data generation
- Lakeflow pipeline building
- Genie space optimization
- MLflow GenAI evaluation
- Lakebase app building
```
