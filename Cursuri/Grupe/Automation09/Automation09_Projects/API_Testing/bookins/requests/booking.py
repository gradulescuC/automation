import requests

def get_booking(id=None):
    response = requests.get(f'https://restful-booker.herokuapp.com/booking/{id}')
    return response