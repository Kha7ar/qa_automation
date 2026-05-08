import requests
import pytest

API_KEY = "free_user_3CpmNnTbyuWO2t0wzu9fEBnuYtw"

@pytest.fixture
def api_url():
    return "https://reqres.in/api"

@pytest.fixture
def headers():
    return {"x-api-key": API_KEY}

@pytest.mark.parametrize("email, password, expected_status, has_token", [
    ("eve.holt@reqres.in", "cityslicka", 200, True),
    ("eve.holt@reqres.in", "", 400, False),
    ("", "cityslicka", 400, False),
])

def test_login(api_url,email, password, expected_status, headers, has_token):
  payload = {"email" : email, "password": password}
  response = requests.post(f"{api_url}/login", json=payload, headers=headers)

  print(f"\nStatus: {response.status_code}")
  print(f"Body: {response.json()}")

  assert response.status_code == expected_status

  if has_token:
    assert "token" in response.json()


