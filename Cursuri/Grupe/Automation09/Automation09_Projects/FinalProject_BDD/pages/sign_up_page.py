from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from pages.base_page import Base_page
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Sign_up_page(Base_page):
    SIGN_UP = (By.XPATH,'//*[@id="root"]/div/div[2]/form/div/div[4]/a')
    LAST_NAME_CONTINUE_BUTTON = (By.XPATH,"//div[@id='root']/div/div[4]/div[2]/div/div[3]/button[@data-test-id='last-name-continue-btn']")
    LAST_NAME = (By.XPATH,'//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div/input')
    FIRST_NAME_CONTINUE_BUTTON = (By.XPATH,'//button[@data-test-id="first-name-continue-btn"]')
    FIRST_NAME = (By.XPATH,'//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div/input')
    CONTINUE_BUTTON = (By.XPATH,'//button[@data-test-id="select-account-continue-btn"]')
    PERSONAL_BUTTON=(By.XPATH,'//input[@value="personal"]')

    def navigate_sign_up_page(self):
        self.chrome.find_element(*self.SIGN_UP).click()

    def click_personal_button(self):
        self.chrome.find_element(*self.PERSONAL_BUTTON).click()

    def click_continue_button(self):
        sleep(2)
        self.chrome.find_element(*self.CONTINUE_BUTTON).click()

    def input_first_name(self,name):
        self.chrome.find_element(*self.FIRST_NAME).send_keys(name)

    def click_continue_first_name_button(self):
        self.chrome.find_element(*self.FIRST_NAME_CONTINUE_BUTTON).click()

    def input_last_name(self,last_name):
        self.chrome.find_element(*self.LAST_NAME).send_keys(last_name)

    def click_last_name_continue_button(self):
        self.chrome.find_element(*self.LAST_NAME_CONTINUE_BUTTON).click()

    def input_email(self,email):
        self.chrome.find_element(*self.LAST_NAME).send_keys(email)

    def check_error_message_email(self):
        expected = 'Please enter a valid email address'
        actual=self.chrome.find_element(By.XPATH,'//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/p')
        self.assertEqual(expected,actual,'the error is different')

    def click_sign_up_button(self):
        self.chrome.find_element(*self.SIGN_UP).click()