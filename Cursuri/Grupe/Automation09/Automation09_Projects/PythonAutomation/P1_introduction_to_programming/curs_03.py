#   # Liste
# nume = "Michael"
# # len(nume)  Va returna 4, pentru ca nume are 4 caractere
# # print(nume[0:2])  Va acoperi primele trei caractere din string
#
nume_as_list=['M','i','c','h','a','e','l']  #in cazul asta ar avem o lista cu 7 elemente, fiecare element reprezentant o litera
print(nume_as_list[0]) # va returna a, pentru ca la liste indicele incepe de la pozitia 0
# print(len(nume_as_list))
print(nume_as_list[:2])
# print("----------------------")
# # Cum scoatem un caracter?
# print(nume_as_list)
# litera = nume_as_list.remove('c')  # in functie de valoare
# print(litera)
# print(nume_as_list)
# print("Test")
# litera1 = nume_as_list.pop(1) # in functie de pozitie - extrage ultimul caracter
# print(litera1)
# print(nume_as_list)
#
# # Cum suprascriem?
# nume_as_list[0] = 'a'
# print(nume_as_list)
#
#
# # Cum adaugam la index?
# nume_as_list.insert(0,'R')
# print(nume_as_list)
#
# # Cum adaugam la final?
# nume_as_list.append('t')
# print(nume_as_list)
#
# # putem pune o lista in alta lista?
# lista_in_lista = [
#      [1,2,3],
#      [4,5,6],
#      [7,8,9],
#      [0]
#  ]
#
# # cum afisez 7?
# print(lista_in_lista)
# print(lista_in_lista[2])
# print(lista_in_lista[2][0])
#
# randul3 = lista_in_lista[2]
# print(randul3[0])
#
# # sau
# print(lista_in_lista[2][0])
#
# # luam la intamplare o valoare
# lista2 = ["tel1","tel2","tel3"]
# import random
#    # definesc indexul
# random_nr = random.randint(0, len(lista2))
#    # aleg telefonul
# # print(lista2[random_nr])
# print("----------------------------------------")
#
# # Set - avem valori unice
#
# vocale = {'a','e','i','o','u'}
# print(vocale)
# # print(vocale[0])
#
# # Adaugam un duplicat
# before = len(vocale)
# vocale.add('a') #daca litera deja exista nu da eroare, ci nu are niciun efect
#
# vocale.add('A')
# print(vocale)
# after = len(vocale)
# if before==after:
#      print("Ai adaugat un duplicat")
# litera = 'b'
# if litera in vocale:
#  print("litera e vocala")
#
#  print("----------------------------------------")
#
# # tuplu - este imutabil, adica o data definit nu se mai poate schimba (adauga sau sterge valori) - permite duplicate, e ordonata
# #  ex: un tuplu cu o echipa de campionat de sah pentru care au fost alesi trei elevi, si e posibil ca doi din ei sa aiba acelasi nume
#
# camere_hotel=(1,2,3,4,5,6,7)
# print(camere_hotel[1])
# print(camere_hotel)
# print(camere_hotel.count(7))  # verifica de cate ori apare un numar intr-un tuplu
# print(camere_hotel.index(7))
# print(len(camere_hotel))
#
# # dictionar - structura cheie-valoare
#
# capitale = {
#      'Romania':'Bucuresti',
#      'Ungaria':'Budapesta',
#      'Italia':'Roma',
#      'Bulgaria':'Sofia'}
#
# # putem sa accesam date?
# print(capitale['Romania'])
# print(capitale.get('Romania'))
#
#   # putem sa actualizam o informatie?
# capitale['Romania'] = 'Cluj'
# capitale.update({'Romania':'Alba'})
# print(capitale)
#
#   # putem sa adaugam o informatie?
# capitale['Ucraina']='Kiev'
# print(capitale)
#
# # putem sa stergem o informatie?
# capitale.pop('Romania')
# print(capitale)
#
# capitale2={'Liechtenstein':'Vaduz','Cehia':'Praga'}
# capitale.update(capitale2)
# print(capitale)
# capitale3 = {'Italia':'Milan'}
# capitale.update(capitale3)
# print(capitale)
#
# print("Test abc")
# print(capitale2.keys())
#
# lista = ["Romania","Bulgaria","Italia"]
# lista.pop(2)
# print(lista)
