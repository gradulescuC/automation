from browser import Browser

# before all este o metoda care contine instructiuni ce trebuie executate inaintea TUTUROR testelor
from pages.login_page import Login_page


def before_all(context):
		context.browser = Browser()
		context.login_page = Login_page()
		# context este ca o cutiuta in care stochez toate obiectele instantiate in clasa environment

# after all este o metoda care contine instructiuni ce trebuie executate dupa TOATE testele
def after_all(context):
		context.browser.close()