# Workshop Plan: Beverage Distribution GenAI MLOps On Databricks

## Summary

Participants use prompts and Genie Code to build an end-to-end Databricks workflow for a synthetic beverage distributor. The workflow creates data, curates tables with Lakeflow, exposes trusted business questions in a Genie space, tracks GenAI/MLOps quality with MLflow, and stores application state in Lakebase.

## Audience

- Data engineers
- Data scientists
- ML engineers
- Solution architects
- Analytics engineers
- Technical product owners

## Duration

Half-day: 3.5 hours.

Full-day option: 6 hours with deeper app and MLflow evaluation work.

## Learning Outcomes

By the end, participants can:

- use Genie Code prompts to generate synthetic domain data and Unity Catalog tables
- create a Lakeflow Spark Declarative Pipeline from natural-language instructions
- improve table metadata and curated views for a Genie space
- create and test natural-language business questions against a Genie space
- track GenAI app behavior and quality with MLflow
- design a Lakebase-backed operational app pattern
- package reusable Genie Code skills for a customer workshop

## Workshop Flow

| Stage | Output | Databricks Capability |
| --- | --- | --- |
| Use case framing | Selected business workflow and success criteria | Workshop design |
| Data creation | Synthetic tables and metadata | Genie Code, Unity Catalog |
| Pipeline creation | Bronze/silver/gold Lakeflow pipeline | Lakeflow Spark Declarative Pipelines |
| Business interaction | Genie space questions and optimization plan | Genie spaces |
| MLOps | Recommendation/evaluation experiment | MLflow 3 for GenAI |
| Operationalization | Lakebase app state model | Databricks Apps, Lakebase |
| Reuse | Skills and prompt pack | Genie Code skills |

## Success Criteria

- Participants can explain the target use case.
- Tables are created without real customer data.
- Pipeline code is generated, reviewed, and corrected.
- Genie space questions produce trusted answers or clear improvement tasks.
- MLflow captures enough artifacts to compare prompt/model iterations.
- Lakebase is positioned for operational state, feedback, and app persistence.

## Risks

| Risk | Mitigation |
| --- | --- |
| Workspace lacks Lakebase or Genie access | Use design exercise and app schema fallback |
| Participants paste prompts without reviewing generated code | Require review checkpoints before running code |
| Synthetic data is too generic | Use the domain contract in `assets/source-data-contract.yml` |
| Genie space answers are weak | Improve table comments, column descriptions, business terms, and sample questions |
| Time runs short | Skip app implementation and cover Lakebase as an architecture exercise |
