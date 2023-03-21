from requests_folder.generate_token import generate_token
from requests_folder.submit_order import submit_order


class TestSubmitOrder:
		def test_submit_order(self):
				token = generate_token()
				response = submit_order(1,"John Smith",token)
				assert response.status_code == 201,"Error, status code is incorrect for submit order"
				assert response.json()["created"]==True,"Error, order create is not correct"
				assert len(response.json()["orderId"])==21,"Error, orderId is invalid"