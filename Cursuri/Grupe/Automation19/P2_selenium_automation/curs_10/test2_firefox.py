import unittest
from time import sleep
from selenium import webdriver
from webdriver_manager.drivers.edge import EdgeChromiumDriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService


from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class Firefox(unittest.TestCase):

    USERNAME = (By.ID,'username')
    PASSWORD = (By.ID, 'password')
    SUBMIT_BUTTON = (By.CLASS_NAME,"radius")
    SUCCESS_MESSAGE = (By.ID,"flash")
    LOGOUT_BUTTON = (By.CLASS_NAME,"secondary")

    def setUp(self) -> None:
        self.driver = driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        # s = Service(ChromeDriverManager().install())
        # self.chrome = webdriver.Chrome(service=s)
        self.driver.maximize_window()
        self.driver.get('https://the-internet.herokuapp.com/login')

    def tearDown(self) -> None:
        self.driver.quit()

    # @positiveTesting @functionalTesting
    # Testare pozitiva = tip de testare in care verificam comportamentul sistemului cu inputuri pe care ar trebui sa le poata procesa
    # Testare negativa = tip de testare in care verificam comportamentul sistemului cu inputuri pe care ar trebui sa nu le poata procesa
    # Testare functionala = tip de testare in care verificam daca sistemul isi indeplineste functiile
    # Testare non-functionala = tip de testare in care verificam CAT DE BINE isi indeplineste sistemul functiile (performance, stress testing, load testing, volume testing, usability testing, localization testing, compatibility testing etc)

    def test_login_user_is_correct(self):
        self.driver.find_element(*self.USERNAME).send_keys("tomsmith")
        sleep(3)

        self.driver.find_element(*self.PASSWORD).send_keys("SuperSecretPassword!")
        sleep(3)

        self.driver.find_element(*self.SUBMIT_BUTTON).click()
        actual_message = self.driver.find_element(*self.SUCCESS_MESSAGE).text.replace("\n","").replace("×","")
        expected_message = "You logged into a secure area"
        print(f"Actual message is {actual_message}")
        print(f"Expected message is {expected_message}")
        sleep(3)
        assert actual_message == expected_message, "Error: Logarea nu s-a facut cu succes"

    def test_logout(self):
        self.driver.find_element(*self.USERNAME).send_keys("tomsmith")
        self.driver.find_element(*self.PASSWORD).send_keys("SuperSecretPassword!")
        self.driver.find_element(*self.SUBMIT_BUTTON).click()
        self.driver.find_element(*self.LOGOUT_BUTTON).click()
        assert self.driver.find_element(*self.SUBMIT_BUTTON).is_displayed()==True,"Error: Delogarea nu s-a facut corect"



'''
pt alte browsere
https://pypi.org/project/webdriver-manager/#use-with-firefox
'''