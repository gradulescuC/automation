from time import sleep
from unittest import TestCase

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

class Test_Formy_v1(TestCase):
		FORM_AUTHENTICATION = (By.LINK_TEXT,"Form Authentication")
		PAGE_HEADING = (By.XPATH,"//h2")
		LOGIN_BUTTON =(By.XPATH,"//form[@id='login']/button")
		USERNAME = (By.ID,"username")
		PASSWORD = (By.ID,"password")
		ERROR_MESSAGE = (By.ID,"flash")
		ELEMENTAL_SELENIUM = (By.LINK_TEXT,"Elemental Selenium")
		LOGIN_INFO = (By.XPATH,"//h4")

		def setUp(self):
				s = Service(ChromeDriverManager().install())
				self.chrome = webdriver.Chrome(service=s)
				self.chrome.maximize_window()
				self.chrome.get("https://the-internet.herokuapp.com/")
				sleep(5)
				self.chrome.find_element(*self.FORM_AUTHENTICATION).click()

		def tearDown(self):
				self.chrome.quit()

		#test12:
		def test_brute_force_password_hacking(self):
				login_message_split = self.chrome.find_element(*self.LOGIN_INFO).text.split()
				for word in login_message_split:
						self.chrome.find_element(*self.USERNAME).send_keys("tomsmith")
						self.chrome.find_element(*self.PASSWORD).send_keys(word)
						self.chrome.find_element(*self.LOGIN_BUTTON).click()
						if "secure" in self.chrome.current_url:
								print(f"Am gasit parola: {word}")
								break
				assert "secure" in self.chrome.current_url,"Nu am gasit parola. Ghinion!"