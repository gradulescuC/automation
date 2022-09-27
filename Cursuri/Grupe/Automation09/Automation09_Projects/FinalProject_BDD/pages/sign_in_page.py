from selenium.webdriver.common.by import By
from pages.base_page import Base_page


class Sign_in_page(Base_page):

    # Sectiune de identificare a elementelor
    EMAIL_INPUT = (By.XPATH,f'//input[@placeholder="Enter your email"]')
    PASS_INPUT= (By.XPATH,f'//input[@placeholder="Enter your password"]')
    LOGIN_BUTTONS = (By.XPATH, '//button[@type="submit"]')
    FORGOT_PASSWORD_LINK= (By.LINK_TEXT,"Forgot password?")

    # sectiune de definire a actiunilor pe care le putem face in raport cu elementele
    def navigate_to_sign_in_page(self):
        self.chrome.get("https://jules.app/")

    def set_email(self,email):
        self.chrome.find_element(*self.EMAIL_INPUT).send_keys(email)

    def set_pass(self,password):
        self.chrome.find_element(*self.PASS_INPUT).send_keys(password)

    def click_login_button(self):
        self.chrome.find_element(*self.LOGIN_BUTTONS).click()

    def click_forgot_password_link(self):
        self.chrome.find_element(*self.FORGOT_PASSWORD_LINK).click()

    def check_current_url(self):
        actual_url = self.chrome.current_url
        expected_url = 'https://jules.app/sign-in'
        self.assertEqual(actual_url,expected_url,"The url does not match")

    # step definition (o agregare de pasi mici care au logica sa fie sub o singura umbrela/functie)
    def user_login(self, email, password):
        self.set_email(email)
        self.set_pass(password)
        self.click_login_button()
