from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from app.models import Actor, Genre, Movie


class ActorService:
    """Data access layer for actor queries and filtering."""

    def __init__(self, db: Session):
        self.db = db

    def list_actors(
        self,
        movie: str | None = None,
        genre: str | None = None,
    ) -> tuple[list[Actor], dict[str, str | int | None]]:
        """Return actors matching optional movie or genre filters."""
        query = select(Actor)

        filters_applied: dict[str, str | int | None] = {
            "movie": movie,
            "genre": genre,
        }

        if movie:
            query = query.join(Actor.movies).where(Movie.title.ilike(f"%{movie}%"))

        if genre:
            query = query.join(Actor.movies).join(Movie.genres).where(
                Genre.name.ilike(f"%{genre}%")
            )

        query = query.order_by(Actor.name)
        actors = self.db.scalars(query).unique().all()
        return actors, filters_applied

    def get_actor(self, actor_id: int) -> Actor | None:
        """Fetch a single actor with movies and derived genres."""
        query = (
            select(Actor)
            .options(joinedload(Actor.movies).joinedload(Movie.genres))
            .where(Actor.id == actor_id)
        )
        return self.db.scalars(query).unique().first()

    @staticmethod
    def unique_genres_for_actor(actor: Actor) -> list[Genre]:
        """Collect distinct genres across all movies an actor has appeared in."""
        seen: set[int] = set()
        genres: list[Genre] = []
        for movie in actor.movies:
            for genre in movie.genres:
                if genre.id not in seen:
                    seen.add(genre.id)
                    genres.append(genre)
        return sorted(genres, key=lambda g: g.name)
