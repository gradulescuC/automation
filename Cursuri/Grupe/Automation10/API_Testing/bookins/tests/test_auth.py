from API_Testing.bookins.requests.auth import auth

def test_auth():
    response = auth('admin', 'password123')
    print(response.json())