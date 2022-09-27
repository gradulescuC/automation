''' a. Usor (recomandat)
1. Revizualizeaza intalnirea 3 si ia notite in caz ca ti-a scapat ceva
2. Vizualizeaza video despre Structuri de date din 'Primii pasi in Programare'
(Daca nu ai facut-o deja)
3. Vizualizeaza video 4 despre Flow Control din 'Primii pasi in Programare'
Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele
si sigur ti se vor intipari in minte mai bine.
https://www.itfactory.ro/8174437-intro-in-programare/

b. Usor spre Mediu (obligatoriu)
'''

print('---------------#1---------------')
# #1. Declara o lista note_muzicale in care sa pui do re mi etc pana la do
# Afiseaz-o.
# Inverseaza ordinea folosind slicing si suprascrie aceasta lista. # Printeaza varianta actuala (inversata)
# Pe aceasta lista, aplica o metoda care banuiesti ca face acelasi lucru, adica sa ii inverseze ordinea.
# (Nu trebuie sa o suprascrii in acest caz, deoarece metoda face asta automat)
# Printeaza varianta actuala a listei. Practic ai ajuns inapoi la varianta initiala
# Concluzii: slicing e temporar, daca vrei sa pastrezi noua varianta va trebuie sa suprascrii lista sau sa o salvezi intr-o lista noua.
# Metoda gasita de tine, face suprascrierea automat si permanentizeaza aceste modificari.
# Ambele variante isi gasesc utilitatea in functie de ce ne dorim in acel moment.

note_muzicale=['do','re','mi','fa','sol','la','si','do']
print(note_muzicale)
note_muzicale=note_muzicale[::-1]
print(note_muzicale)
note_muzicale.reverse()
print(note_muzicale)

print('---------------#2---------------')
# 2. De cate ori apare ‘do’?
print('nota "do" apare de', note_muzicale.count('do'), 'ori')

print('---------------#3---------------')
# 3. Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4], Gasiti 2 variante sa le uniti intr-o singura lista.
# Afisati lista ordonata astfel [0,1,2,3,4,5,6]

lista1=[3,1,0,2]
lista2=[6,5,4]

#varianta 1
lista_final_1=lista1+lista2 #lista_final_1=[*lista1, *lista2] = care e diferenta intre varianta asta si cea de sus?
print(lista_final_1)
print(sorted(lista_final_1))

#varianta 2
lista1.extend(lista2)
print(lista1)
lista1.sort()
print(lista1)

print('---------------#4---------------')
# 4. Sortati si afisati lista generata la ex anterior, Stergeti numarul 0 folosind o functie, Afisati iar lista
lista_final_1.remove(0)
print(sorted(lista_final_1))

print('---------------#5---------------')
# 5.Folosind un if verificati lista generata la ex3 si afisati
# Lista este goala
# Lista nu este goala

if not lista_final_1 == [ ]:
    print('Lista NU este goala')
else:
    print ('Lista este goala')

print('---------------#6---------------')
# 6.Folositi o functie care sa stearga lista de la ex3
lista_final_1.clear()
print(lista_final_1)

print('---------------#7---------------')
# 7.Copy paste la ex 5. Verificati inca o data. Acum ar trebui sa se afiseze ca lista e goala

if not lista_final_1 == [ ]:
    print('Lista NU este goala')
else:
    print ('Lista este goala')

print('---------------#8---------------')
# 8. Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}. Folositi o functie ca sa afisati Elevii (cheile

dict1={'Ana':8, 'Gigel':10, 'Dorel':5}
print(dict1.keys())

print('---------------#9---------------')
# 9. Printati cei 3 elevi si notele lor. Ex: ‘Ana a luat nota {x}’. Doar nota o veti lua folosindu-va de cheie

print('Ana a luat nota', dict1['Ana'])
print('Gigel a luat nota', dict1['Gigel'])
print('Dorel a luat nota', dict1['Dorel'])

print('---------------#10---------------')
# 10.Dorel a facut contestatie si a primit 6. Modificati nota lui Dorel in 6. Printati nota dupa modificare

dict1['Dorel']=6
print('Dorel a facut contestatie si a primit', dict1['Dorel'])

print('---------------#11---------------')
# 11.Gigel se transfera din clasa. Cautati o functie care sa il stearga. Vine un coleg nou. Adaugati Ionica, cu nota 9
# Printati noii elevi

dict1.pop('Dorel')
print(dict1)
dict1['Ionica']=9
print(dict1)

print('---------------#12---------------')
# 12. Set zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}, weekend = {'sambata', 'duminica'}
# Adaugati in zilele_sapt ‘luni’
# Afisati zile_sapt

zile_sapt={'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend={'sambata', 'duminica'}
print(zile_sapt)
zile_sapt.add('luni')
print(zile_sapt)

print('---------------#13---------------')
# 13. Folositi un if si verificati daca: Weekend este un subset al zilelor din sapt, Weekend nu este un subset al zilelor din sapt

if weekend.issubset(zile_sapt):
    print('Weekend este subset al zilelor din sapt')
else:
    print('Weekend nu este un subset al zilelor din sapt')

print('---------------#14---------------')
# 14. Afisati diferentele dintre aceste 2 seturi
diferente=zile_sapt.difference(weekend)
print(diferente)

print('---------------#15---------------')
# 15. Afisati intersectia elementelor din aceste 2 seturi
intersectie=zile_sapt.intersection(weekend)
print(intersectie)

print('---------------#16---------------')

# c. Optionale (may need google)
# 16.
# Ne imaginam o echipa de fotbal pt teren sintetic.
# 3 Schimbari maxime admise
#
# Declara o Lista cu 5 jucatori
# Schimbari_efectuate = va jucati voi cu valori diferite
#
# Daca Jucatorul x e in teren si mai avem schimbari la dispozitie
# Efectuam schimbarea
# Stergem jucatorul scos din lista
# Adaugam jucatorul intrat
# Afisam a intra x, a iesit y, mai aveti z schimbari
# Daca jucatorul nu e in teren:
# Afisati ‘ nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
# Afisati ‘mai aveti z schimbari’
#
# Testati codul cu diferite valori
#
# Google search hint
# “how to check if item is in list python”
