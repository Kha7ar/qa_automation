import requests
import pytest

API_KEY = "free_user_3CpmNnTbyuWO2t0wzu9fEBnuYtw"

@pytest.fixture
def api_url():
    return "https://reqres.in/api"

@pytest.fixture
def mojno_i_ne_headers():
    return {"x-api-key": API_KEY}

def test_get_user(api_url, mojno_i_ne_headers):
    response= requests.get(f"{api_url}/users", headers=mojno_i_ne_headers)
    assert response.status_code == 200
    assert response.elapsed.total_seconds() <=2
