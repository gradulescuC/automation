from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Base_page

class Home_page(Base_page):
		ACCOUNT_DROPDOWN = (By.CSS_SELECTOR,'li[class="oxd-userdropdown"]')
		LOGOUT_LINK = (By.LINK_TEXT,'Logout')

		# am creat o noua metoda de logout pentru situatia in care vrem sa testam niste scenarii
		# pe pagina de login dupa ce deja ne-am logat in aplicatie

		def logout_of_the_application(self):
				account_dropdown = WebDriverWait(self.chrome, 20).until(EC.presence_of_element_located(self.ACCOUNT_DROPDOWN))
				account_dropdown.click()
				self.chrome.find_element(*self.LOGOUT_LINK).click()
