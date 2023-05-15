Feature: Autocomplete page from formy-project
  As a user I want to use autosuggest
  So that I do not have to fill in the whole content

  Scenario: Check Address Field
    Given I go to autocomplete page
    When I type ko
    Then Cluj-Napoca should be available
