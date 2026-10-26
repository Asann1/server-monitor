# server-monitor

Сервис мониторинга серверов: лёгкий агент собирает метрики (CPU, RAM, диск) и отправляет их на backend, который хранит данные, отдаёт их через API и уведомляет, если что-то пошло не так.

> **Статус: в активной разработке.** Проект учебный. Я строю его по слоям, чтобы на практике освоить стек backend-разработки на Python: REST API, базы данных, авторизацию, контейнеризацию, тесты и деплой.

## Как это работает

```
┌────────────┐   HTTP POST    ┌───────────────┐         ┌──────────────┐
│   Agent    │ ─────────────> │ FastAPI (API) │ ──────> │  PostgreSQL  │
│ metrics.py │   /metrics     │               │         │  (в планах)  │
└────────────┘                └───────────────┘         └──────────────┘
 на каждом сервере                    │
                                      └──> Telegram-алерты (в планах)
```

## Стек

| Область | Технологии |
|---|---|
| Язык | Python 3 |
| Сбор метрик | `psutil` |
| API | FastAPI, Pydantic (в работе) |
| База данных | PostgreSQL, SQLAlchemy, Alembic (в планах) |
| Инфраструктура | Docker, Docker Compose, GitHub Actions (в планах) |
| Тесты | pytest (в планах) |

## Возможности

- [x] Агент собирает CPU, RAM и использование диска
- [ ] API принимает метрики от агентов (`POST /metrics`)
- [ ] Хранение метрик в PostgreSQL, эндпоинт с последними данными сервера
- [ ] Авторизация: регистрация пользователей, API-ключ на каждого агента
- [ ] Запуск одной командой через Docker Compose
- [ ] Алерты в Telegram (сервер молчит, высокая нагрузка)
- [ ] Тесты и CI
- [ ] Деплой на VPS

## Запуск

Сейчас работает только агент.

```bash
git clone https://github.com/Asann1/server-monitor.git
cd server-monitor

python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Linux / macOS

pip install psutil
python metrics.py
```

Пример вывода:

```
CPU: 12.4% | RAM: 61.0% | Disk: 47.3%
```

## Структура проекта

```
server-monitor/
├── metrics.py     # агент: сбор метрик
├── README.md
└── .gitignore
```

## Принятые решения

_Раздел будет пополняться по мере разработки: какие технологии выбраны, почему и что пошло не так._

## Автор

[Asann1](https://github.com/Asann1) — осваиваю backend-разработку на Python. Смежный проект: [tg-pc-control-bot](https://github.com/Asann1/tg-pc-control-bot) — Telegram-бот для удалённого управления ПК.
