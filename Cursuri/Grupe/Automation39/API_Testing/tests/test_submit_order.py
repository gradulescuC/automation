from requests_folder.submit_order import submit_order


class Test_submit_order():

		def test_submit_order(self):
				response = submit_order(1,"John Smith")
				assert response.status_code == 201, f"Error: invalid status code. Expected 201, but got {response.status_code}"
				assert len(response.json()["orderId"])==21,"Error, invalid orderid length"
				# assert len(response.json()["orderId"]) > 0, "Error, invalid orderid length"
				assert response.json()["created"]==True, "Error: created status is incorrect"

		def test_submit_order_missing_book_id(self):
				response = submit_order(customer_name="John Smith")
				assert response.json()["error"]=="Invalid or missing bookId.",f"Error message either missing or invalid"
				assert response.status_code==400, f"Error: invalid status code. Expected 400, but got {response.status_code}"

		# testul de mai jos va fi fail din cauza unui bug
		# bug-ul este faptul ca putem sa cream comenzi fara un clientName
		# eroarea pe care o va returna va fi:KeyError: 'error' pentru ca in response dictionary nu exista cheia "error"

		def test_submit_order_missing_customer_name(self):
				response = submit_order(1)
				assert response.json()["error"]=="Invalid or missing customerName.",f"Error message either missing or invalid"
				assert response.status_code==400, f"Error: invalid status code. Expected 400, but got {response.status_code}"

		def test_submit_order_non_existing_book_id(self):
				response = submit_order(100,"John Smith")
				assert response.json()["error"] == "Invalid or missing bookId.", f"Error message either missing or invalid"
				assert response.status_code == 400, f"Error: invalid status code. Expected 400, but got {response.status_code}"

		def test_submit_order_not_available_book_id(self):
				response = submit_order(2,"John Smith")
				assert response.json()["error"] == "This book is not in stock. Try again later.", f"Error message either missing or invalid"
				assert response.status_code == 404, f"Error: invalid status code. Expected 400, but got {response.status_code}"


