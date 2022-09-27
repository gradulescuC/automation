# Varianta 1
number = int(input("Enter number: "))
if number % 2 == 0:
    print(f"Numarul {number} este par.")
else:
    print(f"Numarul {number} este impar.")
# --------------------------------------------------------

# Varianta 2:
'''Write a program to verify if a number is odd or even'''

number = input("Enter a number to be checked: ")

def checkOddEven(x):
    if x % 2 == 0:
        print(f"{x} is even")
    else:
        print(f"{x} is odd")
checkOddEven(int(number))
