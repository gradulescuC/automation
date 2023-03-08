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

href = hyperlink reference
"""

chrome = webdriver.Chrome(executable_path= ChromeDriverManager().install())
time.sleep(3)
chrome.maximize_window()
chrome.get("https://the-internet.herokuapp.com/")
chrome.find_element(By.LINK_TEXT,"Checkboxes").click()

"""
Am identificat elementul dupa textul Checkbox care este pus peste linkul https://the-internet.herokuapp.com/checkboxes
				Ne ajuta sa avem o identificare mai usoara a elementelor de tip ancora pentru a putea interactiona cu ele
"""

time.sleep(2)
chrome.back() # back este o functie prin intermediul careia putem sa apasam pe sagetica de back de la browser
time.sleep(2)
chrome.find_element(By.LINK_TEXT,"Form Authentication").click()
chrome.quit()