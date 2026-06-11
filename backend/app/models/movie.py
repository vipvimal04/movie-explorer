from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.associations import movie_actors, movie_genres

if TYPE_CHECKING:
    from app.models.actor import Actor
    from app.models.director import Director
    from app.models.genre import Genre
    from app.models.review import Review


class Movie(Base):
    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    release_year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str | None] = mapped_column(Text)
    rating: Mapped[float | None] = mapped_column(Float)
    director_id: Mapped[int] = mapped_column(ForeignKey("directors.id"), nullable=False)

    director: Mapped[Director] = relationship("Director", back_populates="movies")
    genres: Mapped[list[Genre]] = relationship(
        "Genre",
        secondary=movie_genres,
        back_populates="movies",
    )
    actors: Mapped[list[Actor]] = relationship(
        "Actor",
        secondary=movie_actors,
        back_populates="movies",
    )
    reviews: Mapped[list[Review]] = relationship(
        "Review",
        back_populates="movie",
        cascade="all, delete-orphan",
    )
