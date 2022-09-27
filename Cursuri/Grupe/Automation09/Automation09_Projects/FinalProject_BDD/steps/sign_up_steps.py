from behave import *

@When('sign_up: I click sign up button')
def step_impl(context):
    context.sign_up_page.click_sign_up_button()

@When('sign_up: I click personal button')
def step_impl(context):
    context.sign_up_page.click_personal_button()

@When('sign_up: I click continue button')
def step_impl(context):
    context.sign_up_page.click_continue_button()

@When('sign_up: I send first name "{name}"')
def step_impl(context,name):
    context.sign_up_page.input_first_name(name)
    print("test")

@When('sign_up: I click continue first name button')
def stem_impl(context):
    context.sign_up_page.click_continue_first_name_button()

@When('sign_up: I send last name "{last_name}"')
def step_impl(context,last_name):
    context.sign_up_page.input_last_name(last_name)

@When('sign_up: I click last_name_continue_button')
def step_impl(context):
    context.sign_up_page.click_last_name_continue_button()

@When('sign_up: I set my email to "{email}"')
def step_impl(context,email):
    context.sign_up_page.input_email(email)

@Then('sign_up: I receive message:Please enter a valid email address')
def step_impl(context):
    context.sign_up_page.check_error_message_email()