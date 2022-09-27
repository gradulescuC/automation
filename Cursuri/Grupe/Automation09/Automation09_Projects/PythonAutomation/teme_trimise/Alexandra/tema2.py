# # 1. Explica cu cuvintele tale in cadrul unui comentari cum functioneaza un if else
# #
# # Un if else conditioneaza un bloc de cod in functie de ce criterii avem nevoie. ( definitie pe moment)
# #
# # 2. Verifica si afiseaza daca x este numar natural sau nu
#
# x = 9
# if ( x > 0):
#     print('numarul este natural')
# else:
#     print('numarul nu este natural')
#
# # 3.Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru
# x = 9
# if ( x > 0 ):
#     print('pozitiv')
# else:
#     print('nr nu este pozitiv')
#     print('nr este neutru')
#
# # 4.Verifica si afiseaza daca x este intre -2 si 13
# x = 9
# if ( x < -2 or x > 13):
#      print('nr se incadreaza')
# else:
#      print('nr nu se incadreaza')

# 5. Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5

# x = 9
# y = 4
# if(x - y < 5):
#      print('Diferenta este mai mica')
# else:
#      print('Diferenta este mai mare')

# # 6. Verifica daca x NU este intre 5 si 27. (a se folosi ‘not’)

# x = 25
# if not x >= 5 or x <= 27:
#     print(f'{x} este cuprins intre 5 si 27')
# else:
#     print(f'{x} nu este cuprins intre 5 si 27')

#
# Run: 30 nu este cuprins intre 5 si 27
#
# x = 12
#
#
# if not x >= 5 or x <= 27:
#     print(f'{x} este cuprins intre 5 si 27')
# else:
#     print(f'{x} nu este cuprins intre 5 si 27')
#
# Run: 12 este cuprins intre 5 si 27
#
#
#
#
# 7. x si y (int) Verifica si afiseaza daca sunt egale,daca nu afiseaza care din ele este mai mare
#
x = 10
y = 2

print( x == y) # x si y nu sunt egale

if x == y:
     print('X si Y sunt egale')
elif x != y:
     print('X si Y sunt diferite')

if x < y:
     print('X este mai mic decat Y')
elif x > y:
     print('X este mai are decat Y')
#
# 8.X, y, z - laturile unui triunghi Afiseaza daca triunghiul este isoscel, echilateral sau oarecare.
#
# x = 15
# y = 17
# z = 15
#
# if x == y == z:
#     print('Triunghi echilateral')
# elif x==y or y==z or x==z:
#     print('Triunghi isoscel')
# else:
#     print ('Triunghi oarecare')
#
#
#9. Citeste o litera de la tastatura. Verifica si afiseaza daca este vocala sau nu


# x = input('Introdu o litera:')
# if(x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' or x == 'A'
#        or x == 'E' or x == 'I' or x == 'O' or x == 'U'):
#     print('Litera', x, 'este vocala')
# else:
#     print('Litera', x , 'este o consoana')
# #


#
# 10. Transforma si printeaza notele din sistem romanesc in sistem american dupa cum urmeaza
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F
#
#  nota_a = '9'
# nota_b = '8'
# nota_c = '7'
# nota_d = '6'
# nota_e = '4'
# nota_f = '3'
#
#
# #supracriem variabilele
#
# nota_a = 'A'
# nota_b = 'B'
# nota_c = 'C'
# nota_d = 'D'
# nota_e = 'E'
# nota_f = 'F'
#
# print(f'Notele americane sunt: {nota_a} {nota_b} {nota_c} {nota_d} {nota_e} {nota_f}')
#
#
# # 11. Verifica daca x are minim 4 cifre (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
#
# x = 15634
# numarul_meu = len(str(x))
# print((numarul_meu))
#
# if x < 4:
#     print('Numarul are mai putin de 4 cifre')
# elif x > 4:
#     print('Numarul are mai mult de 4 cifre')
#
#
# 12.Verifica daca x are exact 6 cifre
#
# x = 15634
# numarul_meu = len(str(x))
# print(numarul_meu)
# if x >= 6:
#     print('Numarul meu are mai putin de 6 cifre')
# elif x <= 6:
#     print('Numarul meu are 6 cifre')
#
#
# 13.Verifica daca x este numar par sau impar
#
# x = 5
# if x % 2 == 0 :
#     print('numarul este par')
# elif x % 2 != 0:
#     print('numarul este impar')
#
#
# 14. x, y, z (int) Afiseaza care este cel mai mare dintre ele?
#
# x = 12
# y = 23
# z = 15
#
# print(max(x,y,z))
#
#
# 15.X, y, z - reprezinta unghiurile unui triunghi Verifica si afiseaza daca triunghiul este valid sau nu
#
#
# x = 5
# y = 3
# z = 4
#
# if x + y + z == 12:
#     print('Triunghiul este valid')
# else:
#     print('Triunghiul nu este valid')
#
#
