from behave import *

@given("Login Page: I am on the saucedemo login page")
def step_impl(context):
		context.login_page_object.navigate_to_homepage()

@when('Login Page: I insert username "{username}" and password "{password}"')
def step_impl(context,username,password):
		context.login_page_object.insert_username(username)
		context.login_page_object.insert_password(password)

@when("Login Page: I click the login button")
def step_impl(context):
		context.login_page_object.click_login_button()

@then("Inventory Page: I can login into the application and see the list of products")
def step_impl(context):
		context.inventory_page_object.check_current_url()

@then('Login Page: I cannot login into the application and I receive error message "{error_message}"')
def step_impl(context,error_message):
		context.login_page_object.check_error_message(error_message)

