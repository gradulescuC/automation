from browser import Browser

# before_all este o metoda care contine toate instructiunile care trebuie rulate inainte de orice test
# este echivalentul metodei setUp de la libraria unit test
from pages.add_user_page import Add_user_page
from pages.home_page import Home_page
from pages.login_page import Login_page


def before_all(context):
		context.browser = Browser() # instantiem un obiect din clasa Browser
		context.login_page = Login_page() # am instantiat un obiect din clasa Login_page
		context.home_page = Home_page()
		context.add_user_page = Add_user_page()
		context.browser.maximise_window()

# after_all este o metoda care contine toate instructiunile care trebuie rulate inainte de orice test
# este echivalentul metodei tearDown de la libraria unit test
def after_all(context):
		context.browser.close_browser() # apelam metoda close_browser pe baza obiectului instantiat din clasa Browser()
