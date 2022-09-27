from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import Base_page

class Advanced_search_page(Base_page):
    SEARCH_TEXT_BOX =(By.ID,"_nkw")
    SUBMIT_SEARCH_BUTTON = (By.XPATH,"//div/button[@type='submit']")
    SEARCH_RESULTS = (By.XPATH, '//h1/span[@class="rcnt"]')

    def set_product_search(self,product_to_be_searched):
        self.chrome.find_element(*self.SEARCH_TEXT_BOX).send_keys(product_to_be_searched)

    def click_search_button(self):
        self.chrome.find_element(*self.SUBMIT_SEARCH_BUTTON).click()

    def check_search_results(self,number_of_results):
        result_list = self.chrome.find_elements(*self.SEARCH_RESULTS)
        resultat_final = result_list.text.replace(',', '')
        assert int(resultat_final) >= int(number_of_results)
        sleep(3)