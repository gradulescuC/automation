"""

Notions to cover:


- Variables (What is a variabile, what is it used for, how to initialize a variable)
- Assert
- Input
- Print and Format inside print
- Constants (What is a constant, what can we use it for, how can we declare it)
- Data Types
- Type Casting
- Dunder methods
- Built-in Functions
- Strings and  Immutability
"""

# There are two types of comments in python
#       - single line comment - marked by #
#       - multi-line comment - marked by three double quotes/single quotes on each side of the comment


"""1. Variables + print

A variable is a rezerved memory space where we can store information
Unlike other programming languages, in python a variable is created only when a value is assigned to it

Rules for naming a variable:
- variable names must not contain spaces
- variable names must not be named with reserved words (for example we cannot name a variable as print)
- variable names must be unique
- variable names must not start with a number (they can contain numbers as long as they do not start with one)
- usually variables follow the format snake_case or camelCase (usually snake_case)
- variable names should start with lowercase
- variables are case sensitive
"""

expectedUsr = 'Gabriela'
expectedPass = 'abcd'
expectedSold = 1000
user = input("Enter User ")
assert user==expectedUsr # assert evaluates of the evaluated expression is true. If not, it returns error and it stops the execution of the program

# Same exercise, more complicated

userName = input("Enter your username: ")
if len(userName) >= 6 and len(userName) <= 12: # Here we use an if statement which checks if the user is between 6 and 12 characters with the help of the len function
    print("Now enter your password")
    userPassword = input("Enter your password: ")
    if len(userPassword) >= 6 and len(userPassword) <= 12: # if the user is correct, we do the same thing with the password
        print("You are able to log in!!!")
    else:
        print("Incorrect password. Choose another.")
else:
    print("Incorrect username. Choose another.")

# Note: In order to find out more about a function, we can use CTRL+Click on the specific function

# Variables are case sensitive
# We can copy the value from a variable into another variable
# Example
user_5 = 100 # instruction for defining and initializing a variable
#print(uSer_5) #  This will not work because the variable name is case sensitive and the system will not recognise this name
score = user_5 # here we assign the value of user_5 to the variable calles 'score'
print(score)

# ------------------------------------------------------------------------------------------------------------


""" 

2. ASSERT


- Assert is a way to make a validation
- It checks if a specific statement is evaluated as true
- If it is true, the code moves on, otherwise it returns error and the run stops
- Normally all automated tests finish with an assert
"""
a = 1
assert a==1
print("This test passed")
# assert a == 2
# print("this will return error and will not be executed")
print(a==2)

userpass = input("introdu parola ")
parola = "pass123"
assert parola == userpass
print("autentificare reusita")


""" 3. Input from keyboard """
x = input("Enter the first number ") # We assign a value from the keyboard to the variable x
y = input("Enter second value ")
output = int(x) + int(y) #  we apply forced conversion (CAST) to a variable (by default the data type of the value given from the keyboard is String)
output = int(x) % int(y)  # the modulo function - useful when we check if a number is odd or even - it returns the remainder from the devision of x by y
x,y,z = 1,2,3 # we can declare and initialise three variables at the same time
print(z)
print(f"{x} with {y} is {output}") # The f in the front lets the system know that we are about to send some variables inside the text that should be read, not displayed as text

# ------------------------------------------------------------------------------------------------------------

""" 4. Formating in print"""

print(f"{x} with {y} is {output}")  #print with formating
print(f"{x} modulo {y} is {output}" )

# Alte exemple de formatare:
name = 'Johnny'
age = 55

print('Hi' + name + '. You\'re' + str(age) + 'years old') # Exemple without formating
                                                             # We wrote You\'re with the character  "\" called escape character
                                                                # because we wanted the system to consider the sigle quote as a character to be displayed on the screen,
                                                                     # not as the end of the text to be displayed
print(f'Hi {name}, You are {age} years old') # Example with formatting

# Before python 3, formating was done with the function .format
# Example:

