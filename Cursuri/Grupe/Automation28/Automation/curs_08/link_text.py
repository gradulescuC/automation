import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/")
driver.find_element(By.LINK_TEXT,"onload").click()
# driver.find_element(By.LINK_TEXT,"Checkboxes").click()
time.sleep(3)
driver.quit()

"""
Linkurile sunt elemente de tip ancora care contin urmatoarele elemente:
1. Inceputul ancorei (<a)
2. Linkul care va reprezenta pagina catre care se navigheaza
3. Textul care se pune peste link (link text)
4. Sfarsitul ancorei (</a>)
<a href="/checkboxes">Checkboxes</a>
"""