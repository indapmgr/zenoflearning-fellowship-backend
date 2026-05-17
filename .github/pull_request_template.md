## What does this PR do?

<!-- Describe what you changed and why -->

## Ticket

<!-- e.g. FEL-006 -->

## Checklist

- [ ] `docker compose run --rm api pytest` passes
- [ ] `docker compose run --rm api ruff format --check .` passes
- [ ] `docker compose run --rm api ruff check .` passes
- [ ] All functions have type hints
- [ ] No secrets or `.env` committed
- [ ] No new dependencies added without maintainer approval
- [ ] No database changes without maintainer approval
- [ ] Branch name follows `<type>/<ticket-id>-<short-description>`
- [ ] PR title follows `<ticket-id>: <short description>`
