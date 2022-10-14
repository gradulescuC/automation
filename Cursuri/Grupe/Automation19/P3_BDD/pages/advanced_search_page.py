from selenium.webdriver.support.select import Select

from pages.base_page import Base_page

class Advanced_search_page(Base_page):
		ENTER_KEYWORDS_OR_ITEM_NUMBER = ()
		KEYWORDS_OPTIONS = ()
		EXCLUDE_WORDS_FROM_SEARCH = ()
		ALL_CATEGORIES = ()
		SEARCH_BUTTON = ()

		def enter_keywords_or_item_number(self):
				self.driver.find_element(*self.ENTER_KEYWORDS_OR_ITEM_NUMBER).send_keys("")


		def select_keywords_options(self):
				keyword_options = Select(self.driver.find_element(*self.KEYWORDS_OPTIONS))
				keyword_options.select_by_visible_text("")

		def exclude_words_from_search(self):
				self.driver.find_element(*self.EXCLUDE_WORDS_FROM_SEARCH).send_keys()

		def select_category_from_dropdown(self):
				category_dropdown = Select(self.driver.find_element(*self.ALL_CATEGORIES))
				category_dropdown.select_by_visible_text("")

		def click_search_button(self):
				self.driver.find_element(*self.SEARCH_BUTTON).click()
