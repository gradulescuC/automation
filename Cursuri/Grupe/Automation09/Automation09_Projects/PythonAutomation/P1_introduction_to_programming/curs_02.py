# A. ASSIGNMENT OPERATORS
x = 3
print(x)
print("-------------------------------------")
x = x+3
print(x)
x+= 3
print(x)
print("-------------------------------------")
x = x - 3
print(x)
x-=3
print(x)
print("-------------------------------------")
x = x*3
print(x)
x*=3
print(x)
print("-------------------------------------")
x = x/3
print(x)
x/=3
print(x)
print("-------------------------------------")

# B. ARITHMETICAL OPERATORS

print(4+6)
print(10%3)
print(2**3)

# C. COMPARISON OPERATORS
y = 2
x = 2
print(x==2)
print(x==y)
print(x!=2)
print(x!=y)
print(x>2)
print(x>y)
print(x<2)
print(x<y)
print(x>=2)
print(x>=y)
print(x<=2)
print(x<=y)

# D. LOGICAL OPERATORS
print(x<2 and x<y)
print(x==2 and x<y)
print(x==2 and x==y)
print(x==2 or x<y)

y = 2
x = 2
print("test")
print(not(x==2 or x<y))

print(not(x==2 or x<y))
print(x<y and x>y and x == y)
print(x<y or x>y and x <= y)

# D. FLOW CONTROL

NOTA_DE_TRECERE = 4.5 # constant that we do not want to change it's value
NOTA_DE_TRECERE_PURTARE = 7
nota_examen = 10
nota_purtare = 10
if nota_examen >= NOTA_DE_TRECERE and nota_purtare >= NOTA_DE_TRECERE_PURTARE:
    print("Am trecut")
    if nota_examen==10 and nota_purtare==10:
        print("felicitari,esti premiant")
else: # Else does not have a condition because it means the instructions to be executed in case the previous condition is evaluated as false
    print("Nu am trecut")


optiune = int(input("Alegeti limba, pentru romana apasati 1, pentru engleza apasati 2"))
if optiune == 1:
    print("Ati ales limba romana")
    optiune1 = input("pentru persoane fizice apasati 1, pentru persoane juridice apasati 2")
    if(optiune1 == 1):
        print("Ati ales persoana fizica")
    elif(optiune1 == 2):
        print("Ati ales persoana juridica")
    else:
        print("Optiune invalida, va rugam sa incercati din nou")
elif optiune==2:
    print("You chose english")
    optiune1 = input("For individual persons press one, for companies press 2")
    if (optiune1 == 1):
        print("You chose individual person")
    elif (optiune1 == 2):
        print("You chose a company")
    else:
        print("Invalid option, please try again")
elif optiune == 3:
    print("return to main menu")






