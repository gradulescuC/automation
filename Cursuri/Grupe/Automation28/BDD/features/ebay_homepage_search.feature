Feature: Test the search functionality in the homepage of Ebay

  Scenario: Check that the user can make a simple search in the Ebay homepage
    Given Home page: I am on Ebay homepage
    When Home page: I search for iphone from category Cell Phones & Smartphones
    Then Home page: I have at least 1000 results returned

  Scenario: Check that the user can make an advanced search for a product
    Given Home page: I am on Ebay homepage
    When Home page: When I click on the advanced link
    When Advanced search page: I type Pampers in the enter keyword textbox
    When Advanced search page: I select Exact words exact order from keyword options
    When Advanced search page: I choose Baby from the category list
    When Advanced search page: I click search button
    Then Home Page: I have at least 1000 results returned