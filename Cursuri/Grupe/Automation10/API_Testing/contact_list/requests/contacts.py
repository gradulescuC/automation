import requests
from requests.structures import CaseInsensitiveDict


def get_contacts(token):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {token}"
    response = requests.get('https://thinking-tester-contact-list.herokuapp.com/contacts', headers=headers)
    return response


def get_contact(token, contact_id):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {token}"
    response = requests.get(f'https://thinking-tester-contact-list.herokuapp.com/contacts/{contact_id}', headers=headers)
    return response


def add_contact(token, json):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {token}"
    response = requests.post(f'https://thinking-tester-contact-list.herokuapp.com/contacts/', headers=headers, json=json)
    return response


def update_contact(token, contact_id, json):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {token}"
    response = requests.patch(f'https://thinking-tester-contact-list.herokuapp.com/contacts/{contact_id}', headers=headers, json=json)
    return response


def delete_contact(token, contact_id):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {token}"
    response = requests.delete(f'https://thinking-tester-contact-list.herokuapp.com/contacts/{contact_id}', headers=headers)
    return response