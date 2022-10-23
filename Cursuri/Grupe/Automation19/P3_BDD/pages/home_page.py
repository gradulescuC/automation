from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.base_page import Base_page


class Home_page(Base_page):
		SEARCH_TEXTBOX = (By.ID,"gh-ac")
		SEARCH_BUTTON = (By.ID,"gh-btn")
		SEARCH_CATEGORIES = (By.ID,"gh-cat")
		ADVANCED_SEARCH_LINK = (By.LINK_TEXT,"Advanced")
		SEARCH_RESULTS = (By.XPATH,'//h1[@class="srp-controls__count-heading"]/span[1]')

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
				result = self.driver.find_element(*self.SEARCH_RESULTS).text
				assert int(result.replace(",",""))>=int(number_of_results)

		def click_advanced_search_link(self):
				self.driver.find_element(*self.ADVANCED_SEARCH_LINK).click()

# <span class ="BOLD" > 467 < / span > >= number_of_results
#TypeError: int() argument must be a string, a bytes-like object or a real number, not 'WebElement'
#ValueError: invalid literal for int() with base 10: '1,200'
#TypeError: '>=' not supported between instances of 'int' and 'str'
