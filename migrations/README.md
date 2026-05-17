# Migrations

SQL migration files live here. Each file creates or modifies a database table.

## Naming convention

```
001_create_students_table.sql
002_create_assignments_table.sql
003_create_batches_table.sql
```

- Always prefix with a zero-padded number
- Always use lowercase and underscores
- Always describe what the migration does

## Running a migration

> PostgreSQL will be introduced in Week 2. Migration run instructions will be added then.

## Rules

- Never modify an existing migration file after it has been run
- Always write a new migration file for schema changes
- Never run migrations directly on the database without a migration file
