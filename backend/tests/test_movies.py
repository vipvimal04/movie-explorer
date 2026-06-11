def test_list_movies_returns_seed_data(client):
    response = client.get("/movies")
    assert response.status_code == 200
    data = response.json()
    assert data["total"] == 5
    assert len(data["items"]) == 5
    assert data["items"][0]["title"]


def test_filter_movies_by_genre(client):
    response = client.get("/movies", params={"genre": "Sci-Fi"})
    assert response.status_code == 200
    data = response.json()
    assert data["total"] == 2
    titles = {item["title"] for item in data["items"]}
    assert titles == {"Inception", "Dune"}


def test_filter_movies_by_director(client):
    response = client.get("/movies", params={"director": "Christopher Nolan"})
    assert response.status_code == 200
    assert response.json()["total"] == 2


def test_filter_movies_by_year(client):
    response = client.get("/movies", params={"year": 1994})
    assert response.status_code == 200
    data = response.json()
    assert data["total"] == 1
    assert data["items"][0]["title"] == "Pulp Fiction"


def test_filter_movies_by_actor(client):
    response = client.get("/movies", params={"actor": "Leonardo DiCaprio"})
    assert response.status_code == 200
    assert response.json()["total"] == 1


def test_invalid_year_returns_400(client):
    response = client.get("/movies", params={"year": 1800})
    assert response.status_code == 400


def test_no_movies_for_filter(client):
    response = client.get("/movies", params={"genre": "Horror"})
    assert response.status_code == 200
    assert response.json()["total"] == 0


def test_get_movie_detail(client):
    list_response = client.get("/movies")
    movie_id = list_response.json()["items"][0]["id"]
    response = client.get(f"/movies/{movie_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["director"]["name"]
    assert len(data["actors"]) > 0
    assert len(data["reviews"]) > 0


def test_get_movie_not_found(client):
    response = client.get("/movies/9999")
    assert response.status_code == 404
