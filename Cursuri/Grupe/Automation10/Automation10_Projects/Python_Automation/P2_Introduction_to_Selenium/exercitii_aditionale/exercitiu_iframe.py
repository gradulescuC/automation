from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.maximize_window()
chrome.get("https://www.techlistic.com/p/selenium-practice-form.html")
# lista_elemente_text= chrome.find_elements(By.TAG_NAME,"textarea")

# Am acceptat cookie-urile Privacy & Transparency
WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.ID, "ez-accept-all"))).click()

#  Am acceptat cookie-urile in germana
WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.ID, "cookieChoiceDismiss"))).click()

# Am identificat frame-ul in care se afla elementul de tip comentariu si ne-am mutat in el
iframe = chrome.find_element(By.ID,"comment-editor")
chrome.switch_to.frame(iframe)

sleep(3)

# Am definit o lista cu toate elementele cu tag-ul textare de pe iframe-ul in care ne-am mutat
lista_elemente_text = chrome.find_elements(By.TAG_NAME,"textarea")

# am verificat cate elemente au fost gasite (in total 2)
print(len(lista_elemente_text))

# Am accesat primul element din lista care este fix cel cu comentariul si am scris in el textul "My Comment"
lista_elemente_text[0].send_keys("My Comment")


# Metoda alternativa de a identifica elementul de tip comment (comment textbox) pe baza e Xpath
# comment = chrome.find_element(By.XPATH,"//textarea[@jsname='YPqjbf']")
# comment.send_keys("My comment")
