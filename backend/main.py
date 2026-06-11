import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from app.config import settings
from app.database import Base, SessionLocal, engine
from app.routers import actors_router, directors_router, genres_router, movies_router
from app.seed import seed_database

app = FastAPI(
    title="Movie Explorer API",
    description="Explore movies, actors, directors, and genres.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(movies_router)
app.include_router(actors_router)
app.include_router(directors_router)
app.include_router(genres_router)


def setup_database() -> None:
    """Create tables and add sample data if the database is empty."""
    Base.metadata.create_all(bind=engine)
    with SessionLocal() as db:
        seed_database(db)


# Skip this when running tests — tests use their own sqlite database.
if os.getenv("SKIP_DB_SETUP") != "1":
    setup_database()
