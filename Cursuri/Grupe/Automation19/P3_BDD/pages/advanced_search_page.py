from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import Base_page

class Advanced_search_page(Base_page):
		ENTER_KEYWORDS_OR_ITEM_NUMBER = (By.ID,"_nkw")
		KEYWORDS_OPTIONS = (By.ID,"_in_kw")
		EXCLUDE_WORDS_FROM_SEARCH = (By.ID,"_ex_kw")
		ALL_CATEGORIES = (By.ID,"e1-1")
		SEARCH_BUTTON = (By.XPATH,"//button[@type='submit' and @class = 'btn btn-prim']")

		def enter_keywords_or_item_number(self,product_name):
				self.wait_and_send_keys_by_selector(product_name)

		def select_keywords_options(self,keyword_options_value):
				self.select_element_by_visible_text(*self.KEYWORDS_OPTIONS,keyword_options_value)

		def exclude_words_from_search(self,*args):
				self.wait_and_send_keys_by_selector(*self.EXCLUDE_WORDS_FROM_SEARCH,args)

		def select_category_from_dropdown(self,category_name):
				self.select_element_by_visible_text(*self.ALL_CATEGORIES,category_name)

		def click_search_button(self):
				self.wait_and_click_element_by_selector(*self.SEARCH_BUTTON)

"""
Am clasa class="btn btn-prim"
Daca am o clasa care contine spatiu inseamna ca avem de fapt
			mai multe clase
- Daca facem cautare dupa clasa (By.CLASS_NAME)
				atunci trebuie sa cautam dupa una dintre clasele separate prin spatiu
- Daca facem cautare dupa XPATH atunci trebuie sa specificam ambele clase
Exemplu:
(By.CLASS_NAME,"btn")
(By.CLASS_NAME."btn-prim")
//button[@type='submit' and @class='btn btn-prim']
"""