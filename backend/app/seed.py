"""Seed the database with sample movies, cast, and reviews."""

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Actor, Director, Genre, Movie, Review


def seed_database(db: Session) -> None:
    if db.scalar(select(Movie).limit(1)):
        return

    genres = {
        name: Genre(name=name)
        for name in ["Action", "Drama", "Sci-Fi", "Crime", "Romance", "Thriller", "Comedy"]
    }
    db.add_all(genres.values())

    directors = {
        "Christopher Nolan": Director(
            name="Christopher Nolan",
            bio="British-American filmmaker known for complex narratives.",
            birth_year=1970,
        ),
        "Quentin Tarantino": Director(
            name="Quentin Tarantino",
            bio="American director known for nonlinear storytelling.",
            birth_year=1963,
        ),
        "Steven Spielberg": Director(
            name="Steven Spielberg",
            bio="Legendary director behind iconic blockbusters.",
            birth_year=1946,
        ),
        "Denis Villeneuve": Director(
            name="Denis Villeneuve",
            bio="Canadian filmmaker acclaimed for atmospheric sci-fi.",
            birth_year=1967,
        ),
    }
    db.add_all(directors.values())

    actors = {
        "Leonardo DiCaprio": Actor(name="Leonardo DiCaprio", birth_year=1974),
        "Marion Cotillard": Actor(name="Marion Cotillard", birth_year=1975),
        "Tom Hardy": Actor(name="Tom Hardy", birth_year=1977),
        "Christian Bale": Actor(name="Christian Bale", birth_year=1974),
        "Heath Ledger": Actor(name="Heath Ledger", birth_year=1979),
        "Uma Thurman": Actor(name="Uma Thurman", birth_year=1970),
        "John Travolta": Actor(name="John Travolta", birth_year=1954),
        "Harrison Ford": Actor(name="Harrison Ford", birth_year=1942),
        "Timothée Chalamet": Actor(name="Timothée Chalamet", birth_year=1995),
        "Zendaya": Actor(name="Zendaya", birth_year=1996),
    }
    db.add_all(actors.values())
    db.flush()

    movies_data = [
        {
            "title": "Inception",
            "release_year": 2010,
            "description": "A thief enters dreams to steal secrets from the subconscious.",
            "rating": 8.8,
            "director": directors["Christopher Nolan"],
            "genres": [genres["Action"], genres["Sci-Fi"], genres["Thriller"]],
            "actors": [
                actors["Leonardo DiCaprio"],
                actors["Marion Cotillard"],
                actors["Tom Hardy"],
            ],
            "reviews": [
                ("Alex", 9.0, "Mind-bending and visually stunning."),
                ("Jordan", 8.5, "Complex but rewarding on repeat viewings."),
            ],
        },
        {
            "title": "The Dark Knight",
            "release_year": 2008,
            "description": "Batman faces the Joker in Gotham City.",
            "rating": 9.0,
            "director": directors["Christopher Nolan"],
            "genres": [genres["Action"], genres["Drama"], genres["Crime"]],
            "actors": [actors["Christian Bale"], actors["Heath Ledger"]],
            "reviews": [
                ("Sam", 9.5, "Heath Ledger's performance is unforgettable."),
            ],
        },
        {
            "title": "Pulp Fiction",
            "release_year": 1994,
            "description": "Interwoven stories of crime in Los Angeles.",
            "rating": 8.9,
            "director": directors["Quentin Tarantino"],
            "genres": [genres["Crime"], genres["Drama"]],
            "actors": [actors["Uma Thurman"], actors["John Travolta"]],
            "reviews": [
                ("Riley", 9.0, "Iconic dialogue and structure."),
            ],
        },
        {
            "title": "Raiders of the Lost Ark",
            "release_year": 1981,
            "description": "Archaeologist Indiana Jones races to find the Ark of the Covenant.",
            "rating": 8.4,
            "director": directors["Steven Spielberg"],
            "genres": [genres["Action"], genres["Thriller"]],
            "actors": [actors["Harrison Ford"]],
            "reviews": [
                ("Casey", 8.0, "The gold standard for adventure films."),
            ],
        },
        {
            "title": "Dune",
            "release_year": 2021,
            "description": "Paul Atreides leads a rebellion on the desert planet Arrakis.",
            "rating": 8.0,
            "director": directors["Denis Villeneuve"],
            "genres": [genres["Sci-Fi"], genres["Drama"], genres["Action"]],
            "actors": [actors["Timothée Chalamet"], actors["Zendaya"]],
            "reviews": [
                ("Morgan", 8.2, "Epic scale with gorgeous cinematography."),
                ("Taylor", 7.8, "Slow burn but immersive world-building."),
            ],
        },
    ]

    for data in movies_data:
        movie = Movie(
            title=data["title"],
            release_year=data["release_year"],
            description=data["description"],
            rating=data["rating"],
            director=data["director"],
            genres=data["genres"],
            actors=data["actors"],
        )
        db.add(movie)
        db.flush()
        for author, rating, comment in data["reviews"]:
            db.add(Review(movie_id=movie.id, author=author, rating=rating, comment=comment))

    db.commit()
