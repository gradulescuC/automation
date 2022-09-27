import requests


def login(email=None, password=None):
    json = {
        'email': email,
        'password': password
    }
    response = requests.post('https://thinking-tester-contact-list.herokuapp.com/users/login', json=json)
    return response


def get_token():
    json = {
        'email': 'andrei.sinpetrean@gmail.com',
        'password': 'secretPass'
    }
    response = requests.post('https://thinking-tester-contact-list.herokuapp.com/users/login', json=json)
    return response.json()['token']
