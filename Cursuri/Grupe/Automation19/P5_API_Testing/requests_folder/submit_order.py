import requests

from requests_folder.get_api_token import get_token


def submit_order(book_id, customer_name):
		request_body = {
				"bookId": book_id,
				"customerName": customer_name
		}
		token = get_token()
		header_params = {'Authorization':token}
		response = requests.post("https://simple-books-api.glitch.me/orders",headers=header_params,json=request_body)
		return response