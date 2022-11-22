alte_numere = [-5, 7, 2, 9] #[-5,2,7,9]
swaped = True
while swaped:
    swaped = False #(swaped = am schimbat doua elemente intre ele)
    for x in range(len(alte_numere) -1):
        if alte_numere[x] > alte_numere[x+1]:
            alte_numere[x], alte_numere[x+1] = alte_numere[x+1], alte_numere[x]
            swaped = True
print(alte_numere)

"""
ITERATIA 1:
swapped == True? DA -> intram in iteratie
swapped = False (presupunem ca lista este sortata)
x = 0 -> alte_numere[0] > alte_numere[1] -> -5 > 7? NU
x = 1 -> alte_numere[1] > alte_numere[2] -> 7 > 2 -> alte_numere[1] = 2,alte_numere[2] = 7
         swapped = True [-5,2,7,9]
x = 2 -> alte_numere[2] > alte_numere[3] -> 7 > 9? NU

ITERATIA 2:
swapped == True? DA -> intram in iteratie
swapped = False  (presupunem ca lista este sortata)
x = 0 -> alte_numere[0] > alte_numere[1] -> -5 > 2? NU
x = 1 -> alte_numere[1] > alte_numere[2] -> 2 > 7? NU
x = 2 -> alte_numere[2] > alte_numere[3] -> 7 > 9? NU
swapper = False (nu s-a mai facut nicio schimbare)

ITERATIA 3:
swapped == True? NU -> iesim din while
"""