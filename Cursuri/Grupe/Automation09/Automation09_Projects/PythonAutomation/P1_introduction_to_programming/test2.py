# https://www.phptravels.net/
# http://automationpractice.com/index.php
# https://formy-project.herokuapp.com/
# https://the-internet.herokuapp.com/
# https://www.techlistic.com/p/selenium-practice-form.html
# jules.app
#
# (obs: nu 3 pe fiecare pagina, 3 in total, de pe ce site doriti, la alegere. Nu toate sites vor avea elemente cu atributul name de ex)
#
# 3 selectors by:
# Id                        rezolvat
# Link text                 rezolvat
# Partial link text         rezolvat
# Name                      rezolvat
# Tag*                      rezolvat
# Class name*                rezolvat
# Css (1 dupa id, 1 dupa clasa, 1 dupa atribut=valoare_partiala)

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.maximize_window()
#

#### By Class_name
#1
# chrome.get('http://automationpractice.com/index.php')
# sleep(3)
# first_name = chrome.find_elements(By.CLASS_NAME, 'sf-with-ul')
# stocare_elemente = chrome.find_elements(By.CLASS_NAME, 'sf-with-ul')
# print(len(stocare_elemente))
# sleep(3)
# chrome.quit()

#2
# chrome.get('https://jules.app/')
# sleep(3)
# chrome.find_elements(By.CLASS_NAME,'MuiInputBase-input')[0].send_keys('marian@gmail.com')
# sleep(2)
# test = chrome.find_elements(By.CLASS_NAME,'MuiInputBase-input')[1].send_keys('password')
# sleep(2)
# chrome.quit()

#3
# chrome.get('https://the-internet.herokuapp.com/tinymce')
# chrome.find_element(By.CLASS_NAME,'tox-mbtn__select-label').click()
# sleep(3)
#
# chrome.quit()
#4
# navigam catre un url
# chrome.get('https://www.phptravels.net/signup')
#
# chrome.find_elements(By.CLASS_NAME, 'form-control')
#
# sleep(2)
#
# lista_formular = chrome.find_elements(By.TAG_NAME, 'input')
# lista_formular[1].send_keys('Marian')
# lista_formular[2].send_keys('Negru')
# lista_formular[3].send_keys('07xxxxx')
# lista_formular[4].send_keys('marian@gmail.com')
# lista_formular[5].send_keys('parola')
# sleep(3)
#
# chrome.quit()
#
# ###      By ID
#
# # #1
#
# chrome.get('https://www.phptravels.net/')
# test = chrome.find_element(By.ID,"languages" ).click()
# sleep(5)
# chrome.quit()
#
# #2
#
# chrome.get('https://the-internet.herokuapp.com/dropdown')
# chrome.find_element(By.ID, 'dropdown').click()
# sleep(3)
# chrome.quit()
#
#3
# chrome.get('https://the-internet.herokuapp.com/dynamic_loading/1')
# chrome.find_element(By.ID,'start').click()   #  nu da eroare dar nici nu da click....d c?
# sleep(3)
# chrome.quit()

