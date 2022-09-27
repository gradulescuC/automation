"""

polymorphismul este o modalitate prin care putem sa dam unei functii un comportament mai variat
                    sau chiar sa implementam doua metode cu acelasi nume

"""

# Exemplu: Functia print este o functie polimorfica pentru ca poate sa fie apelata cu cate argumente avem nevoie
print(len("abc"))
print(len([1, 2, 3, 4]))




# Mai jos am definit o functie cu comportament polimorfic pentru ca am dat lui z valoarea default 0
            # astfel, daca apelam functia doar cu 2 parametri, nu vom primi eraore asa cum ne-am astepta, pentru ca
                # parametrul z are valoarea implicita 0 care se va aduna la suma
# 1. FUNCTIE CU COMPORTAMENT POLIMOFFIC PRIN DEFINIREA PARAMETRILOR DEFAULT
def add(x, y=0, z=0):
    return x + y + z
print(add(2, 3))
print(add(56))
print(add(2, 3, 4))

# 2. FUNCTIE CU COMPORTAMENT POLIMORFIC PRIN DEFINIREA UNUI NUMAR NECUNOSCUT DE ARGUMENTE
def add_multiple_numbers(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(f"Suma este: {add_multiple_numbers(5,2,8)}")
print(f"Suma este: {add_multiple_numbers(51,243,878)}")
print(f"Suma este: {add_multiple_numbers(5,2,8,98,76,23,890,1543)}")




# # Putem sa folosim polimorfismul si in metodele de clasa prin faptul ca implementam doua metode cu acelasi nume in clase diferite
#                 # Ele vor fi diferentiate prin faptul ca vor fi apelate prin obiecte diferite

# 3. METODA CU COMPORTAMENT POLIMORFIC PRIN REIMPLEMETAREA ACELUIASI NUME IN DOUA CLASE DIFERITE, NEINRUDITE
class Romania():
    def language(self):
        print("Romanian")

class USA():
    def language(self):
        print("English")

obj_ro = Romania() # Am instantiat un obiect al clasei Romania
obj_usa = USA() # Am instantiat un obiect al clasei USA
for country in (obj_ro, obj_usa): # Am iterat prin obiectele create
    country.language() # am apelat functia language, care pentru fiecare obiect va printa altceva

# Putem sa implementam polimorfismul si in raport cu mostenirea, prin faptul ca reimplementam in clasa copil o metoda care exista in clasa parinte

# METODA CU COMPORTAMENT POLIMORFIC PRIN REIMPLEMENTAREA ACELUIASI NUME IN CLASA COPIL
class Bird:
    def describe(self):
        print("I'm a bird")

    def fly(self): # Am definit metoda fly in clasa parinte Bird
        print("Flu Flu! I'm flying")
#
#
class Parrot(Bird):
    def talk(self):
        print("I also can talk")

class Penguin(Bird):
    def fly(self): # Am redefinit metoda fly in clasa copil Penguin, cu un comportament specific acestei clase
        print("I actually can't fly. But that's ok, I'm dressed stylish.")


random_bird = Bird() # am instantiat un obiect al clasei Bird
random_bird.describe()
random_bird.fly() # am apelat metoda fly din clasa Bird. Va printa pe ecran Flu Flu! I'm flying
print('------------------------')
#
polly = Parrot()  # am instantiat un obiect al clasei Parrot
polly.describe()
polly.talk()
polly.fly()  # am apelat metoda fly care nu e implementata in clasa Parrot, deci va fi apelata din clasa parinte Bird. Va printa pe ecran Flu Flu! I'm flying
print('------------------------')

pingu = Penguin()  # am instantiat un obiect al clasei Penguin
pingu.describe()
pingu.fly()  # am apelat metoda fly care e implementata in clasa Penguin, deci va fi apelata de aici. Va printa pe ecran I actually can't fly. But that's ok, I'm dressed stylish.
