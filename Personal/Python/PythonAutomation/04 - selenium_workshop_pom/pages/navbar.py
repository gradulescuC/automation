from selenium_workshop_pom.pages.driver import Driver


class Navbar(Driver):
    FORMY_HOME = "Logo"
    FORM = "Form"
    COMPONENTS = "navbarDropdownMenuLink"

    def click_on_formy_home(self):
        print(f"Click on buttons with locator {self.FORMY_HOME}")

    def click_on_form(self):
        print(f"Click on buttons with locator {self.FORM}")

    def click_on_components(self):
        print(f"Click on buttons with locator {self.COMPONENTS}")