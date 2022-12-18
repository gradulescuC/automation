from generic_page_methods import Generic_page_methods


class Login_page(Generic_page_methods):
		USERNAME = ()
		PASSWORD = ()
		LOGIN_BUTTON = ()
		ERROR_MESSAGE = ()


		def navigate_to_homepage(self):
				self.chrome.get("https://www.saucedemo.com/")

		def insert_username(self,username):
				self.chrome.find_element(*self.USERNAME).send_keys(username)

		def insert_password(self,password):
				self.chrome.find_element(*self.USERNAME).send_keys(password)

		def click_login_button(self):
				self.chrome.find_element(*self.LOGIN_BUTTON).click()

		def check_login_error_message(self,expected_error_message):
				self.check_error_message(*self.ERROR_MESSAGE,expected_error_message)

