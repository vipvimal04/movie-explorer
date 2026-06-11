from pydantic import BaseModel, ConfigDict, Field

from app.schemas.common import ActorBrief, DirectorBrief, GenreBrief, ReviewResponse


class MovieListItem(BaseModel):
    """Summary representation used in movie browse listings."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    release_year: int
    rating: float | None = None
    director: DirectorBrief
    genres: list[GenreBrief] = Field(default_factory=list)


class MovieDetail(BaseModel):
    """Full movie representation including cast and reviews."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    release_year: int
    description: str | None = None
    rating: float | None = None
    director: DirectorBrief
    genres: list[GenreBrief] = Field(default_factory=list)
    actors: list[ActorBrief] = Field(default_factory=list)
    reviews: list[ReviewResponse] = Field(default_factory=list)


class MovieListResponse(BaseModel):
    items: list[MovieListItem]
    total: int
    filters_applied: dict[str, str | int | None]
