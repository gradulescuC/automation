from behave import *

@when('User clicks on Admin option in the left side menu')
def step_impl(context):
		context.admin_module_page.click_admin_option()

@when('User selects status "{user_status}" in the Search User section')
def step_impl(context,user_status):
		context.admin_module_page.select_user_status(user_status)