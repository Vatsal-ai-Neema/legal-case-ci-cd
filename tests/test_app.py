from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_endpoint() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_about_endpoint() -> None:
    response = client.get("/about")

    assert response.status_code == 200
    assert response.json()["project"] == "Legal Case CI/CD App"
    assert response.json()["deployment_mode"] == "Self-hosted CD on laptop"


def test_users_endpoint_returns_seeded_data() -> None:
    response = client.get("/users")

    assert response.status_code == 200
    assert len(response.json()) >= 3


def test_cases_endpoint_returns_seeded_data() -> None:
    response = client.get("/cases")

    assert response.status_code == 200
    assert len(response.json()) >= 2


def test_create_case() -> None:
    payload = {
        "title": "Trademark Registration Review",
        "client_name": "Northwind Legal",
        "assigned_to": 2,
        "status": "open",
        "priority": "high",
        "hearing_date": "2026-05-10",
    }

    response = client.post("/cases", json=payload)

    assert response.status_code == 201
    assert response.json()["title"] == payload["title"]


def test_auth_login_success() -> None:
    response = client.post(
        "/auth/login",
        json={"username": "admin", "password": "admin123"},
    )

    assert response.status_code == 200
    assert response.json()["token"] == "demo-jwt-token"


def test_auth_login_failure() -> None:
    response = client.post(
        "/auth/login",
        json={"username": "user", "password": "wrong"},
    )

    assert response.status_code == 401
