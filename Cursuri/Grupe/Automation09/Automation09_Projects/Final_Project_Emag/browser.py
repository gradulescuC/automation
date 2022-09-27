import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class Browser(unittest.TestCase):
    s = Service(ChromeDriverManager().install())
    chrome = webdriver.Chrome(service=s)
    chrome.maximize_window()
    chrome.implicitly_wait(5)
    chrome.set_page_load_timeout(10)
    chrome.maximize_window()

    def close(self):
        self.chrome.quit()