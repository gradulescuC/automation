from requests_folder.get_all_books import get_all_books

class TestGetBooks:

		#@functionalTesting @positiveTesting
		def test_get_all_books_no_filter_check_response_status(self):
				response = get_all_books()
				assert response.status_code == 200

		#@functionalTesting @positiveTesting
		def test_get_all_books_check_number_of_results(self):
				response = get_all_books().json()
				assert len(response) == 6, f"Expected: 6, Actual: {response}"

		#@functionalTesting @positiveTesting
		def test_get_all_books_filter_by_type_fiction(self):
				response = get_all_books("fiction").json()
				assert len(response)==4,f"Expected: 4, Actual: {response}"
				for i in range(len(response)):
						assert response[i]['type'] == 'fiction'

		def test_get_all_books_filter_by_type_non_fiction(self):
				response = get_all_books("non-fiction").json()
				assert len(response)==2, f'Expected: 2, Actual: {response}'
				for i in range(len(response)):
						assert response[i]['type'] == 'non-fiction'

		def test_get_all_books_filter_by_non_existing_type(self):
				response = get_all_books("comedy")
				assert response.status_code==400
				assert response.json()["error"]=="Invalid value for query parameter 'type'. Must be one of: fiction, non-fiction."

# lista = [1,3,4,5,6]
# dictionar = {1:"one",2:"two","trei":"cifra trei"}
# lista[0]
# dictionar[1]
# dictionar["trei"]