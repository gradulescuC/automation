Feature: Ebay Homepage Scenarios

  @P1 #This is a tag that can be used for running a set of tests having the same tag
#        The name of the tag can be any given name (it doesn't have a specific syntax)
  Scenario: Advanced search link

#   Given When And Then
    Given I am on ebay homepage
    When I click on Advanced Link
    Then I navigate to Advanced Search page

  @P2 @setCookies @Test
  Scenario: Search items count

    Given I am on ebay homepage
    When I search for 'Iphone 11'
    Then I have at least 1000 search items returned

  @P3 @setCookies
  Scenario: Search items count2

    Given I am on ebay homepage
    When I search for 'Toy Cars'
    Then I have at least 100 search items returned

  @P4 @setCookies
  Scenario: Search an item in category
    Given I am on ebay homepage
    When I search for 'soap' in 'BaBy' category
    Then I validate at least '50' data present


  @P300
  Scenario: Advance search an item
    Given I am on Ebay Advanced Search Page
    When I advance search an item
      | keyword   | exclude     | min | max |
      | iphone 11 | refurbished | 300 | 900 |


  @outline
  Scenario Outline: Homepage Links
    Given I am on ebay homepage
    When I click on '<link>'
    Then I validate that the page navigates to '<url>' and title contains '<title>'
    Examples:
      | link    | url                                                                                               | title                     |
      | Motors  | https://www.ebay.com/sch/6028/i.html?_from=R40&_nkw=Auto+Parts+Accessories&_blrs=recall_filtering | auto parts accessories    |
      | Fashion | https://www.ebay.com/b/Fashion/bn_7000259856                                                      | Fashion products for sale |
      | Sports  | https://www.ebay.com/b/Sporting-Goods/888/bn_1865031                                              | Sporting Goods for sale   |