from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://formy-project.herokuapp.com/form")
driver.find_element(By.XPATH,"//input[@placeholder='Enter first name']").send_keys("Anton")
driver.find_element(By.XPATH,"//input[@placeholder='Enter last name']").send_keys("Pann")
driver.find_element(By.XPATH,"//div[@class='form-group']/div/input").send_keys("first name prin navigare")
driver.find_element(By.XPATH,"//form//input[@placeholder='Enter last name']").send_keys("last name prin navigare")
driver.find_elements(By.XPATH,"//input[@class='form-control']")[2].send_keys("test job")
driver.find_element(By.XPATH,"//input[@id='first-names'] | //input[@id='last-nam']").send_keys("element cu | ")

"""
x y axis navigation
1. Navigare din parinte in copil se face cu caracterul /
2. Navigare catre un urmas care nu e urmas direct se face cu caracterul //
3. Putem sa navigam in sus catre parent cu "parent::tag"
4. Putem sa navigam catre urmatorul frate cu "following-sibling::tag"
5. Putem sa navigam catre fratele anterior cu "preceding-sibling::tag"
"""

# //div/form//div[@class="form-group"]//strong/following-sibling::input[@placeholder='Enter first name']/parent::div
# driver.find_elements(By.XPATH,'//div[@class='input-group']//label')[0]
# //div[@class='input-group']//label/parent::strong/parent::div/following-sibling::div/following-sibling::div[2]/preceding-sibling::div[1]
sleep(3)
driver.quit()