from behave import *

@when('forgot password: I set my email to "{email}"')
def step_impl(context,email):
    context.forgot_pass.set_email(email)

@then('forgot password: I verify that email validation message is correct')
def step_impl(context):
    context.forgot_pass.verify_email_error_msg()

@When('forgot password: I click on Back to Login button')
def step_impl(context):
    context.forgot_pass.click_back_to_login_link()

@then('forgot_pass: verify that send email button is enabled')
def step_impl(context):
        context.forgot_pass_page.verify_btn_enabled()


