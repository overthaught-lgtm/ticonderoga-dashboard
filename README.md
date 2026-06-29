# Ticonderoga Dashboard

A sleek, efficient Python API serving a dynamic dashboard frontend.

## Overview

This project combines a robust **Flask backend API** with a modern **frontend dashboard** to create a comprehensive monitoring and visualization platform.

## Project Structure

```
ticonderoga-dashboard/
├── api/                    # Backend API package
│   ├── __init__.py
│   ├── app.py             # Flask app factory
│   ├── routes/            # API route blueprints
│   │   ├── __init__.py
│   │   └── health.py      # Health check endpoints
│   └── models/            # Data models (future)
├── frontend/              # Frontend dashboard (future)
│   ├── public/
│   └── src/
├── tests/                 # Test suite
│   ├── __init__.py
│   ├── conftest.py        # Pytest fixtures
│   └── test_health.py
├── pyproject.toml         # Python project config (Poetry)
├── requirements.txt       # Locked dependencies
├── .github/
│   └── workflows/
│       └── ci.yml         # GitHub Actions CI/CD
└── README.md
```

## Getting Started

### Prerequisites
- Python 3.9+
- pip or Poetry

### Installation

**Option 1: Using pip**
```bash
pip install -r requirements.txt
```

**Option 2: Using Poetry**
```bash
poetry install
```

### Running the API

```bash
python -m flask --app api.app run
```

The API will start at `http://localhost:5000/`

### Health Check Endpoints

- `GET /api/health/` - Returns API status
- `GET /api/health/ping` - Simple ping endpoint

### Running Tests

```bash
pytest
```

With coverage:
```bash
pytest --cov=api
```

### Code Quality

**Lint with Ruff:**
```bash
ruff check .
```

**Format with Black:**
```bash
black .
```

**Type checking:**
```bash
mypy api
```

## CI/CD

This project uses GitHub Actions for continuous integration:
- Runs linting (Ruff) and formatting (Black) checks
- Executes test suite across Python 3.9, 3.10, 3.11
- Generates coverage reports
- Performs type checking with mypy

Check `.github/workflows/ci.yml` for details.

## Development Roadmap

- [ ] Dashboard frontend (React/Vue)
- [ ] Database integration (PostgreSQL/SQLite)
- [ ] Authentication & authorization
- [ ] API documentation (OpenAPI/Swagger)
- [ ] Container setup (Docker)
- [ ] Deployment pipeline

## License

MIT

## Author

overthaught-lgtm
