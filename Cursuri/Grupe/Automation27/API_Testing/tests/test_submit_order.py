from requests_folder.submit_order import submit_order


class TestSubmitOrder:
		def test_submit_order(self):
				response = submit_order(1,"Andrei Ghemus")
				assert response.status_code == 201,f"Error: Status code is not valid. Expected: 201, actual: {response.status_code}"
				assert response.json()["created"]==True, f"Error: Order creation status is not correct. Expected: True, Actual: {response.json()['created']}"
				assert len(response.json()["orderId"])>0, f"Error: Order id is invalid. Expected lenght greater than zero. Actual length: {len(response.json()['orderId'])} "