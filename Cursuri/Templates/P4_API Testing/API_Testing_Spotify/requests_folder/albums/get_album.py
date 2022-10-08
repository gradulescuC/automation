import requests

from environment import token

# market=""
#
def get_album_without_market(id):
    header = {'Authorization': token}
    response = requests.get(f'https://api.spotify.com/v1/albums/{id}', headers=header)
    return response

def get_album_with_market(id,market):
    header = {'Authorization': token}
    response = requests.get(f'https://api.spotify.com/v1/albums/{id}?market={market}', headers=header)
    return response