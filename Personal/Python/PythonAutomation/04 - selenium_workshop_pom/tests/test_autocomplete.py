from selenium_workshop_pom.pages.autocomplete import Autocomplete
from selenium_workshop_pom.pages.homepage import Home
from selenium_workshop_pom.tests.test_case import TestCaseModel


class TestAutocomplete(TestCaseModel):
    home = Home()
    auto = Autocomplete()

    def setup(self):
        self.home.open_url("https://formy-project.herokuapp.com/")

    def run(self):
        self.home.click_on_autocomplete()
        self.auto.click_on_address()
        self.auto.click_on_street_address()
        # tema de adaugat din pages-autocomplete - si restul elementelor(city, state,zip,country)

    def tear_down(self):
        self.home.quit_test()

if __name__ == '__main__':  # se poate rula doar in fisierul asta nu si in alt fisier din cadrul pachetului
    test1 = TestAutocomplete()
    test1.setup()
    test1.run()
    test1.tear_down()
