import requests
from requests.structures import CaseInsensitiveDict


def add_order(token, bookId, customerName):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {token}"
    json = {
        'bookId': bookId,
        'customerName': customerName
    }
    response = requests.post(f'https://simple-books-api.glitch.me/orders', headers=headers, json=json)
    return response


def delete_order(token, id):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {token}"
    response = requests.delete(f'https://simple-books-api.glitch.me/orders/{id}', headers=headers)
    return response


def get_orders(token):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {token}"
    response = requests.get(f'https://simple-books-api.glitch.me/orders/', headers=headers)
    return response


def get_order(token, id):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {token}"
    response = requests.get(f'https://simple-books-api.glitch.me/orders/{id}', headers=headers)
    return response


def edit_order(token, id, customerName):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {token}"
    json = {
        'customerName': customerName
    }
    response = requests.patch(f'https://simple-books-api.glitch.me/orders/{id}', headers=headers, json=json)
    return response