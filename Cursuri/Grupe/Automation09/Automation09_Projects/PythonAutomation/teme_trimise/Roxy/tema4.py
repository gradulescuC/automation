# 1. Avand lista
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# Folositi un for ca sa iterati prin toata lista si sa afisati
# ‘Masina mea preferata este x’
# Faceti acelasi lucru cu un for each
# Faceti acelasi lucru cu un while

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for masina in masini :
#     print(f'Masina mea preferata este {masina}')

# 2. Aceeasi lista. Folositi un for else :
# In for - Modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimul
# In else - Printati lista
#
# nr = len(masini)
# print(f'Avem {nr} masini')
# for i in range(1, nr-1) :
#     masini[i] = masini[i].upper()
# #print(f'Elementele scrie cu majuscule inafara de primul si ultimul sunt : {masini}')
# else :
#     print(f'Noua lista este {masini}')
#
# # 3. Aceeasi lista. Vine un cumparator care doreste sa cumpere un Mercedes
# # Iterati prin ea prin modalitatea aleasa de voi
# # Daca masina e mercedes : Printam ‘am gasit masina dorita de dvs’, Iesim din ciclu folosind un cuvant cheie care face acest lucru
# # Altfel Printam Am gasit masina X. Mai cautam
#
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for masina in masini :
#     if masina == 'Mercedes' :
#         print(f'Am gasit masina dorita de dvs. {masina}')
#         break
#     else :
#         print(f'Am gasit masina {masina}. Mai cautam')
#
# # 4. Aceasi lista. Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun.
# # Daca masina e Trabant sau Lastun. Folositi un cuvant cheie care sa dea skip la ce urmeaza (nu trebuie else)
# # Printati S-ar putea sa va placa masina x
#
# for masina in masini :
#     if masina != 'Trabant' and masina != 'Lastun':
#         print(f'S-ar putea sa va placa masina {masina}')
#         continue
#
# # 5. Modernizati parcul de masini. Creati o lista goala, masini_vechi. Iterati prin masini
# # Cand gasiti Lastun sau Trabant:
# #     Salvati aceste masini in masini_vechi
# #     Suprascrieti-le cu ‘Tesla’ (in lista initiala de masini)
# #     Printati Modele vechi: x
# #     Modele noi: x
# #
# masini_vechi = []
# for i in range(len(masini)) :
#     if masini[i] == 'Trabant' or masini[i] == 'Lastun' :
#         masini_vechi.insert(0, 'Trabant')
#         masini_vechi.insert(0, 'Lastun')
#         masini[i] = 'Tesla'
#         break
# print(f'Modele vechi : {masini_vechi}')
# print(f'Modele noi : {masini}')
#
# # 6. Avand dict
# # pret_masini = {
# #     'Dacia': 6800,
# #     'Lastun': 500,
# #     'Opel': 1100,
# #     'Audi': 19000,
# #     'BMW': 23000
# # }
# # Vine un client cu un buget de 15000 euro.
# # Prezentati doar masinile care se incadreaza in acest buget
# # Iterati prin dict.items() si accesati masina si pretul
# # Printati Pentru un buget de sub 15000 euro puteti alege masina xLastun. Iterati prin lista
#
#
# pret_masini = {
#     'Dacia': 6800,
#     'Lastun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
# for masina, pret in pret_masini.items():
#    if pret < 15000 :
#        print(f'Pentru un buget de sub 15000 euro puteti alege masina {masina}')

# # 7. Avand lista numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# # Iterati prin ea. Afisati de cate ori apare 3. (nu aveti voie sa folositi count)
#
x = 0
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for i in numere :
    if i == 3 :
        x = x + 1
