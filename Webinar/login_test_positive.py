# importam selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# initializam chrome
from webdriver_manager.chrome import ChromeDriverManager

# Deschidem browserul chrome
chrome = webdriver.Chrome(executable_path= ChromeDriverManager().install())
sleep(3)

# # maximizam fereastra
chrome.maximize_window()

# # navigam catre un url
chrome.get('https://the-internet.herokuapp.com/login')
sleep(2)


# # completam username
chrome.find_element(By.ID,'username').send_keys('tomsmith')
sleep(3)

# # completam parola
chrome.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
sleep(3)

# # dam click pe login
chrome.find_element(By.XPATH, '//button[@type="submit"]').click()
sleep(3)

# # verificam ca am ajuns pe pagina secure
url = chrome.current_url
assert url == 'https://the-internet.herokuapp.com/secure', "Error, invalid URL loaded"
sleep(3)




# # verificam mesajul de login
# expected_msg = chrome.find_element(By.XPATH, '//div[@id="flash"]').text
# assert expected_msg.__contains__('You logged into a secure area!')
#
# # dam click pe logout
# chrome.find_element(By.XPATH, '//*[@id="content"]/div/a/i').click()
# sleep(3)
#
# # verificam ca am ajuns inapoi pe pagina de login
# url = chrome.current_url
# assert url == 'https://the-internet.herokuapp.com/login'
#
# # verificam mesajul de logout
# expected_msg = chrome.find_element(By.XPATH, '//div[@id="flash"]').text
# assert expected_msg.__contains__('You logged out of the secure area!')
#
# # inchidem chrome
# chrome.quit()
#
# # daca a trecut testul, printam in consola un mesaj de succes
# print('SUCCESS - TEST PASSED')