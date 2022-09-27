import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Chrome("/Users/gradulescu/Desktop/Personal/Cursuri/ITF/Automation Course/Proiecte Python/RepositoryGithub/PythonAutomation/venv/04 - selenium_workshop_pom/resources/chromedriver")
driver.get("https://www.openstreetmap.org")

searchbar = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form[1]/div/div[1]/div/div[1]/input")
go_btn = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form[1]/div/div[1]/div/div[2]/input")
route_btn = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form[1]/div/div[2]/a")
from_bar = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form[2]/div[2]/div[2]/input")
to_bar = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form[2]/div[3]/div[2]/input")
go_btn_route = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form[1]/div/div[2]/a/img")
calculate = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form[2]/div[4]/div[2]/input")


print("Element is visible? " + str(searchbar.is_displayed()))
print("Element is visible? " + str(go_btn.is_displayed()))

searchbar.send_keys("Kogalniceanu Street Bucharest")
go_btn.click()
go_btn_route.click()
from_bar.send_keys("Bucharest")
to_bar.send_keys("Lengerich")
calculate.click()
time.sleep(5)
distance = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[5]/p[1]")
# distance = driver.find_element(By.XPATH, "//*[@id='sidebar_content']/p[1]")
print(distance.text)
driver.quit()