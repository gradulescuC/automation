from selenium.webdriver.common.by import By

from generic_page_methods import Generic_page_methods

class Login_page(Generic_page_methods):
		USERNAME = (By.ID,"user-name")
		PASSWORD = (By.ID,"password")
		LOGIN_BUTTON = (By.ID,"login-button")
		ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error']")
		CLOSE_ERROR_MESSAGE_BUTTON = (By.CLASS_NAME, "error-button")

		def navigate_to_homepage(self):
				self.chrome.get("https://www.saucedemo.com/")

		def insert_username(self,username):
				self.chrome.find_element(*self.USERNAME).send_keys(username)

		def insert_password(self,password):
				self.chrome.find_element(*self.PASSWORD).send_keys(password)

		def click_login_button(self):
				self.chrome.find_element(*self.LOGIN_BUTTON).click()

		def check_login_error_message(self,expected_error_message):
				self.check_error_message(*self.ERROR_MESSAGE, expected_error_message)

		def close_error_message(self):
				self.chrome.find_element(*self.CLOSE_ERROR_MESSAGE_BUTTON).click()

		def check_error_no_longer_visible(self):
				"""
				Metoda 1:

				try:
						self.chrome.find_element(*self.ERROR_MESSAGE)
						found = True
				except:
						found = False
				assert found == True, "Attention, the error was not closed, please check"
				"""

				# Metoda 2:
				error_message_list = self.chrome.find_elements(*self.ERROR_MESSAGE)
				assert len(error_message_list) == 0, "Attention, the error was not closed, please check"


