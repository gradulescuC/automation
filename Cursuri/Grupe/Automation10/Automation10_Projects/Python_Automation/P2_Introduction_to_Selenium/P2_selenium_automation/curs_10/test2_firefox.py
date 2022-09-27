from time import sleep
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
# s = Service(ChromeDriverManager().install())
# self.chrome = webdriver.Chrome(service=s)

driver.maximize_window()

driver.get('https://formy-project.herokuapp.com/form')

first_name = driver.find_element(By.ID, 'first-name')
first_name.send_keys('Gabriela')

sleep(3)
driver.quit()

'''
pt alte browsere
https://pypi.org/project/webdriver-manager/#use-with-firefox
'''