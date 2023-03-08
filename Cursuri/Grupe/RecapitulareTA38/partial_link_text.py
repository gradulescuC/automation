import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

"""
link text = textul care este pus peste un link
linkurile pe un site sunt definite prin intermediul unei ancore (tag-ul a)
un element de tip ancora are urmatoarele componente:
1. tag-ul de inceput (a)
2. linkul catre care se face navigarea (href = "valoare")
3. textul care este afisat peste link (linktext)
4. tag-ul de sfarsit (/a)
<a href="/checkboxes">Checkboxes</a>
"""
chrome = webdriver.Chrome(executable_path= ChromeDriverManager().install())
time.sleep(3)
chrome.maximize_window()
chrome.get("https://the-internet.herokuapp.com/")

"""
Partial link text este o modalitate prin care putem sa identificam elemente de tip ancora
pe baza unei bucati din textul care este scris peste link
"""

time.sleep(2)
# chrome.find_element(By.LINK_TEXT,"Form").click() -> va returna eroare pentru ca nu gaseste elementul de tip ancora care sa contina textul "Form"
chrome.find_element(By.PARTIAL_LINK_TEXT,"Form").click()
chrome.quit()