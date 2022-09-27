# Liste
a = [1, 2, 3]  # Listele sunt definite intotdeauna intre paranteze drepte
b = ['banane', 'mere', 'gutui']
c = [4, 'struguri', True]

print(a)
print(b)
print(c)
print(a, b, c)
# Fiecare element dintr-o lista se afla la o anumita pozitie. In orice lista, prima pozitie este plasata la indicele 0
print(a[0])
print(b[0])
print(c[0])
print(a[0], b[0], c[0])
print("Ultimul caracter din fiecare lista e: ", a[-1], b[-1], c[-1])  # Afiseaza ultimul caracter
print("Ultimul caracter din fiecare lista e: ", a[2], b[2], c[2])  # Afiseaza ultimul caracter
# print(a[3])  #Returneaza eroare: IndexError: list index out of range. In cazul asta executarea restului de instructiuni se va opri
# Acelasi lucru cand se vor executa testele automate
print("Primele doua elemente din lista a sunt:", a[0:2])  # Afiseaza primele doua elemente din lista
print("Elementele din lista a sunt:",
      a[0:3])  # Afiseaza toate elementele din lista. Nu da eroare daca specifici un numar mai mare
print("Elementele din lista a sunt:", a[0:len(a)])  # Afiseaza toate elementele din lista.
# len este prescurtarea de la length si arata cate elemente sunt in lista respectiva
print(
    b.count("mere"))  # Functia count arata cate  elementele din cele mentionate in paranteza exista in lista respectiva
c[-1] = "Portocale"  # Modifica un singur element din lista
print(c)

print(sum(a))  # Calculeaza suma tuturor elementelor din lista a

a.clear()
print(a)

a.append("banane")
print(a)
a.append(3)  # Se pot adauga mai multe elemente cu flow control, intr-un curs viitor
print(a)
print(3 in a)  # Verifica daca un anumit element exista intr-o lista

# Tuples
# Un tuplu incepe intotdeauna cu paranteze rotunde. Tuplurile sunt immutable
# Fiecare element al unui tuplu e plasat la o anumita pozitie, care incepe de la indexul 0
myTuple = (1, 2, 5, 7)
print(myTuple[3])
# print(myTuple[5]) -> Da eroare daca incercam sa accesam un element dintr o pozitie care nu exista
print(len(myTuple))
print(5 in myTuple)  # Verifica daca un anumit element exista intr-un tuple
print(myTuple.count(5))  # Verifica de cate ori apare un anumit element intr-un tuple

# myTuple[0] = 8  -> Returneaza eroare: TypeError: 'tuple' object does not support item assignment - pentru ca un tuple este immutable

tup = 2, 3, 4
print(type(tup))  # Prin conventie, o succesiune de numere asignata la o variabila e vazut ca un tuplu

# Sets
# Sets are a collection of not organized data with unique elements
mySet = {13, 5, 67, 5}
print(mySet)
mySet.add(7);
mySet.add(7.5);
mySet.add(9);
print(mySet)
# print(mySet[0]) -> Returneaza eroare: TypeError: 'set' object is not subscriptable - pentru ca seturile nu sunt ordonate

myList = [13, 5, 67, 5]
print(myList)
print(set(myList))
print(list(set(myList)))

# Dictionaries
# Dictionarele sunt colectii de date neordonate care stocheaza perechi cheie:valoare. Vor fi folosite pentru API Testing

# Exista doua feluri de a defini un dictionar:

myDict1 = dict(a=1, b="Bella Ciao")

myDict = {"a": "My data for a",
          "b": "My data for b",
          7: "Python",
          True: [5, 16, 45],  # Putem de asemenea sa adaugam valori boolean intr-un dictionar
          "c": [dict(a=1, b="Bella"), dict(a=1, b="Ciao"), dict(a=1, b="aloha")]
          }

print(myDict)
print(myDict1)

# Posibilitati de extragere a unui element dintr-un dictionar:
print(myDict["a"])
print(myDict1["b"])
print(myDict[True][0])
print(myDict["c"][2]["b"])
print(myDict.get(7))

# Loop control -> Metoda de a itera printr-o colectie de date

"""k,v = key, value"""
for k,v  in myDict.items():
    # print("Urmatorul element din iteratie este: ",  k,v)
    if k == 7:
        print("Valoarea pentru elementul 7 este : ", v)
    elif k == "c":
        print ("Valoarea pentru elementul c este:" , v)
    else:
        print("Treci la urmatoarea valoare")








