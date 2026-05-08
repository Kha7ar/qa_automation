import requests


def test_create_post(api_url, sample_post):
    response = requests.post(f"{api_url}/posts", json=sample_post)

    assert response.status_code == 201
    body = response.json()
    assert body["title"] == "QA Test"
    assert body["userId"] == 1


import pytest

@pytest.mark.parametrize("title, user_id, expected_status", [
    ("Valid Title", 1, 201),
    ("Another Post", 2, 201),
    ("Third Post", 3, 201),
])
def test_create_posts(api_url, title, user_id, expected_status):
    response = requests.post(f"{api_url}/posts", json={
        "title": title,
        "userId": user_id
    })
    assert response.status_code == expected_status
    assert response.json()["title"] == title