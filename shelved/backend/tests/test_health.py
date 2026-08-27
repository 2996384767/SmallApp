def test_health(client):
    response = client.get("/api/v1/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_database_health(client):
    response = client.get("/api/v1/health/database")

    assert response.status_code == 200
    assert response.get_json() == {"database": "connected", "status": "ok"}
