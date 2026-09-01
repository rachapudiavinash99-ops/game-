def test_user_registration(client):
    response = client.post(
        "/api/v1/auth/register",
        json={
            "username": "new_player_99",
            "email": "new_player_99@test.com",
            "password": "SecurePassword123!",
            "display_name": "Player 99"
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "new_player_99"
    assert data["email"] == "new_player_99@test.com"


def test_duplicate_user_registration(client):
    response = client.post(
        "/api/v1/auth/register",
        json={
            "username": "admin",
            "email": "different_email@test.com",
            "password": "SecurePassword123!"
        }
    )
    assert response.status_code == 400


def test_user_login(client):
    response = client.post(
        "/api/v1/auth/login",
        json={"username": "admin", "password": "AdminPassword123!"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data
    assert data["username"] == "admin"
    assert data["role"] == "ADMIN"


def test_user_login_invalid_password(client):
    response = client.post(
        "/api/v1/auth/login",
        json={"username": "admin", "password": "WrongPassword!"}
    )
    assert response.status_code == 401


def test_get_current_user_profile(client, user_token):
    response = client.get(
        "/api/v1/auth/me",
        headers={"Authorization": f"Bearer {user_token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "alex_cyber"
    assert "profile" in data
