from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())
chrome.maximize_window()
chrome.get("https://www.saucedemo.com/")

chrome.find_element(By.ID,"user-name").send_keys("incorrect_user")
chrome.find_element(By.ID,"password").send_keys("secret_sauce")
chrome.find_element(By.ID,"login-button").click()
error_message = chrome.find_element(By.XPATH,"//h3[@data-test='error']").text
print(error_message)