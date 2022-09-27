# # 1.
# # Avand lista
#
# #masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# # a)	Folositi un for ca sa iterati prin toata lista si sa afisati
# # ‘Masina mea preferata este x’
# # for i in range(len(masini)):
# #     print(f'Masina mea preferata este {masini[i]}')
#
# # rezolvat
#
# # b)	Faceti acelasi lucru cu un for each
# # for masina in masini:
# # print(f'Masina mea preferata este {masina}')
# # rezolvat
#
#
# # c)	Faceti acelasi lucru cu un while
# # i=0
# # while i < len(masini):
# #     print(f'Masina mea preferata este {masini[i]}')
# #     i +=1
#
# # rezolvat
#
#
# # 2.
# # Aceeasi lista
# # Folositi un for else
# # In for
# #    Modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimul
# # In else
# #    Printati lista
#
# # for i in range(len(masini)):
# #     # masini[1:-1] = masini.upper()
# #     # print(masini)
# #     first_element = masini[0]
# #     # print(first_element)
# #     print(f'first {first_element}')
# #     middle_elements = masini[1:-1]
# #     print(f'mid {middle_elements}')
# #     last_elemnet = masini[-1]
# #     print(f'Last {last_elemnet}')
# #     #break
# #     c = middle_elements
# #     print(first_element+c+last_elemnet)
#
# # am incercat sa separ primul si ultimul element din lista iar pe cele din mijloc sa le maresc numai ca
# # nu merge functia upper cand fac slicing dar nici cu replace
#
#
# # 3.
# # Aceeasi lista,
# # Vine un cumparator care doreste sa cumpere un Mercedes
# # Iterati prin ea prin modalitatea aleasa de voi
# # Daca masina e mercedes
# #    Printam ‘am gasit masina dorita de dvs’
# #    Iesim din ciclu folosind un cuvant cheie care face acest lucru
# # Altfel
# #    Printam Am gasit masina X. Mai cautam
#
# masini= ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# # for masina in masini:
# #     if masina=='Mercedes':
# #         print('Am gasit masina dorita de dumneavoastra!')
# #         break
# #     else:
# #         print(f'Am gasit masina {masini}. Mai cautam')
#
# # 4.
# # Aceasi lista
# # Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun.
# # Daca masina e Trabant sau Lastun
# #    Folositi un cuvant cheie care sa dea skip la ce urmeaza
# # (nu trebuie else)
# # Printati S-ar putea sa va placa masina x.
#
# # masini= ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# # for masina in masini:
# #     if 'Trabant' in masina or 'Lastun' in masina:
# #          print(f'S-ar putea sa va placa {masina}')
#
#
# # masini= ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# # for masina in masini:
# #     if masina=='Trabant' or masina=='Lastun':
# #         continue
# #     print(f'S-ar putea sa va placa {masina}')
#
# # Rezolvat
#
#
#
# # 5.
# # Modernizati parcul de masini
# # Creati o lista goala, masini_vechi
# # Iterati prin masini
# # Cand gasiti Lastun sau Trabant:
# # -	Salvati aceste masini in masini_vechi
# # -	Suprascrieti-le cu ‘Tesla’ (in lista initiala de masini)
# # Printati Modele vechi: x
# # Modele noi: x
#
# old_cars = []
# new_cars = [x for x in masini if x != 'Trabant' and x != 'Lastun']
# for x in masini:
#     if 'Trabant' in x:
#         old_cars.append(x)
#     if 'Lastun' in x:
#         old_cars.append(x)
# masini[5] = 'Tesla'
# # masini[7] = 'Tesla'
# print(f'Modele Noi {new_cars}')
# print(f'Modele vechi {old_cars}')
# print(f'Lista masini {masini}')
#
# ######     Rezolvat
# #
# # 6.Avand dict
# # Vine un client cu un buget de 15000 euro
# # Prezentati doar masinile care se incadreaza in acest buget
# # Iterati prin dict.items() si accesati masina si pretul
# # Printati Pentru un buget de sub 15000 euro puteti alege masina xLastun
# # Iterati prin lista
# #
# # pret_masini = {
# #      'Dacia': 6800,
# #      'Lastun': 500,
# #      'Opel': 1100,
# #      'Audi': 19000,
# #      'BMW': 23000
# #  }
# # buget = 15000
# # for masina in pret_masini.values():
# #      if masina <= buget:
# #         print(f'Pentru un buget de sub 15000 euro, puteti alege masina {masina}')
#
#
#
# ######NU reusesc sa afisez keya in loc de Valorare
# #
# #
# # 7.
# # Avand lista
# #numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# # Iterati prin ea
# # for i in numere:
# #     print(i)
#
# # Afisati de cate ori apare 3 fara sa folositi count
#
# # for numar in numere:
# #     if numar == 3:
# #         print(numar)
#
# #
# # 8.
# # Aceeasi lista
# # Iterati prin ea
# # Calculati si afisati suma numerelor
# # (nu aveti voie sa folositi sum)
# # total = 0
# # for sum in range(len(numere)):
# #     total = total+numere[sum]
# # print(f'Suma este {total}')
# # sau
#
# # for sum in numere:
# #     total = total+sum
# # print(f'Suma este {total}')
#
# ####Rezolvat
# #
# # 9.
# # Aceeasi lista
# # Iterati prin ea
# # Afisati cel mai mare numar
# # (nu aveti voie sa folositi max)
# # max_number = numere[0]                    #luam primul nr din lista si-l redenumim max_number
# # for i in numere:                         #cream variabila i din numere
# #     if i > max_number:                   #punem conditia ca i sa fie mai mare decat primul numar din lista
# #        max_number =i                     # daca i este mai mare atunci ii ia valoarea si ruleaza pana cand nu mai gaseste o valoare mai mare
# # print(max_number)
#
# ##### Rezolvat
# #
# # 10.
# # Aceeasi lista
# # Iterati prin ea
# # Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
# # Ex: daca e 3, sa devina -3
# # Afisati noua lista
# # numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# # for i in range(len(numere)):
# #     if i >= 0:
# #         i = -numere[i]
# #         print(f'Lista contine nr: {i}')
#
# #####Rezolvat
# #
# #
# #
# #
# # c. Optionale (may need google)
# #
# # 11.
#
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# # Iterati prin lista alte_numere
# # Populati corect celelalte liste
# # Afisati cele 4 liste la final
# for numar in alte_numere:
#     if numar >=0:
#         numere_pozitive.append(numar)
#         if numar % 2 == 0:
#          numere_pare.append(numar)
#         else:
#           numere_impare.append(numar)
#     else:
#         numere_negative.append(numar)
# print(f'Numerele Pozitive sunt: {numere_pozitive}')
# print(f'Numerele negative sunt: {numere_negative}')
# print(f'Numerele pare sunt {numere_pare}')
# print(f'Numerele impare sunt {numere_impare}')
#
#
# ##### Rezolvat
#
#
# #
# # 12.
# # Aceeasi lista
# # Ordonati crescator lista fara sa folositi sort
# # Va puteti inspira vizual de aici
# # https://www.youtube.com/watch?v=lyZQPjUT5B4


