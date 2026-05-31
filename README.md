# ZenOfLearning Fellowship Backend

Training repository for ZenOfLearning fellowship interns.
**This is not the production backend.**

## Stack

| Layer | Technology |
|---|---|
| Language | Python 3.12 |
| Framework | FastAPI |
| Server | Uvicorn |
| Tests | pytest + httpx |
| Formatter + Linter | ruff |
| Container | Docker + Docker Compose |
| Database | PostgreSQL |

---

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) — required
- Git

That is all. You do not need Python or any other tool installed locally.

---

## Quick Start

```bash
# 1. Clone
git clone <repo-url>
cd zenoflearning-fellowship-backend

# 2. Environment config
cp .env.example .env

# 3. Start the app
docker compose up --build
```

- Health check: http://localhost:8000/health
- Interactive docs: http://localhost:8000/docs

---

## Running Tests

```bash
docker compose run --rm api pytest
```

## Formatting

```bash
docker compose run --rm api ruff format .
```

## Linting

```bash
docker compose run --rm api ruff check .
```

---

## Managing Python Versions (Optional — local development only)

If you prefer to run the app locally without Docker, you will need Python 3.12.
You may already have a different Python version installed — use `pyenv` to manage
multiple versions side by side without replacing your existing setup.

**macOS**
```bash
brew install pyenv
pyenv install 3.12
```

Then add pyenv to your shell. Open `~/.zshrc` and add these lines at the bottom:
```bash
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

Reload your shell:
```bash
source ~/.zshrc
```

**Windows**

Step 1 — Install pyenv-win:
```powershell
pip install pyenv-win --target "$HOME\.pyenv"
```

Step 2 — Add these two entries to your user PATH (Search → "Edit environment variables for your account"):
```
%USERPROFILE%\.pyenv\pyenv-win\bin
%USERPROFILE%\.pyenv\pyenv-win\shims
```

Step 3 — Restart PowerShell, then install Python 3.12:
```powershell
pyenv --version
pyenv install 3.12
```

Verify pyenv picks up the right version inside the repo:
```bash
cd zenoflearning-fellowship-backend
python --version
# Expected: Python 3.12.x
```

**Local setup (after Python 3.12 is installed)**
```bash
python3.12 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
cp .env.example .env
uvicorn src.main:app --reload
```

---

## Deployment

This repo deploys to two Render servers automatically.

| Server | Branch | URL |
|---|---|---|
| Dev | `develop` | https://zenoflearning-backend-dev.onrender.com |
| Prod | `main` | https://zenoflearning-backend-prod.onrender.com |

**How it works:**
- Merge to `develop` → Render auto-deploys to dev server
- Merge to `main` → Render auto-deploys to prod server
- CI must pass before any merge is allowed

**Health check (public, no auth):**
```
GET https://zenoflearning-backend-dev.onrender.com/health
GET https://zenoflearning-backend-prod.onrender.com/health
→ {"status": "ok"}
```

**Manual PR preview:**
If you want to test a specific PR live before merging, go to the Render dashboard → select the dev service → manually deploy the PR branch. No automatic PR previews.

**Coming later:**
- PostgreSQL database
- Authentication

---

## AI Policy

Interns must not use AI coding agents for implementation. See [CONTRIBUTING.md](CONTRIBUTING.md).

test
