from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from app.models import Director, Genre, Movie


class DirectorService:
    """Data access layer for director queries."""

    def __init__(self, db: Session):
        self.db = db

    def list_directors(self) -> list[Director]:
        query = select(Director).order_by(Director.name)
        return list(self.db.scalars(query).all())

    def get_director(self, director_id: int) -> Director | None:
        query = (
            select(Director)
            .options(joinedload(Director.movies).joinedload(Movie.genres))
            .where(Director.id == director_id)
        )
        return self.db.scalars(query).unique().first()

    @staticmethod
    def unique_genres_for_director(director: Director) -> list[Genre]:
        """Collect distinct genres across all movies a director has made."""
        seen: set[int] = set()
        genres: list[Genre] = []
        for movie in director.movies:
            for genre in movie.genres:
                if genre.id not in seen:
                    seen.add(genre.id)
                    genres.append(genre)
        return sorted(genres, key=lambda g: g.name)
