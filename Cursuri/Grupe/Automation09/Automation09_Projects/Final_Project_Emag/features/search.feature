Feature: Emag search feature

    Background:
      Given home: I am a user on emag.ro Home page

    @emag
    Scenario Outline: Test search functionality
      When home: I search after "<query>"
#      Then products: I verify that results contain search query "<query>"
     Then products: I verify that I have at least "<number>" results


    Examples:
      | query   | number |
      | iphone  | 80     |
      | samsung | 400    |