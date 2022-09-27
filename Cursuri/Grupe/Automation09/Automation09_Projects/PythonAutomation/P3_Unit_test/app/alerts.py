from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class Alerts():
    ALERT = (By.XPATH, '//button[text()="Click for JS Alert"]')
    CONFIRM = (By.XPATH, '//button[text()="Click for JS Confirm"]')
    PROMPT = (By.XPATH, '//button[text()="Click for JS Prompt"]')


    def alert_method(self):
        self.s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(5)
        self.chrome.get("https://the-internet.herokuapp.com/javascript_alerts")
        self.chrome.find_element(*self.ALERT).click()
        # Switch the control to the Alert window
        obj = self.chrome.switch_to.alert
        # Retrieve the message on the Alert window
        msg = obj.text
        print("Alert shows following message: " + msg)
        sleep(3)
        # use the accept() method to accept the alert
        obj.accept() # metoda accept reprezinta echivalentul clickului pe butonul "OK" din alerta
        print("Clicked on the OK Button in the Alert Window")
