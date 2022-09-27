from behave import *
# given, when, and, but, then -> sintaxa gherkin
# given seteaza situatia curenta
# when defineste pasii din test
# then efectueaza verificarea testului

@given('sign in: I am a user on jules sign in page')
def step_impl(context):
    context.sign_in_page.navigate_to_sign_in_page()

@when('sign in: I set my email to "{email}"')
def step_impl(context,email):
    context.sign_in_page.set_email(email)

@when('sign in: I set my password to "{password}"')
def step_impl(context,password):
    context.sign_in_page.set_pass(password)

@when('sign in: I click the forgot password link')
def step_impl(context):
    context.sign_in_page.click_forgot_password_link()

@Then('sign in page: I am returned to the homepage')
def step_impl(context):
    context.check_current_url()
















