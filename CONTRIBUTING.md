# Contributing — Intern Guide

Welcome to the ZenOfLearning fellowship backend. Read this fully before you write your first line of code.

---

## AI Policy

You must **not** use AI coding agents — Claude Code, GitHub Copilot, Cursor, ChatGPT, Gemini, or any similar tool — to generate implementation code in this repository.

Write the code yourself. This is a learning environment. AI-generated solutions undermine your training and will be rejected in code review.

Maintainers (Avishkar and Indap) are the only people authorised to use AI tooling in this repo.

---

## Branch Workflow

This repo uses two protected branches:

| Branch | Purpose |
|---|---|
| `develop` | Default branch. All intern PRs target this. |
| `main` | Stable branch. Maintainers only — released from `develop` when ready. |

`develop` is the default branch. When you clone the repo, you are already on `develop`.

All PRs must target `develop`. Maintainers periodically merge `develop` into `main` as a release — interns never touch `main`.

You must **never** commit directly to `main` or `develop`. Always branch off `develop`.

```bash
git checkout develop
git pull origin develop
git checkout -b feature/FEL-006-health-endpoint
```

### Branch Naming

```
<type>/<ticket-id>-<short-description>
```

| Type | When to use |
|---|---|
| `feature` | New ticket work |
| `fix` | Bug fix |
| `docs` | Documentation only |
| `chore` | Repo, config, or maintenance work |
| `hotfix` | Urgent fix to main — maintainers only |

Examples:
```
feature/FEL-006-health-endpoint
feature/FEL-015-students-crud
docs/FEL-023-docker-readme
chore/INIT-003-ci-and-docs
```

---

## Commit Messages

Format: `<ticket-id>: <short imperative description>`

- Lowercase
- No trailing period
- Imperative mood ("add", not "added" or "adds")

```
FEL-006: add health endpoint
FEL-015: add students crud
FEL-023: update docker readme
```

---

## Type Hints

All functions must have type annotations. This is enforced by ruff (`ANN` rules).

```python
# correct
def greet(name: str) -> dict[str, str]:
    return {"greeting": f"Hello, {name}!"}

# will fail ruff check
def greet(name):
    return {"greeting": f"Hello, {name}!"}
```

---

## Before Every Commit

Run these three commands before every commit and make sure all pass:

```bash
docker compose run --rm api ruff format .
docker compose run --rm api ruff check .
docker compose run --rm api pytest
```

---

## Pull Requests

PRs must target `develop`, not `main`.

**PR title format:** `<ticket-id>: <short description>`
```
FEL-006: add health endpoint
FEL-015: add students crud
```

Before opening a PR, confirm every item below:

- [ ] Branched off `develop` and PR targets `develop`
- [ ] All tests pass (`docker compose run --rm api pytest`)
- [ ] Code is formatted (`docker compose run --rm api ruff format --check .`)
- [ ] Ruff reports no issues (`docker compose run --rm api ruff check .`)
- [ ] All functions have type hints
- [ ] No secrets or `.env` committed
- [ ] No new dependencies added without maintainer approval
- [ ] No database changes without maintainer approval
- [ ] PR title follows `<ticket-id>: <short description>`
- [ ] PR description explains what the change does and why

---

## No Secrets Policy

Never commit secrets, credentials, API keys, or passwords. Never commit your `.env` file.

Use `.env.example` as a template. Your `.env` is gitignored and stays on your machine only.

If you accidentally commit a secret, tell a maintainer immediately.

---

## Adding Dependencies

Do not add packages to `requirements.txt` or `requirements-dev.txt` without explicit approval from Avishkar or Indap.

If you think a package would be useful, raise it in your next check-in.

---

## Database Changes

Do not create, modify, or delete database tables, columns, or migrations without explicit approval from a maintainer.

All schema changes must be discussed and planned before any code is written.

---

## Code Review and Live Walkthrough

When a maintainer requests a live walkthrough of your PR, you are expected to:

- Explain what your code does and why you wrote it that way
- Walk through your tests and what they cover
- Answer questions about your implementation decisions

This is a normal part of the review process and a learning opportunity. If you cannot explain your code, it will not be merged.

---

## Getting Help

Stuck? That is expected and normal.

1. Spend 20–30 minutes trying to work it out yourself first
2. Check the FastAPI docs, Python docs, or the README
3. Ask in the team channel — include what you tried, what you expected, and what actually happened
4. Reach out to Avishkar or Indap directly if it is blocking you

Do not silently struggle for hours. Asking for help is part of the process.
