from requests_folder.delete_order import delete_order
from requests_folder.submit_order import submit_order

class TestDeleteOrder:
		def test_delete_order(self):
				response = delete_order(submit_order(2,"Maria Anton").json()["orderId"])
				assert response.status_code == 204
				assert response.json()==""

"""
Raport de bug:

Summary: Order not found when executing Delete Order Request
Preconditions: At least an order must submitted into the system
Steps to reproduce:
1. Prepare the api request for Delete Order with the following setup:
- Authorization: <token>
- endpoint: https://simple-books-api.glitch.me/orders/S0wZ9xKqmEd6i8gX_RXS6
- http method: delete
2. Send the request and validate the results
Expected results: The order is deleted successfully and the request response status is 204
Actual results: The order is not deleted and an error is returned: No order with id S0wZ9xKqmEd6i8gX_RXS6.
								Status code is 404
"""