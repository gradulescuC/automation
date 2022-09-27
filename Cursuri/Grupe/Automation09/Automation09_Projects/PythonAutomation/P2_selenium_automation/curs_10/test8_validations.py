import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Test_validations(unittest.TestCase):

    def setUp(self) -> None:
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.get("https://formy-project.herokuapp.com/form")
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(5)

    def tearDown(self):
        self.chrome.quit()

    def test_url(self):
        actual = self.chrome.current_url
        expected = 'https://formy-project.herokuapp.com/forms'
        # expected value, actual value, mesaj in caz de fail
        self.assertEqual(expected, actual, 'URL is incorrect')


# https://the-internet.herokuapp.com/key_presses