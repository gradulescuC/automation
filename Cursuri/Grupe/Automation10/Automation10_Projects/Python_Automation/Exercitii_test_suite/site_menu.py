import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class Site_menu(unittest.TestCase):

    MENU_LIST = (By.XPATH,"//div[@id='page_list_top']/div/div/div/div/div/ul/li[@class='overflowable-item']")
    JAVA_ELEMENT = (By.XPATH,"//div[@id='PageList2']/div/div/div/div/ul/li/a[@href='https://www.techlistic.com/p/java.html']")

    def setUp(self) -> None:
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(5)
        self.chrome.get("https://www.techlistic.com/")

    def tearDown(self) -> None:
        self.chrome.quit()


    def test_extract_menu_items(self):
        lista_elemente = self.chrome.find_elements(*self.MENU_LIST)
        assert len(lista_elemente) == 12, "Error: numarul de optiuni in meniu este inconsistent"
        return lista_elemente


    def test_java_element(self):
        java_option = self.chrome.find_element(*self.JAVA_ELEMENT).text
        assert java_option.lower() == "java","Error: primul element din meniu nu este corect"






