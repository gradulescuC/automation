'''
1.
Declara o lista note_muzicale in care sa pui do re mi etc pana la do
a)	Afiseaz-o
b)	Inverseaza ordinea folosind slicing si suprascrie aceasta lista
c)	Printeaza varianta actuala (inversata)
d)	Pe aceasta lista, aplica o metoda care banuiesti ca face acelasi lucru, adica sa ii inverseze ordinea.
    (Nu trebuie sa o suprascrii in acest caz, deoarece metoda face asta automat)
e)	Printeaza varianta actuala a listei. Practic ai ajuns inapoi la varianta initiala

Concluzii: slicing e temporar, daca vrei sa pastrezi noua varianta va trebuie sa suprascrii lista sau sa o salvezi
intr-o lista noua. Metoda gasita de tine, face suprascrierea automat si permanentizeaza aceste modificari.
Ambele variante isi gasesc utilitatea in functie de ce ne dorim in acel moment.
'''

# note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# print(note_muzicale)  # A
# note_muzicale = note_muzicale[::-1]  # B
# print(note_muzicale)  # C
# (note_muzicale.reverse())  # D
# print(note_muzicale)  # E

'''
2. 
De cate ori apare ‘do’?
'''
# print('Nota muzicala DO apare de ', note_muzicale.count('do'), ' ori!')

'''
3.
Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4]
Gasiti 2 variante sa le uniti intr-o singura lista. 
Afisati lista ordonata astfel [0,1,2,3,4,5,6
'''
# lista_1 = [3, 1, 0, 2]
# print(lista_1)
# lista_2 = [6, 5, 4]
# print(lista_2)
# lista_3 = lista_1 + lista_2
# print(lista_3)
# lista_3.sort()
# print(lista_3)
#V2

# lista_2 += lista_1
# lista_2.sort()
# print(lista_2)

'''
4.
Sortati si afisati lista generata la ex anterior
Stergeti numarul 0 folosind o functie
Afisati iar lista
'''

lista_1 = [3, 1, 0, 2]
print(lista_1)
lista_2 = [6, 5, 4]
print(lista_2)
lista_3 = lista_1 + lista_2
lista_3.sort()
print(lista_3)
trash = lista_3.pop(0)
print(trash,'is deleted')
print(lista_3)

'''
5.
Folosind un if verificati lista generata la ex3 si afisati
-	Lista este goala
-	Lista nu este goala

NOTA: In Python modul cel mai Pytonian este sa folosesti listele drept True sau False prin faptul ca ele sunt sau nu goale 
'''
# lista_1 = [3, 1, 0, 2]
# print(lista_1)
# lista_2 = [6, 5, 4]
# print(lista_2)
# lista_3 = lista_1 + lista_2
# lista_3.sort()
# #V1
# if lista_3:
#     print('The list is not empty ',lista_3)
# else:
#     print('The list is empty',lista_3)
'''
6. 
Folositi o functie care sa stearga lista de la ex3
7. 
Copy paste la ex 5. Verificati inca o data.
Acum ar trebui sa se afiseze ca lista e goala
'''
# #V2
# lista_2.clear()
# if bool(lista_2):  # in loc de bool se poate folosi si len
#     print('The list is not empty ',lista_2)
# else:
#     print('The list is empty',lista_2)
# #V3
# lista_1.clear()
# if len(lista_1) == 0 :
#     print('The list is empty', lista_1)
# else:
#     print('The list is not empty ', lista_1)

'''
8. 
Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
Folositi o functie ca sa afisati Elevii (cheile)
'''
# dict1 = {'Ana' : 8 ,  'Gigel' : 10 , 'Dorel' : 5}
# print(dict1.keys())

'''
9. 
Printati cei 3 elevi si notele lor
Ex: ‘Ana a luat nota {x}’
Doar nota o veti lua folosindu-va de cheie
'''
# print('Ana a luat nota ',(dict1.get('Ana')))
# print('Gigel a luat nota ',(dict1.get('Gigel')))
# print('Dorel a luat nota ',(dict1['Dorel']))

'''
10.
Dorel a facut contestatie si a primit 6
Modificati nota lui Dorel in 6
Printati nota dupa modificare
'''
# dict1['Dorel'] = 6
# print(dict1['Dorel'])

'''
11.
Gigel se transfera din clasa
Cautati o functie care sa il stearga
Vine un coleg nou. Adaugati Ionica, cu nota 9
Printati noii elevi
'''

# dict1.pop('Gigel')
# print(dict1.keys())
# dict1['Ionica'] = 9
# print(dict1.keys())

'''
12.
Set
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
Adaugati in zilele_sapt ‘luni’
Afisati zile_sapt
'''
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
print(zile_sapt)
zile_sapt.add('luni') # in seturi nu se accepta duplicate , doar elemente unice, daca ar fi scris cu majuscule ar accepta
print(zile_sapt)
print(weekend)

'''
13.
Folositi un if si verificati daca 
-	Weekend este un subset al zilelor din sapt
-	Weekend nu este un subset al zilelor din sapt
'''
if weekend.issubset(zile_sapt):
    print('Weekend este un subset al zile_saptamana')
else:
    print('Weekend nu este un subset al zile_saptamana')

'''
14. 
Afisati diferentele dintre aceste 2 seturi
'''
print(zile_sapt.difference(weekend))

'''
15.
Afisati intersectia elementelor din aceste 2 seturi
'''

print(zile_sapt.intersection(weekend))