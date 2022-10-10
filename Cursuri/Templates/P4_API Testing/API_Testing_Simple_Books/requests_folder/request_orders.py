import requests

from requests_folder.api_clients import get_token


def submit_order():
        token = get_token()
        header = {'Authorization': token}
        json = {"bookId": 3,
                "customerName": "John"}
        order = requests.post('https://simple-books-api.glitch.me/orders', headers=header, json=json)
        return order

def update_an_order():
    token = get_token()
    header = {'Authorization': token}
    data = {"customerName": "John Torp"}
    update = requests.patch(f'https://simple-books-api.glitch.me/orders/962GD8yfvoXccF42zNHdH',headers=header,json=data)
    return update