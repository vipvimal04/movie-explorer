def test_list_directors(client):
    response = client.get("/directors")
    assert response.status_code == 200
    assert response.json()["total"] == 4


def test_get_director_profile(client):
    response = client.get("/directors")
    director_id = response.json()["items"][0]["id"]
    detail = client.get(f"/directors/{director_id}")
    assert detail.status_code == 200
    data = detail.json()
    assert len(data["movies"]) > 0


def test_get_director_not_found(client):
    response = client.get("/directors/9999")
    assert response.status_code == 404
