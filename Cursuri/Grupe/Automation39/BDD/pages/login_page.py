from selenium.webdriver.common.by import By

from pages.base_page import Base_page

class Login_page(Base_page):

		USERNAME = (By.XPATH,'//input[@placeholder="Username"]')
		PASSWORD = (By.XPATH,'//input[@placeholder="Password"]')
		LOGIN_BUTTON = (By.CSS_SELECTOR,'button[type="submit"]')
		LOGIN_ERROR_MESSAGE = (By.CSS_SELECTOR,'div.orangehrm-login-error i + p')

		def navigate_to_homepage(self):
				# am scris self.chrome in loc de chrome ca sa anuntam sistemul ca facem referinta
							# catre atributul chrome definit in clasa stramos Broswer mostenita prin clasa
									# parinte Base_page
				# daca nu am fi scris self in fata sistemul ar fi cautat valoarea chrome intre
							# parametrii functiei
				self.chrome.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

		def insert_username(self,username="Admin"):
				self.chrome.find_element(*self.USERNAME).send_keys(username)

		def insert_password(self,password="admin123"):
				self.chrome.find_element(*self.PASSWORD).send_keys(password)

		def click_login_button(self):
				self.chrome.find_element(*self.LOGIN_BUTTON).click()

		def check_current_url(self):
				actual_url = self.chrome.current_url
				expected_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'
				assert expected_url == actual_url, "The url is incorrect. Please check the login functionality"

		def check_error_message(self,expected_error_message):
				actual_error_message = self.chrome.find_element(*self.LOGIN_ERROR_MESSAGE).text
				# Ce e la linia de mai jos se va extrage daca nu folosim metoda "text"
				# < p< pclass ="oxd-text oxd-text--p oxd-alert-content-text" data-v-7588b244="" data-v-0b423d90="" > Invalid credentials < / p >
				assert expected_error_message == actual_error_message, f"Error, the login message is incorrect. Expected: {expected_error_message}, actual: {actual_error_message}"