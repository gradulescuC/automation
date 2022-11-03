from time import sleep
from unittest import TestCase

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

class Test_Formy(TestCase):
		FORM_AUTHENTICATION = (By.LINK_TEXT,"Form Authentication")
		PAGE_HEADING = (By.XPATH,"//h2")
		LOGIN_BUTTON =(By.XPATH,"//form[@id='login']/button")
		USERNAME = (By.ID,"username")
		PASSWORD = (By.ID,"password")
		ERROR_MESSAGE = (By.ID,"flash")
		ELEMENTAL_SELENIUM = (By.LINK_TEXT,"Elemental Selenium")
		LOGIN_INFO = (By.XPATH,"//h4")
		ERROR_CLOSED=(By.XPATH,'//a[@class="close"]')

		def setUp(self):
				s = Service(ChromeDriverManager().install())
				self.chrome = webdriver.Chrome(service=s)
				self.chrome.maximize_window()
				self.chrome.get("https://the-internet.herokuapp.com/")
				sleep(5)
				self.chrome.find_element(*self.FORM_AUTHENTICATION).click()

		def tearDown(self):
				self.chrome.quit()

	# test 1
		def test_check_url(self):
				expected_url = "https://the-internet.herokuapp.com/login"
				actual_url = self.chrome.current_url
				sleep(5)
				assert expected_url==actual_url,"Error: URL is not correct or accesing the form authentication was not properly"


		# test2
		def test_check_title(self):
				expected_title = "The Internet"
				actual_title = self.chrome.title
				assert expected_title==actual_title,"Error: Title is incorrect"
				"""
				operatori de atribuire:=, +=, -=, *=,/=
				operatori de comparatie: ==,<=,>=,<,>,!=
				"""

		def test_close_error_message(self):
				self.chrome.find_element(*self.LOGIN_BUTTON).click()
				sleep(2)
				self.chrome.find_element(*self.ERROR_CLOSED).click()
				assert self.chrome.find_element(*self.ERROR_CLOSED).is_displayed()==False,f"Eroarea nu a disparut. Expected {self.chrome.find_element(*self.ERROR_CLOSED).is_displayed()}"

		#test3
		def test_check_heading(self):
				expected_heading = "Login Page"
				actual_heading = self.chrome.find_element(*self.PAGE_HEADING).text
				assert expected_heading == actual_heading,f"Error: The heading is not correct. Expected: {expected_heading}, actual: {actual_heading}"

		#test4
		def test_login_button_displayed(self):
				assert self.chrome.find_element(*self.LOGIN_BUTTON).is_displayed()==True,"Error: Login button is not displayed"

		#tes5
		def test_check_elemental_selenium_href_link(self):
				href_value_actual = self.chrome.find_element(*self.ELEMENTAL_SELENIUM).get_attribute("href")
				href_value_expected = "http://elementalselenium.com/"
				assert href_value_expected == href_value_actual,"Error: href value is not correct"


		#indicatii test 6:
		# click login
		# assert ERROR_MESSAGE is displayed (metoda isDisplayed)

		#test7
		def test_check_error_message(self):
				self.chrome.find_element(*self.USERNAME).send_keys("testUser")
				self.chrome.find_element(*self.PASSWORD).send_keys("testPassword")
				self.chrome.find_element(*self.LOGIN_BUTTON).click()
				expected_error = "Your username is invalid!"
				actual_error = self.chrome.find_element(*self.ERROR_MESSAGE).text
				assert expected_error in actual_error
				# actual_error = self.chrome.find_element(*self.ERROR_MESSAGE).text.replace("\n","").replace("×","")
				# assert expected_error==actual_error,f"Error message incorrect. Expected: {expected_error}, actual {actual_error}"




		# indicatii test8:
		# click login
		# apasa x sa inchizi eroarea
		# verifica daca eroarea mai este afisata (try except)

		# indicatii test 9:
		# definesti o constanta LISTA_LABELS care sa fie creata pe baza elementelor cu tag-ul label
		# apoi o sa definesti doua variabile username si password care sa contina elementelor din pozita 0 si respectiv pozitia 1 din lista
		# assert 1: verifica ca primul label este username: varianata1 - metoda text, varianta2 - metoda get_attribute
		# assert 2: verifica ca al doilea label este password: varianata1 - metoda text, varianta2 - metoda get_attribute


		# indicatii ex: 10:
		# inserezi user
		# inserezi pass
		# click login
		# assert secure in self.chrome.current_url

		#indicatii ex 11:
		# insert username
		# insert password
		# click login
		# click logout
		# check_url (assert expected == actual)