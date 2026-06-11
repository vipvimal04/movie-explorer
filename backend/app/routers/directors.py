from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.controllers.director_controller import DirectorController
from app.database import get_db
from app.schemas.director import DirectorDetail, DirectorListResponse

router = APIRouter(prefix="/directors", tags=["Directors"])


@router.get("", response_model=DirectorListResponse, summary="List all directors")
def list_directors(db: Session = Depends(get_db)) -> DirectorListResponse:
    return DirectorController(db).list_directors()


@router.get(
    "/{director_id}",
    response_model=DirectorDetail,
    summary="Get director profile",
    responses={404: {"description": "Director not found"}},
)
def get_director(director_id: int, db: Session = Depends(get_db)) -> DirectorDetail:
    return DirectorController(db).get_director(director_id)
