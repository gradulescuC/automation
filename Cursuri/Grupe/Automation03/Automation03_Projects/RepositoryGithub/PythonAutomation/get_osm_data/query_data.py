import requests as requests

url = "https://overpass.kumi.systems/api/interpreter"
# query = """[out:json];node [amenity=nightclub] (53.2987342,-6.3870259,53.4105416,-6.1148829); out;"""
query = """[out:json];node [amenity=restaurant] (44.41753369503389, 26.072517039539676, 44.42420592698686, 26.100913238552188); out;"""
response = requests.get(url, params = {"data":query})
data = response.json()
print(data)