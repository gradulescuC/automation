Feature: Login on herokuapp

  @regression
  Scenario: Login with valid credentials
    Given I go to herokuapp.com
    When I enter my username and password and I click login
    Then I should be able to enter the application and see the logout button