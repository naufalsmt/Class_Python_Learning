import requests

def test_post_request():
    url = 'https://jsonplaceholder.typicode.com/posts'
    payload = {
        "title": "QA automation test",
        "body": "Created using pytest",
        "userId": 1
    }

    response = requests.post(url, json=payload, timeout=5)
    assert response.status_code == 201, \
        f'response status is 201, but got {response.status_code}'

    data = response.json()
    assert data['title'] == payload['title']
    assert data['body'] == payload['body']
    assert data['userId'] == payload['userId']
    assert 'id' in data