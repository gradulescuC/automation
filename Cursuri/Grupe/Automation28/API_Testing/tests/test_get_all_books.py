from requests_folder.get_all_books import get_all_books


class TestGetBooks:
		def test_get_all_books_no_filter_check_response_status_code(self):
				response = get_all_books()
				assert response.status_code==200,f"Error: status code is incorrect. Expected: 200, actual: {response.status_code}"

		def test_get_all_books_no_filter_check_number_of_results(self):
				response = get_all_books()
				assert len(response.json())==6,f"Error, invalid number of books returned. Expected: 6, actual: {len(response.json())}"

		def test_get_all_books_filter_by_type_fiction(self):
				response = get_all_books(type="fiction")
				for i in range(len(response.json())):
						assert response.json()[i]["type"]=="fiction",f"Error: filter by type fiction did not work"

		def test_get_all_books_filter_by_type_non_fiction(self):
				response = get_all_books(type="non-fiction")
				for i in range(len(response.json())):
						assert response.json()[i]["type"]=="non-fiction",f"Error: filter by type non-fiction did not work"

		def test_get_all_books_filter_by_type_fiction_and_valid_limit(self):
				response = get_all_books("fiction",3)
				for i in range(len(response.json())):
						assert response.json()[i]["type"]=="fiction",f"Error: filter by type fiction did not work"
				assert len(response.json())==3;

		def test_get_all_books_filter_by_valid_limit(self):
				response = get_all_books(limit=3)
				assert len(response.json())==3;

		def test_get_all_books_filter_by_invalid_limit_greater_than_20(self):
				response = get_all_books(limit=25)
				assert response.status_code==400
				assert response.json()["error"]=="Invalid value for query parameter 'limit'. Cannot be greater than 20."

		def test_get_all_books_filter_by_invalid_limit_smaller_than_0(self):
				response = get_all_books(limit=-3)
				assert response.status_code == 400
				assert response.json()["error"] == "Invalid value for query parameter 'limit'. Must be greater than 0."

