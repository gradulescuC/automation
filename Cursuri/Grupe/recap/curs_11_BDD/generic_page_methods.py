from browser import Browser


class Generic_page_methods(Browser):
		def check_error_message(self, by, selector,expected_error_message):
				actual_error_message = self.chrome.find_element(by,selector).text
				assert expected_error_message == actual_error_message, f"fError: Incorrect error message. Expected: {expected_error_message}, Actual: {actual_error_message}"