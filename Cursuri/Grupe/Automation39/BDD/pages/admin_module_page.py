from selenium.webdriver.common.by import By

from pages.base_page import Base_page


class Admin_module(Base_page):

		MENU_MODULE_LIST = (By.XPATH,'//a[@class="oxd-main-menu-item"]')
		STATUS_DROPDOWN = (By.XPATH,'//div[@class="oxd-select-text oxd-select-text--active"]')

		def click_admin_option(self):
				self.chrome.find_elements(self.MENU_MODULE_LIST)[0].click()


		def select_user_status(self,user_status):
				self.chrome.find_elements(*self.STATUS_DROPDOWN)[1].click()

