# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
#
# Folositi un for ca sa iterati prin toata lista si sa afisati
# 'Masina mea preferata este x'
# Faceti acelasi lucru cu un for each
# Faceti acelasi lucru cu un while

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

# For este un tip de iteratie care se foloseste pentru a trece secvential prin lista si a identifica elementele pe baza de index

# For each este un tip de iteratie care se foloseste pentru a trece secvental prin lista si a identifica elementele pe baza de continut

# For each este util atunci cand vrem sa parcurgem toata lista si sa afisam ceva din ea.
# Daca vrem sa aducem modificari listei atunci cel mai recomandat ar fi for

print("---------FOR---------------")
#
# for i in range(0,len(masini)):
#     print(f"Masina mea preferata este {masini[i]}")

"""
Modalitatea de executie a instructiunii de mai sus:
len(masini)=8
i = 0 -> 0 < 9? DA -> Masina mea preferata este masini[0] ->   Masina mea preferata este Audi -> 
i = 1 -> 1 < 9? DA -> Masina mea preferata este masini[1] ->   Masina mea preferata este Volvo -> 
i = 2 -> 2 < 9? DA -> Masina mea preferata este masini[2] ->   Masina mea preferata este BMW -> 
i = 3 -> 3 < 9? DA -> Masina mea preferata este masini[3] ->   Masina mea preferata este Mercedes -> 
i = 4 -> 4 < 9? DA -> Masina mea preferata este masini[4] ->   Masina mea preferata este Aston Martin -> 
i = 5 -> 5 < 9? DA -> Masina mea preferata este masini[5] ->   Masina mea preferata este Lastun -> 
i = 6 -> 6 < 9? DA -> Masina mea preferata este masini[6] ->   Masina mea preferata este Fiat -> 
i = 7 -> 7 < 9? DA -> Masina mea preferata este masini[7] ->   Masina mea preferata este Trabant -> 
i = 8 -> 8 < 9? DA -> Masina mea preferata este masini[9] ->   Masina mea preferata este Opel -> 
"""

print("---------FOR-EACH---------------")

# for masina in masini:
#     print(f"Masina mea preferata este {masina}")

"""Modalitatea de executie a instructiunii de mai sus:
len(masini)=8
IT1: masina = Audi -> Masina mea preferata este Audi 
IT2: masina = Volvo ->   Masina mea preferata este Volvo 
IT3: masina = BMW ->  Masina mea preferata este BMW 
IT4: masina = Merecdes ->   Masina mea preferata este Mercedes 
IT5: masina = Aston Martin  Masina mea preferata este Aston Martin
IT6: masina = Lastun   Masina mea preferata este Lastun 
IT7: masina = Fiat ->  Masina mea preferata este Fiat 
IT8: masina - Trabant ->   Masina mea preferata este Trabant 
IT9: masina = Opel  ->   Masina mea preferata este Opel 
"""

print("---------WHILE---------------")
#
# index_masina = 5
# while index_masina<len(masini):
#     print(f"Masina mea preferata este {masini[index_masina]}")
#     index_masina += 1

"""    
Modalitatea de executie a instructiunii de mai sus:
len(masini)=8
index_masina = 0 -> 0 < 9? DA -> Masina mea preferata este masini[0] ->   Masina mea preferata este Audi -> 
index_masina = 1 -> 1 < 9? DA -> Masina mea preferata este masini[1] ->   Masina mea preferata este Volvo -> 
index_masina = 2 -> 2 < 9? DA -> Masina mea preferata este masini[2] ->   Masina mea preferata este BMW -> 
index_masina = 3 -> 3 < 9? DA -> Masina mea preferata este masini[3] ->   Masina mea preferata este Mercedes -> 
index_masina = 4 -> 4 < 9? DA -> Masina mea preferata este masini[4] ->   Masina mea preferata este Aston Martin -> 
index_masina = 5 -> 5 < 9? DA -> Masina mea preferata este masini[5] ->   Masina mea preferata este Lastun -> 
index_masina = 6 -> 6 < 9? DA -> Masina mea preferata este masini[6] ->   Masina mea preferata este Fiat -> 
index_masina = 7 -> 7 < 9? DA -> Masina mea preferata este masini[7] ->   Masina mea preferata este Trabant -> 
index_masina = 8 -> 8 < 9? DA -> Masina mea preferata este masini[9] ->   Masina mea preferata este Opel -> 
"""



