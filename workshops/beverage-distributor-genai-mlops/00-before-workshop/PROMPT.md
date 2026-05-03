# Prompt

```text
Use Genie Code Agent mode.

I am preparing to run a Databricks workshop from this repo:
databricks-workshops/workshops/beverage-distributor-genai-mlops

Do not create, run, modify, or deploy anything yet. First create a readiness plan and wait for approval.

Workshop objective:
Participants should sequentially build a prompt-driven Databricks solution for a beverage distributor:
1. Use case
2. Synthetic data
3. Lakeflow pipeline
4. Unity Catalog metric view
5. Genie space
6. Business-user question scenarios
7. MLflow GenAI evaluation
8. Lakebase operational database
9. Databricks App

Check whether the workspace appears ready for:
- Unity Catalog
- CREATE CATALOG or access to catalog `workshop`
- CREATE SCHEMA or access to schema `workshop.beverage_distribution`
- CREATE TABLE permissions
- SQL warehouse access
- Lakeflow Spark Declarative Pipelines
- Genie Code Agent mode
- Genie spaces
- metric views
- MLflow experiment creation
- Databricks Apps
- Lakebase Autoscaling or Lakebase database resources
- ability to use prompts without custom skill installation
- optional ability to copy or read `.assistant/skills`
- optional ability to install Databricks AI Dev Kit skills if the environment supports Node/npm and external GitHub access

Return a readiness report with:
1. Green/yellow/red status for each capability.
2. Exact missing permission or admin ask if known.
3. Whether the workshop can run hands-on, partially hands-on, or demo-only.
4. The exact next folder to open.
5. A fallback path from `99-backup` for any red item.
6. Whether skillless prompt-only delivery is recommended.
7. Whether AI Dev Kit skills are feasible or should be skipped.

Wait for my approval before taking any action.
```
