import pytest

@pytest.mark.parametrize(
    'response, exp_status_code, exp_msg',
    [
        (
                {
                    'status': 200,
                    'message': 'success',
                    'transaction_id': 'TRX101',
                    'amount': 100
                },
            200,
            'success'
        ),
        (
                {
                    'status': 400,
                    'message': 'fail',
                    'transaction_id': None,
                    'amount': 0
                },
            400,
            'fail'
        )
    ],
    ids=[
        'success payment',
        'fail payment'
    ]
)
def test_payment_response(response, exp_status_code, exp_msg):
    assert response['status'] == exp_status_code, \
        "unexpected status code"
    assert response['message'] == exp_msg, \
        "unexpected message"
    if exp_msg == 'success':
        assert response['transaction_id'] is not None, \
        "unexpected transaction_id"