from requests_folder.get_all_books import get_all_books


class Test_get_books():

		def test_get_all_books_no_filter_check_response_status(self):
				# response-ul returnat de get_all_books contine toate informatiile
				# returnate de requestul acesta: body, status code, cookies
				response = get_all_books()
				assert response.status_code == 200, f"Error: the expected status code is 200 but got {response.status_code}"

		def test_get_all_books_no_filter_check_number_of_results(self):
				# response-ul returnat de get_all_books contine toate informatiile
				# returnate de requestul acesta: body, status code, cookies
				response = get_all_books().json() # json reprezinta corpul raspunsului returnat de request
				assert len(response) == 6, f"Error: the number of results returned is incorrect"


		def test_get_all_books_filter_by_type_fiction(self):
				response = get_all_books("fiction").json()
				assert len(response) == 4, f"Error: the number of results returned is incorrect"
				for i in range(len(response)):
						assert response[i]["type"]=="fiction","Error: the type of the book is incorrect"

		def test_get_all_books_filter_by_type_non_fiction(self):
				response = get_all_books("non-fiction").json()
				assert len(response) == 2, f"Error: the number of results returned is incorrect"
				for i in range(len(response)):
						assert response[i]["type"] == "non-fiction", "Error: the type of the book is incorrect"

		def test_get_all_books_filter_by_type_non_existing_type(self):
				response = get_all_books("comedy")
				assert response.status_code == 400, f"Error: invalid status code. Expected 400, but got {response.status_code}"
				assert response.json()["error"]=="Invalid value for query parameter 'type'. Must be one of: fiction, non-fiction.",f"Invalid error message. Expected: 'Invalid value for query parameter 'type'. Must be one of: fiction, non-fiction.', actual: {response.json()['error']}"

		def test_get_all_books_filter_by_type_invalid_type_special_characters(self):
				response = get_all_books("!@£$%^&*()_-=[];'\,./<>?:|{}")
				assert response.status_code == 400, f"Error: invalid status code. Expected 400, but got {response.status_code}"
				assert response.json()["error"]=="Invalid value for query parameter 'type'. Must be one of: fiction, non-fiction.",f"Invalid error message. Expected: 'Invalid value for query parameter 'type'. Must be one of: fiction, non-fiction.', actual: {response.json()['error']}"

		def test_get_all_books_filter_by_type_invalid_type_numbers(self):
				response = get_all_books("12234567890")
				assert response.status_code == 400, f"Error: invalid status code. Expected 400, but got {response.status_code}"
				assert response.json()["error"]=="Invalid value for query parameter 'type'. Must be one of: fiction, non-fiction.",f"Invalid error message. Expected: 'Invalid value for query parameter 'type'. Must be one of: fiction, non-fiction.', actual: {response.json()['error']}"

		def test_get_all_books_filter_by_limit(self):
				response = get_all_books(limit=3)
				# tema pentru acasa: de completat testul

""" Exemple de interpretare response.json():
https://developer.spotify.com/documentation/web-api/reference/get-an-album

response.json()["artists"][0]["external_urls"]["spotify"]=="string"
response.json()["artists"][0]["followers"]["total"]==0
"""