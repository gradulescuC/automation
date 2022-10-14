from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import Base_page


class Home_page(Base_page):
		SEARCH_TEXTBOX = ()
		SEARCH_BUTTON = ()
		SEARCH_CATEGORIES = ()
		ADVANCED_SEARCH_LINK = ()
		SEARCH_RESULTS = ()

		def navigate_to_homepage(self):
				self.driver.get("https://www.ebay.com/")

		def insert_search_value(self,product_name):
				self.driver.find_element(*self.SEARCH_TEXTBOX).send_keys(product_name)

		def choose_category(self,category_name):
				category_dropdown = Select(self.driver.find_element(*self.SEARCH_CATEGORIES)) # am creat un obiect al clasei select
				category_dropdown.select_by_visible_text(category_name) # pe baza obiectului creat am accesat metoda select_by_visible_text

		def click_search_button(self):
				self.driver.find_element(*self.SEARCH_BUTTON).click()


		def check_search_results(self,number_of_results):
				result = self.driver.find_element(*self.SEARCH_RESULTS)
				assert int(result)>=number_of_results


