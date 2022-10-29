Feature: Check search functionality
  """
  Background = daca o sa consider ca un pas este valabil pentru toate scenariile, pentru a economisi cod,
              voi putea trece pasul la inceputul unui feature file sub keywword-ul background.
              Asta inseamna ca sistemul va sti automat ca va trebui sa ia in considerare acel step pentru toate scenariile
  """
  Background:
    Given Home Page: I am on Ebay homepage
  """
  tag-urile reprezinta o modalitate prin intermediul careia noi putem sa marcam doar anumite teste pentru executie
  un scenariu poate sa aiba mai multe tag-uri
  tag-ul se adauga prin semnul @ plus un text cu care vrem sa marcam testul respectiv
  textul poate sa fie orice, dar se recomanda sa fie sugestiv
  """

@homepageSearch @functionalTesting @regressionTesting
Scenario Outline: Searching product on Ebay home page will return at least two results
  When Home Page: I search "<product_name>" from category "<category_name>"
  Then Home Page: I have at least "2" results returned

  """
  Scenario outline este o modalitate prin care putem sa executam acelasi test de mai multe ori
  folosindu-ne de un tabel de examples.
  Pentru scenario outline vom parametriza elementele dinamice, adica cele care vrem sa se schimbe la fiecare rulare
  """
  Examples:
    | product_name | category_name |
    | Pampers      | Baby          |
    | Harry Potter | Books         |
    | embelishment | Crafts        |

  @advancedSearchFeature @functionalTesting
  Scenario: Searching products on Ebay Advanced search page will return at least two results
  When Home Page: When I click on the Advanced link
  When Advanced Search Page: I type "Pampers" in the enter keyboard textbox
  When Advanced Search Page: I choose "Exact words, exact order" from the list
  When Advanced Search Page: I choose "Baby" from the category list
  When Advanced Search Page: I click search button
  Then Home Page: I have at least "2" results returned