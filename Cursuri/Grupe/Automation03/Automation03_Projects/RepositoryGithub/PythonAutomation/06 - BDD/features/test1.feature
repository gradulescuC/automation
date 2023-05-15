Feature: Alegem un nume
  As a GPS user
  I want to query for many addresses
  So that I will reuse the steps

  Scenario Outline: Opertiunea Monstrul
    Given I enter the website
    When I search for "<adr>"
    Then A list with "<expected_adr>" will be returned
    Examples:
      | adr          | expected_adr |
      | Fetesti      | Ialomita     |
      | Buftea       | Ilfov        |
      | Posta Calnau | Buzau        |
