import requests
from random import randint

def get_token():
    nr = randint(1, 9999999)
    json = {
        'clientName': 'Marin',
        'clientEmail': f'valid_email{nr}@email.com'
    }
    response = requests.post('https://simple-books-api.glitch.me/api-clients/', json=json)
    return response.json()['accessToken']