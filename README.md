# FastAPI Task Manager

**REST API на FastAPI + PostgreSQL + Docker**

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.112-009688?logo=fastapi)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## Описание

Полнофункциональный REST API для управления задачами:
- CRUD операции над задачами
- JWT аутентификация
- PostgreSQL + SQLAlchemy 2.0
- Alembic миграции
- Redis кэш

---

## Быстрый старт
`ash
git clone https://github.com/Shamanchi/fastapi-task-manager
cd fastapi-task-manager
cp .env.example .env
docker-compose up -d
`

### Переменные окружения
| Переменная | Описание |
|------------|----------|
| DATABASE_URL | PostgreSQL URL |
| SECRET_KEY | JWT секрет |
| ALGORITHM | JWT алгоритм |
| ACCESS_TOKEN_EXPIRE_MINUTES | TTL токена |

---

## API Endpoints
| Метод | Путь | Описание |
|-------|------|----------|
| GET | /api/v1/tasks | Список задач |
| POST | /api/v1/tasks | Создать задачу |
| GET | /health | Health check |

---

## Тесты
`ash
pytest -v
`

---

## Docker
`ash
docker build -t fastapi-task-manager .
docker-compose up -d
`

---

## Структура
`
├── app/
│   ├── api/routes.py
│   ├── core/config.py
│   ├── core/logging.py
│   ├── services/database.py
│   └── main.py
├── tests/test_api.py
├── .github/workflows/ci.yml
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
`

---

## CI/CD
GitHub Actions: Ruff, MyPy, Pytest, Docker build

---

## Лицензия
MIT

---

> Источник темы: Каталог портфолио, запись fastapi-task-manager