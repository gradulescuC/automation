Feature: Check search functionality

Scenario: Searching product on Ebay home page will return at least two results
  Given Home Page: I am on Ebay homepage
  When Home Page: I search "Pampers" from category "Baby"
  Then Home Page: I have at least "2" results returned