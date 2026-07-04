from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_health_endpoint():

    response = client.get('/health')

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

import uuid


def test_create_user():

    username = f"luffy-{uuid.uuid4().hex[:8]}"

    email = f"{uuid.uuid4().hex[:8]}@gmail.com"

    response = client.post(
        "/users/",
        json={
            "username": username,
            "email": email,
            "password": "gear5",
        },
    )

    assert response.status_code == 201

    body = response.json()

    assert body["username"] == username

    assert body["email"] == email

    assert body["is_active"] is True

def test_login():

    response = client.post(
        "/auth/login",
        json={
            "username": "Monkey D. Luffy",
            "password": "gear5",
        },
    )

    assert response.status_code == 200

    body = response.json()

    assert "access_token" in body

    assert body["token_type"] == "bearer"