# Prompt

```text
Use Genie space Agent mode if it is enabled for the Genie space. If Genie space Agent mode is not enabled, use standard Genie questions.

Use skill: @business-scenario-synthesizer

You are in step 06 of the workshop: synthesize a realistic business-user scenario and run questions against the Genie space named:
Beverage Account Intelligence

Scenario:
A regional sales leader is preparing for a Monday account review. They need to identify accounts that need follow-up, understand why they need follow-up, see whether inventory or promotion constraints matter, and decide what the field team should do next.

Use these business personas:
- VP of Sales: cares about region-level performance and risk.
- Regional Sales Manager: cares about reps, territories, and account prioritization.
- Field Sales Rep: cares about what action to take for each account.

Generate and run or prepare these questions:
1. Which accounts need attention this week and why?
2. Which sales reps have the most high-risk accounts?
3. Which regions have the highest paid net amount and which have the highest reorder risk?
4. Which high-risk accounts also have active promotions?
5. Which products have low available inventory and could block a recommendation?
6. For the top high-risk account, what next action should the sales rep take?
7. What evidence supports that recommendation?
8. What question failed or returned a weak answer, and what metadata would improve it?

Return:
- the exact business question
- the answer summary
- supporting table or metric used
- whether the answer was trusted, weak, or failed
- improvement needed

At the end, create a file named `06-business-scenarios/scenario-results.md` if file editing is available.

First show the scenario plan and question list. Wait for approval before running questions against the Genie space.

Do not use real customer data. If the Genie space cannot answer, explain whether the issue is missing data, weak metadata, missing metric, or ambiguous business language.
```
