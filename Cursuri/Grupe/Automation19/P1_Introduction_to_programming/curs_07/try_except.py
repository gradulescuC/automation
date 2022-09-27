# exceptie = o eroare in Python, ceva ce nu poate sa faca codul si opreste executia
# se trateaza prin try except

# number = 0
# number2 = 10 / number


# try: #in try punem codul despre care presupunem ca ar putea genera o execptie
#     number = 0
#     number2 = 10/number
# except Exception as e: #in except tratam orice exceptie (salvam mesajul ei in variabila e)
#     print(f'Error: {e}')
#
# print('ajung aici')



# lista_culori=["rosu","albastru","fuchsia","magenta","siclam","turcoise"]
# try:
#     # for i in range(9):
#     #     print(lista_culori[i])
#     number = 0
#     number2 = 10/number
# except Exception as e:
#     print(f"Attention! The range is too large for the given list. Error: {e}")

# print('am ajuns aici') # fiindca am prins exceptia, codul merge mai departe


# fortezi o exceptie
numar_studenti = int(input("Introduceti numarul de studenti: "))
lista_studenti = []
for student in range(numar_studenti):
    lista_studenti.append("Maria")
    if(student>2):
        raise IndexError('Limita elevilor din clasa este 30')

print(f"lista de studenti este: {lista_studenti}")