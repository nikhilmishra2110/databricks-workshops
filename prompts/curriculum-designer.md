# Prompt: Curriculum Designer

## Purpose

Design a database workshop plan with clear outcomes, exercises, timing, and facilitator notes.

## Best Used When

- starting a new workshop
- adapting a workshop for a different audience
- turning loose notes into a structured agenda

## Inputs

- `{{workshop_goal}}`
- `{{audience}}`
- `{{database_dialect}}`
- `{{duration_minutes}}`
- `{{participant_prerequisites}}`
- `{{tools_available}}`

## Prompt

```text
You are a senior database workshop designer.

Create a workshop plan for:

- Goal: {{workshop_goal}}
- Audience: {{audience}}
- Database dialect: {{database_dialect}}
- Duration: {{duration_minutes}} minutes
- Prerequisites: {{participant_prerequisites}}
- Tools available: {{tools_available}}

Return:

1. Learning outcomes written as observable skills.
2. A timed agenda.
3. Exercise sequence with difficulty progression.
4. Required setup assets.
5. Facilitator notes for common confusion points.
6. A short assessment or exit ticket.

Keep the plan practical for a live workshop. Prefer hands-on work over lecture.
```

## Expected Output

A workshop outline that can be moved into `workshop-plan.md` and `agenda.md`.

## Human Review Checklist

- [ ] Outcomes are measurable
- [ ] Timing is realistic
- [ ] Exercises can run with the available tools
- [ ] Assumptions about participant skill are explicit
- [ ] Sensitive data is not required

