# from os import path
#
# class Configuration:
#     DEFAULT_CONFIG_FILE = 'app.config.yaml'
#     DEFAULT_CONFIG_OVERRIDE = 'app.override.yaml'
#     DEFAULT_CONFIG_PATH = 'config'
#
#     # def __init__(self, config_file=None, config_path=None):
#     #     self.config_file = config_file if config_file else self.DEFAULT_CONFIG_FILE
#     #     self.config_path = config_path if config_path else self.DEFAULT_CONFIG_PATH
#     #     # setup application override configuration
#     #     print(path.join(self.config_path, self.DEFAULT_CONFIG_OVERRIDE))
#
#     def customer_configuration(self):
#         # print(path.join(self.config_path, self.DEFAULT_CONFIG_OVERRIDE))
#         print(self.DEFAULT_CONFIG_PATH)
#
#
# conf = Configuration
# conf.customer_configuration()

class Masina:
    # fields/attribute
    culoare = "Galben" #daca dam o valoare default nu mai e nevoie de constructor
    marca = None
    model = None
    viteza = 0

    # constructor
    def __init__(self,model,culoare): # self reprezinta un placeholder pentru viitorul nume al obiectului care se va instantia
                                       # model si culoare reprezinta ARGUMENTELE constructorului si ele vor fi considerate obligatorii la momentul instantierii obiectului
        self.model = model  #  aici vom atribui atributelor clasei valorile date ca si PARAMETRU in interiorul constructorului
                                       # in stanga egalului vor fi intotdeauna atributele clasei care vor trebui initializate, iar in dreapta argumentele constructorului care vor fi stocate in atributele clasei
        self.culoare = culoare
        while type(model) is not str: # verific daca inputul de la utilizator este un string
            input('Invalid value, please try again.') # daca nu este string, promptez utilizatorul sa introduca o noua valoare
        if culoare == 'orange': # verificam daca culoarea data ca si argument in constructor este orange
            self.culoare = 'portocaliu' # daca este orange, o schimbam in portocaliu pentru ca nu avem culoarea orange in baza de date

bmw = Masina("X5","")