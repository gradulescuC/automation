import random

import requests

def generate_token():
		nr = random.randint(1,9999999999999999999999999999999)
		request_body = {
				"clientName":"TA28",
				"clientEmail":f"TA28{nr}@gmail.com"
		}
		response = requests.post("https://simple-books-api.glitch.me/api-clients/",json=request_body)
		return response.json()["accessToken"]
