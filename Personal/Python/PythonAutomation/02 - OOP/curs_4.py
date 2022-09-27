"""

Function used to get the max out of three numbers
Another approach for the same problem using nested functions
Define four functions for basic calculator operations

-- embeded function = functie predefinita in python
"""

from math import sqrt
print(max(7,5,12))

def max2(num1,num2):
     if num1>num2: #se face comparatia intre cele doua numere
        return num1 #se returneaza num1 daca e mai mare decat num2
     else:  #acest else e optional, daca il eliminam, sistemul va subintelege ca acel return num2 e pe ramura de else, dar in cazul asta va trebui sa schimbam indentarea lui return num2 pe aceeasi linie cu if
         return num2

def max3(num1,num2,num3): #functie cu trei argumente
    return max2(num1,max2(num2,num3)) #aici primul parametru al functiei max2 e num2, iar al doilea parametru e maximul dintre num2 si num3

print(max2(5,7))
print(max3(7,12,5))

print("--------------------------")
print("Nested Functions ")

# Nested functions (functii care se afla in interiorul altei functii)
def max3v2(num1,num2,num3): #functie cu trei argumente
    a = 3 #definim o variabila a in care stocam valoarea 3. E o variabila locala, nu o sa o putem folosi in alta parte in afara functiei
    def max2v2(num1,num2): #definim functia max2v2 in interiorul functiei mx3v2
        if num1 > num2:  # se face comparatia intre cele doua numere
            return num1  # se returneaza num1 daca e mai mare decat num2
        else:
            return num2
    print(a)
    return max2v2(num1,max2v2(num2,num3)) #se returneaza rezultatul unei functii

print("Numarul maxim este", max3v2(45,23,12))
# functia max2v2 e valabila doar in interiorul functiei max3v2
# print(a) -- Variabila a nu va fi vazuta pentru ca e declarata in interiorul functiei max3v2. Instructiunea asta va da eroare pentru ca variabila a nu e recunoscuta
#avantajele functiilor nested e de a putea sa grupam codul astfel incat sa nu complicam codul cu instructiuni pe care le vom folosi doar o singura   data

print("--------------------------")
print("Operatii matematice")

def mathOperations(a,b,operation): #functie de calcul a operatiilor matematice, cu trei argumente
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "radical":
        return sqrt(a)
    else:
        print ("other methods to be added")

print(mathOperations(5,7,"+"))
print(mathOperations(5,7,"-"))
print(mathOperations(5,7,"*"))
print(mathOperations(144,16,"radical"))

