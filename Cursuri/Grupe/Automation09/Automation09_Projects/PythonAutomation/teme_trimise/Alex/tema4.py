#1 Avand lista masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

#a Folositi un for ca sa iterati prin toata lista si sa afisati ‘Masina mea preferata este x’
#
masini =['Audi','Volvo','BMW','Mercedes','Aston Martin','Lastun','Fiat','Trabant','Opel']
# length = len(masini)
# for x in range(length):
#    print(f'Masina mea preferata este: {masini[x]}')


#b Faceti acelasi lucru cu un for each

# for marci in masini:
#     print(f'Marcile sunt: {masini}')


#c Faceti acelasi lucru cu un while

# i = 2
# while i<8:
#    print(f'Masina preferata este {masini[i]}')
#    i = i+1

#2.Aceeasi lista Folositi un for else; Modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimu
# for i in range(len(masini)):
#    if i==1 or i==2 or i==3 or i==4 or i==5 or i==6 or i==7:
#       print(masini[i].upper())
#    else:
#       print(masini[i].lower())

#3 Aceeasi lista, Vine un cumparator care doreste sa cumpere un Mercedes
# Iterati prin ea prin modalitatea aleasa de voi;
# Daca masina e mercedes Printam ‘am gasit masina dorita de dvs’

# for i in range(len(masini)):
#    if masini[i] == 'Opel':
#       print(f'Am gasit masina dvs!{masini[i]}')
#       break
#    else:
#     print(f'Am gasit masina: {masini[i]}, mai cautam')


#4 Aceasi lista Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun.

# for i in range(len(masini)):
#     if masini[i] == 'Trabant' or masini[i]=='Lastun':
#       continue
#     print(f'S-ar putea sa va placa masina {masini[i]}')

#5 Modernizati parcul de masini. Creati o lista goala, masini_vechi;Iterati prin masini

masini_vechi = []
#
# if masini == 'Lastun' or 'Trabant':
#     masini_vechi.append('Lastun, Trabant')                  #adaug masinile vechi intr-o lista goala creata mai sus
#     print(f'Masinile vechi sunt: {masini_vechi}')           #afisez lista cu masinile vechi
# del masini[5]                                               #scot din lista initiala masinile vechi
# del masini [6]
# masini.append("Tesla")                                      #adaug tesla la lista cu masini
# print(f'Noile noastre masini sunt: {masini}')               #afisez noile masini
#

# masini_vechi = []
# for i in range(len(masini)):
#     if masini[i] == 'Lastun' or masini[i]=='Trabant':
#         masini_vechi.append(masini[i])
#         masini[i]='Tesla'
# print(masini)
# print(masini_vechi)

#6 Vine un client cu un buget de 15000 euro.Prezentati doar masinile care se incadreaza in acest buget

pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}

# lista_masini = list(pret_masini.items())            #am definit o lista folosint dictionarul din enunt

buget = 15000                                       #am definit bugetul clientului


for masina in pret_masini.keys():
     if pret_masini[masina] <= buget:
        print(f'Pentru un buget de sub 15000 euro, puteti alege masina {masina}')

#7 Avand lista numere Iterati prin ea;Afisati de cate ori apare 3 (nu aveti voie sa folositi count).
#
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# counter = 0
# for i in numere:
#     if i == 3:
#         counter += 1
# print(counter)

#8 Aceeasi lista; Iterati prin ea;Calculati si afisati suma numerelor (nu aveti voie sa folositi sum).

# total = 0
# for i in numere:
#    total += i
# print(total)

#9 Aceeasi lista; Iterati prin ea;Afisati cel mai mare numar (nu aveti voie sa folositi max).

# max = 0
#
# for num in numere:
#     if max < num:
#         max = num
# print(max)

#10 Aceeasi lista; Iterati prin ea; Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa Ex: daca e 3, sa devina -3;Afisati noua lista.
#
# pozitiv = []
#
# for pozitive in numere:
#     if pozitive > 0:
#        pozitiv.append(-abs(pozitive))
# print(pozitiv)



