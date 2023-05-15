import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

context_menu = (By.CSS_SELECTOR,"#content > ul > li:nth-child(7) > a")
context_btn=(By.ID,"hot-spot")
driver = webdriver.Chrome("/Users/gradulescu/Desktop/Personal/Cursuri/ITF/Automation Course/RepositoryGithub/PythonAutomation/04 - selenium_workshop_pom/resources/chromedriver")
driver.get("https://the-internet.herokuapp.com")

driver.find_element(*context_menu).click()
driver.find_element(*context_btn).click()

action = ActionChains(driver)
action.context_click(driver.find_element(*context_btn)).perform()
time.sleep(3)
driver.switch_to.alert.dismiss()
driver.quit()