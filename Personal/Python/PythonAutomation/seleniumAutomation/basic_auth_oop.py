import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAuth(unittest.TestCase):
    auth_btn = (By.CSS_SELECTOR, "#content > ul > li:nth-child(3) > a")

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(
            "/Users/gradulescu/Desktop/Personal/Cursuri/ITF/Automation Course/RepositoryGithub/PythonAutomation/04 - selenium_workshop_pom/resources/chromedriver")
        self.driver.get("https://the-internet.herokuapp.com/")

    def test_auth(self):
        self.driver.find_element(*self.auth_btn).click()
        usr = "admin"
        pwd = "admin"

        self.driver.get("https://" + usr + ":" + pwd + "@the-internet.herokuapp.com/basic_auth")

        if self.driver.title == "The Internet":
            print("Test passed")

        self.driver.back()
        self.driver.back()

    def tearDown(self) -> None:
        time.sleep(3)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()  # Daca fisierul e rulat din locatia curenta, sa il vada ca pe un unit test, nu ca pe un python script



