from selenium_workshop_pom.pages.driver import Driver


class Autocomplete(Driver):
    ADDRESS = "autocomplete"
    STREET_ADRESS = "street_number"
    ROUTE = "route"
    CITY = "locality"
    STATE = "administrative_area_level_1"
    ZIP_CODE = "postal_code"
    COUNTRY = "country"

    def click_on_address    (self):
        print(f"Click on element with the locator {self.ADDRESS}")

    def click_on_street_address(self):
        print(f"Click on element with the locator {self.STREET_ADRESS}")

    def click_on_route(self):
        print(f"Click on element with the locator {self.ROUTE}")

    def click_on_city(self):
        print(f"Click on element with the locator {self.CITY}")
