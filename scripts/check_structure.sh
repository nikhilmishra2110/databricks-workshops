#!/usr/bin/env bash
set -euo pipefail

required_paths=(
  "README.md"
  "AGENTS.md"
  "SKILLS.md"
  "catalog.yml"
  ".github/pull_request_template.md"
  "docs/databricks/current-product-notes.md"
  "workshops/beverage-distributor-genai-mlops/README.md"
  "workshops/beverage-distributor-genai-mlops/00-before-workshop/PROMPT.md"
  "workshops/beverage-distributor-genai-mlops/01-use-case/PROMPT.md"
  "workshops/beverage-distributor-genai-mlops/02-generate-synthetic-data/PROMPT.md"
  "workshops/beverage-distributor-genai-mlops/02-generate-synthetic-data/data-contract.yml"
  "workshops/beverage-distributor-genai-mlops/03-build-lakeflow-pipeline/PROMPT.md"
  "workshops/beverage-distributor-genai-mlops/04-create-metric-view/PROMPT.md"
  "workshops/beverage-distributor-genai-mlops/04-create-metric-view/metric-view.sql"
  "workshops/beverage-distributor-genai-mlops/05-create-optimize-genie-space/PROMPT.md"
  "workshops/beverage-distributor-genai-mlops/05-create-optimize-genie-space/business-context.yml"
  "workshops/beverage-distributor-genai-mlops/06-business-scenarios/PROMPT.md"
  "workshops/beverage-distributor-genai-mlops/07-mlflow-genai-evaluation/PROMPT.md"
  "workshops/beverage-distributor-genai-mlops/07-mlflow-genai-evaluation/evaluation-rubric.yml"
  "workshops/beverage-distributor-genai-mlops/08-create-lakebase/PROMPT.md"
  "workshops/beverage-distributor-genai-mlops/08-create-lakebase/lakebase_schema.sql"
  "workshops/beverage-distributor-genai-mlops/09-build-app/PROMPT.md"
  "workshops/beverage-distributor-genai-mlops/09-build-app/app-architecture.md"
  "workshops/beverage-distributor-genai-mlops/99-backup/README.md"
  "workshops/beverage-distributor-genai-mlops/99-backup/fallback-pipeline.py"
  "workshops/beverage-distributor-genai-mlops/99-backup/notebooks/00_run_all_backup.py"
  "workshops/beverage-distributor-genai-mlops/99-backup/notebooks/01_create_lakehouse_assets.py"
  "workshops/beverage-distributor-genai-mlops/99-backup/notebooks/02_create_mlflow_evaluation.py"
  "workshops/beverage-distributor-genai-mlops/99-backup/notebooks/03_create_lakebase_with_sdk.py"
  "workshops/beverage-distributor-genai-mlops/99-backup/notebooks/04_generate_app_files.py"
  ".assistant/skills/lakeflow-pipeline-builder/SKILL.md"
  ".assistant/skills/metric-view-builder/SKILL.md"
  ".assistant/skills/business-scenario-synthesizer/SKILL.md"
  ".assistant/skills/lakebase-app-builder/SKILL.md"
  ".assistant/skills/databricks-app-builder/SKILL.md"
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
