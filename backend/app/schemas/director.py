from pydantic import BaseModel, ConfigDict, Field

from app.schemas.common import GenreBrief


class DirectorMovieBrief(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    release_year: int
    rating: float | None = None


class DirectorListItem(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    birth_year: int | None = None


class DirectorDetail(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    bio: str | None = None
    birth_year: int | None = None
    movies: list[DirectorMovieBrief] = Field(default_factory=list)
    genres: list[GenreBrief] = Field(default_factory=list)


class DirectorListResponse(BaseModel):
    items: list[DirectorListItem]
    total: int
