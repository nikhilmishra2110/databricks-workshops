#!/usr/bin/env bash
set -euo pipefail

required_paths=(
  "README.md"
  "catalog.yml"
  "prompts/README.md"
  "prompts/curriculum-designer.md"
  "prompts/sql-debugging-coach.md"
  "workshops/_template/workshop-plan.md"
  "workshops/_template/agenda.md"
  "examples/intro-sql/setup.sql"
  "checklists/pre-workshop.md"
  "rubrics/workshop-readiness.md"
  ".github/pull_request_template.md"
  "workshops/southern-glaciers-genai-mlops/README.md"
  "workshops/southern-glaciers-genai-mlops/prompts/prompt-pack.md"
  "workshops/southern-glaciers-genai-mlops/assets/source-data-contract.yml"
  ".assistant/skills/lakeflow-pipeline-builder/SKILL.md"
  ".assistant/skills/lakebase-app-builder/SKILL.md"
)

missing=0

for path in "${required_paths[@]}"; do
  if [[ ! -e "$path" ]]; then
    printf 'Missing required path: %s\n' "$path" >&2
    missing=1
  fi
done

if [[ "$missing" -eq 1 ]]; then
  exit 1
fi

printf 'Repository structure check passed.\n'
