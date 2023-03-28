import random

import requests


def generate_token():
    nr = random.randint(1, 9999999999999999999999999999999999)
    request_body = {
        "clientName": f"Postman{nr}",
        "clientEmail": f"jessy{nr}@example.com"
    }
    make_request = requests.post('https://simple-books-api.glitch.me/api-clients/', json=request_body)
    token = make_request.json()['accessToken']

def submit_order(book_id, customer_name):
    request_body = {
            "bookId": book_id,
            "customerName": customer_name
    }
    token = generate_token()
    header_params = {'Authorization': token}
    make_request = requests.get('https://simple-books-api.glitch.me/orders', json=request_body, headers=header_params)
    return make_request

def test_submit_oder_invalid_error_msg():
        make_request = submit_order(1003, 'John')
        assert make_request.json()["error"] == 'Invalid or missing bookId'


