Feature: Search something on Google

  @regression
  Scenario: Open google and insert Flat Earth Society
    Given I enter google.ro
    When I enter something in the text field
    Then Results are displayed
