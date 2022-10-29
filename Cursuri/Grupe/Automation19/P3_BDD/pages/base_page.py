from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from browser import Browser


class Base_page(Browser):
		COOKIES_ACCEPT_BUTTON = (By.ID,"gdpr-banner-accept")
		def wait_and_click_element_by_selector(self,by,selector):
				WebDriverWait(self.driver,20).until(EC.presence_of_element_located((by,selector)))
				self.driver.find_element(by,selector).click()

		def wait_and_send_keys_by_selector(self,by,selector,text):
				WebDriverWait(self.driver,20).until(EC.presence_of_element_located((by,selector)))
				self.driver.find_element(by,selector).send_keys(text)

		def select_element_by_visible_text(self,by,selector,select_value):
				dropdown_options = Select(self.driver.find_element(by,selector))
				dropdown_options.select_by_visible_text(select_value)

		def verify_text_on_elem_by_selector(self,by,selector,expected):
				actual = self.driver.find_element(by,selector).text
				assert actual == expected,"Error: text on element is incorrect"