"""Aceeasi lista
Folositi un for else
In for
   Modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimul In else 
   Printati lista
"""
#
# for i in range(len(masini)):
#     if i==0 or i==len(masini)-1:
#         print(masini[i])
#     else:
#         print(masini[i].upper())
#
# print("---------")
# for i in range(len(masini)):
#     if not(i==0 or i==len(masini)-1):
#         print(masini[i].upper())
#     else:
#         print(masini[i])

"""
Aceeasi lista, 
Vine un cumparator care doreste sa cumpere un Mercedes
Iterati prin ea prin modalitatea aleasa de voi
Daca masina e mercedes 
   Printam 'am gasit masina dorita de dvs'
   Iesim din ciclu folosind un cuvant cheie care face acest lucru
Altfel
   Printam Am gasit masina X. Mai cautam	
"""

# for masina in masini:
#     if masina=='Mercedes':
#         print(f"Am gasit masina dorita de dumneavoastra, {masina}")
#         break
#     else:
#         print(f"Am gasit masina {masina}, mai cautam")

""""
Aceasi lista
Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun. 
Daca masina e Trabant sau Lastun
   Folositi un cuvant cheie care sa dea skip la ce urmeaza
(nu trebuie else)
Printati S-ar putea sa va placa masina x

"""

# for masina in masini:
#     if masina=='Trabant' or masina == 'Lastun':
#         continue
#     print(f"S-ar putea sa va placa masina {masina}")

"""
Modernizati parcul de masini
Creati o lista goala, masini_vechi
Iterati prin masini
Cand gasiti Lastun sau Trabant:
Salvati aceste masini in masini_vechi
Suprascrieti-le cu 'Tesla' (in lista initiala de masini)
Printati Modele vechi: x
Modele noi: x
"""
# masini_vechi=[]
# for i in range(len(masini)):
#     if masini[i]=='Trabant' or masini[i]=='Lastun':
#         masini_vechi.append(masini[i])
#         masini[i]='Tesla'

# masini_vechi=[]
# for i in range(len(masini)):
#     if  masini[i]=='Trabant' or masini[i]=='Lastun':
#         masini_vechi.append(masini[i])
#         print(masini)
# masini.append("Tesla")
#
# print(masini_vechi)
# print(masini)

"""
Avand dict
pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
Vine un client cu un buget de 15000 euro
Prezentati doar masinile care se incadreaza in acest buget
Iterati prin dict.items() si accesati masina si pretul
Printati Pentru un buget de sub 15000 euro puteti alege masina xLastun
Iterati prin lista

"""

# pret_masini = {
#     'Dacia': 6800,
#     'Lastun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
#
# print(pret_masini.items())
# print(pret_masini.keys())
# print(pret_masini.values())
#
# for masina,pret in pret_masini.items():
#     if pret<=15000:
#         print(f"Pentru un buget de sub 15000 euro puteti alege masina {masina} la pretul de {pret}")
#
# for masina in pret_masini.keys():
#     if pret_masini[masina]<=15000:
#         print(f"Pentru masina {masina} aveti pretul {pret_masini[masina]}")

"""

Avand lista
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
Iterati prin ea
Afisati de cate ori apare 3
(nu aveti voie sa folositi count)


"""
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# nrAparitii = 0
# for nr in numere:
#     if nr == 3:
#         nrAparitii += 1
#         print(f"Numarul 3 apare de {nrAparitii} ori")

"""

Aceeasi lista
Iterati prin ea
Calculati si afisati suma numerelor
(nu aveti voie sa folositi sum)

"""

numere = [5, 7, 8, 9, 3, 3, 1, 0, -4, 3,87]
# Total = 0
# for nr in numere:
#     Total += nr
#
# print(f"Suma totala a numerelor este {Total} ")


