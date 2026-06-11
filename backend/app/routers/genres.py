from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.controllers.genre_controller import GenreController
from app.database import get_db
from app.schemas.genre import GenreListResponse

router = APIRouter(prefix="/genres", tags=["Genres"])


@router.get("", response_model=GenreListResponse, summary="List all genres")
def list_genres(db: Session = Depends(get_db)) -> GenreListResponse:
    return GenreController(db).list_genres()
