from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Genre


class GenreService:
    """Data access layer for genre queries."""

    def __init__(self, db: Session):
        self.db = db

    def list_genres(self) -> list[Genre]:
        query = select(Genre).order_by(Genre.name)
        return list(self.db.scalars(query).all())
