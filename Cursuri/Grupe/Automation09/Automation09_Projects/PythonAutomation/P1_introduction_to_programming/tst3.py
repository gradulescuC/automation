# avem nevoie sa importam cateva librarii gratuite care ne ajuta sa controlam chrome
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
#maximizam fereastra
chrome.maximize_window()

# # navigam catre un url
chrome.get('https://automationpractice.com/')

# selector by CSS - ID
# chrome.find_element(By.CSS_SELECTOR, '#search_query_top').send_keys('shoes')
# chrome.find_element(By.CSS_SELECTOR, '.search_query').send_keys('shoes')
chrome.find_element(By.CSS_SELECTOR,'input[placeholder="Search"').send_keys('shoes')

sleep(3)
chrome.quit()