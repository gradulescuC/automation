# importam selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# initializam chrome
from webdriver_manager.chrome import ChromeDriverManager

chrome = webdriver.Chrome(executable_path= ChromeDriverManager().install())

# maximizam fereastra
chrome.maximize_window()

# navigam catre un url
chrome.get('https://the-internet.herokuapp.com/login')

# cu sleep putem pune pauza de cateva secunde sa asteptam sa vedem si noi ceva
sleep(3)

# completam username
chrome.find_element(By.ID, 'username').send_keys('tomsmith')
sleep(3)

# completam parola
chrome.find_element(By.ID, 'password').send_keys('SuperSecretPassword')
sleep(3)

# dam click pe login
chrome.find_element(By.XPATH, '//*[@id="login"]/button/i').click()
sleep(3)

# verificam ca am ramas pe pagina de login
url = chrome.current_url
assert url == 'https://the-internet.herokuapp.com/login'

# verificam mesajul de eroare (parola gresita)
expected_msg = chrome.find_element(By.XPATH, '//div[@id="flash"]').text
assert expected_msg.__contains__('Your password is invalid!')

# inchidem chrome
chrome.quit()

# daca a trecut testul, printam in consola un mesaj de succes
print('SUCCESS - TEST PASSED')