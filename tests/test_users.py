import pytest
from app.schemas import *
from jose import jwt
from app.config import settings

# def test_root(client):
#     res = client.get("/")
#     assert res.json().get('message') == "Hello World, this the changed i made"
#     assert res.status_code == 200


def test_create_user(client):
    res = client.post("/users/", json={"email": "parham@gmail.com", "password": "password123"})
    new_user = ResponsedUser(**res.json())
    assert new_user.email == "parham@gmail.com"
    assert res.status_code == 201

def test_login_user(test_user, client):
    res = client.post("/login", data={"username": test_user['email'], "password": test_user['password']})
    login_res = Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get("user_id")
    assert id == test_user['id']
    assert login_res.token_type == "bearer"
    assert res.status_code == 200

@pytest.mark.parametrize("email, password, status_code", [
    ('wrongEmail@gmail.com', 'password123', 403),
    ('parham@gmail.com', 'wrongPassword', 403),
    ('wrongGmail@Gmail.com', 'wrongpassword', 403),
    (None, 'password123', 422),
    ('parham@gmail.com', None, 422)
])
def test_incorrect_login(test_user, client, email, password, status_code):
    res = client.post("/login", data={"username": email, "password": password})
    assert res.status_code == status_code
    # assert res.json().get('detail') == "Invalid credentials"