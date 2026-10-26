def test_payment():
    response = {
        'status_code' : 200,
        'message' : 'success',
        'transaction_id' : 'TRX101',
        # 'transaction_id' : None,
        'amount' : 100
    }

    assert response['message'] == 'success'
    assert response['transaction_id'] is not None
    assert response['amount'] == 100
    assert response['status_code'] == 200
