from pages.base_page import Base_page
from pages.sign_in_page import Sign_in_page

class Test_sign_in(Base_page):

    def setup_method(self):
        self.chrome.get("https://jules.app/")
        self.set_email = Sign_in_page()


    def test_set_email(self):
        self.set_email.set_email('abc@gmail.com')