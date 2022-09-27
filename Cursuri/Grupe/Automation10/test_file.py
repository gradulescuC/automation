lista_dictionare = [
    {"cheie1":"valoare1","cheie2":"valoare2"},
    {"cheie3":"valoare3","cheie4":"valoare4"},
]

tuplu_dictionare = (
    {"cheie1":"valoare1","cheie2":"valoare2"},
    {"cheie3":"valoare3","cheie4":"valoare4"},
)

# set_dictionare = {
#     {"cheie1":"valoare1","cheie2":"valoare2"},
#     {"cheie3":"valoare3","cheie4":"valoare4"},
# }


set_numere = {1,4,6,8}
print(set_numere)
set_numere.add(9)
print(set_numere)

print(type(lista_dictionare),type(tuplu_dictionare))

for i in range(0,len(lista_dictionare)):
    print(lista_dictionare[i])

for i in lista_dictionare:
    print(i)