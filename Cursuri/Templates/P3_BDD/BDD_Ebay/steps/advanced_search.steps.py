from behave import *

@when('Advanced Search Page: I click on the Advanced Search Link and I search for "{product_to_be_searched}"')
def step_impl(context,product_to_be_searched):
    context.home_page_object.click_advanced_search_link()
    context.advanced_page_object.set_product_search(product_to_be_searched)

@then("Advanced Search Page: I get at least '{number_of_results}' results")
def step_impl(context,number_of_results):
    context.advanced_page_object.check_search_results(number_of_results)

