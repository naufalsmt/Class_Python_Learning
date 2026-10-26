import requests

def test_real_api_practice1():
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    req = requests.get(url, timeout=10)
    assert req.status_code == 200

    data = req.json()
    assert data['id'] == 1
    assert data['userId'] == 1
    assert data['title'] is not None
    assert data['body'] is not None

