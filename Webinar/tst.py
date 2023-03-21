from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager



def test_parola():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://the-internet.herokuapp.com/login")
    user3 = driver.find_element(By.ID,"username").send_keys("tomsmith")
    parole = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/h4').text.split()
    list_parole = list(parole)
    pwd2 = driver.find_element(By.ID,"password")
    login3 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/form/button')
    for i, parola in enumerate(list_parole):
        pwd2.send_keys(parola)
        login3.click()
        try:
            WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="flash"]'))
            )
            print(f"Parola {parola} nu a functionat!")
        except NoSuchElementException:
            print(f"Parola {parola} a functionat!")