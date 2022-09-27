#
# b. Dificultate medie (Faceti cat puteti din ele)
#
# 1.
# Avand lista
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
#
# Folositi un for ca sa iterati prin toata lista si sa afisati
# ‘Masina mea preferata este x’
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
#
print(len(masini))
#
for i in masini:
    print(f'Masina preferata este {i}')
# Run:
# Masina preferata este Audi
# Masina preferata este Volvo
# Masina preferata este BMW
# Masina preferata este Mercedes
# Masina preferata este Aston Martin
# Masina preferata este Lastun
# Masina preferata este Fiat
# Masina preferata este Trabant
# Masina preferata este Opel
#
# Faceti acelasi lucru cu un for each
#
for masina in masini:
    print(f'Masina preferata este {masina}')
#
# Run:
# Masina preferata este Audi
# Masina preferata este Volvo
# Masina preferata este BMW
# Masina preferata este Mercedes
# Masina preferata este Aston Martin
# Masina preferata este Lastun
# Masina preferata este Fiat
# Masina preferata este Trabant
# Masina preferata este Opel
#
# Faceti acelasi lucru cu un while

# 2.
# Aceeasi lista
# Folositi un for else
# In for
#    Modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimul In else
#    Printati lista
#
# 3.
# Aceeasi lista,
# Vine un cumparator care doreste sa cumpere un Mercedes
# Iterati prin ea prin modalitatea aleasa de voi
# Daca masina e mercedes
#    Printam ‘am gasit masina dorita de dvs’
#    Iesim din ciclu folosind un cuvant cheie care face acest lucru
# Altfel
#    Printam Am gasit masina X. Mai cautam
#
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

for x in masini :
    if x == 'Mercedes':
        print(f'Am gasit masina dorita de dvs, {x}.')
        break
else :
    print(f'Nu am gasit masina {x}. Mai cautam')
#
#
# Run: Am gasit masina dorita de dvs, Mercedes.
#
# 4.
# Aceasi lista
# Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun.
# Daca masina e Trabant sau Lastun
#    Folositi un cuvant cheie care sa dea skip la ce urmeaza
# (nu trebuie else)
# Printati S-ar putea sa va placa masina x
#
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for x in masini :
    if x != 'Lastun' and x != 'Trabant':
        print(f'S-ar putea sa va placa masina {x}.')
        continue
# Run:
# S-ar putea sa va placa masina Audi.
# S-ar putea sa va placa masina Volvo.
# S-ar putea sa va placa masina BMW.
# S-ar putea sa va placa masina Mercedes.
# S-ar putea sa va placa masina Aston Martin.
# S-ar putea sa va placa masina Fiat.
# S-ar putea sa va placa masina Opel.
#
# 5.
# Modernizati parcul de masini
# Creati o lista goala, masini_vechi
# Iterati prin masini
# Cand gasiti Lastun sau Trabant:
# Salvati aceste masini in masini_vechi
# Suprascrieti-le cu ‘Tesla’ (in lista initiala de masini)
# Printati Modele vechi: x
# Modele noi: x
#
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []

for i in range(len(masini)) :
    if masini[i] == 'Lastun' or masini[i] =='Trabant':
        masini_vechi.insert(0, 'Lastun')
        masini_vechi.insert(0, 'Trabant')
        masini[i] = 'Tesla'
        break

# print(f'Modele vechi: {masini_vechi}')
# print(f'Modele noi: {masini}')



# 6.
# Avand dict
pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
# Vine un client cu un buget de 15000 euro
# Prezentati doar masinile care se incadreaza in acest buget
# Iterati prin dict.items() si accesati masina si pretul
# Printati Pentru un buget de sub 15000 euro puteti alege masina xLastun
# Iterati prin lista
#
for masina, pret in pret_masini.items() :
    if pret <= 15000 :
        print(f'Pentru un buget de sub 15000 euro puteti alege {masina}.')
# Run:
# Pentru un buget de sub 15000 euro puteti alege Dacia.
# Pentru un buget de sub 15000 euro puteti alege Lastun.
# Pentru un buget de sub 15000 euro puteti alege Opel.
#
#
# 7.
# Avand lista
# numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# Iterati prin ea
# Afisati de cate ori apare 3
# (nu aveti voie sa folositi count)
#
cifra = 0
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for cifra in numere :
    if cifra == 3:
        cifra = cifra + 1
        print(f'Cifra 3 se regaseste de {cifra} ori. ')


# 8.
# Aceeasi lista
# Iterati prin ea
# Calculati si afisati suma numerelor
# (nu aveti voie sa folositi sum)
#
#
# 9.
# Aceeasi lista
# Iterati prin ea
# Afisati cel mai mare numar
# (nu aveti voie sa folositi max)
#
#
# 10.
# Aceeasi lista
# Iterati prin ea
# Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
# Ex: daca e 3, sa devina -3
# Afisati noua lista
#
#
#
#
#
# c. Optionale (may need google)
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
#
# 12.
# Aceeasi lista
# Ordonati crescator lista fara sa folositi sort
# Va puteti inspira vizual de aici
# https://www.youtube.com/watch?v=lyZQPjUT5B4

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
for i in range(0, len(alte_numere) - 1):
    for j in range(len(alte_numere) - 1):
        if (alte_numere[j] > alte_numere[j + 1]):
            temp = alte_numere[j]
            alte_numere[j] = alte_numere[j + 1]
            alte_numere[j + 1] = temp
print(alte_numere)

# 13.
# Ghicitoare de numar
# numar_secret = Generati un numar random intre 1 si 30
# Numar_ghicit = None
# Folosind un while
#    User alege un numar
#    Programul ii spune:
# Nr secret e mai mare
# Nr secret e mai mic
# Felicitari! Ai ghicit!
#
#
#
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
#
# Ex:3
# 1
# 22
# 333

for i in range(7):
    count = 0
    while count<i:
        print(i, end="")
        count+=1
    print()

# 15.
tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
# Iterati prin lista 2d
# Printati ‘Cifra curenta este x’
# (hint: nested for - adica for in for)

for i in range(len(tastatura_telefon)):
   for j in range(len(tastatura_telefon[i])):
       print(f'Cifra curenta este {tastatura_telefon[i][j]}')