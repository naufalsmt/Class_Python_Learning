import pytest
import requests


@pytest.fixture
def base_url():
    return 'https://jsonplaceholder.typicode.com/'


def test_get_posts(base_url):
    url = f'{base_url}/posts/1'
    response = requests.get(url)
    assert response.status_code == 200, \
        f'expected 200, but got {response.status_code}'

    data = response.json()
    assert data['id'] == 1
    assert data['title'] != ''


def test_get_users(base_url):
    url = f'{base_url}/users/1'
    response = requests.get(url)
    assert response.status_code == 200, \
        f'expected 200, but got {response.status_code}'

    data = response.json()
    assert data['id'] == 1
    assert data['name'] != ''