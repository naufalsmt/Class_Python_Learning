import pytest

def login_simulate(username, password):
    if username == 'admin' and password == 'pass123':
        return {
        'status_code': 200,
        'message': 'success'
        }
    return{
        'status_code': 401,
        'message': 'fail'
    }

@pytest.mark.parametrize(
    'username, password, exp_status',
    [
        ('admin', 'pass123', 200),
        ('wrong', 'pass123', 401),
        ('admin', 'pass13', 401),
        ('wrong', 'pass13', 401)
    ]
)
def test_success_login(username, password, exp_status):
    response = login_simulate(username, password)
    assert response['status_code'] == exp_status
