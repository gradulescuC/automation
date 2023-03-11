from selenium.webdriver.common.by import By

from base_page import Base_page


class Login_page(Base_page):
		USERNAME = (By.XPATH,'//input[@name="username"]')
		PASSWORD = (By.XPATH,'//input[@name="password"]')
		LOGIN_BUTTON = (By.XPATH,'//button[@type="submit"]')

		def navigate_to_login_page(self):
				self.chrome.get("https://opensource-demo.orangehrmlive.com/")

		def insert_username(self,username):
				self.chrome.find_element(*self.USERNAME).send_keys(username)

		def insert_password(self,password):
				self.chrome.find_element(*self.PASSWORD).send_keys(password)

		def click_login_button(self):
				self.chrome.find_element(*self.LOGIN_BUTTON).click()

		def check_user_is_logged(self):
				current_url = self.chrome.current_url
				expected_content = "dashboard"
				assert expected_content in current_url,"Error, URL was not loaded properly. Check if login was successful"

"""
despachetarea tuplului prin *
elementul nedespachetat: (By.XPATH,'//input[@name="username"]')
elementul despachetat: By.XPATH,'//input[@name="username"]'

Despachetarea este necesara pentru ca metoda find_element(s) are nevoie de doua argumente:
- tipul de selector
- valoarea de cautare
Daca noi nu facem despachetarea, metoda o sa primeasca in loc de doua argumente, unul singur
"""