"""
Aceeasi lista
Iterati prin ea
Afisati cel mai mare numar
(nu aveti voie sa folositi max)

"""
# max = 0
# pozitie = 0
# while pozitie<len(numere):
#     if max<numere[pozitie]:
#         max = numere[pozitie]
#         pozitie+=1
#     print(f"Cel mai mare numar este {max} ")


"""
Aceeasi lista
Iterati prin ea
Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
Ex: daca e 3, sa devina -3
Afisati noua lista

"""

# for i in range(len(numere)):
#     if numere[i]>0:
#         numere[i] = -numere[i]
# print(numere)

# numere_v1 = []
# for numar in numere:
#     numere_v1.append(-numar)
#
# print(numere_v1)

# i = 0
# while i < len(numere):
#     if numere[i]>0:
#         numere[i]=-numere[i]
#     i+=1
# print(numere)


"""
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Iterati prin lista alte_numere 
Populati corect celelalte liste
Afisati cele 4 liste la final
"""
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []

# for i in range(len(alte_numere)):
#     if(alte_numere[i]%2==0):
#         numere_pare.append(alte_numere[i])
#         if(alte_numere[i])<0:
#             numere_negative.append(alte_numere[i])
#         else:
#             numere_pozitive.append(alte_numere[i])
#     else:
#         numere_impare.append(alte_numere[i])
#         if (alte_numere[i]) < 0:
#             numere_negative.append(alte_numere[i])
#         else:
#             numere_pozitive.append(alte_numere[i])

# for nr in alte_numere:
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

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]

# Algoritmul de sortare a unei liste prin metoda bulelor
# print(f'Lista originala este {alte_numere}')
# swap = 0
# for i in range(len(alte_numere)) :
#     for j in range(len(alte_numere) - 1 ) : # m-am ajutat de internet, dar nu prea inteleg de ce s-a mai facut si partea asta
#         if alte_numere[j] > alte_numere[j+1]:
#             # alte_numere[j], alte_numere[j+1] = alte_numere[j+1], alte_numere[j]
#             swap = alte_numere[j]
#             alte_numere[j]=alte_numere[j+1]
#             alte_numere[j+1] = swap
# print(f'Lista ordonata este {alte_numere}')


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

# a_n = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# j = 0
# swapped = False
#
# i = 0
# 0 < 9> DA
#     a_n[0]>a_n[1]
# a_n = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# i = i+1
#
# 1 < 9? DA
#     a_n[1] > a_n[2]
#     a_n[1] = 2
#     a_n[2] = 7
#     swapped = True
# a_n = [-5, 2, 7, 9, 12, 3, 1, -6, -4, 3]
#
# 2<9? DA
#     a_n[2] > a_n[3]
# a_n = [-5, 2, 7, 9, 12, 3, 1, -6, -4, 3]
#
# 3<9? DA
#     a_n[3] > a_n[4]
# a_n = [-5, 2, 7, 9, 12, 3, 1, -6, -4, 3]
#
# 4<9? DA
#     a_n[4] > a_n[5]
#     swapped = True
# a_n = [-5, 7, 2, 9, 3, 12, 1, -6, -4, 3]
#
# 5<9? DA
#     a_n[5] > a_n[6]
#     swapped = True
# a_n = [-5, 7, 2, 9, 3, 1, 12, -6, -4, 3]
#
# 6<9? DA
#     a_n[6] > a_n[7]
#     swapped = True
# a_n = [-5, 7, 2, 9, 3, 1, -6, 12, -4, 3]
#
# 7<9? DA
#     a_n[7] > a_n[8]
#     swapped = True
# a_n = [-5, 7, 2, 9, 3, 1, -6, -4, 12, 3]
#
# 8<9? DA
#     swapped = True
# a_n = [-5, 7, 2, 9, 3, 1, -6, -4, 3, 12]
#
# 9<9? NU

x = int(input("Introduceti dimensiunea copacului: "))
for i in range(1, x+1):
    print(f"{i}" * i)