Feature: We want to check the login functionality of the website https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
 """
  Background este o modalitate prin care putem sa oferim un context comun tuturor testelor
  Aici se plaseaza instructiuni Given care vor fi citite de catre toate testele din fisierul curent
  """

Background:
    Given I am on orangeHRM login page

Scenario:  Check that the user can login into the application with proper username and password
  When Login Page: The user enters a valid email as "Admin" and a valid password as "admin123"
  When The user clicks on the login button
  Then The user is logged in successfully

  @T1
Scenario Outline: Check that the user cannot login into the application with invalid credentials
  When Login Page: The user enters value "<username>" on the username field and value "<password>" on the password field
  When The user clicks on the login button
  Then Login Page: The user receives message "<error_message>" and does not migrate away from the login page
  Examples:
    | username | password  | error_message       |
    | Admin    | admin123* | Invalid credentials |
    | Admin1   | admin123  | Invalid credentials |
    | Admin3   | admin123* | Invalid credentials |



















