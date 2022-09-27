# #Explica cu cuvintele tale in cadrul unui comentari cum functioneaza un if else
# #evalueaza daca o expresie e adevarata sau falsa, daca e adevarata, se executa if, altfel else se executa.
# #Prin if else controlam fluxul codului.
#
# #2.Verifica si afiseaza daca x este numar pozitiv sau nu
# #numar pozitiv > 0; #numar negativ <0; numar neutru +- = 0 nu schimba valarea ; numar neutru */ = 1
#
# x = 2
# if x >= 0 :
#     print('X este un numar pozitiv')
#
# #3.Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru
#
# x = 2
# if x > 0  :
#     print( 'Cifra 2 este un numar pozitiv')
#     if x < 0 :
#         print('Cifra 2 este un numar negativ')
# else:
#         print('Cifra 2 este un numar neutru')
#
# #4. Verifica si afiseaza daca x este intre -2 si 13
#
# x = 2  # am verificat si cu cifra 14 pentru a vedea daca merge pe else
# if x > -2 and x <= 13 :
#     print('Cifra 2 este in sirul numeric -2 si 13')
# else:
#     print('Cifra 2 este nu este in sirul numeric -2 si 13')
#
# #5. Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5
# x = 4
# y = 2
# if (x-y <= 5):
#     print ('Rezultatul este 2')
# else:
#     print('Rezultatul este nul')

#6. Verifica daca x NU este intre 5 si 27. (a se folosi ‘not’)

x = 4  # am verificat si cu cifra 7 pentru a vedea daca merge pe else

if not x >=5 and x <= 27 :
    print('Cifra 4 nu este in intre 5 si 27')
else:
    pass
print('Cifra 4 este in intre 5 si 27')
#
# #7.x si y (int) Verifica si afiseaza daca sunt egale, daca nu afiseaza care din ele este mai mare
#
# x = 3
# y = 5
#
# if x == y:
#     print ('X si Y au valori egale')
# else:
#     print('X si Y nu au valori egale')
#     if y >= x :
#         print ( 'Y are valoare mai mare ca X')
#
# #8. X, y, z - laturile unui triunghi
# ##de revizuit
# #Afiseaza daca triunghiul este echilateral (laturi egale), isoscel (cele 2 latura congruente) sau oarecare.
#
# x = 4
# y = 4
# z = 4
#
# if x == y == z :
#     print ('Triunghiul este echilateral')
#
# elif x == y and (x , y) != z :
#         print ('Triunghiul este isoscel')
# else:
#     print ('Triunghiul este oarecare')
#
#
# #9. Citeste o litera de la tastatura, Verifica si afiseaza daca este vocala sau nu
#
# v = input('Introduceti o vocala ')
#
# if (v == 'a' or v == 'A' or v == 'e' or v == 'E'or v == 'i' or v == 'I' or v == 'o'or v == 'O' or v == 'u' or v == 'U' ) :
#
#     print('Este o vocala')
# else:
#     print('Nu este o vocala')
#
# #10.Transforma si printeaza notele din sistem românesc in sistem american dupa cum urmeaza
#
# #Peste 9 => A ;  Peste 8 => B; Peste 7 => C; Peste 6 => D; Peste 4 => E ; 4 sau sub => F
#
# nota = 3
#
# if nota >= 9:
#     print ('A')
# if nota == 8:
#     print ('B')
# if nota == 7:
#     print ('C')
# if nota == 6:
#     print ('D')
# if nota == 4:
#     print ('E')
# if nota <= 4:
#     print('F')
#
# #11.Verifica daca x are minim 4 cifre (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
# #12.Verifica daca x are exact 6 cifre
#
# count = 0
# x = 789567
#
# while (x > 0) :
#     x = x // 10
#     count = count + 1
#
# print ('NUmarul total de cifre:' , count)
# if count >=4 and count == 6:
#     print ('Numarul are cel putin 4 cifre')
#
# #13. Verifica daca x este numar par sau impar
#
# x = 4 # am facut verificarea si cu 7
#
# if (x % 2) == 0:
#
#     print('x este numar par')
# else:
#     print('x este numar impar')
#
# #14. x, y, z (int) Afiseaza care este cel mai mare dintre ele?
#
# x = 11
# y = 9
# z = 3
#
# if x > y and x > z  :
#   print ('Valoarea cea mai mare o are ' , x )
#
# elif y > x and y > z :
#     print ('Valoarea cea mai mare o are' , y )
# else :
#
#
#
# #15. X, y, z - reprezinta unghiurile unui triunghi
# #Verifica si afiseaza daca triunghiul este valid sau nu
# #a+b>c ; a+c> b; b+c > a
#
# x = 7 # am verificat si cu 4 => merge pe elif
# y = 10
# z = 5
#
#
# if x + y > z and x + z > y and y + z > x  :
#
#  print ('Triunghiul este valid' )
#
# elif y > x and y > z :
#
#      print ('Triunghiul nu este valid' )
#
#
# #16. Pentru exercitiile cu biletele de avion incercati sa aplicati tehnicile de equivalence partitioning si boundary value analysis astfel incat sa eficientizati testarea.
# #Sa tineti cont de urmatoarea chestie: tehnicile de testare vor fi aplicate nu pe faptul ca o persoana are pasaport sau nu ci pe varsta persoanei
# #Tehnicile de testare discutate vor fi aplicate pe condiția age>=18 și vor consta în crearea unor clase de echivalență din care vom alege cate o singura valoare și respectiv valorile de graniță pentru a le folosi în testare
#
# #**** -  nu am inteles ce trebuie facut
#
# # Age = input( 'introduceti varsta')
# # pasaport = input('Are pasaportul valid : DA/NU ')
# # ambii_parinti = input('Are ambii parinti? DA/NU ')
# # permisiune = input('Are permisiune? DA/NU/NA ')
# #
# # If age >=18 and pasaport == 'DA':
# # 	print(permite calatoria)
# # elif pasaport == 'DA' and (ambii părinți == 'DA' or permisiune == 'DA') :
# #     print('Permite calatoria')
# # else :
# #     print('Nu permite calatoria')
#
#
#
