def test_list_genres(client):
    response = client.get("/genres")
    assert response.status_code == 200
    data = response.json()
    assert data["total"] == 7
    names = {item["name"] for item in data["items"]}
    assert "Sci-Fi" in names
