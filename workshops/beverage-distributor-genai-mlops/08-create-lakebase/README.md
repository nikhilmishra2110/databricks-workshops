# 08 - Create Lakebase

## Goal

Create Lakebase operational state for saved recommendations, human feedback, and follow-up status.

## Lakebase Purpose

Lakebase is not the analytics source of record in this workshop. It stores app state.

## Correct Implementation Pattern

- Use Lakebase Autoscaling if available.
- Use Databricks Python SDK for control-plane automation when APIs are available.
- Use the Lakebase SQL editor or a Postgres client to create app schemas and tables.
- In the Databricks App, connect through the Lakebase App resource and injected `PG*` environment variables.
- Do not hardcode database hostnames, usernames, passwords, or connection strings.

## Done When

- Lakebase project, branch, and database are created or clearly planned.
- App schema exists.
- Feedback and action-plan tables exist.
- Participants understand what belongs in Unity Catalog vs Lakebase.
- The App resource model is understood before step 09.

## Backup

If Lakebase is unavailable, use `../99-backup/fallback-lakebase-sqlite.md` for local app-state simulation.
