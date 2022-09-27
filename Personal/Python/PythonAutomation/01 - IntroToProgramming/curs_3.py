"""
NOTIONS TO COVER:

- If statement recap
- For loop
- While loop
- Break and continue
- Functions

"""


""""
1. IF statement recap

Check the number of rabbits

"""

print("IF STATEMENT RECAP")
print()
m_rabb = int(input("Insert the number of male rabbits: "))
f_rabb = int(input("Insert the number of female rabbits: "))
if (m_rabb>0 and f_rabb>0):
    breed = input("Do you want to breeed? ")
    if breed == 'no': # here we have a nested if (if inside an if)
        print("Keep male and female rabbits apart")
    else:
        print("Breed ok")
# -------------------------------------------------------------

"""

2. For Loop

A for loop is used to loop through an iterable object (like a list, tuple, set, etc.) and perform the same action for each entry. 
For example, a for loop would allow us to iterate through a list, performing the same action on each item in the list

"""


print("FOR LOOP INSTRUCTIONS")
print()
my_list = [1,2,3,7,5,14,22] # Define a new list with 7 elements. We want to calculate the sum of all the numbers inside
n = 0 # We start with a counter that we initialize with 0 (we haven't added any number yet)

for i in my_list: # we define an index called i in which we are going to store each element in the list
    print(f"Adding {i} to {n}")
    n = n + i # as long as we haven't reached the end of the list we will add the current element to the previous total
    print(f"Current sum is {n}")
else:
    print("We are done with the sum") # when we are going to reach the end of line we are going to print a message
print(f"The sum of the elements in the list is: {n}")

# -------------------------------------------------------------

"""

3. While loop

A while Loop is a block of code  that gets executed repeatedly until a given condition is satisfied. 
When the condition becomes false, the line immediately after the loop in the program is executed.

"""


print("WHILE LOOP INSTRUCTIONS")
print()
my_list = [1, 2, 3, 4, 5, 43] # Define a new list with 6 elements. We want to calculate the sum of all the numbers inside
n = 0 # We start with a counter that we initialize with 0 (we haven't added any number yet)
position = 0 # We define the position from which we want to start
while position < len(my_list): # As long as I haven't reached the last index in the list (we use < because we start from index 0, so the last index will always be smaller by 1 than the total numer of elements)
    n = n + my_list[position] # we add to the current sum the value of the next element in the list
    position+=1 # we increment the position by 1 so we move on to the next element
else:
    print("We are done with the numbers") # Unlike other programming languages, while loop supports else condition
print(f"The sum of the elements is {n}")
# -------------------------------------------------------------

"""

4. BREAK AND CONTINUE 

The BREAK statement is used to terminate the loop or statement in which it is present. 
After that, the control will pass to the statements that are present after the break statement, if available.
If the break statement is present in the nested loop, then it terminates only those loops which contains break statement.

CONTINUE is also a loop control statement just like the break statement. 
CONTINUE statement is opposite to that of break statement, instead of terminating the loop, it forces to execute 
                                                                                        the next iteration of the loop.
As the name suggests the continue statement forces the loop to continue or execute the next iteration. 
When the continue statement is executed in the loop, the code inside the loop following the continue statement 
                                                          will be skipped and the next iteration of the loop will begin.

"""

for i in range(10): # if we do not have a list or something to work with but just want to iterate the loop
                                        # for a number of times we can use the range function
                                        # the range function is used to define the point where an iteration should stop
    if i == 7: # we check if we got to the seventh iteration of the for loop
        print(f"The last number to be printed is {i}. After that we are going to get out of the FOR loop (it will NOT execute the rest of the statements, if any)")
        break # we instruct the system to break the current execution and get out of the FOR loop

print("-------------------------------------")

for i in range(10): # Again we want to iterate through the FOR loop 10 times
    if i == 7: # we check if we got to the seventh iteration of the for loop
        print(f"The number that was skipped is {i}")
        continue # we instruct the system to skip the rest of the instructions (if any) in the current iteration and move to the next one

"""
5. FUNCTIONS

A function is a named section of a code that performs a specific task. This typically involves taking some input, manipulating the input and returning an output.
The function will not be executed unless we call it
Calling the function is done through specifying the name of the function followed by the arguments specified between paranthesis
An argument is an information about how many inputs does the function need
When calling a function, we need to specify as many arguments as we passed when we created the function
A function is defined with the keyword def
The body of the function is identified by an indentation from the edge of the python file
A function can or cannot have a return value
A return value is a way of sending data outside of the function
"""

print("Let's define a function that will return a greeting for a specific person: ")
def say_hello(name):
    print("Hello ", name + ", this is a print without formating")
    print(f"Hello {name}, this is a print with formatting")

name  = input("Let's read a name from the keyboard so we can greet this person properly: ")
print(f"Now let's do the actual greeting. ")
say_hello(name)
print("Test")
print()

print("\nWe can also call the method inside print: "+ str(say_hello(name)))

print("Test1")
print("\nWhen we call a method, we need to NOT specify the argument between quotes or double quotes,"
                        " unless it is an explicit text we want to use as argument."
                        "If we want to use a variable as argument, it will NOT be placed between quotes or double quotes"
      )
print("Test2")
print("This is what will print if we put the argument between double quotes")
say_hello("name")  # This will print on the screen "Hello name" instead of "Hello Maria" (or any other name we send from input)

# say_hello() This instruction will return error: TypeError: say_hello() missing 1 required positional argument: 'name'
            #The error will be returned because we told the system that he should wait one argument, but we provided none when calling the function

print("We can assign the return value of the function to the variable x. If the function has no return value, 'none' will be the default")
x = say_hello("Maria")
print(f"The value of the return function is: {x}")

def say_hello2(name,email, password="abc123"):  #Putem aplica un parametru default
    return name + ", Bine ai venit! Adresa ta de email este " + email + " iar parola e " + password

y = say_hello2(name = "Andreea",email = "Andreea@yahoo.com" ,password="qwerty")
y = say_hello2(email = "Andreea@yahoo.com",name = "Andreea" ,password="qwerty") #Not a good practice

print(y)
y = say_hello2("Andreea","Andreea@yahoo.com" ,"qwerty")
print(y)
z = say_hello2("Mirabela","mirabela@yahoo.com")
print(z)

def say_hello3(*myParam): # args = arbitrary arguments. Ajuta atunci cand nu vrem sa definim un numar fix de parametri. Utila atunci cand definesc un scop de configurare a testelor. (ce test sa rulez, din ce suita sa rulez, ce rapoarte sa generez)
    print("Hello", myParam[0])
    print("Hello", myParam[-1])

say_hello3("Mihaela","Andrei","Marius","Razvan","Ivan")


def say_hello4(**test): #Argumente arbitrare pe baza de keyword
    print("Your name is ", test["name"])
    print("Your salary is", test["salary"])
    print("Your email is ", test["email"])

say_hello4(name="Jon Snow",salary = 1000, email = "jon.snow@gmail.com")
