from behave import *

@given("Home Page: I am on Ebay homepage")
def step_impl(context):
		context.home_page_object.navigate_to_homepage()

@when('Home Page: I search "{product_name}" from category "{category_name}"')
def step_impl(context,product_name,category_name):
		context.home_page_object.insert_search_value(product_name)
		context.home_page_object.choose_category(category_name)
		context.home_page_object.click_search_button()

@then('Home Page: I have at least "{number_of_results}" results returned')
def step_impl(context,number_of_results):
		context.home_page_object.check_search_results(number_of_results)

@when('Home Page: When I click on the Advanced link')
def step_impl(context):
		context.home_page_object.click_advanced_search_link()
