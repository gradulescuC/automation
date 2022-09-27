from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductsPage(BasePage):

    RESULTS_TITLE = (By.XPATH, '//a[@data-zone="title"]')
    VEZI_DETALII_COS_BTN = (By.XPATH, '//a[text()="Vezi detalii cos"]')

    def click_vezi_detalii_cos(self):
        self.wait_and_click_elem_by_selector(*self.VEZI_DETALII_COS_BTN)

    def verify_results_contain_text(self, text):
        title_list = self.driver.find_elements(*self.RESULTS_TITLE)
        for i in range(5):
            title = title_list[i].text.lower()
            self.assertTrue(text in title, 'Result does not contain search query')

    def add_to_basket_by_partial_product_name(self, partial_name):
        self.driver.find_element(By.XPATH, f'//a[contains(text(), "{partial_name}")]/parent::div/parent::div/parent::div//button[text()="Adauga in Cos"]').click()








