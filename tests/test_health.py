"""Tests for health check endpoints."""


def test_health_status(client):
    """Test the health status endpoint."""
    response = client.get("/api/health/")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "ok"
    assert data["version"] == "0.1.0"


def test_health_ping(client):
    """Test the ping endpoint."""
    response = client.get("/api/health/ping")
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "pong"


def test_404_not_found(client):
    """Test 404 error handling."""
    response = client.get("/api/nonexistent")
    assert response.status_code == 404
    data = response.get_json()
    assert "error" in data
