# Databricks Workshops

Reusable assets for planning and running Databricks customer workshops, with an emphasis on prompt-driven development using Genie Code, Lakeflow pipelines, Genie spaces, MLflow, Databricks Apps, and Lakebase.

The first packaged workshop is:

- `workshops/beverage-distributor-genai-mlops/`: a customer-facing GenAI + MLOps workshop for a beverage distribution use case.

This repo stores:

- prompt packs for Genie Code, Databricks workshop planning, SQL coaching, schema review, Lakeflow pipeline creation, Genie space optimization, MLflow evaluation, and Lakebase app setup
- `.assistant/skills/` examples for Genie Code Agent mode
- workshop templates for agendas, facilitator guides, learner handouts, and exercises
- reusable SQL datasets, setup scripts, and examples
- checklists and rubrics for workshop readiness and learner evaluation

## Repository Map

```text
.
|-- .assistant/skills/        # Genie Code skill examples
|-- prompts/                 # Reusable prompt cards
|-- workshops/_template/      # Copy this folder for each new workshop
|-- workshops/beverage.../    # Starter Databricks GenAI/MLOps workshop
|-- examples/intro-sql/       # Starter workshop with sample SQL assets
|-- docs/                     # Operating model and design guidance
|-- checklists/               # Repeatable planning and publishing checklists
|-- rubrics/                  # Evaluation rubrics
|-- templates/                # Reusable markdown templates
|-- scripts/                  # Lightweight repo validation helpers
`-- .github/                 # GitHub issue and PR templates
```

## Quick Start

1. Copy `workshops/_template` into a new folder:

   ```bash
   cp -R workshops/_template workshops/your-workshop-name
   ```

2. Fill in the workshop plan:

   - `workshops/your-workshop-name/workshop-plan.md`
   - `workshops/your-workshop-name/agenda.md`
   - `workshops/your-workshop-name/facilitator-guide.md`
   - `workshops/your-workshop-name/learner-handout.md`

3. Add prompts from `prompts/` into the workshop prompt pack.

4. Add setup scripts, datasets, and exercises.

5. Run the structure check:

   ```bash
   ./scripts/check_structure.sh
   ```

## Recommended GitHub Setup

Suggested repository name:

```text
databricks-workshops
```

Suggested visibility:

- private if prompts, datasets, or client-specific examples are sensitive
- public if this is meant to be a shared open workshop library

Suggested topics:

```text
database, sql, workshops, prompts, education, data-engineering
```

To create and push with the GitHub CLI:

```bash
gh repo create nikhilmishra2110/databricks-workshops --private --source=. --remote=origin --push
```

Change `--private` to `--public` if you want the assets to be public.

## Databricks Skill Setup

Databricks Genie Code skills live in a `.assistant/skills/` directory inside a Databricks workspace or user folder. This repo includes starter skills under `.assistant/skills/` so they can be copied or synced into the appropriate Databricks location.

Recommended workspace path:

```text
Workspace/.assistant/skills/
```

Recommended user path:

```text
/Users/{username}/.assistant/skills/
```

## Asset Naming

Use predictable names so assets are easy to find:

```text
YYYY-MM-topic-audience
intro-sql-analysts
postgres-performance-developers
schema-design-product-teams
```

For prompts, use:

```text
verb-object-role.md
curriculum-designer.md
schema-design-reviewer.md
sql-debugging-coach.md
```

## Contribution Flow

1. Open an issue using the workshop asset request template.
2. Create or update the relevant workshop, prompt, checklist, or rubric.
3. Test examples locally when they include runnable SQL.
4. Open a pull request using the checklist in `.github/pull_request_template.md`.

## License

Add a license before publishing externally. A common setup is:

- MIT for scripts and code examples
- CC BY 4.0 for written workshop content
