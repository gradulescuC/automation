from behave import *

@when('Advanced Search Page: I type "{product_name}" in the enter keyboard textbox')
def step_impl(context,product_name):
		context.advanced_search_page_object.enter_keywords_or_item_number(product_name)

@when('Advanced Search Page: I choose "{keyword_options}" from the list')
def step_impl(context,keyword_options):
		context.advanced_search_page_object.select_keywords_options(keyword_options)

@when('Advanced Search Page: I choose "{category_name}" from the category list')
def step_impl(context,category_name):
		context.advanced_search_page_object.select_category_from_dropdown(category_name)

@when('Advanced Search Page: I click search button')
def step_impl(context):
		context.advanced_search_page_object.click_search_button()