
from math import sqrt, ceil

#Can I have a stepover in a for loop? -> Yes. See below
v = 0
list_1 = [9, 5, 7, 2, 5, 3, 8, 14, 6, 11]

for i in range(0, len(list_1), 2):
    print(list_1[i])

# Can I limit the number of decimals on sqrt? -> No but you can use round function to do this
print("The root of 8 is: ", round(sqrt(8),2))

age = 18

# Can I have multiple conditions in a for loop? -> No, but you can have multiple conditions in an if statement
if ((age >= 8) and (age <= 12)):
    print("YOU ARE ALLOWED. WELCOME !")
else:
    print("SORRY ! YOU ARE NOT ALLOWED. BYE !")