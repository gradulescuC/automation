from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initializam chrome
s = Service(ChromeDriverManager().install()) # Stocam serviciul de chrome
chrome = webdriver.Chrome(service=s) # definirea unei variabile care va stoca driverul de chrome

# maximizam fereastra
chrome.maximize_window() # este o metoda folosita pentru maximizarea browserului
chrome.get('http://automationpractice.com/index.php') # metoda get este o metoda prin care putem naviga la un anumit link


'''
contoruri:
id: 1
name: 1
class: 1
'''

sleep(4)
search_bar = chrome.find_element(By.ID,"search_query_top")
search_bar.click()
search_bar.send_keys("faded")
submit_search_button = chrome.find_element(By.NAME,"submit_search").click()
sleep(5)
chrome.find_element(By.CLASS_NAME,"product_img_link").click()
chrome.find_element(By.XPATH,"title='Close'").click()

# //div/a[@title="Faded Short Sleeve T-shirts"]
# //a[@title="Faded Short Sleeve T-shirts"]/img
# [class="product_img_link"]