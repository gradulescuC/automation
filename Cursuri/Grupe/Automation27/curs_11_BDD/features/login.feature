Feature: Check the functionality of the login page

  Scenario: Check that you can login into the application when providing correct credentials
    Given Login Page: I am on the saucedemo login page
    When Login Page: I insert username "standard_user" and password "secret_sauce"
    When Login Page: I click the login button
    Then Inventory Page: I can login into the application and see the list of products

  Scenario:  Check that you cannot login into the application when providing incorrect username
    Given Login Page: I am on the saucedemo login page
    When Login Page: I insert username "incorrect_user" and password "secret_sauce"
    When Login Page: I click the login button
    Then Login Page: I cannot login into the application and I receive an error message

  Scenario:  Check that you cannot login into the application when providing incorrect password
    Given Login Page: I am on the saucedemo login page
    When Login Page: I insert username "standard_user" and password "incorrect_password"
    When Login Page: I click the login button
    Then Login Page: I cannot login into the application and I receive error message "Epic sadface: Username and password do not match any user in this service"

