from behave import *

@given("I am on orangeHRM login page")
def step_impl(context):
		context.login_page.navigate_to_login_page()

@when('Login Page: The user enters a valid email as "{username}" and a valid password as "{password}"')
def step_impl(context,username, password):
		context.login_page.insert_username(username)
		context.login_page.insert_password(password)

@when("The user clicks on the login button")
def step_impl(context):
		context.login_page.click_login_button()

@then("The user is logged in successfully")
def step_impl(context):
		context.login_page.check_user_is_logged()

@when('Login Page: The user enters value "{username}" on the username field and value "{password}" on the password field')
def step_impl(context,username,password):
		context.login_page.insert_username(username)
		context.login_page.insert_password(password)

@then('Login Page: The user receives message "{error_message}" and does not migrate away from the login page')
def step_impl(context,error_message):
		context.login_page.check_error_message(error_message)

