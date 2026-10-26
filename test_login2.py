def simulate_login(username, password):
    if username == 'admin' and password == '123':
        return {
            'status_code': 200,
            'message': 'success',
            'id': 1
        }
    return {
        'status_code': 401,
        'message': 'fail',
        'id': 'null'
    }

def test_login_pass():
    response = simulate_login('admin', '123')
    assert response['status_code'] == 200
    assert response['message'] == 'success'
    assert response['id'] == 1


def test_login_fail():
    response = simulate_login('admin1', '1243')
    assert response['status_code'] == 401
    assert response['message'] == 'fail'
    assert response['id'] == 'null'
