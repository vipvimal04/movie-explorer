from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.controllers.actor_controller import ActorController
from app.database import get_db
from app.schemas.actor import ActorDetail, ActorListResponse

router = APIRouter(prefix="/actors", tags=["Actors"])


@router.get(
    "",
    response_model=ActorListResponse,
    summary="List actors with optional filters",
)
def list_actors(
    movie: str | None = Query(None, description="Filter by movie title"),
    genre: str | None = Query(None, description="Filter by genre name"),
    db: Session = Depends(get_db),
) -> ActorListResponse:
    return ActorController(db).list_actors(movie=movie, genre=genre)


@router.get(
    "/{actor_id}",
    response_model=ActorDetail,
    summary="Get actor profile",
    responses={404: {"description": "Actor not found"}},
)
def get_actor(actor_id: int, db: Session = Depends(get_db)) -> ActorDetail:
    return ActorController(db).get_actor(actor_id)
