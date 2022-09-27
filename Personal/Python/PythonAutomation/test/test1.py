from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.get("https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe#try_it")
sleep(2)
chrome.maximize_window()
sleep(1)
iframe = chrome.find_element(By.XPATH,'//*[@id="content"]/article/section[1]/div/iframe')
chrome.switch_to.frame(iframe)
sleep(1)
chrome.find_element(By.XPATH,"//div[@id='editor-container']/section/div/button[2]").click()
# chrome.find_element(By.XPATH,"//tab-container/div/button").click()