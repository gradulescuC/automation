import time
from selenium import webdriver
from selenium.webdriver.common.by import By

user = (By.ID,"username")
pwd = (By.ID,"password")
login = (By.CLASS_NAME,"radius")
logout = (By.CLASS_NAME,"button")
text_field=(By.CLASS_NAME,"subheader")

driver = webdriver.Chrome("/Users/gradulescu/Desktop/Personal/Cursuri/ITF/Automation Course/RepositoryGithub/PythonAutomation/04 - selenium_workshop_pom/resources/chromedriver")
driver.get("https://the-internet.herokuapp.com/login")
time.sleep(1)
# driver.find_element(*user).send_keys("tomsmith")
driver.find_element(By.ID,"username").send_keys("tomsmith")
driver.find_element(*pwd).send_keys("SuperSecretPassword!")
driver.find_element(*login).click()

driver.refresh()
time.sleep(5)

driver.find_element(*logout).click()
content = driver.find_element(*text_field).text
print(content)
driver.quit()

# TODO: Adaugati urmatorul cod (inainte de driver.quit() si analizati rezultatul:
#           driver.refresh()
#           content = driver.find_element(*text_field).text
#           print(content)
# TODO: De extras din intregul text (content) username-ul si parola, si sa le transmitem dinamic in username si password
# TODO: De generat niste scripturi cu ide-ul din chrome si de adaptat astfel incat sa puteti sa reproduceti activitatea din browser
# TODO: https://www.openstreetmap.org -> De introdus date in box-ul de cautare sa cautam dupa adresa, apoi sa dati click pe butonul de rute in care sa definim start point si destination sa cautati distanta intre doua locatii
# TODO: Aditional: sa luati distanta si durata de mai sus si sa o afisati in consola