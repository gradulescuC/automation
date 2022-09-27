#1 Explica cu cuvintele tale in cadrul unui comentari cum functioneaza un if else
'''

if si else sunt niste conditii date unui bloc de cod
daca prima conditie (if) este indeplinita, codul trece mai departe si sare peste else;
daca if nu este indeplinit se va executa codul dupa else.

'''

#2 Verifica si afiseaza daca x este numar pozitiv sau nu

# x = 4
# y = 1
# print(x>0)
#
# #3 Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru
#
# print(x > 0 and x < 0 and x==0)
#
# #4 Verifica si afiseaza daca x este intre -2 si 13
#
# print(x>=-2 or x<=13)

#5Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5

# print((x-y)<5)

#6Verifica daca x NU este intre 5 si 27. (a se folosi ‘not’)

# print(not(x >= 5 or x == 27))  #am returnat o valoare opusa pentru valoarea lui x

#7Verifica si afiseaza daca sunt egale, daca nu afiseaza care din ele este mai mare

# if x == y :
#     print('X este egal cu Y')
# if x < y :
#     print('X este mai mic decat Y')
# else: x > y
# print('X este mai mare decat y')

#8Afiseaza daca triunghiul este isoscel, echilateral sau oarecare.
# x = 3
# y = 5
# z = 4
#
# if x == z and y != z :
#     print('Triunghiul este isoscel')
# if x == z and x == y and x ==z :
#     print('Triunghiul este echilateral')
# if x != z and x != y and y != z :
#     print('Triunghiul este oarecare')

#9Citeste o litera de la tastatura; Verifica si afiseaza daca este vocala sau nu

# vocala = str(input('Introduceti o litera: '))
#
#
# if vocala.lower() == 'a' or vocala.lower() == 'i' or vocala.lower() == 'u' or vocala.lower() == 'e' or vocala.lower() == 'u' :
#     print('Este o vocala')
# else :
#     print('Nu este o vocala')


#10Transforma si printeaza notele din sistem românesc in sistem american dupa cum urmeaza

# grade = int(input('Introdu nota: '))
# if grade >= 9 :
#     print('A')
# if grade >= 8 and grade < 9 :
#     print('B')
# if grade >= 7 and grade < 8 :
#     print('C')
# if grade >= 6 and grade <7 :
#     print('D')
# if grade > 4 and grade == 5 and grade < 6 :
#     print('E')
# if grade <= 4 :
#     print('F')
# if grade > 10 or grade < 3 :
#     print('Invalid grade')

#11 Verifica daca x are minim 4 cifre

# n=int(input("Enter number:"))
# count=0
# while(n>0):
#     count=count+1
#     n=n//10
# if count < 4 :
#     print('The number has less than 4 digits')
# else :
#     print("The number of digits in the number are:",count)

#12 .Verifica daca x are exact 6 cifre

# x=int(input('Introdu un numar: '))
# count=0
# while(x>0):
#     count=count+1
#     x=x//10
# if count == 6 :
#     print('Numarul are 6 cifre')
# else :
#     print('Acest numar este invalid')

#13 Verifica daca x este numar par sau impar
# x=int(input("introduceti o valoare :"))
#
# if x %2 == 0:
#         print ('Numarul este par')
# else:
#     print ("Numarul este impar")

#14 Afiseaza care este cel mai mare dintre ele?
#
# x, y, z = input('Introduceti cele 3 numere').split( )
# x = int(x)
# y = int(y)
# z = int(z)
#
# if x > y and x > z :
#     print('Primul numar este cel mai mare')
# if y > x and y > z :
#     print('Al 2 lea numar este cel mai mare')
# if x == y and x == z :
#     print('Numerele sunt egale')
# if z > y and z > x :
#     print('Ultimul numar este cel mai mare')

#15 Verifica si afiseaza daca triunghiul este valid sau nu
# x, y, z = input('Introduceti cele 3 unghiuri separate de spatiu').split()
# x = int(x)
# y = int(y)
# z = int(z)
# if x + y + z == 180 : #suma unghiurilor unui triunghi
#     print('Triunghiul este valid')
# else :
#     print('Triunghiul nu este valid')

#16 Pentru exercitiile cu biletele de avion incercati sa aplicati tehnicile de equivalence partitioning si boundary value analysis astfel incat sa eficientizati testarea.


# varsta = int(input('Va rog introduceti varsta :  '))
# ambii_parinti = input('Are ambii parinti? DA/NU ')
# permisiune = input('Are permisiune? DA/NU/NA ' )
#
#
# if varsta >= 18 and (ambii_parinti == 'NU' or permisiune == 'NA') :
#         print('Permite calatoria')
#
# elif varsta <18 and ambii_parinti == 'DA' and permisiune == 'DA' :
#     print('Permite calatoria')
#
# else :
#     print('Nu permite calatoria')

