# 1. Declara o lista note_muzicale in care sa pui do re mi etc pana la do
# a)	Afiseaz-o
# b)	Inverseaza ordinea folosind slicing si suprascrie aceasta lista
# c)	Printeaza varianta actuala (inversata)
# d)	Pe aceasta lista, aplica o metoda care banuiesti ca face acelasi lucru, adica sa ii inverseze ordinea. (Nu trebuie sa o suprascrii in acest caz, deoarece metoda face asta automat)
# e)	Printeaza varianta actuala a listei. Practic ai ajuns inapoi la varianta initiala

# list1 = ['do','re','mi','fa','sol','la','si','do']   # exemplu suprascriere
# print(list1)
# list2 = ['do','re','mi','fa','sol','la','si','do']
# print(list2[:: -1])
# list.reverse(list2)
# print(list.reverse(list2))
# print(list2)
#
# #Concluzii: slicing e temporar, daca vrei sa pastrezi noua varianta va trebuie sa suprascrii lista sau sa o salvezi intr-o lista noua.
# # Metoda gasita de tine, face suprascrierea automat si permanentizeaza aceste modificari.
# # Ambele variante isi gasesc utilitatea in functie de ce ne dorim in acel moment.
#
# #2. De cate ori apare ‘do’?
# #list1 = ['do','re','mi','fa','sol','la','si','do']
# cnt = list1.count('do')
# print(cnt)

#3.Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4]
#Gasiti 2 variante sa le uniti intr-o singura lista.
#Afisati lista ordonata astfel [0,1,2,3,4,5,6]

# #varianta cu sorted
list2 = [3, 1, 0, 2]
list3 = [6, 5, 4]
list4 = sorted(list2 + list3)
# print(list4)
#
# #varianta cu merge + sort
# def Merge(list2,list3) :
#     lista4 = list2 + list3
#     lista4.sort()
#     return(lista4)
# print(Merge(list2,list3))

# 4.Sortati si afisati lista generata la ex anterior
# Stergeti numarul 0 folosind o functie
# Afisati iar lista

list4 = sorted(list2 + list3)
print(list4)
print(list4[0]) # am accesat primul element din lista si l-am afisat pe ecran
print(len(list4))
print(list4[1:7])
print(list4)

#5. Folosind un if verificati lista generata la ex3 si afisati

#-	Lista este goala
#-	Lista nu este goala

a = [list4]
b = []
if not b:
    print('lista nu este goala')
else:
    print('lista este goala')


#6. Folositi o functie care sa stearga lista de la ex3
#
print(list4)
list4.clear()
print(list4)


#7. Copy paste la ex 5. Verificati inca o data.
#Acum ar trebui sa se afiseze ca lista e goala
### de revazut
a = list4
b = []
if b:
    print('lista nu este goala')
else:
    print('lista este goala')

#8.Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
#Folositi o functie ca sa afisati Elevii (cheile)

dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(dict1.keys())

#9.Printati cei 3 elevi si notele lor
#Ex: ‘Ana a luat nota {x}’
#Doar nota o veti lua folosindu-va de cheie

for k,v in dict1.items():
    print(k,'a luat nota',v)

#10.Dorel a facut contestatie si a primit 6
#Modificati nota lui Dorel in 6
#Printati nota dupa modificare

dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
dict1 ['Dorel'] = '6' # am actualizat valoarea pe baza de cheie
print(dict1)
print(dict1['Dorel'])

#11.Gigel se transfera din clasa, cautati o functie care sa il stearga
#Vine un coleg nou. Adaugati Ionica, cu nota 9
#Printati noii elevi

#adaugare informatie noua
dict1 ['Ionica'] = '9' # initializare informatie noua
print(dict1)

#stergere informatie existenta
dict1.pop('Dorel') # stergere informatie deja stocata
print(dict1)

#12.#Set- zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
#weekend = {'sambata', 'duminica'}
#Adaugati in zilele_sapt ‘luni’
#Afisati zile_sapt

zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
zile_sapt.add('luni')
print(zile_sapt.add('luni'))  #Add an element to a set. This has no effect if the element is already present!!!.
print(zile_sapt)


# 13.Folositi un if si verificati daca
# -	Weekend este un subset al zilelor din sapt
# -	Weekend nu este un subset al zilelor din sapt

print(weekend)

if weekend == zile_sapt:
     print(print ('Weekend este un subset al zilelor din sapt'))
else:
     print(print('Weekend nu este un subset al zilelor din sapt'))

#14. Afisati diferentele dintre aceste 2 seturi

print(zile_sapt.difference(weekend))

#15.Afisati intersectia elementelor din aceste 2 seturi

print(zile_sapt.intersection(weekend))