import requests

def submit_order(bookId, customerName,token):
		header_params = {'Authorization': token}
		request_body = {
				"bookId": {bookId},
				"customerName": {customerName}
		}
		response = requests.post("https://simple-books-api.glitch.me/orders",json=request_body,headers=header_params)
		return response