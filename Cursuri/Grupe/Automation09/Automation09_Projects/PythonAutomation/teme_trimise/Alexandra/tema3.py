# 1.
# Declara o lista note_muzicale in care sa pui do re mi etc pana la do
# Afiseaz-o
# Inverseaza ordinea folosind slicing si suprascrie aceasta lista
# Printeaza varianta actuala (inversata)
# Pe aceasta lista, aplica o metoda care banuiesti ca face acelasi lucru, adica sa ii inverseze ordinea. (Nu trebuie sa o suprascrii in acest caz, deoarece metoda face asta automat)
# Printeaza varianta actuala a listei. Practic ai ajuns inapoi la varianta initiala
#
# Concluzii: slicing e temporar, daca vrei sa pastrezi noua varianta va trebuie sa suprascrii lista sau sa o salvezi intr-o lista noua.
# Metoda gasita de tine, face suprascrierea automat si permanentizeaza aceste modificari.
# Ambele variante isi gasesc utilitatea in functie de ce ne dorim in acel moment.
#
# note_muzicale = ['do','re','mi','fa','sol','la', 'si','do']
# print(note_muzicale)
note_muzicale1 = ['do','re','mi','fa','sol','la', 'si','do']
# print(note_muzicale1 [ :: -1])
# list.reverse(note_muzicale1)
# print(note_muzicale1)
# note_muzicale1.reverse()
# print(note_muzicale1)
#
# Run:
# ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# ['do', 'si', 'la', 'sol', 'fa', 'mi', 're', 'do']
# ['do', 'si', 'la', 'sol', 'fa', 'mi', 're', 'do']
#
#
#
#
# 2.
# De cate ori apare ‘do’?
#
#
# nota = note_muzicale1.count('do')
# print(nota)
#
# Run: 2
#
#
#
# 3.
# Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4]
# Gasiti 2 variante sa le uniti intr-o singura lista.
# Afisati lista ordonata astfel [0,1,2,3,4,5,6]
#

list1 = [3, 1, 0, 2]
list2 = [6, 5, 4]
new_list = list1 + list2
print(new_list)
#
# Metoda sorted
#
# new_list = sorted(list1 + list2)
# print(new_list)
#
# Metoda sort
#
#
# def lista_noua (list1, list2) :
#     lista_noua = list1 + list2
#     lista_noua.sort()
#     return(lista_noua)
# print(lista_noua(list1, list2))
#
#
#
# 4.
# Sortati si afisati lista generata la ex anterior
# Stergeti numarul 0 folosind o functie
# Afisati iar lista
#
#
# new_list = sorted(list1 + list2)
# print(new_list)
# print(new_list[0])
# print(len(new_list))
# print(new_list[1:7])
#
#
#
# 5.
# Folosind un if verificati lista generata la ex3 si afisati
# Lista este goala
# Lista nu este goala

if len(new_list) == 0 :
    print('Lista este goala')
else :
    print('Lista nu este goala')

#
# 6.
# Folositi o functie care sa stearga lista de la ex3

new_list.clear()
print(new_list)
#
#
# 7.
# Copy paste la ex 5. Verificati inca o data.
# Acum ar trebui sa se afiseze ca lista e goala

# if len(new_list) == 0 :
if new_list==[]:
    print('Lista este goala')
else:
    print('Lista nu este goala')

#
# 8.
# Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folositi o functie ca sa afisati Elevii (cheile
#
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
def getList(dict1):
    return dict1.keys()
print(getList(dict1))
#
#
# 9.
# Printati cei 3 elevi si notele lor
# Ex: ‘Ana a luat nota {x}’
# Doar nota o veti lua folosindu-va de cheie

dict1 = {'Ana' : 8,
         'Gigel' : 10,
         'Dorel' : 5}
print(dict1.keys())
for k,v in dict1.items():
    print(k,'a luat nota',v)
#
#
#
#
# 10.
# Dorel a facut contestatie si a primit 6
# Modificati nota lui Dorel in 6
# Printati nota dupa modificare
#
dict1['Dorel'] = '6'
print(dict1)
#
#
#
# 11.
# Gigel se transfera din clasa
# Cautati o functie care sa il stearga
# Vine un coleg nou. Adaugati Ionica, cu nota 9
# Printati noii elevi
#
#
dict1.pop('Gigel')
print(dict1)

dict1['Ionica'] = '9'
print(dict1)
#
#
# Run:
# {'Ana': 8, 'Dorel': '6'}
# {'Ana': 8, 'Dorel': '6', 'Ionica': '9'}
#
#
#
# 12.
# Set
# zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# weekend = {'sambata', 'duminica'}
# Adaugati in zilele_sapt ‘luni’
# Afisati zile_sapt
#
# zile_sapt = { 'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# weekend = {'sambata', 'duminica'}
# zile_sapt.add('luni')
# print(zile_sapt.add('luni'))
# Run : none
#
#
#
# 13.
# Folositi un if si verificati daca
# Weekend este un subset al zilelor din sapt
# Weekend nu este un subset al zilelor din sapt
#
#
zile_sapt = { 'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}

if weekend.issubset(zile_sapt):
     print(print ('Weekend este un subset al zilelor din sapt'))
else:
     print(print('Weekend nu este un subset al zilelor din sapt'))
#
#
# 14.
# Afisati diferentele dintre aceste 2 seturi
#
#
# print(zile_sapt.difference(weekend))
#
#
# 15.
# Afisati intersectia elementelor din aceste 2 seturi
#
#
# print(zile_sapt.intersection(weekend))
#
#
# c. Optionale (may need google)
# 16.
# Ne imaginam o echipa de fotbal pt teren sintetic.
# 3 Schimbari maxime admise
#
# Declara o Lista cu 5 jucatori
# Schimbari_efectuate = va jucati voi cu valori diferite
# Schimbari_max = 3
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

jucatori = ['Marian','Mihai','Ionel','Matei','Petru']
schimbari_efectuate = 0
#
if 'Marian' in jucatori and schimbari_efectuate <=3 :
    jucatori.remove('Marian') and jucatori.insert('Doru')
    schimbari_efectuate = schimbari_efectuate + 1
    print(f'Marian a parasit meciul, insa a intrat Doru, mai avem { 3 - schimbari_efectuate} schimbari')
else :
    print('Nu se poate efectua schimbarea pentru ca jucatorul nu este in teren')
print(f'Mai avem { 3- schimbari_efectuate} schimbari')

if 'Petru' in jucatori and schimbari_efectuate <= 3 :
    jucatori.remove('Petru') and jucatori.insert('Sebastian')
    schimbari_efectuate = schimbari_efectuate + 2
    print(f'Petru a parasit terenul, insa a fost inlocuit cu Sebastian, ne mai raman {3 - schimbari_efectuate} schimbari')
else:
    print('Nu se poate efectua schimbarea')
print(f'Mai avem { 3 - schimbari_efectuate} schimbari')
#
#
#
#
#
#
#
#
#
