import requests

BASE_URL = "http://127.0.0.1:5000"

def test_get_all_posts():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_single_post():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code in [200, 404]

def test_create_post():
    data = {
        "title": "Test Post"
    }
    response = requests.post(f"{BASE_URL}/posts",json=data)
    assert response.status_code == 201
    assert response.json()["title"] == data["title"]

def test_create_post_no_title():
    response = requests.post(f"{BASE_URL}/posts",json={})
    assert response.status_code == 400
    assert "error" in response.json()
