from behave import *

@given('Home Page: I am on Ebay homepage')
def step_impl(context):
    context.home_page_object.navigate_to_home_page()

@when('Home Page: I search an item')
def step_impl(context):
    context.home_page_object.set_product_search()
    context.home_page_object.click_search_button()

@then('Home Page: I have at least 2 results returned')
def step_impl(context):
    context.home_page_object.check_search_results()

@when('Home Page: I search for "{product_name}" in "{category_name}"')
def step_impl(context,product_name,category_name):
    context.home_page_object.set_product_search_with_parameter(product_name)
    context.home_page_object.choose_category(category_name)
    context.home_page_object.click_search_button()

@then('Home Page: I have at least "{number_of_results}" results returned')
def step_impl(context,number_of_results):
    context.home_page_object.check_search_results_with_parameters(number_of_results)