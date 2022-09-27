from books.requests.api_clients import *
from random import randint

class TestApiClient:

    nr = randint(1, 9999999)
    clientName = 'Marin'
    clientEmail = f'valid_email{nr}@email.com'
    response = login(clientName, clientEmail)

    def test_login_200(self):
        assert self.response.status_code == 201, 'status code is not ok'

    def test_login_has_token_key(self):
        assert 'accessToken' in self.response.json().keys(), 'token key not present'

    def test_login_409(self):
        self.response = login(self.clientName, self.clientEmail)
        assert self.response.status_code == 409, 'status code is not ok'
        assert self.response.json()['error'] == 'API client already registered. Try a different email.', 'existing user msg not ok'

    def test_invalid_email(self):
        self.response = login('andy', 'abc')
        assert self.response.status_code == 400, 'status code is not ok'
        assert self.response.json()['error'] == 'Invalid or missing client email.', 'invalid email error msg is not ok'