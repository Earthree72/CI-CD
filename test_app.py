import pytest
from main import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SECRET_KEY"] = "test-secret"
    with app.test_client() as client:
        with client.session_transaction() as sess:
            sess.clear()  # Clear session before each test
        yield client

# ---------------------------
# TEST LOGIN FUNCTION
# ---------------------------

def test_login_success(client):
    response = client.post("/login", json={
        "username": "admin",
        "password": "password123"
    })
    assert response.status_code == 200
    assert response.get_json() == {"message": "Login successful"}

def test_login_fail(client):
    response = client.post("/login", json={
        "username": "admin",
        "password": "wrongpass"
    })
    assert response.status_code == 401
    assert response.get_json() == {"error": "Invalid credentials"}

# ---------------------------
# TEST SUBTRACT FUNCTION
# ---------------------------

def test_subtract_without_login(client):
    response = client.get("/subtract/10/3")
    assert response.status_code == 401
    assert "Unauthorized" in response.get_json()["error"]

def test_subtract_with_login(client):
    # First log in
    client.post("/login", json={
        "username": "admin",
        "password": "password123"
    })

    # Now subtract
    response = client.get("/subtract/10/3")
    assert response.status_code == 200
    assert response.get_json() == {"result": 7}
