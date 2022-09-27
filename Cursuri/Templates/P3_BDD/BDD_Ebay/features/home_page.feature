Feature: Testing scenarios on ebay.com
  Background:
    Given Home Page: I am on Ebay homepage
    Then Home Page: I have at least 2 results returned

  @T1
  Scenario: Searching product on Ebay home page
    When Home Page: I search an item

  @T2 @parameter
  Scenario:
    When Home Page: I search for "catcher in the rye" in "Books"

  @T3 @outline, @parameter
  Scenario Outline:
    When Home Page: I search for "<product_name>" in "<category_name>"
    Then Home Page: I have at least "<number_of_results>" results returned
    Examples:
      | product_name                                                                    | category_name        | number_of_results |  |
      | catcher in the rye                                                              | Books                | 1000              |  |
      | headphones                                                                      | Consumer Electronics | 1000              |  |
      | Bluetooth 5.0 Wireless Headphones Earphones Mini In-Ear Pods For iPhone Android | All Categories       | 14                |  |

