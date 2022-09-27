from bookins.requests.auth import *

from Automation09_Projects.API_Testing.bookins.requests.auth import auth

def test_auth():
    response = auth('admin', 'password123')
    print(response.json())