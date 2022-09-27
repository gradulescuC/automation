Feature: filling the form

  @TestBDDRo21
  Scenario: test the auto-complete over the address field
    Given I am on "formy project" page
    When I insert data in the auto-complete field
    Then I am able to see the data in the web-browser