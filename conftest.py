import pytest

@pytest.fixture
def api_url():
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture
def sample_post():
    return {
        "title": "QA Test",
        "body": "My first post",
        "userId": 1
    }