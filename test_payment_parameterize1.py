import pytest

def payment(amount):
    if amount <= 0:
        return {
            'status': 'failed',
            'statusCode': 400
        }
    return {
        'status': 'success',
        'statusCode': 200
    }

@pytest.mark.parametrize(
    'amount, exp_status, exp_code',
    [
        (100, 'success', 400),
        (0, 'failed', 400),
        (-100, 'failed', 400),
    ],
    ids=[
        'valid_payment',
        'zero_payment',
        'negative_payment'
    ]
)
def test_success(amount, exp_status, exp_code):
    response = payment(amount)
    assert response['statusCode'] == exp_code
    assert response['status'] == exp_status