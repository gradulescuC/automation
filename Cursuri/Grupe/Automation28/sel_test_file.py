# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
# import Action chains 
from selenium.webdriver.common.action_chains import ActionChains
# create webdriver object
driver = webdriver.Chrome()
# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")
# get element 
element = driver.find_element(By.LINK_TEXT,"Courses")
# create action chain object
action = ActionChains(driver)
# double click the item
action.double_click(on_element=element)
# perform the operation
action.perform()