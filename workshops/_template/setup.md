# Setup: {{workshop_title}}

## Requirements

- Database: {{database_dialect}}
- Client: {{client_tool}}
- Files: {{files_needed}}

## Setup Steps

1. Install or open the required database client.
2. Create the workshop database or schema.
3. Run the setup SQL.
4. Confirm that the sample tables exist.

## Verification Query

```sql
SELECT 1 AS setup_ok;
```

## Troubleshooting

| Problem | Fix |
| --- | --- |
| Connection fails | Confirm host, port, database, username, and network access |
| Table not found | Confirm the setup script ran in the right database/schema |
| Syntax error | Confirm the database dialect matches the workshop |

