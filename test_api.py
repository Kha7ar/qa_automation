import requests

api_url = "https://jsonplaceholder.typicode.com"


def test_get_posts():
    response = requests.get(f"{api_url}/posts")

    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 2

    body = response.json()
    assert isinstance(body, list)
    assert len(body) == 100


def test_get_single_post():
    response = requests.get(f"{api_url}/posts/1")

    assert response.status_code == 200

    body = response.json()
    assert body["id"] == 1
    assert isinstance(body["title"], str)
    assert body["userId"] == 1


def test_create_post():
    new_post = {
        "title": "QA Test",
        "body": "My first post",
        "userId": 1
    }

    response = requests.post(f"{api_url}/posts", json=new_post)

    assert response.status_code == 201

    body = response.json()
    assert body["title"] == "QA Test"
    assert body["userId"] == 1
    assert isinstance(body["id"], int)


def test_update_post():
    updated_post = {
        "title": "Updated Title",
        "body": "Updated body",
        "userId": 1
    }

    response = requests.put(f"{api_url}/posts/1", json=updated_post)

    assert response.status_code == 200

    body = response.json()
    assert body["title"] == "Updated Title"


def test_delete_post():
    response = requests.delete(f"{api_url}/posts/1")

    assert response.status_code == 200


def test_post_not_found():
    response = requests.get(f"{api_url}/posts/999")

    assert response.status_code == 404