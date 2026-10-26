class APIResponse:
    def __init__(self, status_code, message, id):
        self.status_code = status_code
        self.message = message
        self.id = id

    @property
    def status_code(self):
        return self.__status_code

    @status_code.setter
    def status_code(self, new_status_code):
        if 100 <= new_status_code <= 599:
            self.__status_code = new_status_code
        else:
            raise ValueError('Invalid status code')

    def get_response(self):
        return 100 < self.status_code <= 599


response = APIResponse(200, 'success', 10)
print(response.status_code)
print(response.message)
print(response.id)
print(response.get_response())

assert response.status_code == 200
assert response.message == 'success'
assert response.id == 10
assert response.get_response()

print("API passed successfully")
