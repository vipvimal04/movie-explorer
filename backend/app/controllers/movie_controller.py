from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.movie import MovieDetail, MovieListItem, MovieListResponse
from app.services.movie_service import MovieService


class MovieController:
    
    def __init__(self, db: Session):
        self.service = MovieService(db)

    def list_movies(
        self,
        genre: str | None = None,
        director: str | None = None,
        year: int | None = None,
        actor: str | None = None,
    ) -> MovieListResponse:
        if year is not None and (year < 1888 or year > 2100):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid release year. Must be between 1888 and 2100.",
            )

        movies, filters_applied = self.service.list_movies(
            genre=genre,
            director=director,
            year=year,
            actor=actor,
        )

        return MovieListResponse(
            items=[MovieListItem.model_validate(movie) for movie in movies],
            total=len(movies),
            filters_applied=filters_applied,
        )

    def get_movie(self, movie_id: int) -> MovieDetail:
        movie = self.service.get_movie(movie_id)
        if movie is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Movie with id {movie_id} not found.",
            )
        return MovieDetail.model_validate(movie)
