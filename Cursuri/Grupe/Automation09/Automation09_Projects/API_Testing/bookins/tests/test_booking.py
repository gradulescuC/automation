from bookins.requests.booking import *


def test_get_booking():
    response = get_booking(1)
    print(response.json())

