def test_list_actors(client):
    response = client.get("/actors")
    assert response.status_code == 200
    assert response.json()["total"] == 10


def test_filter_actors_by_movie(client):
    response = client.get("/actors", params={"movie": "Inception"})
    assert response.status_code == 200
    assert response.json()["total"] == 3


def test_filter_actors_by_genre(client):
    response = client.get("/actors", params={"genre": "Crime"})
    assert response.status_code == 200
    assert response.json()["total"] >= 2


def test_get_actor_profile(client):
    response = client.get("/actors")
    actor_id = response.json()["items"][0]["id"]
    detail = client.get(f"/actors/{actor_id}")
    assert detail.status_code == 200
    data = detail.json()
    assert "movies" in data
    assert "genres" in data


def test_get_actor_not_found(client):
    response = client.get("/actors/9999")
    assert response.status_code == 404
