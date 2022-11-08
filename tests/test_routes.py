def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet_returns_json(client, two_planets):
    response = client.get("planets/1")
    response_body = response.get_json()
    
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Mars",
        "description": "Red Planet",
        "num_moon": 2
    } 

def test_get_one_planet_empty_db_return_404(client):
    response = client.get("planets/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert "msg" in response_body