#
# #         BY  Link text
#
# #1
# chrome.get('https://the-internet.herokuapp.com/')
# chrome.find_element(By.LINK_TEXT,'A/B Testing').click()
# sleep(3)
# chrome.quit()
#
# #2
# chrome.get('https://the-internet.herokuapp.com/')
# chrome.find_element(By.LINK_TEXT,'Context Menu').click()
# sleep(2)
# chrome.quit()
#
# #3
# chrome.get('https://the-internet.herokuapp.com/')
# chrome.find_element(By.LINK_TEXT,'Typos').click()
# sleep(3)
# chrome.quit()
#
#
# #4
# chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
# sleep(5)
# chrome.find_element(By.LINK_TEXT,'Automate Amazon like E-Commerce website with Selenium').click()  #nu merge pe acestsite, am incercat mai multe link-uri
# sleep(5)
# chrome.quit()
# ###
# #5
# chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')    #putem sa scapam de reclame/politica de confidentialitate ca sa ruleze mai departe?
# sleep(10)
# chrome.find_element(By.LINK_TEXT,'Automate Google search with Selenium').click()
# sleep(8)
# chrome.quit()
# #
#
# ##  BY Partial Link Text
#
# #1
# chrome.get('https://the-internet.herokuapp.com/dynamic_loading')
# chrome.find_element(By.PARTIAL_LINK_TEXT, 'Example 1').click()
# sleep(3)
# chrome.quit()
#
# #2
# chrome.get('https://the-internet.herokuapp.com/dynamic_loading')
# chrome.find_element(By.PARTIAL_LINK_TEXT,'after the fact').click()
# sleep(3)
# chrome.quit()
#
#
# #3
# chrome.get('https://jules.app/')
# chrome.find_element(By.PARTIAL_LINK_TEXT,'Sign').click()
# pas = chrome.find_elements(By.PARTIAL_LINK_TEXT,'Sign')
# print(len(pas))
# sleep(3)
# chrome.quit()
#
# # By NAME
# #1
# chrome.get('http://automationpractice.com/index.php')
# chrome.find_element(By.NAME, 'search_query').send_keys('Tesla')
# sleep(5)
# chrome.quit()
#
# #2
# chrome.get('http://automationpractice.com/index.php?id_category=8&controller=category')
# chrome.find_element(By.NAME, 'layered_id_attribute_group_1').click()
# sleep(3)
# chrome.quit()
#
#
# #3
# chrome.get('http://automationpractice.com/index.php')
# chrome.find_element(By.NAME,'email').send_keys('marian@gmail.com')
# sleep(3)
# chrome.quit()
#
#
# # By Tag NAME
#
# #1
# chrome.get('https://formy-project.herokuapp.com/autocomplete')
# chrome.find_element(By. TAG_NAME, 'input').send_keys('marian@gmail.com')
# lista_input = chrome.find_elements(By.TAG_NAME, 'input')
# lista_input[1].send_keys('Aleea Meseriasilo')
# lista_input[2].send_keys('Zimbrului')
# lista_input[3].send_keys('Bucuresti')
# lista_input[4].send_keys('bucursti')
# lista_input[5].send_keys('1258')
# lista_input[6].send_keys('Romania')
# sleep(8)
# chrome.quit()
#
#
# #2
# chrome.get('https://formy-project.herokuapp.com/form')
# chrome.find_element(By.TAG_NAME,'input').send_keys('Marian')
# list= chrome.find_elements(By.TAG_NAME, 'input')
# list[1].send_keys('Negru')
# list[2].send_keys('Automation Testing')
# chrome.find_element(By.ID,'radio-button-1').click()
# chrome.find_element(By.CSS_SELECTOR,'input#checkbox-1').click()
# #chrome.find_element(By.XPATH,'//input[@id="select-menu"]').click()    ###### nu merge si nu stiu dc
# chrome.find_element(By.CSS_SELECTOR,'input[placeholder="mm/dd/yyyy"]').send_keys('12.2.22')
# sleep(5)
# chrome.quit()
#
# #    CSS - Class
# #1
# chrome.get('https://www.phptravels.net/signup')
# chrome.find_elements(By.CSS_SELECTOR,'input.form-control')
# find= chrome.find_elements(By.CSS_SELECTOR,'input.form-control')
# sleep(3)
# find[0].send_keys('hello')
# find[1].send_keys('I Am')
# sleep(3)
# chrome.quit()
#
#
# # CSS-ID
#
#
# chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
# chrome.find_element(By.CSS_SELECTOR,'input#datepicker').send_keys('15.04.22')
# sleep(3)
#
#
#
# # *La tag si class name veti folosi find elementS! - salvati in lista. Interactionati cu un element la alegere din lista
#
# # La Xpath:
# # 3 dupa atribut valoare
# # 1
# chrome.get('https://formy-project.herokuapp.com/autocomplete')
# chrome.find_element(By.XPATH,'//input[@id="autocomplete"]').send_keys('Marian')
# sleep(3)
# chrome.quit()
#
# #2
# chrome.get('http://automationpractice.com/index.php')
# chrome.find_element(By.XPATH,'//*[@id="search_query_top"]').send_keys('Google.com')
# sleep(3)
# chrome.quit()
#
# #3
# chrome.get('https://formy-project.herokuapp.com/autocomplete')
# chrome.find_element(By.XPATH,'//html/body/div[1]/form/div/div/input').send_keys('M')
# sleep(1)
# chrome.find_element(By.XPATH,'/html/body/div[1]/form/div/div[2]/input').send_keys('a')
# sleep(1)
# chrome.find_element(By.XPATH,'/html/body/div[1]/form/div/div[3]/input').send_keys('r')
# sleep(1)
#
# chrome.find_element(By.XPATH,'/html/body/div[1]/form/div/div[4]/input').send_keys('i')
# sleep(1)
# chrome.find_element(By.XPATH,'/html/body/div[1]/form/div/div[5]/input').send_keys('a')
# sleep(1)
# chrome.find_element(By.XPATH,'/html/body/div[1]/form/div/div[6]/input').send_keys('n')
# sleep(1)
# chrome.find_element(By.XPATH,'/html/body/div[1]/form/div/div[7]/input').send_keys('Romania')
# sleep(3)
# chrome.quit()
#
#
#
# # 3 dupa textul de pe element
# # 1 dupa partial text
# #
# #
# # 1 cu SAU, folosind pipe |
# # 1 cu *
# # 1 in care le iei ca pe o lista de xpath si in python ajunge 1 element, deci cu (xpath)[1]
# # 1 in care sa folosesti parent::
# # 1 in care sa folosesti fratele anterior sau de dupa (la alegere)
# # 1 functie ca si cea de la clasa prin care sa pot alege eu prin param cu ce element vreau sa interactionez.
# #
# # Studiu extra daca doriti:
# # https://www.automatetheplanet.com/most-exhaustive-xpath-locators-cheat-sheet/
#