# server-monitor

A server monitoring service: a lightweight agent collects metrics (CPU, RAM, disk) and sends them to a backend that stores the data, exposes it through an API, and sends alerts when something goes wrong.

> **Status: work in progress.** This is a learning project. I'm building it in layers to get hands-on experience with the core backend stack in Python: REST APIs, databases, authentication, containerization, testing, and deployment.

## How it works

```
┌────────────┐   HTTP POST    ┌───────────────┐         ┌──────────────┐
│   Agent    │ ─────────────> │ FastAPI (API) │ ──────> │  PostgreSQL  │
│ metrics.py │   /metrics     │               │         │   (planned)  │
└────────────┘                └───────────────┘         └──────────────┘
 runs on each server                  │
                                      └──> Telegram alerts (planned)
```

## Tech stack

| Area | Technologies |
|---|---|
| Language | Python 3 |
| Metrics collection | `psutil` |
| API | FastAPI, Pydantic (in progress) |
| Database | PostgreSQL, SQLAlchemy, Alembic (planned) |
| Infrastructure | Docker, Docker Compose, GitHub Actions (planned) |
| Testing | pytest (planned) |

## Roadmap

- [x] Agent collects CPU, RAM, and disk usage
- [ ] API accepts metrics from agents (`POST /metrics`)
- [ ] Metrics stored in PostgreSQL, endpoint for a server's latest data
- [ ] Authentication: user registration, a separate API key per agent
- [ ] One-command startup with Docker Compose
- [ ] Telegram alerts (server went silent, high load)
- [ ] Tests and CI
- [ ] Deployment to a VPS

## Getting started

Only the agent works at the moment.

```bash
git clone https://github.com/Asann1/server-monitor.git
cd server-monitor

python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Linux / macOS

pip install psutil
python metrics.py
```

Example output:

```
CPU: 12.4% | RAM: 61.0% | Disk: 47.3%
```

## Project structure

```
server-monitor/
├── metrics.py     # agent: metrics collection
├── README.md
└── .gitignore
```

## Design decisions

_This section will grow as the project does: which technologies I chose, why, and what went wrong along the way._

## Author

[Asann1](https://github.com/Asann1): learning backend development with Python. Related project: [tg-pc-control-bot](https://github.com/Asann1/tg-pc-control-bot), a Telegram bot for remote PC control.
