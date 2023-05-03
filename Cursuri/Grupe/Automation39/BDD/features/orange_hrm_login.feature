# In feature o sa punem o descriere a functionalitatii pe care o testam in fisierul curent
    # Atunci cand veti lucra in Jira, acest feature este echivalentul unui EPIC
    # In general un feature inglobeaza mai multe teste pe care le putem face
      # pentru aceeasi functionalitate
Feature: Check that the login functionality of the Orange HRM website is working properly

  # Given este ca un fel de context general in care se desfasoara activitatea noastra, ca un fel de preconditii
  Background:
    Given The user is on the Orange HRM login page

  @T1  @positiveTesting
  Scenario: Check that the user can login into the application when inserting valid username and valid password
    # in python keyword-ul and nu este recunoscut
     The user inserts valid information on the username and password fields
#    When The user inserts valid username "Admin" and valid password "admin123"
    When The user clicks on the login button
    Then The user is logged into the application

#  @T2  @negativeTesting
#  Scenario: Check that the user cannot login into the application when inserting invalid username and valid password
#    When The user inserts invalid username and valid password
#    When The user clicks on the login button
#    Then The user receives error message and cannot login into the application

#  @T3  @negativeTesting
#  Scenario: Check that the user cannot login into the application when inserting invalid username and valid password
#    When The user inserts valid username and invalid password
#    When The user clicks on the login button
#    Then The user receives error message and cannot login into the application
#
#
#  @T4  @negativeTesting
#  Scenario: Check that the user cannot login into the application when inserting invalid username and valid password
#    When The user inserts invalid username and invalid password
#    When The user clicks on the login button
#    Then The user receives error message and cannot login into the application

#  Folosim scenario outline atunci cand toti pasii sunt identici, mai putin valorile de testat
#  @T5 @negativeTesting
#  Scenario Outline: Check that the user cannot login into the application when inserting invalid credentials
#    When The user inserts username "<username>" and password "<password>"
#    When The user clicks on the login button
#    Then The user receives error message: "<error_message>" and cannot login into the application
#    Examples:
#      | username     | password     | error_message       |
#      | Admin        | testPassword | Invalid credentials |
#      | testUsername | admin123     | Invalid credentials |
#      | testUsername | testPassword | Invalid credentials |

#  Atunci cand o valoare de testat este identica pentru toate scenariile din outline, o putem parametriza direct in pas
  @T6 @negativeTesting
  Scenario Outline: Check that the user cannot login into the application when inserting invalid credentials
    When The user inserts username "<username>" and password "<password>"
    When The user clicks on the login button
    Then The user receives error message: "Invalid credentials" and cannot login into the application
    Examples:
      | username     | password     |  |
      | Admin        | testPassword |  |
      | testUsername | admin123     |  |
      | testUsername | testPassword |  |