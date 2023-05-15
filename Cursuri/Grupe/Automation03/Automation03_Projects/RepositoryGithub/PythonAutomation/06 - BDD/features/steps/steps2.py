import time

from behave import *
from selenium.webdriver.common.by import By

@when(u'I type "{location}"')
def step_impl(context,location):
    context.browser.find_element(By.ID, "autocomplete").send_keys(location)


@then(u'I will see the "{results}"')
def step_impl(context,results):
    time.sleep(2)
    message = context.browser.find_element(By.CSS_SELECTOR,"body > div.pac-container.hdpi > div > div:nth-child(2) > span").text
    assert message == "This page can't load Google Maps correctly."
    print("The selected location is in" + results )
    time.sleep(3)