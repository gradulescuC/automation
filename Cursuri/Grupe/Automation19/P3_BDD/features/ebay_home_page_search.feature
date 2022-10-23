Feature: Check search functionality

Scenario: Searching product on Ebay home page will return at least two results
  Given Home Page: I am on Ebay homepage
  When Home Page: I search "Pampers" from category "Baby"
  Then Home Page: I have at least "2" results returned

Scenario: Searching products on Ebay Advanced search page will return at least two results
  Given Home Page: I am on Ebay homepage
  When Home Page: When I click on the Advanced link
  When Advanced Search Page: I type "Pampers" in the enter keyboard textbox
  When Advanced Search Page: I choose "Exact words, exact order" from the list
  When Advanced Search Page: I choose "Baby" from the category list
  When Advanced Search Page: I click search button
  Then Home Page: I have at least "2" results returned