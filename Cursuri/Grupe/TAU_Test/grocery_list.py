import time
import unittest
import HtmlTestRunner
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as EC

class MyTests(unittest.TestCase):

    def setUp(self) -> None:
        self.firefox = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.firefox.get("https://formy-project.herokuapp.com/")
        self.firefox.maximize_window()
        self.firefox.implicitly_wait(3)

    def tearDown(self) -> None:
        self.firefox.quit()

    def test_dragdrop_img_in_box(self):
        self.firefox.find_element(By.LINK_TEXT, "Drag and Drop").click()
        elem1 = WebDriverWait(self.firefox, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="image"]/img')))
        elem2 = WebDriverWait(self.firefox, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="box"]')))
        action = ActionChains(self.firefox)
        action.drag_and_drop(elem1, elem2).perform()
        time.sleep(2)
        expected = "Dropped!"
        actual = self.firefox.find_element(By.XPATH, '//*[@id="box"]/p').text
        self.assertEqual(expected, actual, f"ERROR: Expected {expected}, Actual: {actual}")