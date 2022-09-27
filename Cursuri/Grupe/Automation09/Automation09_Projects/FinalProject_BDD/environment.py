from pages.sign_in_page import Sign_in_page
from browser import Browser
from pages.forgot_password_page import Forgot_password_page
from pages.sign_up_page import Sign_up_page


def before_all(context):
    context.browser = Browser()
    context.sign_in_page = Sign_in_page()
    context.forgot_pass = Forgot_password_page()
    context.sign_up_page = Sign_up_page()

def after_all(context):
    context.browser.close()

    # contextul e ca o cutiuta care contine cate un obiect de tipul fiecarei clase de pagini
    # de fiecare data cand adaugam o pagina noua in proiect, o vom adauga in context

    # before_all = nume de metoda standardizat care instruieste sistemul ca acele instructiuni trebuie executate intotdeauna
                    # inainte de excutarea unui scenariu