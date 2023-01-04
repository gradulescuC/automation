from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.base_page import Base_page

class Home_page(Base_page):
		SEARCH_TEXTBOX = ()
		SEARCH_BUTTON = ()
		SEARCH_CATEGORIES = ()
		ADVANCED_SEARCH_LINK = ()
		SEARCH_RESULTS = ()

		def  navigate_to_homepage(self):
				self.chrome.get()

		def insert_search_value(self):
				self.chrome.find_element(*self.SEARCH_TEXTBOX).send_keys("iphone")

		def choose_category(self):
				category_dropdown = Select(self.chrome.find_element(*self.SEARCH_CATEGORIES))
				category_dropdown.select_by_visible_text("Cell Phones & Smartphones")

		def click_search_button(self):
				self.chrome.find_element(*self.SEARCH_BUTTON).click()

		def check_search_results(self):
				result = self.chrome.find_element(*self.SEARCH_RESULTS).text
				assert result >=1000


		def click_advanced_search_link(self):
				self.chrome.find_element(*self.ADVANCED_SEARCH_LINK).click()