print('Hi {}. You  are {} years old.'.format('Johnny',55)) # Here the brackets will be replaced sequantially with the values between parantheses
print('Hi {}. You  are {} years old.'.format(name, age))
print('Hi {new_name}. You  are {new_age} years old.'.format(new_name = 'sally', new_age=100)) # Here we defined in-line the values for name and age


# ------------------------------------------------------------------------------------------------------------


"""5. CONSTANTS"""

# Constant = memory space that cannot/should not change its value
# Constants are not supported by python, and that's why if we want to define something as a constant, as a convention we will use
                                        #capital letters so that people know that that is a constant
# Useful when generating all sort of utilities for automation, where we define test inputs that should not change their behaviour
# Ex: username, sleep between automation test steps (we can agree at project level the sleep time)

PI = 3.14

# ------------------------------------------------------------------------------------------------------------

"""

6. DATA TYPES


A data type is an information that informs the system about the type of information we can store in a specific variable

The most used data types in python:
- int (short for integer) -> Can store only integer values (1,2,9,99,167834534 etc)
- float -> Can store decimal numbers (16 decimal points)
- bool (short for boolean) -> Can store true or false values  (with first letter in capital letter)
- string -> Can store text
"""

age = 3
quantity = 24.5
isActive = True
customer_name = "john"

float_nr = 123456789.1234567890123456
print(float_nr)

# We cannot concatenate two variables having two data types, but we have workarounds for this
name = 'Michael'
age = 33
# print("My name is" + name + "and I have" + age + "years old") - this will return error because we cannot concatenate string and numeric data types
print("My name is" + name + "and I have" + str(age) + "years old") # this will work
print("my name is {0} and I am {1} years old ".format(name,age))  #this is harder to read and it is not recommended.
print(f"My name is {name} and I have {age} years old") # this is the best option (the most optimal)
                            #f forces the variables between brackets to be treated as strings
                            #f is short for - format string -

"""

7. TYPE CASTING

Type casting means changing the data type of the value in a specific variable

"""

type_casting_example = 33
print('---------------------------')
print(type(type_casting_example))
print(type(float(type_casting_example)))
print(type(str(type_casting_example)))
type_casting_example_1 = float(type_casting_example)
print(type(type_casting_example), type(type_casting_example_1))




"""8. Dunder methods -> DUNDER = Double underscore"""

# Examples of dunders:
_x = 7  # it specifies a variable considered through convention as PROTECTED (it cannot be used in other packages). It is NOT dunder
__x = 8 # Variables preceded by __ are dunders and are a way to define PRIVATE variables (they cannot be used outside the class).
                    # The dunders are usually python reserved, so it is not recommended to defined variables as dunders

#Example of dunders:
if __name__ == '__main__':  # It checks if the program is executed individually or it is called from another program
    print("Another module")
    a: int = 5 # We ca declare a variable also by explicitely declaring the data type
    b: str = 'Johny goes to school'
    print(type(a))
    print(type(b))
    #c = a + b -> Here it will return concatenation error because we cannot sum a numerical data type with a string data type
    c = str(a) + b # Here it will be ok because we did a CAST to string for the variable a
    print(c)
    print(a)

# ------------------------------------------------------------------------------------------------------------

""" 9. Built in functions """

greet = 'Hello'
print("Calculate the length of the string and print it entirely")
print(len(greet)) # The len function is the short version of length and it shows how many characters there are in a string
print(greet[0:len(greet)]) # Here we applied the concept of slicing, which means that we can 'cut' the text and display it in 'slices'
                              # In this case we specified that we want to display everything from the beginning of the string (position 0) until we go through the entire length of the string
quote = 'to be or not to be'
print("Display the string in capitals - we can use upper or capitalize")
print(quote.upper())
print(quote.capitalize())
print("Find the first instance of the word 'be' in the text stored in the variable 'quote'")
print(quote.find('be'))
print("Replace all the instances of 'be' with 'me'")
print(quote.replace('be','me'))
print(quote)
name = 'Andreea'
print("The type function can be used to display in the console the data type of a specific variable")
print(type(name))
name = 1
print(type(name))

