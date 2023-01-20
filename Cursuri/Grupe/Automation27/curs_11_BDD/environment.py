from browser import Browser
from pages.inventory_page import Inventory_page
from pages.login_page import Login_page


# before all este o metoda care contine instructiuni ce trebuie executate inaintea TUTUROR testelor
def before_all(context):
		context.browser = Browser()
		context.login_page_object = Login_page()
		context.inventory_page_object = Inventory_page()
		# context este ca o cutiuta in care stochez toate obiectele instantiate in clasa environment

# after all este o metoda care contine instructiuni ce trebuie executate dupa TOATE testele
def after_all(context):
		context.browser.close()
