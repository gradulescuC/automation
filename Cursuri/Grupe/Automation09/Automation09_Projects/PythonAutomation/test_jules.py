from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.get("https://jules.app/sign-up")
sleep(2)
chrome.maximize_window()
sleep(1)
chrome.find_element(By.XPATH,'//input[@value="personal"]').click()
sleep(1)
chrome.find_element(By.XPATH,"//button[@data-test-id='select-account-continue-btn']").click()
sleep(2)
chrome.find_element(By.XPATH,'//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div/input').send_keys("abc")
chrome.find_element(By.XPATH,"//button[@data-test-id='first-name-continue-btn']").click()
sleep(2)
chrome.find_element(By.XPATH,'//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div/input').send_keys("def")
chrome.find_element(By.XPATH,"//div[@id='root']/div/div[4]/div[2]/div/div[3]/button[@data-test-id='last-name-continue-btn']").click()

# chrome.find_element(By.XPATH,"//tab-container/div/button").click()