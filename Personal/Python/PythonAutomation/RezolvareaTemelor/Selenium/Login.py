import time

from selenium.webdriver.common.by import By
from selenium import webdriver

user = (By.ID,"username")
pwd = (By.ID,"password")
login = (By.CLASS_NAME,"radius")
logout = (By.CLASS_NAME,"button")
text_field = (By.CLASS_NAME,"subheader")
driver = webdriver.Chrome("/Users/gradulescu/Desktop/Personal/Cursuri/ITF/Automation Course/RepositoryGithub/PythonAutomation/04 - selenium_workshop_pom/resources/chromedriver")
driver.get("https://the-internet.herokuapp.com/login")
time.sleep(1)
content = driver.find_element(*text_field).text

list_of_words = content.split(".")
print(list_of_words)

second_split=list_of_words[1].split()
get_username=second_split[1]
get_pwd=second_split[6]

print(get_username)
print(get_pwd)

driver.find_element(*user).send_keys(get_username)
driver.find_element(*pwd).send_keys(get_pwd)
driver.find_element(*login).click()
driver.quit()