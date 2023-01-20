from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import Base_page


class Search_results_page(Base_page):
		ELEMENT_TO_BE_ADDED_TO_CART = (By.XPATH,"//span[contains(text(),'Apple iPhone 14 Pro Unlocked eSim, Pre-Order..')]")
		COLOUR_DROPDOWN = (By.ID,"x-msku__select-box-1000")
		STORAGE_CAPACITY_DROPDOWN = (By.ID,"x-msku__select-box-1001")
		LOCK_STATUS_DROPDOWN = (By.ID,"x-msku__select-box-1002")
		SIM_CARD_SLOT = (By.ID,"x-msku__select-box-1003")
		property_dictionary = {}
		property = []

		def open_identified_product(self):
				self.chrome.find_element(*self.ELEMENT_TO_BE_ADDED_TO_CART).click()

		def add_element_to_dictionary(self, property, value):
				self.property_dictionary[property] = value
				return self.property_dictionary

		def choose_product_specifications(self, *args):
				for prop in args:
						self.property.append(prop)
				# colour_dropdown = Select(self.chrome.find_element(*self.COLOUR_DROPDOWN))
				# colour_dropdown.select_by_visible_text(self.property_dictionary.get(property[i]))
				# colour_dropdown.select_by_visible_text("Gold")


				"""
				1. Definim dictionar care sa stocheze toate perechile cheie: valoare pe care le folosim in cautarea diverselor produse (culoare:gold)
				2. Definim o lista care sa stocheze toate atributele necesare pentru produsul nostru
				3. Folosim un if pentru a parcurge lista si dictionarul create anterior
				4. In momentul in care gasim in dictionar atributul existentent din lista, o sa ii luam valoarea 
								si o trimitem ca si parametru la metoda select_by_visible_text
				"""


				storage_capacity_dropdown = Select(self.chrome.find_element(*self.STORAGE_CAPACITY_DROPDOWN))
				lock_status_dropdown = Select(self.chrome.find_element(*self.LOCK_STATUS_DROPDOWN))
				sim_card_slot_dropdown = Select(self.chrome.find_element(*self.SIM_CARD_SLOT))







