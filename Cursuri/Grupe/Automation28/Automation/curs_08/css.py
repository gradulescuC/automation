from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://formy-project.herokuapp.com/form")
"""
cum sa gandim css selector?
1. # inseamna cautare dupa id
2. . inseamna cautare dupa clasa
3. daca precedam # sau . de numele unui tag, atunci sistemul va cauta elementele cu tag-ul respectiv si id-ul / clasa in scop
4. putem sa cautam elemente cu un anumit tag cu filtrare de tipul atribut = valoare
5. Putem sa cautam primul copil al unui element cu caracterul > 
6. Putem sa cautam orice copil al unui element daca specificam tag-ul copilului care ne intereseaza separat prin spatiu de parinte
7. Daca vrem sa cautam primul copil al unui element putem sa specificam first-of-type
8. Daca vrem sa cautam ultimul copil al unui element putem sa specificam last-of-type
9. Daca nu este nici primul nici ultimul, putem sa folosim nth-of-type(al_catalea_element_este)
10. Daca vrem sa gasim un frate al elementului ne folosim de caracterul +

Referinte css selector: https://www.w3schools.com/cssref/css_selectors.php

"""
driver.find_element(By.CSS_SELECTOR,"#first-name").send_keys("Anton")
driver.find_element(By.CSS_SELECTOR,"#last-name").send_keys("Pann")
driver.find_elements(By.CSS_SELECTOR,".form-control")[2].send_keys("Tester")
driver.find_elements(By.CSS_SELECTOR,".form-control")[2].clear()
driver.find_elements(By.CSS_SELECTOR,"input[type='text']")[2].send_keys("Tester Dupa Clear")
first_name_text = driver.find_elements(By.CSS_SELECTOR,"strong > label")[0].text
print(first_name_text)
studies_text = driver.find_elements(By.CSS_SELECTOR,"div label")[3].text
print(studies_text)
assert studies_text == "Highest level of education"
driver.find_element(By.CSS_SELECTOR,"div.input-group>div:nth-of-type(2) input").click()
driver.find_element(By.CSS_SELECTOR,"div.input-group>div:last-of-type input").click()
driver.find_element(By.CSS_SELECTOR,"div.form-group>div:first-of-type input").send_keys("first of type")
text_sex = driver.find_elements(By.CSS_SELECTOR,"div.input-group>div:first-of-type label")[1].text
print(text_sex)
assert text_sex == "Sex",f"Expected: Sex, Actual {text_sex}"
driver.find_element(By.CSS_SELECTOR,"div.form-group > div>strong+input").send_keys("following sibling")
sleep(3)
driver.quit()