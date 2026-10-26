import pytest
import requests

@pytest.fixture
def base_payload():
    return {
        "title": "QA automation test",
        "body": "Testing API with pytest",
        "userId": 1
    }


def test_post_api(base_payload):
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.post(url, json=base_payload, timeout=5)
    assert response.status_code == 201, \
        f'expected 201, got {response.status_code}'

    data = response.json()
    assert data['title'] == base_payload['title']
    assert data['body'] == base_payload['body']
    assert data['userId'] == base_payload['userId']