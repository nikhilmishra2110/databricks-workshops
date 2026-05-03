# Intro SQL Workshop

Audience: analysts or operators who are new to SQL.

Database: SQLite-compatible SQL.

Duration: 60 to 90 minutes.

## Learning Outcomes

Participants can:

- read a simple table schema
- filter rows with `WHERE`
- sort and limit results
- join two related tables
- group rows and calculate simple aggregates

## Files

- `setup.sql` creates and seeds the sample tables
- `exercises/01-select-filter.md` covers selection, filtering, sorting, and limits
- `exercises/02-joins-aggregation.md` covers joins and aggregates
- `data/` stores CSV copies of the sample data

## Run Locally With SQLite

```bash
sqlite3 intro_sql.sqlite < setup.sql
sqlite3 intro_sql.sqlite
```

Inside SQLite:

```sql
.tables
SELECT * FROM customers LIMIT 5;
```

