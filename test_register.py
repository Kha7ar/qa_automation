from wsgiref.validate import header_re

import requests
import pytest

@pytest.fixture
def api_url():
    return "https://reqres.in/api"

@pytest.mark.parametrize("email, password, expected_status", [
    ("eve.holt@reqres.in", "pistol", 200),
    ("eve.holt@reqres.in", "", 400),
    ("", "pistol", 400),
])

def test_register(api_url, email, password, expected_status):
    headers = {"x-api-key": "free_user_3CpmNnTbyuWO2t0wzu9fEBnuYtw"}
    payload = {"email" : email, "password": password}
    response = requests.post(f"{api_url}/register", json=payload, headers=headers)
    assert response.status_code == expected_status
    if expected_status == 200:
        assert "token" in response.json()


