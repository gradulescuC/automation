# avem nevoie sa importam cateva librarii gratuite care ne ajuta sa controlam chrome
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

# maximizam fereastra
chrome.maximize_window()

chrome.get("https://the-internet.herokuapp.com/login")

chrome.find_element(By.XPATH, "//button[@class='radius']").click()
chrome.find_element(By.XPATH, "//a[@class='close']").click()
sleep(1000)
# mesaj = chrome.find_element(By.XPATH,"//div[@id='flash-messages']/div[@id='flash']").text
# print(mesaj)
