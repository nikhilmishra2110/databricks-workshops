# Workshop Design Principles

## Start From The Job

Define what participants should be able to do after the workshop. Keep outcomes observable:

- "write a join across two tables"
- "explain why a query returns duplicate rows"
- "choose an index for a slow lookup query"

Avoid outcomes that are too vague:

- "understand SQL"
- "learn databases"

## Keep The Data Small

Small datasets make live workshops easier to debug. Use enough rows to show the concept, not enough rows to mimic production volume.

Good workshop data includes:

- recognizable entities
- predictable edge cases
- a few nulls where useful
- clear relationships between tables

## Prefer One New Concept At A Time

Exercises should add difficulty gradually. If a learner is practicing joins, avoid adding complex date parsing at the same time unless that is the point.

## Make Failure Useful

Prepare common mistakes as teachable moments:

- wrong join key
- row filter used when group filter is needed
- missing `GROUP BY` column
- unexpected duplicates
- dialect mismatch

## Leave A Trail For The Next Facilitator

After each workshop, update:

- confusing instructions
- setup issues
- questions participants asked
- exercises that ran too short or too long
- prompts that produced useful facilitator support

