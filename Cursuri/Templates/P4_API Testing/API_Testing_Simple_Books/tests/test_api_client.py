from requests.api_clients import get_token


class TestApiClient:
    response = get_token()

    def test_login_200(self):
        assert self.response.status_code == 201, 'status code is not ok'

    def test_login_has_token_key(self):
        assert 'accessToken' in self.response.json().keys(), 'token key not present'

    def test_login_409(self):
        self.response = get_token()
        assert self.response.status_code == 409, 'status code is not ok'
        assert self.response.json()['error'] == 'API client already registered. Try a different email.', 'existing user msg not ok'

    def test_invalid_email(self):
        self.response = get_token()
        assert self.response.status_code == 400, 'status code is not ok'
        assert self.response.json()['error'] == 'Invalid or missing client email.', 'invalid email error msg is not ok'