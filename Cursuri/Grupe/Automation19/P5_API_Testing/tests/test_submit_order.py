from requests_folder.submit_order import submit_order

class TestSubmitOrder:

		def test_submit_order(self):
				response = submit_order(1,"John Doe")
				assert response.status_code == 201
				assert response.json()["created"]==True
				assert len(response.json()['orderId'])>0

