import requests
import random

def generate_token():
		nr = random.randint(1,99999999999999999999)
		request_body = {
						"clientName": "Razvan Maxim",
						"clientEmail": f"razvan.maxim{nr}@gmail.com"
		}
		response = requests.post("https://simple-books-api.glitch.me/api-clients/",json=request_body)
		token = response.json()["accessToken"]
		return token

def delete_order(orderId):
		token = generate_token()
		header_params = {'Authorization': token}
		response = requests.delete(f"https://simple-books-api.glitch.me/orders/{orderId}",headers=header_params)
		return response


def submit_order(bookid, customer_name):
		request_body = {
				"bookId": bookid,
				"customerName": customer_name
		}
		token = generate_token()
		header_params = {'Authorization': token}
		response = requests.post("https://simple-books-api.glitch.me/orders", json=request_body, headers=header_params)
		return response

# order_response = submit_order(1,"Maria Anton")
# print(order_response.json())
response = delete_order("HE9ou2IsJFokibIcI_2-H")
print(response.json())
# assert response.status_code == 204, f'Error expected 204, actual {response}'
# assert response.json()==""