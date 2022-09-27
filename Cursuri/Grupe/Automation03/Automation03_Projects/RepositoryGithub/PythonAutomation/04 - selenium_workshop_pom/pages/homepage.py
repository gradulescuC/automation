from selenium_workshop_pom.pages.driver import Driver

# pdb = python debugger daca lucram din consola

class Home(Driver):
    BUTTONS = "Buttons"
    AUTOCOMPLETE = "Autocomplete"
    CHECKBOX = "Checkbox"

    def click_on_buttons(self):
        print(f"Click on element with the locator {self.BUTTONS}")

    def click_on_autocomplete(self):
        print(f"Click on element with the locator {self.AUTOCOMPLETE}")

    def click_on_CHECKBOX(self):
        print(f"Click on element with the locator {self.CHECKBOX}")

