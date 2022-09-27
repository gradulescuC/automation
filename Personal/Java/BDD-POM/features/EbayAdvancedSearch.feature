Feature: Ebay Advanced Search Page

  @P24
  Scenario: Ebay Logo on Advanced Search Page

    Given I am on Ebay Advanced Search Page
    When I click on Ebay Logo
    Then I am navigated to Ebay homepage

  @P25

  Scenario Outline: Advance search an item
    Given I am on the advanced search page
    When I advance search an item
    Examples:
      | keyword   | exclude     | min | max |
      | iphone 11 | refurbished | 300 | 900 |

