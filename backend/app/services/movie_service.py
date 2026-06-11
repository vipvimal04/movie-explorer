from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from app.models import Actor, Director, Genre, Movie


class MovieService:
    """Data access layer for movie queries and filtering."""

    def __init__(self, db: Session):
        self.db = db

    def list_movies(
        self,
        genre: str | None = None,
        director: str | None = None,
        year: int | None = None,
        actor: str | None = None,
    ) -> tuple[list[Movie], dict[str, str | int | None]]:
        """Return movies matching optional filters along with applied filter metadata."""
        query = select(Movie).options(
            joinedload(Movie.director),
            joinedload(Movie.genres),
        )

        filters_applied: dict[str, str | int | None] = {
            "genre": genre,
            "director": director,
            "year": year,
            "actor": actor,
        }

        if genre:
            query = query.join(Movie.genres).where(Genre.name.ilike(f"%{genre}%"))

        if director:
            query = query.join(Movie.director).where(Director.name.ilike(f"%{director}%"))

        if year is not None:
            query = query.where(Movie.release_year == year)

        if actor:
            query = query.join(Movie.actors).where(Actor.name.ilike(f"%{actor}%"))

        query = query.order_by(Movie.release_year.desc(), Movie.title)
        movies = self.db.scalars(query).unique().all()
        return movies, filters_applied

    def get_movie(self, movie_id: int) -> Movie | None:
        """Fetch a single movie with related entities eagerly loaded."""
        query = (
            select(Movie)
            .options(
                joinedload(Movie.director),
                joinedload(Movie.genres),
                joinedload(Movie.actors),
                joinedload(Movie.reviews),
            )
            .where(Movie.id == movie_id)
        )
        return self.db.scalars(query).unique().first()
