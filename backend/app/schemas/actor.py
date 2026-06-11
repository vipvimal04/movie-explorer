from pydantic import BaseModel, ConfigDict, Field

from app.schemas.common import GenreBrief


class ActorMovieBrief(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    release_year: int
    rating: float | None = None


class ActorListItem(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    birth_year: int | None = None


class ActorDetail(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    bio: str | None = None
    birth_year: int | None = None
    movies: list[ActorMovieBrief] = Field(default_factory=list)
    genres: list[GenreBrief] = Field(default_factory=list)


class ActorListResponse(BaseModel):
    items: list[ActorListItem]
    total: int
    filters_applied: dict[str, str | int | None]
