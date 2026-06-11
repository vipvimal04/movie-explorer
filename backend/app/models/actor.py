from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.associations import movie_actors

if TYPE_CHECKING:
    from app.models.movie import Movie


class Actor(Base):
    __tablename__ = "actors"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    bio: Mapped[str | None] = mapped_column(Text)
    birth_year: Mapped[int | None] = mapped_column()

    movies: Mapped[list[Movie]] = relationship(
        "Movie",
        secondary=movie_actors,
        back_populates="actors",
    )
