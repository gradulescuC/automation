import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class Demo_signup(unittest.TestCase):
    FIRST_NAME = (By.NAME,"firstname")
    LAST_NAME = (By.NAME, "lastname")
    GENDER_MALE = (By.ID,"sex-0")
    GENDER_FEMALE = (By.ID,"sex-1")
    EXPERIENCE = (By.ID,"exp-6")
    MANUAL_TESTER = (By.ID,"profession-0")
    AUTOMATION_TESTER = (By.ID,"profession-1")
    DROPDOWN_CONTINENTS = (By.ID,"continents")
    SUBMIT_BUTTON = (By.ID,"submit")
    AUTOMATION_TOOLS = (By.ID,"tool-1")
    SELENIUM_COMMANDS = (By.ID,"selenium_commands")
    # ERROR_MESSAGE = (By.XPATH,<xpath>)

    def setUp(self) -> None:
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(5)
        self.chrome.get("https://www.techlistic.com/p/selenium-practice-form.html")

    def tearDown(self) -> None:
        self.chrome.quit()

    # presupunem de dragul exercitiul ca doar firstname, lastname si gender sunt obligatorii
    # rezultate asteptate: formularul este trimis cu succes daca toate campurile obligatorii sunt completate
    def test_check_form_mandatory_fields_ok(self):
        self.chrome.find_element(*self.FIRST_NAME).send_keys("Anton")
        self.chrome.find_element(*self.LAST_NAME).send_keys("Pann")
        self.chrome.find_element(*self.GENDER_MALE).click()
        self.chrome.find_element(*self.SUBMIT_BUTTON).click()


    # rezultate asteptate: formularul nu este trimis daca firstname nu este completat, si un mesaj de eroare este returnat
    def test_check_form_mandatory_fields_nok_fn_missing(self):
        self.chrome.find_element(*self.LAST_NAME).send_keys("Pann")
        self.chrome.find_element(*self.GENDER_MALE).click()
        self.chrome.find_element(*self.SUBMIT_BUTTON).click()
        # expected_error = "Atentie, firstName este un camp obligatoriu"
        # actual_error = self.chrome.find_element(*self.ERROR_MESSAGE).text
        # assert expected_error == actual_error,"Atentie, mesajul de eroare nu este corect"

    # rezultate asteptate: formularul nu este trimis daca lastname nu este completat, si un mesaj de eroare este returnat
    def test_check_form_mandatory_fields_nok_ln_missing(self):
        self.chrome.find_element(*self.FIRST_NAME).send_keys("Anton")
        self.chrome.find_element(*self.GENDER_MALE).click()
        self.chrome.find_element(*self.SUBMIT_BUTTON).click()
        # expected_error = "Atentie, lastName este un camp obligatoriu"
        # actual_error = self.chrome.find_element(*self.ERROR_MESSAGE).text
        # assert expected_error == actual_error,"Atentie, mesajul de eroare nu este corect"

    # rezultate asteptate: formularul nu este trimis daca gender nu este completat, si un mesaj de eroare este returnat
    def test_check_form_mandatory_fields_nok_gender_missing(self):
        self.chrome.find_element(*self.FIRST_NAME).send_keys("Anton")
        self.chrome.find_element(*self.LAST_NAME).send_keys("Pann")
        self.chrome.find_element(*self.SUBMIT_BUTTON).click()
        # expected_error = "Atentie, gender este un camp obligatoriu"
        # actual_error = self.chrome.find_element(*self.ERROR_MESSAGE).text
        # assert expected_error == actual_error,"Atentie, mesajul de eroare nu este corect"


    # rezultat asteptat: Atunci cand completez toate campurile, valorile de input sunt acceptate si formularul este transmis cu succes
    def test_check_submit_form_all_fields_filled(self):
        self.chrome.find_element(*self.FIRST_NAME).send_keys("Anton")
        self.chrome.find_element(*self.LAST_NAME).send_keys("Pann")
        self.chrome.find_element(*self.GENDER_MALE).click()
        self.chrome.find_element(*self.SUBMIT_BUTTON).click()
        self.chrome.find_element(*self.EXPERIENCE).click()
        self.chrome.find_element(*self.MANUAL_TESTER).click()
        dropdown = Select(self.chrome.find_element(*self.DROPDOWN_CONTINENTS))
        dropdown.select_by_visible_text("Europe")
        self.chrome.find_element(*self.AUTOMATION_TOOLS)
        dropdown_selenium_commands = Select(self.chrome.find_element(*self.SELENIUM_COMMANDS))
        dropdown_selenium_commands.select_by_visible_text("Wait Commands")
        self.chrome.find_element(*self.SUBMIT_BUTTON).click()








