Feature: Address search on www.openstreetmap.org
  As a user
  I want to type an address in the text field
  So it will be shown on the map

  Scenario: Look for an address
    Given I access https://www.openstreetmap.org
    When I type an address in the text field
    Then I want it to be shown on the map