# Prompt: Workshop Retrospective

## Purpose

Turn workshop notes and feedback into concrete improvements.

## Best Used When

- after running a workshop
- when revising exercises
- when deciding what to keep, cut, or clarify

## Inputs

- `{{workshop_goal}}`
- `{{agenda}}`
- `{{facilitator_notes}}`
- `{{participant_feedback}}`
- `{{observed_sticking_points}}`

## Prompt

```text
You are helping improve a database workshop after delivery.

Workshop goal:
{{workshop_goal}}

Agenda:
{{agenda}}

Facilitator notes:
{{facilitator_notes}}

Participant feedback:
{{participant_feedback}}

Observed sticking points:
{{observed_sticking_points}}

Return:

1. What worked and should stay.
2. What confused participants.
3. Exercise changes to make before the next run.
4. Setup or tooling issues to fix.
5. Prompt updates to add to the repo.
6. A prioritized action list.

Be specific and tie each recommendation to evidence in the notes or feedback.
```

## Expected Output

An action list that can become issues or pull requests.

## Human Review Checklist

- [ ] Recommendations are traceable to actual feedback
- [ ] Fixes are specific enough to implement
- [ ] Next-run changes are prioritized

