# print('-----------1------------')
'''
1.
Avand lista
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

Folositi un for ca sa iterati prin toata lista si sa afisati
‘Masina mea preferata este x’
Faceti acelasi lucru cu un for each
Faceti acelasi lucru cu un while
'''
'''------------FOR------------'''
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for i in masini:
#     print(f'Masina mea preferata este {i} ')
'''----------FOR-EACH----------'''
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for marca in masini:
#     print(f'Masina mea preferata este {marca}')
'''-----------WHILE-------------'''
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# i = 0
# while i < len(masini):
#     for marca in masini:
#        print(f'Masina mea preferata este {marca}')
#     i += 1
# # print('-----------2------------')
# '''
# 2.
# Aceeasi lista
# Folositi un for else
# In for
#    Modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimul
# In else
#    Printati lista
# '''

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for maj in masini[1:-1]:
#      print(f'Acestea le-am scris cu majuscule uite asa= ', maj.upper())
# else:
#      print(f'Acestea nu le-am modificat = ', masini[0], ' si ', masini[-1])
# # print('-----------3------------')
#
# '''
# 3.
# Aceeasi lista,
# Vine un cumparator care doreste sa cumpere un Mercedes
# Iterati prin ea prin modalitatea aleasa de voi
# Daca masina e mercedes
#    Printam ‘am gasit masina dorita de dvs’
#    Iesim din ciclu folosind un cuvant cheie care face acest lucru
# Altfel
#    Printam Am gasit masina X. Mai cautam
# '''
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for client_vrea in masini:
#      if client_vrea == 'Mercedes':
#          print(f'Clientul si-a gasit masina dorita adica un',client_vrea)
#          break
# print('-----------4-5-v1----------')
# '''
# 4.
# Aceasi lista
# Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun
#
# 5.
# Modernizati parcul de masini
# Creati o lista goala, masini_vechi
# Iterati prin masini
# Cand gasiti Lastun sau Trabant:
# -	Salvati aceste masini in masini_vechi
# -	Suprascrieti-le cu ‘Tesla’ (in lista initiala de masini)
# Printati Modele vechi: x
# Modele noi: x
#
# '''
#
# # masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# # masini_vechi = []
# # nr = 0
# # for prezentare in masini:
# #     if prezentare == 'Lastun':
# #         nr = masini.index('Lastun')
# #         masini_vechi.append(prezentare)
# #         masini.remove('Lastun')
# #         masini.insert((nr), 'Tesla')
# #     elif prezentare == 'Trabant':
# #         nr = masini.index('Trabant')
# #         masini_vechi.append(prezentare)
# #         masini.remove('Trabant')
# #         masini.insert((nr), 'Tesla')
# #     else:
# #         pass
# # print(masini_vechi)
# # print(masini)
# # print('---------4-v2---------')
#
#
# '''
# 4.
# Aceasi lista
# Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun
# Daca masina e Trabant sau Lastun
# Folositi un cuvant cheie care sa dea skip la ce urmeaza
# (nu trebuie else)
# Printati S-ar putea sa va placa masina x
# '''
# # masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# # for prezentare in masini:
# #     if prezentare == 'Lastun':
# #         continue
# #     elif prezentare == 'Trabant':
# #         continue
# #     print(f's-ar putea sa va placa masina', prezentare)
# # print('---------5-v2---------')
#
# '''
# 5.
# Modernizati parcul de masini
# Creati o lista goala, masini_vechi
# Iterati prin masini
# Cand gasiti Lastun sau Trabant:
# -	Salvati aceste masini in masini_vechi
# -	Suprascrieti-le cu ‘Tesla’ (in lista initiala de masini)
# Printati Modele vechi: x
# Modele noi: x
# '''
#
# # masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# # masini_vechi = []
# # nr = 0
# # for masina in masini:
# #     if masina == 'Lastun':
# #         nr = masini.index('Lastun')
# #         masini_vechi.append(masina)
# #         masini.remove('Lastun')
# #         masini.insert((nr), 'Tesla S')
# #     elif masina == 'Trabant':
# #         nr = masini.index('Trabant')
# #         masini_vechi.append(masina)
# #         masini.remove('Trabant')
# #         masini.insert((nr), 'Tesla X')
# # print(f'Modele vechi:', masini_vechi)
# # print(f'Modele noir', masini)
# # print('-----------6------------')
#
# '''
# 6.
# Avand dict
# pret_masini = {
#     'Dacia': 6800,
#     'Lastun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000 }
# Vine un client cu un buget de 15000 euro
# Prezentati doar masinile care se incadreaza in acest buget
# Iterati prin dict.items() si accesati masina si pretul
# Printati Pentru un buget de sub 15000 euro puteti alege masina x
# Iterati prin lista
#
# '''
#
# pret_masini = {
#      'Dacia': 6800,
#      'Lastun': 500,
#      'Opel': 1100,
#      'Audi': 19000,
#      'BMW': 23000 }
# buget = 15000
# for oferta in pret_masini.items():
#      if oferta[1] <= buget:
#          print(f'Pentru un buget de sub 15000 euro puteti alege masina', oferta[0])
# # print('-----------7------------')
#
# '''
# 7.
# Avand lista
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# Iterati prin ea
# Afisati de cate ori apare 3
# (nu aveti voie sa folositi count)
#
# '''
#
# # numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# # numaratoare = 0
# # for numar in numere:
# #     if numar == 3:
# #         numaratoare += 1
# # print(f'In lista de numere nr 3 apare de ', numaratoare, 'ori')
# # print('-----------8------------')
#
#
# '''
# 8.
# Aceeasi lista
# Iterati prin ea
# Calculati si afisati suma numerelor
# (nu aveti voie sa folositi sum)
# '''
# # numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# # sum = 0
# # for numar in numere:
# #     sum += numar
# # print(f'Suma numerelor din lista este:', sum)
# # print('-----------9------------')
#
# '''
# 9.
# Aceeasi lista
# Iterati prin ea
# Afisati cel mai mare numar
# (nu aveti voie sa folositi max)
# '''
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# nr_max = None
# for nr in numere:
#      if (nr_max is None or nr > nr_max):
#          nr_max = nr
# print(f'Cel mai mare numar este:' , nr_max)
# # print('-----------10------------')
#
# '''
# 10.
# Aceeasi lista
# Iterati prin ea
# Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
# Ex: daca e 3, sa devina -3
# Afisati noua lista
# '''
#
# # numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# # neg = []
# # for poz in numere:
# #     if poz >= 0:
# #         neg.append(poz*(-1))
# #     else:
# #         neg.append(poz)
# # print(neg)
# # print('-----------11------------')
#
# '''
# Optionale (may need google)
#
# 11.
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# Iterati prin lista alte_numere
# Populati corect celelalte liste
# Afisati cele 4 liste la final
# '''
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# for nr in alte_numere:
#      if nr < 0:
#          numere_negative.append(nr)
#          if (nr % 2) == 0:
#              numere_pare.append(nr)
#          else:
#              numere_impare.append(nr)
#      else:
#          numere_pozitive.append(nr)
#          if (nr % 2) == 0:
#              numere_pare.append(nr)
#          else:
#              numere_impare.append(nr)
# # print(f'Acestea sunt numere pare: ',numere_pare)
# # print(f'Acestea sunt numere impare:', numere_impare)
# # print(f'Acestea sunt numere pozitive', numere_pozitive)
# # print(f'Acestea sunt numere negative', numere_negative)
# # print('-----------12------------')
#
# '''
# 12.
# Aceeasi lista
# Ordonati crescator lista fara sa folositi sort
# Va puteti inspira vizual de aici
# https://www.youtube.com/watch?v=lyZQPjUT5B4
# '''
# a_n = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# print(f'lista nesortata este {a_n}')
# for j in range(len(a_n)):
#      swapped = False
#      i = 0
#      while i<len(a_n)-1:
#          if a_n[i]>a_n[i + 1]:
#              a_n[i], a_n[i + 1] = a_n[i + 1], a_n[i]
#              swapped = True
#          i = i+1
#      if swapped == False:
#         break
# print (f'lista sortata este {a_n}')
# # print('-----------13------------')
#
#
# '''
# 13.
# Ghicitoare de numar
# numar_secret = Generati un numar random intre 1 si 30
# Numar_ghicit = None
# Folosind un while
#    User alege un numar
#    Programul ii spune:
# -	Nr secret e mai mare
# -	Nr secret e mai mic
# -	Felicitari! Ai ghicit!
# Norocul meu ca m-am uitat un pic la un webinar de python pe youtube ;-)
# macar am comentarii perfecte ca sa si inteleg, mersi Andy!
# '''
# # import random  # imprumutam cod extern, ca sa nu mai reinventam noi logica
# #
# # numar_secret = random.randint(0, 30)  # generam un numar aleatoriu intre 0 si 30
# # numar_ghicit = None  # setam numarul ghicit cu o valoare gresita
# #
# # # atat timp cat numarul ghicit e diferit de numarul secret jocul incepe/continua
# # while numar_ghicit != numar_secret:  # != verifica daca stanga e diferita de dreapta
# #     # luam de la tastatura o valoare si o transformam in nr intreg
# #     numar_ghicit = int(input("ghiceste un numar intre 0 si 30 \n"))
# #     # scriem logica pentru cele 3 cazuri posibile
# #     if numar_secret > numar_ghicit:
# #         print("Numarul secret e mai mare")
# #     elif numar_secret < numar_ghicit:
# #         print("Numarul secret e mai mic")
# #     else:
# #         print("Felicitari!!!")
#
#
# '''
# 14.
# Alegeti un numar de la tastatura
# Ex:7
# Scrieti un program care sa genereze in consola urmatoarea piramida
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# '''
# x = int(input('Introduceti un numar care da inaltimea si baza piramidei:\n'))
# for nr in range(x) :
#     while()

# x = 1
# while x<=7:
#     for i in range(x,x+1):
#         print(str(i)*x)
#     x+=1
