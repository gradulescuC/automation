from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())

# cu metoda get putem sa deschidem un site
chrome.get("https://www.elefant.ro/")
chrome.maximize_window()
sleep(3)
try:
		accept_cookies_button = chrome.find_element(By.ID,"CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
		accept_cookies_button.click()
		assert accept_cookies_button.text == "ACCEPT"
except:
		pass

"""
Link text este pe scurt textul care este pus peste un link

a) <a href="link catre care navigam">link text</a> -> a este prescurtarea de la ancora si este o legatura catre o alta pagina (link)
"""

# chrome.find_element(By.LINK_TEXT,"Contact").click()
# assert chrome.current_url=="https://www.elefant.ro/helpdesk/contact-us","Error, the url is not correct"

chrome.find_element(By.PARTIAL_LINK_TEXT,"ANSPDCP").click()
assert chrome.current_url == "https://www.elefant.ro/anspdcp:-comunicate-gdpr-cms-page.helpdesk.ANSPDCP","Error, the GDPR url is not correct"

# Instructiunea de mai returneaza eroare: unable to locate element pentru ca nu exista niciun element care sa aiba textul complet "ANSPDCP"
chrome.find_element(By.LINK_TEXT,"ANSPDCP").click()
