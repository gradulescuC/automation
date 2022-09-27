from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.base_page import Base_page

class Home_page(Base_page):
    SEARCH_TEXT_BOX = (By.ID, "gh-ac")
    SEARCH_BUTTON   = (By.ID, "gh-btn")
    SEARCH_RESULTS  = (By.XPATH, '//h1/span[@class="BOLD"]')
    CATEGORY_DROPDOWN = (By.ID,"gh-cat")
    ADVANCED_SEARCH_LINK=(By.LINK_TEXT, 'Advanced')


    def navigate_to_home_page(self):
        self.chrome.get('https://www.ebay.com/')

    def set_product_search(self):
        self.chrome.find_element(*self.SEARCH_TEXT_BOX).send_keys("Iphone")


    def click_search_button(self):
        self.chrome.find_element(*self.SEARCH_BUTTON).click()
        sleep(3)

    def check_search_results(self):
        result_list = self.chrome.find_elements(*self.SEARCH_RESULTS)
        resultat_final = result_list[0].text.replace(',', '')
        assert int(resultat_final) >= 2
        sleep(3)

    #
    # def set_product_search_with_parameter(self,product):
    #     self.chrome.find_element(*self.SEARCH_TEXT_BOX).send_keys(product)
    #     sleep(3)
    #
    # def check_search_results_with_parameters(self,number_of_results):
    #     result_list = self.chrome.find_elements(*self.SEARCH_RESULTS)
    #     resultat_final=result_list[0].text.replace(',', '')
    #     assert int(resultat_final) >= int(number_of_results)
    #
    #
    #
    # def choose_category(self,category):
    #     category_dropdown = Select(self.chrome.find_element(*self.CATEGORY_DROPDOWN))
    #     category_dropdown.select_by_visible_text(category)
    #     sleep(3)
    #
    # def click_advanced_search_link(self):
    #     self.chrome.find_element(*self.ADVANCED_SEARCH_LINK).click()