from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(executable_path= ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://formy-project.herokuapp.com/form")
driver.find_element(By.CLASS_NAME,"form-control").send_keys("First name is identified by class")
driver.find_elements(By.CLASS_NAME,"form-control")[1].send_keys("Last name is identified by class in list")
driver.find_elements(By.CLASS_NAME,"form-control")[2].send_keys("Job identified by class in list")

# lista_elemente_form_control = driver.find_elements(By.CLASS_NAME,"form-control")
# lista_elemente_form_control[1].send_keys("Last name is identified by class in list")
# lista_elemente_form_control[2].send_keys("Job identified by class in list")