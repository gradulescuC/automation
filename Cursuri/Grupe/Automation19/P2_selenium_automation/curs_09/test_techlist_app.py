import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Techlist(unittest.TestCase):

    JAVA_TUTORIAL_LINK = (By.LINK_TEXT,"Java Tutorial")
    FIRST_NAME_INPUT = (By.XPATH,"//input[@name='firstname']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@name='lastname']")
    GENDER_MALE_RADIO_BUTTON = (By.ID,"sex-0")
    YEAR_OF_EXPERIENCE_1_RADIO_BUTTON = (By.ID,"exp-0")
    PROFFESSION_CHECKBOX = (By.ID,"profession-1")
    AUTOMATION_TOOLS_CHECKBOX_SELENIUM = (By.ID,"tool-2")
    CONTINENTS_DROPDOWN = (By.ID,"continents")
    SELENIUM_COMMANDS_DROPDOWN =(By.ID,"selenium_commands")
    SUBMIT_BUTTON = (By.ID,"submit")

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get("https://www.techlistic.com/p/selenium-practice-form.html")
        WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located((By.ID, "ez-accept-all"))).click()

    def tearDown(self):
        self.chrome.quit()

    # @unittest.skip
    def test_check_title(self):  # keyword-ul test este obligatoriu pentru numele metodelor
        expected_title = "Demo Sign-Up Selenium Automation Practice Form"
        actual_title = self.chrome.find_element(By.XPATH,"//a[@name='3077692503353518311']//following-sibling::h3").text
        assert expected_title == actual_title, f"The title is wrong. Expected {expected_title}, found {actual_title}"
        print(f"The title is correct: {actual_title}")

    def test_check_url(self):
        self.chrome.find_element(*self.JAVA_TUTORIAL_LINK).click() # caracterul * din fata semnifica actiunea de despachetare a tuplului
        # self.chrome.find_element((By.LINK_TEXT,"Java Tutorial")) - gresit
        # self.chrome.find_element(By.LINK_TEXT,"Java Tutorial") - corect
        WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located((By.ID, "cookieChoiceDismiss"))).click()
        expected_url = "https://www.techlistic.com/p/java.html"
        actual_url = self.chrome.current_url  # metoda care extrage url-ul de pe pagina pe care suntem in momentul rularii
        assert expected_url == actual_url, f"Error: incorrect URL. Expected: {expected_url} Actual: {actual_url}"
        print(f"The URL is correct: {actual_url}")

    def test_complete_form(self):
        WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located((By.ID, "cookieChoiceDismiss"))).click()
        self.chrome.find_element(*self.FIRST_NAME_INPUT).send_keys("Bogdan")
        sleep(2)
        self.chrome.find_element(*self.LAST_NAME_INPUT).send_keys("Mihalcea")
        sleep(2)
        self.chrome.find_element(*self.GENDER_MALE_RADIO_BUTTON).click()
        sleep(2)
        self.chrome.find_element(*self.YEAR_OF_EXPERIENCE_1_RADIO_BUTTON).click()
        sleep(2)
        self.chrome.find_element(*self.PROFFESSION_CHECKBOX).click()
        sleep(2)
        self.chrome.find_element(*self.AUTOMATION_TOOLS_CHECKBOX_SELENIUM).click()
        sleep(2)
        continents = Select(self.chrome.find_element(*self.CONTINENTS_DROPDOWN))
        sleep(2)
        continents.select_by_visible_text("Australia")
        sleep(2)
        selenium_commands = Select(self.chrome.find_element(*self.SELENIUM_COMMANDS_DROPDOWN))
        sleep(2)
        selenium_commands.select_by_visible_text("Wait Commands")
        sleep(2)
        self.chrome.find_element(*self.SUBMIT_BUTTON).click()
        sleep(2)







