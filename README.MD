# Movie Explorer

A full-stack platform for exploring movies, actors, directors, and genres. Built with **FastAPI** (Python) and **Vue 3** (TypeScript + Vite + Tailwind CSS), fully dockerized.

## Features

- Browse movies with title, release year, genres, director, and rating
- Filter movies by genre, director, release year, or actor (server-side)
- Movie detail pages with cast, director, genres, and reviews
- Actor and director profile pages with filmography
- Watch Later list stored in browser local storage (no auth required)
- OpenAPI/Swagger docs at `/docs`
- Linting and unit tests run during Docker builds


```
backend/
  app/
    routers/       # HTTP routes and query params
    controllers/   # Request orchestration and validation
    services/      # Database queries and business logic
    models/        # SQLAlchemy ORM models
    schemas/       # Pydantic request/response DTOs
```

### Frontend (Vue 3 + Vite)

```
frontend/
  src/
    api/           # API client
    components/    # Reusable UI components
    views/         # Route-level pages
    composables/   # Shared logic (favorites)
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/movies` | List movies (`genre`, `director`, `year`, `actor` filters) |
| GET | `/movies/{id}` | Movie details |
| GET | `/actors` | List actors (`movie`, `genre` filters) |
| GET | `/actors/{id}` | Actor profile |
| GET | `/directors` | List directors |
| GET | `/directors/{id}` | Director profile |
| GET | `/genres` | List genres |
| GET | `/health` | Health check |
| GET | `/docs` | Swagger UI |


## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) and Docker Compose

## Quick Start (Docker)

```bash
# Build and start all services (db, backend, frontend)
docker compose up --build

# Run in background
docker compose up --build -d
```

| Service | URL |
|---------|-----|
| Frontend | http://localhost:3000 |
| Backend API | http://localhost:8000 |
| Swagger docs | http://localhost:8000/docs |
| PostgreSQL | localhost:5432 |

Stop services:

```bash
docker compose down
```

Remove database volume:

```bash
docker compose down -v
```

## Local Development (without Docker)

### Backend

```bash
cd backend
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Start PostgreSQL (or use docker compose up db)
export DATABASE_URL=postgresql://movieuser:moviepass@localhost:5432/moviedb
export CORS_ORIGINS=http://localhost:5173

uvicorn main:app --reload
```

Run tests and lint:

```bash
ruff check .
pytest
```

### Frontend

```bash
cd frontend
npm install
export VITE_API_URL=http://localhost:8000
npm run dev
```

Run tests and lint:

```bash
npm run lint
npm run test
npm run build
```

## Testing

- **Backend**: pytest with SQLite in-memory DB (18 tests covering filters, profiles, and edge cases)
- **Frontend**: Vitest unit tests for favorites composable and movie card component

Both are executed automatically during `docker compose build`.

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | FastAPI, SQLAlchemy, PostgreSQL, Pydantic |
| Frontend | Vue 3, TypeScript, Vite, Tailwind CSS, Vue Router |
| Tooling | Ruff, ESLint, pytest, Vitest |
| Infrastructure | Docker, Docker Compose, Nginx |

## Sample Data

On first startup the backend seeds 5 movies, 10 actors, 4 directors, 7 genres, and sample reviews.
