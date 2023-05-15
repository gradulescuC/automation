"""Descriere metoda bubble sort """
lista = [12, 45, 67, 8, 91]
pahar = 0
for i in range(0, len(lista)):
    for j in range(1, len(lista) - i):
        if lista[j - 1] > lista[j]:
            pahar = lista[j - 1]
            lista[j - 1] = lista[j]
            lista[j] = pahar

for i in range(0, len(lista)):
    print(lista[i])
