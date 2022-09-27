# 1.Explica cu cuvintele tale in cadrul unui comentari cum functioneaza un if else
# Instructiunea if else este o modalitate de a decide executia unei comenzi in functie de anumite conditii.

# 2.Verifica si afiseaza daca x este numar pozitiv sau nu
# x = int(input('Introdu un numar: '))
# if x > 0:
#     print('Numarul introdus este pozitiv')
# else:
#     print('Numarul introdus nu este pozitiv')

# 3.Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru
# x = int(input('Introdu un numar: '))
# if x > 0:
#     print('Numarul introdus este pozitiv')
# elif x < 0:
#     print('Numarul introdus este negativ')
# else:
#     print('Numarul este neutru')

# 4.Verifica si afiseaza daca x este intre -2 si 13
# x= int(input('Introdu un numar: '))
# if x > -2 and x < 13:
#     print('Numarul este intre -2 si 13')
# else:
#     print('In afara intervalului')

# 5.Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5
# x = int(input('x = '))
# y = int(input('y = '))
# diferenta = x - y
# if diferenta < 5:
#     print('Diferenta dintre cele 2 numere este mai mica decat 5')
# else:
#     print('Diferenta dintre cele doua numere este mai mare de 5')

# 6.Verifica daca x NU este intre 5 si 27. (a se folosi ‘not’)
# x = int(input('Introdu un numar: '))
# if not (x > 5 and x < 27):
#     print('x nu este in intervalul 5 - 27')
# else:
#     print('x este in intervalul 5 - 27')


# 7.
# x si y (int)
# Verifica si afiseaza daca sunt egale, daca nu afiseaza care din ele este mai mare
# x = int(input('x = '))
# y = int(input('y = '))
# if x == y:
#     print('Numerele sunt egale')
# elif x > y:
#     print('x este mai mare decat y')
# else:
#     print('x este mai mic decat y')

# 8.
# X, y, z - laturile unui triunghi
# Afiseaza daca triunghiul este isoscel, echilateral sau oarecare.
# x = int(input('Prima latura a triunghiului: '))
# y = int(input('A doua latura a triunghiului: '))
# z = int(input('A treia latura a triunghiului: '))
# if x != y and x != z and y != z:
#     print('Triunghiul este oarecare')
# elif x == y and x == z and y == z:
#     print('Triunghiul este echilateral')
# else:
#     print('Triunghiul este isoscel')

# 9.
# Citeste o litera de la tastatura
# Verifica si afiseaza daca este vocala sau nu
# x = input('Introdu o litera: ')
# if x == 'a' or x == 'o' or x == 'i' or x == 'e' or x == 'u':
#     print('Litera introdusa este vocala')
# else:
#     print('Litera introdusa este consoana')

# 10. Transforma si printeaza notele din sistem românesc in sistem american dupa cum urmeaza
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F
# x = int(input('Introdu nota: '))
# if x <= 4 and x >=1:
#     print('In sistemul american ai nota F')
# elif x > 4 and x <= 6:
#     print('In sistemul american ai nota E')
# elif x > 6 and x <= 7:
#     print('In sistemul american ai nota D')
# elif x > 7 and x <= 8:
#     print('In sistemul american ai nota C')
# elif x > 8 and x <= 9:
#     print('In sistemul american ai nota B')
# elif x <= 10:
#     print('In sistemul american ai nota A')
# else:
#     print('Nota nu exista')


# c. Optionale (may need google)

# 11.
# Verifica daca x are minim 4 cifre
# (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
# try:
#     x = int(input('Introdu niste cifre: '))
#     if len(str(x)) > 4:
#         print('Ai introdus minim 4 cifre')
#     else:
#         print('Nu ai introdus minim 4 cifre')
# except:
#     print('Nu ai introdus cifre')


# 12.
# Verifica daca x are exact 6 cifre
# try:
#     x = int(input('Introdu niste cifre: '))
#     if len(str(x)) == 6:
#         print('Ai introdus exact 6 cifre')
#     else:
#         print('Nu ai introdus exact 6 cifre')
# except:
#     print('Nu ai introdus cifre')

# 13.
# Verifica daca x este numar par sau impar
# try:
#     x = int(input('Introdu niste cifre: '))
#     if x % 2 == 0:
#         print('Numarul este par')
#     else:
#         print('Numarul este impar')
# except:
#     print('Nu ai introdus cifre')

# 14.
# x, y, z (int)
# Afiseaza care este cel mai mare dintre ele?
# try:
#     x = int(input('x = '))
#     y = int(input('y = '))
#     z = int(input('z = '))
#     if x > y and x > z:
#         print('x este cel mai mare')
#     elif y > z and y > z:
#         print('y este cel mai mare')
#     elif z > x and z > y:
#         print('z este cel mai mare')
#     else:
#         print('Nu se poate defini')
# except:
#     print('Eroare la introducerea datelor')

# 15.
# X, y, z - reprezinta unghiurile unui triunghi
# Verifica si afiseaza daca triunghiul este valid sau nu
# try:
#     x = int(input('Primul unghi al triunghiului: '))
#     y = int(input('A doilea unghi al triunghiului: '))
#     z = int(input('A treilea unghi al triunghiului: '))
#     suma = x + y + z
#     if suma == 180:
#         print('Valorile introduse iti dau un triunghi valid')
#         if x != y and x != z and y != z:
#             print('Triunghiul este oarecare')
#         elif x == y and x == z and y == z:
#             print('Triunghiul este echilateral')
#         else:
#             print('Triunghiul este isoscel')
#     else:
#         print(f'Suma unghiurilor este {suma}, asadar nu este un triunghi valid')
# except:
#     print('Eroare la introducerea datelor')