# #
# # 13.
# # Ghicitoare de numar
# # numar_secret = Generati un numar random intre 1 si 30
# # Numar_ghicit = None
# # Folosind un while
# #    User alege un numar
# #    Programul ii spune:
# # -	Nr secret e mai mare
# # -	Nr secret e mai mic
# # -	Felicitari! Ai ghicit!
# #
import random
nr_secret = int(random.randint(1,30))
numar_ghicit = int(input("Alege numarul"))
while numar_ghicit != nr_secret:
    if numar_ghicit > nr_secret:
        print('Numarul secret este mai mic')
        numar_ghicit = int(input('Alege un nr.'))
    if numar_ghicit < nr_secret:
        print('Numarul secret este mai mare')
        numar_ghicit = int(input('Alege un nr.'))
print("Felicitari")
#
# #####Rezolvat
#
#
# # 14.
# # Alegeti un numar de la tastatura
# # Ex:7
# # Scrieti un program care sa genereze in consola urmatoarea piramida
# # 1
# # 22
# # 333
# # 4444
# # 55555
# # 666666
# # 7777777
# #
# # Ex:3
# # 1
# # 22
# # 333
# #
# #
# # 15.
# # tastatura_telefon = [
# #   [1, 2, 3],
# #   [4, 5, 6],
# #   [7, 8, 9],
# #   [0]
# # ]
# # Iterati prin lista 2d
# # Printati ‘Cifra curenta este x’
# # (hint: nested for - adica for in for)
