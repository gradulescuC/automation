import random
import requests

def get_token():
		nr = random.randint(1,999999999)
		request_body=	{
				'clientName':"numeTest",
				'clientEmail':f'numeTest{nr}@gmail.com'
		}
		response = requests.post("https://simple-books-api.glitch.me/api-clients/",json = request_body )
		token = response.json()["accessToken"]
		return token