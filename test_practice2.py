from http.client import responses

import requests
import pytest

API_KEY = "free_user_3CpmNnTbyuWO2t0wzu9fEBnuYtw"

@pytest.fixture
def api_url():
    return "https://reqres.in/api"

@pytest.fixture
def danniye():
    return {"x-api-key": API_KEY}

def test_users_two(api_url, danniye):
    response = requests.get(f"{api_url}/users/2", headers=danniye)
    assert response.status_code == 200
    body = response.json()

    assert body["data"]["id"] == 2

    assert "@" in body["data"]["email"]

    assert isinstance(body["data"]["first_name"], str)

def test_user_not_found(api_url, danniye):
    response = requests.get(f"{api_url}/users/999", headers=danniye)
    assert response.status_code == 404

    body = response.json()

    assert body == {}

def test_create_user(api_url, danniye):
    payload = {"name": "Khazar", "job": "QA Engineer"}
    response = requests.post(f"{api_url}/users", headers=danniye, json=payload)
    assert response.status_code == 201

    body = response.json()

    assert body["name"] == "Khazar"
    assert body ["job"] == "QA Engineer"
    assert "id" in body


def test_update_user(api_url, danniye):
    payload = {"name": "Khazar", "job": "Senior QA"}
    response = requests.put(f"{api_url}/users/2", headers=danniye, json=payload)
    assert response.status_code == 200

    body = response.json()
    assert body["name"] == "Khazar"
    assert body["job"] == "Senior QA"
    assert "updatedAt" in body

def test_delete_user(api_url, danniye):
    response = requests.delete(f"{api_url}/users/2", headers=danniye)
    assert response.status_code == 204
    assert response.text == ""



@pytest.mark.parametrize("user_id, expected_email", [
    (1, "george.bluth@reqres.in"),
    (2, "janet.weaver@reqres.in"),
    (3, "emma.wong@reqres.in"),
])
def test_get_user(api_url, danniye, user_id, expected_email):
    response = requests.get(f"{api_url}/users/{user_id}", headers=danniye)
    assert response.status_code == 200

    body = response.json()

    assert body["data"]["id"] == user_id
    assert body["data"]["email"] == expected_email

@pytest.mark.parametrize("name, job, expected_status", [
    ("Khazar", "QA Engineer", 201),
    ("Ali", "Developer", 201),
    ("Leyla", "Designer", 201),
])

def test_create_users(api_url, danniye, name, job, expected_status):
    payload = {"name": name, "job": job}
    response = requests.post(f"{api_url}/users", headers=danniye, json=payload)

    assert response.status_code == expected_status

    body = response.json()

    assert body ["name"] == name
    assert body ["job"] == job
    assert "id" in body

@pytest.mark.parametrize("user_id, name, job", [
    (1, "George", "Manager"),
    (2, "Janet", "Designer"),
    (3, "Emma", "Developer"),
])

def test_update_users(api_url, danniye, user_id, name, job):
    payload = {"name" : name, "job" : job}
    response = requests.put(f"{api_url}/users/{user_id}", headers=danniye, json=payload)
    assert response.status_code == 200

    body = response.json()

    assert body["name"] == name
    assert body["job"] == job
    assert "updatedAt" in body

@pytest.mark.parametrize("user_id, expected_status", [
    (1, 204),
    (2, 204),
    (3, 204),
])

def test_delete_users(api_url, danniye, user_id, expected_status):
    response = requests.delete(f"{api_url}/users/{user_id}", headers=danniye)
    assert response.status_code == expected_status
    assert response.text == ""

def test_users_list(api_url, danniye):
    response = requests.get(f"{api_url}/users", headers=danniye)
    assert response.status_code == 200
    body = response.json()
    assert body ["page"] == 1
    assert isinstance(body["data"], list)
    assert len(body["data"]) ==6

@pytest.mark.parametrize("email, password, expected_status", [
    ("eve.holt@reqres.in", "pistol", 200),
    ("eve.holt@reqres.in", "", 400),
    ("", "pistol", 400),
])
def test_register(api_url, danniye, email, password, expected_status):
    payload = {"email" : email, "password" : password}
    response = requests.post(f"{api_url}/register", headers=danniye, json=payload)

    assert response.status_code == expected_status
    if expected_status == 200:
        assert "token" in response.json()