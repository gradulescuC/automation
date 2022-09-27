from contact_list.requests.users import *


class TestLogin:

    user = 'andrei.sinpetrean@gmail.com'
    pswd = 'secretPass'

    def setup_method(self):
        self.response = login(self.user, self.pswd)

    def test_login_200(self):
        assert self.response.status_code == 200, 'status code is not ok'

    def test_login_info(self):
        assert self.response.json()['user']['firstName'] == 'Andy', 'firstName is not correct'
        assert self.response.json()['user']['lastName'] == 'Sinpetrean', 'lastName is not correct'
        assert self.response.json()['user']['email'] == 'andrei.sinpetrean@gmail.com', 'email is not correct'

    def test_login_401(self):
        r = login('invalid_user', 'invalidPass')
        assert r.status_code == 401, 'status code is not ok'





