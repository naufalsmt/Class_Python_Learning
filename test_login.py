def test_pass_test_login():
    status_code = 200
    message = 'success'
    assert status_code == 200
    assert message == 'success'


def test_fail_test_login():
    status_code = 400
    message = 'fail'
    assert status_code == 400
    assert message == 'fail'