# ------------------------------------------------------------------------------------------------------------
""" 10. STRING (index, len, slicing, metode) / Immutability -> Immutable is when no change is possible over time in a variable. 
In Python, if the value of an object cannot be changed over time, then it is known as immutable. 
Once created, the value of these objects is permanent. 
Also, when we replace the data in a variable we do not actually replace it, we point the same variable name to a different memory location
We can slice a string by using the following sintax: my_str[start_pos,end_pos,step]


Python Data Types – Immutable Type
Boolean
Numeric
String
Tuple

--------------------------------

Python Data Types – Mutable Type
List
Set
Dictionary

"""

print("Immutability example")
age = 42
print(id(age))  # Here it returned the id 140207831785040 (might be different on some other system/laptop/pc and might differ between runs)
print(type(age))
print(age)

print("We assign a new value to the variable, but it will actually not replace but define another memory to which the variable age will point")
age = 43
print(age)
print(id(age)) #  Here it returned the id 140207831785072 because we point towards some other address in the memory


list_example=[1,45,'test','andrada'] # we can add different types of data to a list
list_example[0] = '1212' # This will work because selfish is a list, and the list is not immutable
print(list_example)

variable_int_example = 5678
# print(variable_int_example[0]) # This will return an error: TypeError: 'int' object is not subscriptable

""" Subscriptable means that the object implements the __getitem__() method.
 In other words, it describes objects that are "containers", meaning they contain other objects. 
 This includes strings, lists, tuples, and dictionaries, but not int
 
 Note: In programming, the index of subscriptable objects ALWAYS starts with 0
 

"""
variable_example = 'testWordExample'
print(variable_example[0])  # This will no longer return error, because this time we try to slice a string, and strings are subscriptable
print(variable_example[7])
print()

print("Slicing exercises")
""""Slicing model: object_name[start:stop:stepover] """

#[start]
print("Here we print exerything starting from the index 1 until the end (which means we exclude the first a)")
print(variable_example[1:])  # here we print exerything starting from the index 1 until the end (which means we exclude the first a)
                                    # If we do not specify the stop and stepover, they will be by default stop = until the end and stepover = 1

#[start:stop]
print("Here will print everything from index 0 until index 8")
print(variable_example[0:8]) # here will print everything from index 0 until index 8

#[start:stop:stepover]
print("Here will print everything from index 0 until index 8, but it will only print every second character")
print(variable_example[0:8:2])

print("Here it will print everything from the start util the index 5. If start is not specified, it will be by default index 0")
print(variable_example[:5])

print("Here it will print everything from the start util the end, with a stepover of 1 - we had to specify '::', otherwise the system will have considered the 1 as start""")
print(variable_example[::1])

print("Here it will print the third character from the end (- means that it will start from the end instead of beginning and 3 is the position of the character in the string)")
print(variable_example[-3])
print("Here it will print everything from the end backwards")
print(variable_example[::-1])
print("Here it will print everything from the end backwards with a step of 2")
print(variable_example[::-2])

print()
print("String methods")
sentence = "Mn name is python and i am a snakes"
print(sentence.count('a')) # counts how many times do we have the character a in the string
print(sentence.upper())
print(sentence.replace('i','y'))
print(sentence.find('y'))
print("This is the split sentence")
print(sentence.split())
# https://stackoverflow.com/questions/509211/understanding-slice-notation/46614773 -> More info about slice notation
myStr = 'Today is wednesday'
# I want to go through it until the one before the last character
# I want to find out the last index
last_index = len(myStr)-1 # we add -1 because the index starts from 0
print(last_index) # we check the last index
print(f"The last letter in '{myStr}' is '{myStr[last_index]}'")
print(myStr[0:last_index])
part1 = sentence[0] # we save the first character
part2 = sentence[1:].replace('s','$')
print(part1,part2)

print("String index")
print(myStr[0])
print(myStr[10])
print(myStr[last_index])


    

















