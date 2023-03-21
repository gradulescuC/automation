import requests

def patch_order(customerName,orderId, token):
		header_params={'Authorization':token}
		request_body={
				"customerName":{customerName}
		}
		response = requests.patch(f"https://simple-books-api.glitch.me/orders/{orderId}", headers=header_params, json=request_body)
		return response