import requests


def auth(username=None, password=None):
    data = {
        'username': username,
        'password': password
    }
    response = requests.post('https://restful-booker.herokuapp.com/auth', data)
    return response
