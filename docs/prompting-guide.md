# Prompting Guide For Database Workshops

## Prompt Pattern

Use prompts that clearly state:

- role
- workshop context
- database dialect
- participant level
- input material
- output format
- review criteria

## Good Placeholders

```text
{{audience}}
{{database_dialect}}
{{schema_context}}
{{learner_sql}}
{{error_message}}
{{exercise_goal}}
{{time_limit_minutes}}
```

## Prompt Review

Before using a prompt live:

- confirm it does not require sensitive data
- confirm it asks for dialect-specific SQL
- test it with a realistic learner mistake
- check whether the output is concise enough for a workshop setting

## Live Use Guidance

During workshops, prompts should support the facilitator. They should not replace the facilitator's judgment or become a hidden answer key.

Good live prompt outputs:

- short hints
- targeted explanations
- corrected query plus reason
- follow-up questions

Less useful live outputs:

- long lectures
- generic SQL tutorials
- solutions that ignore the provided schema
- answers that switch dialects

