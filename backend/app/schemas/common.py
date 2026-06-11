from pydantic import BaseModel, ConfigDict


class GenreBrief(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str


class DirectorBrief(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str


class ActorBrief(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str


class ReviewResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    author: str
    rating: float
    comment: str | None = None


class ErrorResponse(BaseModel):
    detail: str
