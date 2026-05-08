from http.client import responses

import requests
import pytest

API_KEY = "free_user_3CpmNnTbyuWO2t0wzu9fEBnuYtw"

@pytest.fixture
def api_url():
    return "https://reqres.in/api"

@pytest.fixture
def headers():
    return {"x-api-key": API_KEY}

@pytest.mark.parametrize("page, expected_per_page", [
    (1, 6),
    (2, 6),
])

def test_get_users_pagination(api_url, headers, page, expected_per_page):
    payload = {"page": page}
    response = requests.get(f"{api_url}/users", headers=headers, params=payload)

    assert response.status_code == 200

    body = response.json()

    assert body["per_page"] == expected_per_page
    assert isinstance(body["data"], list)