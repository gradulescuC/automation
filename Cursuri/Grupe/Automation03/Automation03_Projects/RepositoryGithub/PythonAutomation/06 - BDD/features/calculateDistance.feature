Feature: Calculate the distance between two locations on https://www.openstreetmap.org
  As a user
  If I type in two locations
  I want the distance between them to be shown on the screen

  Scenario: Distance between two locations
    Given I access https://www.openstreetmap.org and after I press route button
    When I type in two locations, one in every text field and I press GO
    Then The distance should be shown on the screen