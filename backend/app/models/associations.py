from sqlalchemy import Column, ForeignKey, Table

from app.database import Base

movie_genres = Table(
    "movie_genres",
    Base.metadata,
    Column("movie_id", ForeignKey("movies.id", ondelete="CASCADE"), primary_key=True),
    Column("genre_id", ForeignKey("genres.id", ondelete="CASCADE"), primary_key=True),
)

movie_actors = Table(
    "movie_actors",
    Base.metadata,
    Column("movie_id", ForeignKey("movies.id", ondelete="CASCADE"), primary_key=True),
    Column("actor_id", ForeignKey("actors.id", ondelete="CASCADE"), primary_key=True),
)
