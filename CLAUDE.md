# CLAUDE.md — Maintainer Reference

## AI Policy


Interns participating in the ZenOfLearning fellowship must not use AI coding agents
(Claude Code, GitHub Copilot, Cursor, ChatGPT, Gemini, or similar) for implementation tasks.
The purpose of this training repo is hands-on learning. AI-assisted implementation
defeats that purpose.

## Repo Purpose

This is the backend training repository for ZenOfLearning fellowship interns.
It is **not** the production ZenOfLearning backend.

## Stack

- Python 3.12
- FastAPI + Uvicorn
- pytest + httpx
- ruff (formatting + linting)
- Docker + Docker Compose
- PostgreSQL

## Maintainer Notes

- Default branch is `develop` — interns branch off this
- Interns work on branches: `<type>/<ticket-id>-<short-description>`
- All intern PRs target `develop`; maintainers release `develop` → `main`
- Database models and CRUD are introduced progressively via Trello tickets
- Keep `src/main.py` as a thin skeleton; do not implement route bodies for interns
