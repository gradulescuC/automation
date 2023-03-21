Feature: Check the functionality of the login page

  Background:
    Given Login Page: I am on the saucedemo login page

  """
  Background = daca o sa consider ca un pas given este valabil pentru toate scenariile sau mai multe scenarii, atunci pentru
  a economisi cod voi putea trece acel pas la inceputul unui feature file sub keyword-ul  Background care inseamna
  ca se da un context general pentru testele care ne intereseaza
  """

  @T1 @loginSuccessful @regressionTesting
  Scenario: Check that you can login into the application when providing correct credentials
    When Login Page: I insert username "standard_user" and password "secret_sauce"
    When Login Page: I click the login button
    Then Inventory Page: I can login into the application and see the list of products

    """
    Scenario outline este o modalitate prin care putem sa executam acelasi test de mai multe ori folosindu-ne de un
    tabel de examples
    Pentru scenario outline vom parametriza elementele dinamice (adica cele care isi schimba valoarea la fiecare test)
    si vom rula testul de atatea ori cate randuri avem in tabelul de exemple

    Pentru a rula testele in mod individual putem sa ne folosim de conceptul de tag-uri
    Tag-urile incep cu @ si sunt urmate de un text la alegerea utilizatorului
    Un test poate sa fie reprezentat de mai multe tag-uri
    """

    @T2 @invalidLogin @regressionTesting
  Scenario Outline:  Check that you cannot login into the application when providing incorrect username
    When Login Page: I insert username "<username>" and password "<password>"
    When Login Page: I click the login button
    Then Login Page: I cannot login into the application and I receive error message "<error_message>"

    @ex1
    Examples:
      | username       | password           | error_message                                                             |  |  |
      | incorrect_user | secret_sauce       | Epic sadface: Username and password do not match any user in this service |  |  |
      | standard_user  | incorrect_password | Epic sadface: Username and password do not match any user in this service |  |  |

     @ex2
    Examples:
      | username       | password           | error_message                                                             |  |  |
      | incorrect_user | incorrect_password | Epic sadface: Username and password do not match any user in this service |  |  |

    Scenario: Check that the user can close the missing username or password error message
      When Login Page: I click the login button
      When I close the error message
      Then The error message is no longer visible on the website