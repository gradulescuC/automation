# # 1. Explica cu cuvintele tale in cadrul unui comentari cum functioneaza un if else
# # In cadrul unui if else, se testeaza o prima conditie in partea de if, daca aceasta este indeplinita se poate afisa
# # ceva, iar daca nu e indeplinita acea conditie se trece la partea de else unde de asemenea se poate pune un print
# # pentru a afiseaza daca nu e indeplinita conditia de la if
#
# # 2. Verifica si afiseaza daca x este numar pozitiv sau nu
# x = int(input('Dati un numar x : '))
# if x >= 0 :
#     print(f'{x} este numar pozitiv')
# else :
#     print(f'{x} nu este numar pozitiv')
#
# # 3. Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru
#
# if x > 0 :
#     print(f'{x} este numar pozitiv')
# elif x < 0 :
#     print(f'{x} este numar negativ')
# else :
#     print(f'{x} este numar neutru')
#
# # 4. Verifica si afiseaza daca x este intre -2 si 13
#
# if x > -2 and x < 13 :
#     print(f'{x} este intre -2 si 13')
# else :
#     print(f'{x} nu este intre -2 si 13')
#
# # 5. Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5
# y = int(input('Dati un numar y : '))
# dif = x - y
# print(f'Diferenta dintre {x} si {y} este {dif}')
# if dif < 5 :
#     print(f'Diferenta dintre {x} si {y} este < 5')
# else :
#     print(f'Diferenta dintre {x} si {y} nu este < 5')
#
# # 6. Verifica daca x NU este intre 5 si 27. (a se folosi ‘not’)
# if not(x > 5 and x < 27) :
#     print(f'{x} nu este intre 5 si 27')
# else :
#     print(f'{x} este intre 5 si 27')
#
# # 7. x si y (int)
# # Verifica si afiseaza daca sunt egale, daca nu afiseaza care din ele este mai mare
#
# if x == y :
#     print(f'cele doua numere sunt egale')
# elif x > y :
#     print(f'{x} este mai mare decat {y}')
# else :
#     print(f'{y} este mai mare decat {x}')
#
# # 8. x, y, z - laturile unui triunghi
# # Afiseaza daca triunghiul este isoscel, echilateral sau oarecare
# x = int(input('Dati un numar x : '))
# y = int(input('Dati un numar y : '))
# z = int(input('Dati un numar z : '))
# if x == y or y == z or x == z :
#     print('Triunghiul este isoscel')
# elif x ==y and y == z :
#     print ('Triunghiul este isoscel')
# else :
#     print('Triunghiul este oarecare')
#
# # 9. Citeste o litera de la tastatura
# # Verifica si afiseaza daca este vocala sau nu
# l = input('Scrie o litera : ')
# if l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u' :
#     print(f'Litera {l} este o vocala')
# else :
#     print(f'Litera {l} nu este o vocala')
#
# # 10. Transforma si printeaza notele din sistem românesc in sistem american dupa cum urmeaza
# # Peste 9 => A
# # Peste 8 => B
# # Peste 7 => C
# # Peste 6 => D
# # Peste 4 => E
# # 4 sau sub => F
# nota = int(input('Nota este (pana la 10): '))
# if nota > 9 and nota <=10 :
#     print(f'Nota {nota} in stil american este A')
# elif nota > 8 and nota <= 9 :
#     print(f'Nota {nota} in stil american este B')
# elif nota > 7 and nota <= 8 :
#     print(f'Nota {nota} in stil american este C')
# elif nota > 6 and nota <= 7 :
#     print(f'Nota {nota} in stil american este D')
# elif nota > 4 and nota <= 6 :
#     print(f'Nota {nota} in stil american este E')
# elif nota <= 4 and nota > 0 :
#     print(f'Nota {nota} in stil american este F')
# else :
#     print(f'Nota {nota} nu este o nota valida')
#
# 11. Verifica daca x are minim 4 cifre
# (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
x = input('Scrieti un numar ')
nr_cifre = len(x)
if nr_cifre >=4 :
    print(f'Numarul {x} are minim 4 cifre')
else :
    print(f'Numarul {x} nu are minim 4 cifre')
#
# # 12. Verifica daca x are exact 6 cifre
# if nr_cifre == 6 :
#     print(f'Numarul {x} are exact 6 cifre')
# else :
#     print(f'Numarul {x} nu are exact 6 cifre')
#
# # 13. Verifica daca x este numar par sau impar
# x = int(input('Scrieti un numar '))
# if x % 2 == 0 :
#     print(f'Numarul {x} este numar par')
# else :
#     print(f'Numarul {x} este numar impar')
#
# # 14. x, y, z (int)
# # Afiseaza care este cel mai mare dintre ele?
#
# x = int(input('x = '))
# y = int(input('y = '))
# z = int(input('z = '))
# if x > y and x > z :
#     print(f'x = {x} este numarul cel mai mare')
# elif y > x and y > z :
#     print(f'y = {y} este numarul cel mai mare')
# elif z > x and z > y :
#     print(f'z = {z} este numarul cel mai mare')
# elif x == y and x > z :
#     print(f'x = {x} si y = {y} sunt egale si mai mari ca z = {z}')
# elif x == z and x > y :
#     print(f'x = {x} si z = {z} sunt egale si mai mari ca y = {y}')
# elif y == z and y > x :
#     print(f'y = {y} si z = {z} sunt egale si mai mari ca x = {x}')
# else :
#     print(f'x = {x}, y = {y}, z = {z} sunt egale')
#
# 15. x, y, z - reprezinta unghiurile unui triunghi
# Verifica si afiseaza daca triunghiul este valid sau nu
# x = int(input('Scrieti primul unghi : '))
# y = int(input('Scrieti al doilea unghi : '))
# z = int(input('Scrieti al treilea unghi : '))
# suma = x + y + z # suma celor 3 unghiuri
# if x < 180 and x > 0 and y < 180 and y > 0 and z < 180 and z > 0 and suma == 180 :
#     print('Triunghiul este valid')
# else :
#     print('Triunghiul nu este valid')