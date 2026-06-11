from app.routers.actors import router as actors_router
from app.routers.directors import router as directors_router
from app.routers.genres import router as genres_router
from app.routers.movies import router as movies_router

__all__ = ["actors_router", "directors_router", "genres_router", "movies_router"]
