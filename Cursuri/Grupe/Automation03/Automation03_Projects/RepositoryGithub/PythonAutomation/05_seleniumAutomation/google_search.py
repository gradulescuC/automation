import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("/04 - selenium_workshop_pom/resources/chromedriver")

# driver  = element cu care putem avea acces la toate metodele de selenium
driver.get("https://google.ro")
time.sleep(1)
# button = driver.find_element_by_id("L2AGLb")
# button = driver.find_element(By.ID,"L2AGLb")
# button = driver.find_element(By.CLASS_NAME,"jyfHyd") -> Va da eroare pentru ca nu va putea sa identifice elementul avand in vedere ca nu este o clasa unica
button = driver.find_element(By.CSS_SELECTOR,"#L2AGLb > div")
time.sleep(3)
button.click()
search_bar = driver.find_element(By.NAME,"q")
search_bar.send_keys("Flat Earth Society")
search_bar.submit()
time.sleep(2)
driver.quit()

