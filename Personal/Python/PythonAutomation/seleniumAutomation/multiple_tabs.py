import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestMultipleTabs(unittest.TestCase):
    multiple_tabs = (By.CSS_SELECTOR,"#content > ul > li:nth-child(33) > a")
    multiple_tabs_btn = (By.CSS_SELECTOR,"#content > div > a")

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(
            "/Users/gradulescu/Desktop/Personal/Cursuri/ITF/Automation Course/RepositoryGithub/PythonAutomation/04 - selenium_workshop_pom/resources/chromedriver")
        self.driver.get("https://the-internet.herokuapp.com")

    def test_multiple_tabs(self):
        self.driver.find_element(*self.multiple_tabs).click()
        time.sleep(1)
        self.driver.find_element(*self.multiple_tabs_btn).click()
        time.sleep(2)
        one = self.driver.window_handles[0]
        two = self.driver.window_handles[1]
        i = 0
        while i<100:
            self.driver.switch_to.window(one)
            self.driver.switch_to.window(two)
            i+=1
            print(i)

    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()