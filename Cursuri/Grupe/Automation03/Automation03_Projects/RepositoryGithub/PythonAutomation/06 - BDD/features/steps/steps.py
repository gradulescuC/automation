import time

from behave import *
from selenium.webdriver.common.by import By

@given("I go to autocomplete page")
def step_impl(context):
    context.browser.get("https://formy-project.herokuapp.com/")
    time.sleep(3)
    context.browser.find_element(By.LINK_TEXT, "Autocomplete").click()
    time.sleep(3)

@when("I type ko")
def step_impl(context):
    context.browser.find_element(By.ID, "autocomplete").send_keys("Craiova")


@then("Cluj-Napoca should be available")
def step_impl(context):
    print("Good job")


print("---------------------------------------------------------------------")

@given("I enter google.ro")
def step_impl(context):
    context.browser.get("https://google.ro")
    authorization = (By.CSS_SELECTOR, "#L2AGLb > div")
    context.browser.find_element(*authorization).click()


@when("I enter something in the text field")
def step_impl(context):
    search_bar = context.browser.find_element(By.NAME, "q")
    search_bar.send_keys("Flat Earth Society")
    search_bar.submit()


@then("Results are displayed")
def step_impl(context):
    print("Search is complete")
    time.sleep(3)

print("-----------------------------------------------------------")


@given("I go to herokuapp.com")
def step_impl(context):
    context.browser.get("https://the-internet.herokuapp.com/login")
    time.sleep(2)


@when("I enter my username and password and I click login")
def step_impl(context):
    context.browser.find_element(By.ID, "username").send_keys("tomsmith")
    context.browser.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    context.browser.find_element(By.CLASS_NAME, "radius").click()


@then("I should be able to enter the application and see the logout button")
def step_impl(context):
    context.browser.find_element(By.CLASS_NAME, "button")
    time.sleep(2)
    context.browser.quit()

print("-----------------------------------------------------------")

@given("I have cucumber installed")
def step_impl(context):
    print("Un mesaj important")


@when("Winter season is coming")
def step_impl(context):
    print("Prepare for impact")


@then("All tests should pass")
def step_impl(context):
    print("Good job")


print("---------------------------------------------------------------------")

@given("I access https://www.openstreetmap.org")
def step_impl(context):
    context.browser.get("https://www.openstreetmap.org")

@when("I type an address in the text field")
def step_impl(context):
    searchbar = context.browser.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form[1]/div/div[1]/div/div[1]/input")
    go_btn = context.browser.find_element(By.CSS_SELECTOR, "#sidebar > div.search_forms > form.search_form.px-1.py-2 > div > div.col > div > div.input-group-append > input")
    searchbar.send_keys("Kogalniceanu Street Bucharest")
    time.sleep(3)
    go_btn.click()
    time.sleep(3)

@then("I want it to be shown on the map")
def step_impl(context):
    print("Address shown")

print("-----------------------------------------------------------")


@given("I access https://www.openstreetmap.org and after I press route button")
def step_impl(context):
    context.browser.get("https://www.openstreetmap.org")
    route_btn = context.browser.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form[1]/div/div[2]/a")
    route_btn.click()

@when("I type in two locations, one in every text field and I press GO")
def step_impl(context):
    from_bar = context.browser.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form[2]/div[2]/div[2]/input")
    to_bar = context.browser.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form[2]/div[3]/div[2]/input")
    calculate_btn = context.browser.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form[2]/div[4]/div[2]/input")
    from_bar.send_keys("Bucharest")
    to_bar.send_keys("Lengerich")
    time.sleep(3)
    calculate_btn.click()


@then("The distance should be shown on the screen")
def step_impl(context):
    time.sleep(5)
    distance = context.browser.find_element(By.XPATH, "//*[@id='sidebar_content']/p[1]")
    print(distance.text)