#1 Declara o lista note_muzicale in care sa pui do re mi etc pana la do
#
note_muzicale = ['Do','Re','Mi','Fa','Sol','La','Si','Do']  #am creat o lista
print(note_muzicale)                                        #am afisat o lista
reversed = note_muzicale[::-1]                              #am inversat lista folosind slice
print(reversed)                                             #am printat lista inversata
re_reversed = note_muzicale[::1]                            #am reinversat lista inversata tot cu slice (alta metoda nu stiu)
print(re_reversed)                                          #am afisat-o

# #2 De cate ori apare ‘do’?
#
# print(note_muzicale.count('Do'))                           #am afisat de cate ori apare nota Do cu functia COUNT


#3 Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4]
# Gasiti 2 variante sa le uniti intr-o singura lista. Afisati lista ordonata astfel [0,1,2,3,4,5,6]

#varianta 1
list1 = [3,1,0,2]
list2 = [6,5,4]
list3 = list1 + list2                           #creez o lista noua.
list3.sort()                                    #cu functia .sort am sortat noua lista
print(list3)
#
# #varianta 2
# print(list1[2],list1[1],list1[3],list1[0],list2[2],list2[1],list2[0])

#4 Sortati si afisati lista generata la ex anterior
# print(list3)                                           #am afisat lista generata anterior
# print(list3[1:7])                                      #am folosit slice pentru a afisat tot mai putin 0
# print(list3.remove(0))                                 #folosind remove am scos cifra 0

#5 Folosind un if verificati lista generata la ex3 si afisati

if list3 :
    print('Lista nu este goala')
else :
    print('Lista este goala')

#6 Folositi o functie care sa stearga lista de la ex

remove_list = list3.clear()                     #am sters toate elementele din lista.
print(remove_list)                              #am demonstrat ca nu mai este nimic in lista.

#
# #7 Copy paste la ex 5. Verificati inca o data.Acum ar trebui sa se afiseze ca lista e goala
#
if list3 :
    print('Lista nu este goala')
else :
    print('Lista este goala')               #se va apela la functia else deoarece am sters lista mai sus.

#8 Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5} Folositi o functie ca sa afisati Elevii (cheile)

dict1 = {'Ana' : 8,'Gigel' : 10,'Dorel' : 5}

# print(dict1.keys())
#
# #9 Printati cei 3 elevi si notele lor
#
# print(dict1)

#10 Dorel a facut contestatie si a primit 6; Modificati nota lui Dorel in 6

# dict1['Dorel'] = '6'
# print(dict1)

#11 Gigel se transfera din clasa; Cautati o functie care sa il stearga ; Vine un coleg nou. Adaugati Ionica, cu nota 9
# dict1['Ionica'] = '9'
# dict1.pop('Gigel')
# print(dict1)

#12 Set zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'} weekend = {'sambata', 'duminica'}

zile_sapt = {'luni','marti','miercuri','joi','vineri','sambata','duminica'}
weekend = {'sambata','duminica'}
zile_sapt.add('LUNI')
print(zile_sapt)

#13 Folositi un if si verificati daca: Weekend este un subset al zilelor din sapt sau Weekend nu este un subset al zilelor din saptamana.

if not zile_sapt == weekend :
    print('Weekendul este un subset al zileleor din sapt')
else :
    print('wekeendul nu este un subset al zilelor din sapt')

# #14 Afisati diferentele dintre aceste 2 seturi

# print(zile_sapt.difference(weekend))                    #afisez diferenta dintre o saptamana intraega si weekend

#15 Afisati intersectia elementelor din aceste 2 seturi

# print(zile_sapt.intersection(weekend))                  #afisez zilele comune dintre 2 seturi




