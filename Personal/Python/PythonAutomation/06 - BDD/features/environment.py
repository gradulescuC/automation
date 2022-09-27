# environment.py e un fisier required de cucumber
import time
from selenium import webdriver

def before_all(context):
    context.browser=webdriver.Chrome("/Users/gradulescu/Desktop/Personal/Cursuri/ITF/Automation Course/Proiecte Python/RepositoryGithub/PythonAutomation/venv/04 - selenium_workshop_pom/resources/chromedriver")

def after_all(context):
    context.browser.quit()  # context  e un parametru caruia ii definesc anumite variabile ce sunt citite doar atunci cand avem nevoie
                            # cu acest context vom face legatura cu testele noastre
    time.sleep(3)