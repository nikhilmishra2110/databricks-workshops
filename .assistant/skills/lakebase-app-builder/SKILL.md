---
name: lakebase-app-builder
description: Use when designing a Databricks App backed by Lakebase Postgres for operational state, feedback, action plans, or prompt test cases.
---

# Lakebase App Builder

Use this skill when adding Lakebase to a Databricks App workflow.

## Positioning

Lakebase is for operational state and low-latency app data. Unity Catalog tables remain the analytical source of record.

## Steps

1. Confirm whether Lakebase is enabled and which version is available.
2. Name the project, branch, database, and app schema.
3. Define PostgreSQL tables for app state.
4. Identify Databricks App resources and permissions.
5. Describe environment variables and connection handling.
6. Define what the app reads from Unity Catalog and writes to Lakebase.
7. Add cleanup and ownership notes.

## Good Lakebase State

- saved action plans
- recommendation feedback
- workflow status
- prompt test cases
- lightweight user preferences

## Avoid

- storing large analytical fact tables
- duplicating governed lakehouse sources
- putting credentials in app code
- assuming Lakebase is enabled without checking

## Output Format

Return:

- resource naming
- PostgreSQL DDL
- app architecture
- permission checklist
- data flow
- operational risks

