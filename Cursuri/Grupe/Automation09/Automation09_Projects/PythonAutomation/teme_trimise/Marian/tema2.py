#1.Explica cu cuvintele tale in cadrul unui comentari cum functioneaza un if else
#if conditioneaza rezultatul si daca este adevarat printeaza ceva iar in caz ca nu este adevarat "else" face altceva

#2.Verifica si afiseaza daca x este numar pozitiv sau nu
# x = float(input())
# if x > 0:
#     print("numarul este pozitiv")
# else:
#     print('numarul este negativ')

# rezolvat

#3.Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru
# x = float(input('alege un nr.'))
# if x > 0:
#     print("numarul este pozitiv")
# elif x == 0 or x * 5 == 5:
#         print('numarul este neutru')
# else:
#     print('numarul este negativ')

#rezolvat

# 4. Verifica si afiseaza daca x este intre -2 si 13
# x = float(input('afiseaza un numar'))
# if x > -2 and x < 13:
#     print('se incadreaza intre valorile date')
# else:
#     print('numarul nu se incadreza intre valorile date')

#rezolvat

# 5. Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5
# x = float(input('scrie primul numar'))
# y = float(input('scrie al doilea numar'))
# if (x-y) < 5:
#     print ('este mai mica')
# else:
#     print('diferenta este mai mare')

#rezolvat

# 6. Verifica daca x NU este intre 5 si 27. (a se folosi ‘not’)
# x = float(input('scrie un numar '))
# if  not x>=27 and x>5:
#     print(' este intre cele doua valori')
# else:
#     print('Numarul nu este intre cele doua valori')

#rexolvat

# 7.x si y (int)
# Verifica si afiseaza daca sunt egale, daca nu afiseaza care din ele este mai mare
# x = int(input('valoarea lui x'))
# y = int(input('valoarea lui y'))
# if x == y:
#     print('numerele sunt egale')
# elif x>y:
#     print('x este mai mare')
# else:
#     print('y este mai mare')

# rezolvat

# 8. X, y, z - laturile unui triunghi
# Afiseaza daca triunghiul este isoscel, echilateral sau oarecare

# x = float(input('latura 1:'))
# y = float(input('latura 2:'))
# z = float(input('latura 3:'))
# if (x == y and x != z) or (x == z and x!=y) or (y == z and y!=x):
#     print('triunghiul este isoscel')
# elif x == y == z:
#     print('triungiul este echilateral')
# else:
#     print('triunghiul este oarecare')

# rezolvat

# 9. Citeste o litera de la tastatura
# Verifica si afiseaza daca este vocala sau nu
# litera = input('introdu litera pe care vrei sa o verifici:').lower()
# if litera == 'a' or litera == 'e' or litera == 'i' or litera == 'o' or litera == 'u' or litera == 'ă' or litera == 'î':
#     print(f'litera "{litera}" este o vocala!')
# else:
#     print(f'litera "{litera}" este o consoana!')

#rezolvat
#
# 10.Transforma si printeaza notele din sistem românesc in sistem american dupa cum urmeaza
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F
# nota =float(input('introduce nota in sistem Romanesc'))
# if nota <=4:
#     print(f'nota {nota} in sistem American este F')
# elif nota > 4 and nota <= 6:
#      print(f'Nota {nota} in sistem American este E')
# elif nota > 6 and nota <= 7:
#      print(f'Nota {nota} in sistem American este D')
# elif nota > 7 and nota <=8:
#     print(f'Nota {nota} in sistem American este C')
# elif nota > 8 and nota <=9:
#     print(f'Nota {nota} in sistem American este B')
# else: print(f'Nota {nota} in sistem American este A')

# rezolvat

#optionale

# 11.Verifica daca x are minim 4 cifre
# (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
#varianta 1 de rezolvare
#x = input('alege un nr:')
# assert len(x) >= 4
# print('True')

# varianta 2 de rezolvare
# if  len(x) >= 4:
#     print('True')
# else:
#     print('False')

#varianta 3
# if not len(x) < 4:
#     print('True')
# else:
#     print('False')


#12.Verifica daca x are exact 6 cifre
#x = input('alege un numar')
# assert len(x) == 6
# print('True')


#varianta 2 de reolvare
# if len(x) ==6:
#     print('numarul are 6 caractere')
# else:
#     print(f'numarul are {len(x)} caractrere in loc de 6 caractere')

#Varianta 3
#if not len(x) == 6:
#     print('True')
# else:
#     print('False')

#rezolvat

#13.Verifica daca x este numar par sau impar
# x = int(input('verifica un numar:'))
# if x % 2 == 0:
#     print(f'numarul {x} este par')
# else:
#     print(f'numarul {x} este impar')

#rezolvat

# #14. x, y, z (int).  Afiseaza care este cel mai mare dintre ele?
# x =int(input('primul numar'))
# y = int(input('al doilea numar'))
# z = int(input('al treilea numar'))
# if  x>y and x>z or y!=z and x>y and y==z or x>z and x ==y or x>y and x ==z:
#     print(f'{x} este cel mai mare numar')
# elif y>x and y>z and x!=z or y>x and y>z and z ==x or y>x and y ==z:
#     print(f'{y} este cel mai mare numar')
# elif z>x and z>y and x!=z or z>x and z>y and x ==z or z ==y and y>x:
#     print(f'{z} este cel mai mare numar')

#rezolvat

# 15. X, y, z - reprezinta unghiurile unui triunghi
# Verifica si afiseaza daca triunghiul este valid sau nu
# x = float(input('angle 1'))
# y = float(input('angle 2'))
# z = float(input('angle 3'))
# if (x+y+z ==180) and x!=0 and y!=0 and z!=0:
#     print('Triangle is valid')
# else: print('Triangle is invalid')
# rezolvat

# 16. Pentru exercitiile cu biletele de avion incercati sa aplicati tehnicile de
# equivalence partitioning si boundary value analysis astfel incat sa eficientizati testarea.
# Sa tineti cont de urmatoarea chestie: tehnicile de testare vor fi aplicate nu pe faptul ca o
# persoana are pasaport sau nu ci pe varsta persoanei


# pasaport = input('Are pasaportul valid : DA/NU ')
# ambii_parinti = input('Are ambii parinti? DA/NU ')
# permisiune = input('Are permisiune? DA/NU/NA ')
# age = 18
# if  pasaport == "DA":
#      if age >=18:
#          print('permite calatoria')
#      elif ambii_parinti == 'DA' or permisiune == 'DA':
#         print('Permite calatoria')
#      else:
#          print('nu permite calatoria')
# else :
#     print('Nu permite calatoria')

#varianta 2

# pasaport = input('Are pasaport valid: DA/NU')
# varsta = int(input('introdu varsta'))
# if  pasaport == 'DA'and varsta >=18:
#     print('Calatorie placuta')
# elif pasaport == 'NU':
#     print('nu se permite Calatoria')
# else:
#     ambii_parinti = input('Are ambii parinti? DA/NU ')
#     permisiune = input('Are permisiune? DA/NU/NA ')
#     if  pasaport == 'DA' and varsta < 18 and (ambii_parinti =='DA' or permisiune =='DA'):
#         print('CALATORIE PLACUTA')
#     elif ambii_parinti == 'NU' and permisiune == 'NU':
#         print('Nu se permite calatoria')