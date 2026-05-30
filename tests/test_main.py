from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_health_returns_200() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_get_students_returns_list() -> None:
    response = client.get("/students")

    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "name": "Yangzoom Lama"},
        {"id": 2, "name": "John Doe"},
        {"id": 3, "name": "lily Jones"},
    ]