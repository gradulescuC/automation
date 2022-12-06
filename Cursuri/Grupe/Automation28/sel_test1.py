import time
from selenium import webdriver
from selenium.webdriver.common.by import By
chrome = webdriver.Chrome()
chrome.maximize_window()
chrome.get("http://elementalselenium.com")
time.sleep(2)
chrome.find_element(By.NAME,"fields[programming_language]").click()
time.sleep(1)
optiuni = chrome.find_elements(By.TAG_NAME,"option")
optiuni[4].click()
time.sleep(4)
