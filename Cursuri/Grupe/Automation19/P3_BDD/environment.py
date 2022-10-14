from browser import Browser
from pages.advanced_search_page import Advanced_search_page
from pages.home_page import Home_page

def before_all(context):
		context.browser = Browser()
		context.home_page_object = Home_page()
