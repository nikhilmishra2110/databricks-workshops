# Facilitator Guide

## Before The Workshop

- [ ] Confirm the customer name and whether "Southern Glaciers" should be changed.
- [ ] Confirm workspace features: Genie Code, Genie spaces, Lakeflow, MLflow, Apps, Lakebase.
- [ ] Decide whether Lakebase is hands-on or architecture-only.
- [ ] Import or copy the skills in `.assistant/skills/`.
- [ ] Run the optional data notebook if you want pre-created tables.
- [ ] Review the prompts in `prompts/prompt-pack.md`.

## Facilitation Pattern

For each hands-on section:

1. State the business outcome.
2. Paste the prompt.
3. Ask Genie Code to propose a plan first.
4. Review generated code or resource changes.
5. Run only after approval.
6. Inspect results and ask for an improvement.

## Key Teaching Points

- Prompts are part of the development workflow, not a replacement for review.
- Good Genie spaces need curated tables, comments, sample questions, and business terms.
- Lakeflow pipeline code should be small, testable, and layered.
- MLflow should capture prompt/model versions, inputs, outputs, metrics, traces, and feedback.
- Lakebase is for operational state and low-latency app data, not a replacement for governed lakehouse tables.

## Common Issues

| Issue | Facilitator Response |
| --- | --- |
| Genie Code generates a broad plan | Ask it to narrow to one table, one pipeline, or one app endpoint |
| Generated SQL uses the wrong catalog | Point it to `assets/resource-names.yml` |
| Genie space answers are generic | Improve metadata and add sample questions |
| Lakebase permissions are missing | switch to design-only exercise and capture required admin asks |
| Participants want real data | Use synthetic data first, then discuss approved data onboarding |

