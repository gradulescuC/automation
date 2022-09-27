""""# Check the number of rabbits"""
m_rabb = int(input("Introduceti numarul de iepuri masculi "))
f_rabb = int(input("Introduceti numarul de iepuri femele "))
if (m_rabb>0 and f_rabb>0):
    breed = input("Do you want to breeed? ")
    if breed == 'no':
        print("Keep male and female rabbits apart")
    else:
        print("Breed ok")
# -------------------------------------------------------------
# For Loop
my_list = [1,2,3,7,5,14,22]
n = 0

for i in my_list:
    n = n + i
else:
    print("We are done with the sum")
print(n)

# -------------------------------------------------------------
# While loop
my_list = [1, 2, 3, 4, 5, 43]
n = 0
position = 0
while position < len(my_list):
    n = n + my_list[position]
    position+=1
else:
    print("We are done with the numbers")
print(n)
# -------------------------------------------------------------

# Break and continue
for x in range(10):
    if x == 7:
        break
    print(f"The number is {x}")
print("-------------------------------------")
for x in range(10):
    if x == 7:
        continue
    print(f"The number is {x}")

# -------------------------------------------------------------
# Functii

# Functia nu se executa decat daca o apelam
# Apelarea functiei se face prin specificarea numelui functiei urmata de parametrul utilizat pus intre paranteze
# Cate argumente specificam la definirea functiei, atatia parametri trebuie sa pasam la apelarea functiei
# Escape character (\n )anunta sistemul ca trebuie sa scrie restul rezultatelor pe un rand nou
def say_hello(name: str):
    """
# @type name: str
"""
    print("Hello ", name)
    print(f"Hello {name}")

nume  = "Gica Popescu"
say_hello("Gica Popescu")
say_hello("nume")
say_hello("Gica Hagi")
# say_hello()
x = say_hello("Maria")
print(x)

def say_hello2(name,email, password="abc123"):  #Putem aplica un parametru default
    return name + ", Bine ai venit! Adresa ta de email este " + email + " iar parola e " + password

y = say_hello2(name = "Andreea",email = "Andreea@yahoo.com" ,password="qwerty")
y = say_hello2(email = "Andreea@yahoo.com",name = "Andreea" ,password="qwerty") #Not a good practice

print(y)
y = say_hello2("Andreea","Andreea@yahoo.com" ,"qwerty")
print(y)
z = say_hello2("Mirabela","mirabela@yahoo.com")
print(z)

def say_hello3(*myParam): # args = arbitrary arguments. Ajuta atunci cand nu vrem sa definim un numar fix de parametri. Utila atunci cand definesc un scop de configurare a testelor. (ce test sa rulez, din ce suita sa rulez, ce rapoarte sa generez)
    print("Hello", myParam[0])
    print("Hello", myParam[-1])

say_hello3("Mihaela","Andrei","Marius","Razvan","Ivan")


def say_hello4(**test): #Argumente arbitrare pe baza de keyword
    print("Your name is ", test["name"])
    print("Your salary is", test["salary"])
    print("Your email is ", test["email"])

say_hello4(name="Jon Snow",salary = 1000, email = "jon.snow@gmail.com")