print(f'Cifra 3 apare de {x} ori')
#
# # 8. Aceeasi lista. Iterati prin ea. Calculati si afisati suma numerelor (nu aveti voie sa folositi sum)
#
# suma = 0
# for i in numere :
#     suma = suma + i
# print(f'Suma numerelor este {suma}')
#
# # 9. Aceeasi lista. Iterati prin ea. Afisati cel mai mare numar (nu aveti voie sa folositi max)
#
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# max_nbr = 0
# for maxim in numere :
#     if maxim > max_nbr :
#         max_nbr = maxim
# print(f'Valoarea maxima este {max_nbr}')
#
# # 10.Aceeasi lista. Iterati prin ea. Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
# # Ex: daca e 3, sa devina -3
# # Afisati noua lista
#
# for i in numere :
#     numere = -abs(i)
#     print(f'Numarul pozitiv transformat in negativ este : {numere}')


# print('----------OPTIONALE-----------')
# # 11.alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# # numere_pare = []
# # numere_impare = []
# # numere_pozitive = []
# # numere_negative = []
# # Iterati prin lista alte_numere. Populati corect celelalte liste. Afisati cele 4 liste la final
#
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
#
# for nr in alte_numere :
#     if nr % 2 == 0 and nr > 0 :
#         numere_pare.append(nr)
#         numere_pozitive.append(nr)
#     elif nr % 2 ==0 and nr < 0:
#         numere_pare.append(nr)
#         numere_negative.append(nr)
#     elif nr % 2 == 1 and nr > 0 :
#         numere_impare.append(nr)
#         numere_pozitive.append(nr)
#     elif nr % 2 == 1 and nr < 0 :
#         numere_impare.append(nr)
#         numere_negative.append(nr)
# print(f'Lista cu numere pare este {numere_pare}')
# print(f'Lista cu numere impare este {numere_impare}')
# print(f'Lista cu numere pozitive este {numere_pozitive}')
# print(f'Lista cu numere negative este {numere_negative}')
#
# # 12. Aceeasi lista. Ordonati crescator lista fara sa folositi sort
# # Va puteti inspira vizual de aici : https://www.youtube.com/watch?v=lyZQPjUT5B4
#
# print(f'Lista originala este {alte_numere}')
# for i in range(len(alte_numere)) :
#     for j in range(len(alte_numere) - 1 ) : # m-am ajutat de internet, dar nu prea inteleg de ce s-a mai facut si partea asta
#         if alte_numere[j] > alte_numere[j+1] :
#             alte_numere[j], alte_numere[j+1] = alte_numere[j+1], alte_numere[j]
# print(f'Lista ordonata este {alte_numere}')
#
# # 13. Ghicitoare de numar
# # numar_secret = Generati un numar random intre 1 si 30
# # Numar_ghicit = None
# # Folosind un while
# #    User alege un numar
# #    Programul ii spune:
# # Nr secret e mai mare
# # Nr secret e mai mic
# # Felicitari! Ai ghicit!
#
# numar_secret = int(input('Generati un numar random intre 1 si 30 : '))
# numar_ghicit = None
# while numar_secret >=0 and numar_secret <= 30 :
#     numar_ghicit = int(input('Alege un numar : '))
#     if numar_secret > numar_ghicit :
#         print('Numarul secret este mai mare')
#     elif numar_secret < numar_ghicit :
#         print('Numarul secret e mai mic')
#     else :
#         print('Felicitari! Ai ghicit')
#     break
#
# # 14. Alegeti un numar de la tastatura. Ex:7
# # Scrieti un program care sa genereze in consola urmatoarea piramida
# # 1
# # 22
# # 333
# # 4444
# # 55555
# # 666666
# # 7777777
# # Ex:3
# # 1
# # 22
# # 333
#
# numar = int(input('Alegeti un numar : '))
# for i in range(1, numar+1) :
#     print(f'{i}' * i)

# # 15.tastatura_telefon = [
# #                           [1, 2, 3],
# #                           [4, 5, 6],
# #                           [7, 8, 9],
# #                           [0]
# #                          ]
# # Iterati prin lista 2d
# # Printati ‘Cifra curenta este x’
# # (hint: nested for - adica for in for)
tastatura_telefon = [
                        [1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9],
                        [0]
                    ]
for i in range(len(tastatura_telefon)) :
    for j in range(len(tastatura_telefon[i])) :
        print(f'Cifra curenta este : {tastatura_telefon[i][j]}')