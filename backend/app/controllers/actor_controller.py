from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.actor import ActorDetail, ActorListItem, ActorListResponse
from app.schemas.common import GenreBrief
from app.services.actor_service import ActorService


class ActorController:

    def __init__(self, db: Session):
        self.service = ActorService(db)

    def list_actors(
        self,
        movie: str | None = None,
        genre: str | None = None,
    ) -> ActorListResponse:
        actors, filters_applied = self.service.list_actors(movie=movie, genre=genre)
        return ActorListResponse(
            items=[ActorListItem.model_validate(actor) for actor in actors],
            total=len(actors),
            filters_applied=filters_applied,
        )

    def get_actor(self, actor_id: int) -> ActorDetail:
        actor = self.service.get_actor(actor_id)
        if actor is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Actor with id {actor_id} not found.",
            )

        detail = ActorDetail.model_validate(actor)
        detail.genres = [
            GenreBrief.model_validate(genre)
            for genre in self.service.unique_genres_for_actor(actor)
        ]
        return detail
