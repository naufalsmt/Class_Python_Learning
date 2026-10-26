import pytest
import requests

@pytest.mark.parametrize(
    'post_id',
    [1, 2, 3],
    ids=[
        'first_post', 'second_post', 'third_post',
    ]
)

def test_positive_scenario(post_id):
    url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'
    response = requests.get(url, timeout=5)
    assert response.status_code == 200, \
        f'unexpected HTTP status for {post_id}'

    data = response.json()
    assert data['id'] == post_id, \
        f'expected post id is {post_id}, but got {data.get(id)}'
    assert data['title'] is not None, \
        f'post id {post_id} does not contain title'

def test_negative_scenario():
    url = 'https://jsonplaceholder.typicode.com/posts/99999'
    response = requests.get(url, timeout=5)
    assert response.status_code == 404, \
        f'expected 404, but got {response.status_code}'
