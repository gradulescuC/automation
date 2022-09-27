"""

Mostenire = un concept prin care putem sa oferim unor alte clase niste functionalitati deja definite intr-o clasa
 existenta cu scopul de a economisi cod

mostenire = cand o clasa copil mosteneste o clasa parinte si are acces la toate atributele si metodele ei

O veti gasi in engleza sub numele de inheritance

Pentru ca o clasa sa poata mosteni o alta clasa, clasa Parinte trebuie specificata intre paranteze langa clasa copil
        in momentul definirii

Clasa parinte = clasa care doneaza
Clasa copil = clasa care primeste

"""
class Test:
    testVariable = 0

class Chef(Test): # clasa parinte Test a "donat" atributul testVariable clasei Chef
    cutite = 1
    def make_salad(self):
        print("salad")

    def make_fries(self):
        print("fries")


chef = Chef()
test = Test()
chef.testVariable = 3 # am schimbat valoarea atributului testVariable la 3 pentru obiectul chef
print(chef.testVariable)
print(test.testVariable)

class Chef_indian:
    def make_curry(self):
        print('curry')

# clasa copil care mosteneste clasa Chef (se trece intre paranteze numele clasei parinte)
class JapaneseChef(Chef):
    def make_sushi(self):
        print("sushi")

class ItalianChef(Chef_indian,JapaneseChef): # Putem sa oferim mai mult de o clasa ca si parinte pentru o anumita clasa
    tava = 1
    def make_pizza(self):
        print("pizza")


newbe = Chef() # Am definit un obiect instantiat din clasa Chef
newbe.make_fries() # Am apelat metota make_fries din clasa Chef
print("-------------------------------")
nakamoto = JapaneseChef() # initializam un obiect de tip JapaneseChef

# Observam ca deorarece clasa JapaneseChef mosteneste clasa Chef, atunci orice obiect instantiat
                #din clasa JapaneseChef va avea acces la toate atributele si metodele din clasa parinte Chef
print(nakamoto.cutite)
print(nakamoto.make_fries())
print(nakamoto.make_salad())
print(nakamoto.make_sushi())
print(nakamoto.testVariable)  # avem acces si la atributul testVariable care este definit in clasa Test
                                    # care este parintele lui Chef care este parintele lui JapaneseChef
                                        # cu alte cuvinte Test este un stramos (bunic) al lui JapaneseChef

print("-------------------------------")


mario = ItalianChef() #  am instantiat un obiect al clasei ItalianChef
mario.make_pizza()
print(mario.tava)
mario.make_sushi() # deoarece clasa ItalianChef mosteneste si clasa JapaneseChef, vom putea avea acces si
            # la metoda make_sushi
mario.make_curry() # deoarece clasa ItalianChef mosteneste si clasa Chef_indian, vom putea avea acces si
            # la metoda make_curry