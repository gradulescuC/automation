from selenium.webdriver.support.select import Select
from pages.base_page import Base_page


class Advanced_search_page(Base_page):
		ENTER_KEYWORDS_OR_ITEM_NUMBER = ()
		KEYWORD_OPTIONS = ()
		EXCLUDE_WORDS_FROM_SEARCH = ()
		SEARCH_CATEGORIES = ()
		SEARCH_BUTTON = ()

		def enter_keywords_or_item_number(self):
				self.chrome.find_element(*self.ENTER_KEYWORDS_OR_ITEM_NUMBER).send_keys("iphone")

		def select_keyword_options(self):
				keyword_dropdown = Select(self.chrome.find_element(*self.KEYWORD_OPTIONS))
				keyword_dropdown.select_by_visible_text("Exact words, exact order")

		def select_search_category(self):
				category_dropdown = Select(self.chrome.find_element(*self.KEYWORD_OPTIONS))
				category_dropdown.select_by_visible_text("Cell Phones & Smartphones")

		def exclude_words_from_search(self):
				self.chrome.find_element(*self.EXCLUDE_WORDS_FROM_SEARCH).send_keys("iphone 9")

		def click_search_button(self):
				self.chrome.find_element(*self.SEARCH_BUTTON).click()
