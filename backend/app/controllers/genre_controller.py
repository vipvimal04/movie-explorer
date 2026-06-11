from sqlalchemy.orm import Session

from app.schemas.genre import GenreListResponse, GenreResponse
from app.services.genre_service import GenreService


class GenreController:
    """Orchestrates genre-related request handling."""

    def __init__(self, db: Session):
        self.service = GenreService(db)

    def list_genres(self) -> GenreListResponse:
        genres = self.service.list_genres()
        return GenreListResponse(
            items=[GenreResponse.model_validate(genre) for genre in genres],
            total=len(genres),
        )
