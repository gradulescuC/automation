import time

from selenium.webdriver.common.by import By
from selenium import webdriver

auth_btn = (By.CSS_SELECTOR,"#content > ul > li:nth-child(3) > a")
driver = webdriver.Chrome("/Users/gradulescu/Desktop/Personal/Cursuri/ITF/Automation Course/RepositoryGithub/PythonAutomation/04 - selenium_workshop_pom/resources/chromedriver")
driver.get("https://the-internet.herokuapp.com")

driver.find_element(*auth_btn).click()

usr="admin"
pwd = "admin"

driver.get("https://" +usr + ":" + pwd + "@the-internet.herokuapp.com/basic_auth")
if driver.title=="The Internet":
    print("Test passed")

driver.back()
driver.back()
driver.quit()