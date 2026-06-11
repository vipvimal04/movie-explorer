from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.controllers.movie_controller import MovieController
from app.database import get_db
from app.schemas.movie import MovieDetail, MovieListResponse

router = APIRouter(prefix="/movies", tags=["Movies"])


@router.get(
    "",
    response_model=MovieListResponse,
    summary="List movies with optional filters",
    responses={
        400: {"description": "Invalid filter value (e.g. release year out of range)"},
    },
)
def list_movies(
    genre: str | None = Query(None, description="Filter by genre name (case-insensitive)"),
    director: str | None = Query(None, description="Filter by director name"),
    year: int | None = Query(None, description="Filter by release year"),
    actor: str | None = Query(None, description="Filter by actor name"),
    db: Session = Depends(get_db),
) -> MovieListResponse:
    return MovieController(db).list_movies(
        genre=genre,
        director=director,
        year=year,
        actor=actor,
    )


@router.get(
    "/{movie_id}",
    response_model=MovieDetail,
    summary="Get movie details",
    responses={404: {"description": "Movie not found"}},
)
def get_movie(movie_id: int, db: Session = Depends(get_db)) -> MovieDetail:
    return MovieController(db).get_movie(movie_id)
