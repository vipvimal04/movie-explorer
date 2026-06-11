from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.common import GenreBrief
from app.schemas.director import DirectorDetail, DirectorListItem, DirectorListResponse
from app.services.director_service import DirectorService


class DirectorController:
    """Orchestrates director-related request handling."""

    def __init__(self, db: Session):
        self.service = DirectorService(db)

    def list_directors(self) -> DirectorListResponse:
        directors = self.service.list_directors()
        return DirectorListResponse(
            items=[DirectorListItem.model_validate(director) for director in directors],
            total=len(directors),
        )

    def get_director(self, director_id: int) -> DirectorDetail:
        director = self.service.get_director(director_id)
        if director is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Director with id {director_id} not found.",
            )

        detail = DirectorDetail.model_validate(director)
        detail.genres = [
            GenreBrief.model_validate(genre)
            for genre in self.service.unique_genres_for_director(director)
        ]
        return detail
