Feature: Autocomplete page
  As a user I want to use autocomplete option
  I want to use autocomplete option
  So that I do not need to fill in the blanks

 Scenario Outline: # functionalitate de BDD prin care pot sa pasez parametri
    Given I go to autocomplete page
    When I type "<location>"
    Then I will see the "<results>"
    Examples:
      | location | results   |
      | Dubai    | Arabia    |
      | Agigea   | Constanta |
      | Fetesti  | Ialomita  |


#parametrii trebuie sa fie pusi in formatul "<text>"