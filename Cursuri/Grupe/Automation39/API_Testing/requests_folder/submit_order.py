import requests
from requests_folder.api_authentication import generate_token

def submit_order(bookId="", customer_name=""):
		request_body = {
						"bookId": bookId,
						"customerName": customer_name
				}
		token = generate_token()
		header_params = {'Authorization':token}
		response = requests.post("https://simple-books-api.glitch.me/orders",json=request_body, headers=header_params)
		return response

# Aduceti-va aminte de la dictionare - exemplu de polimorfism
def test_function(**keyargs):
		pass

test_function(test_cheie1="valoare_cheie1", test_cheie2="valoare_cheie2")
test_function(test_cheie1="valoare_cheie1", test_cheie2="valoare_cheie2",test_cheie3="valoare_cheie3")