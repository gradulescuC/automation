import random

import null as null

def checkNumber(guess_number):
    num = random.randrange(1, 11)
    if guess_number == num:
        print("Nice! You got it.")
    elif guess_number < num:
        print("Bigger")
    else:
        print("Lower")
    print(f'The number to guess was {num}!')

name = input('Enter your name: ')
answer = input(f"Hello {name}, do you want to play 'Guess the number'?\nAnswer 'Yes' or 'No': ")
while answer != 'Yes' and answer != 'No':
    answer = input(f"{name}, please answer with 'Yes' or 'No': ")
if answer == 'No':
    print(f"Goodbye {name}, hope next time you'll play!!!")
else:
    try:
        guess_number = int(input(f"{name} enter a number between 1 and 10: "))
        while guess_number < 1 or guess_number > 10:
            guess_number = int(input("The number has to be between 1 and 10! Please enter it: "))
        checkNumber(guess_number)

    except:
        guess_number = input("Error! Must be a number between 1 and 10!\nTry again: ")
        while guess_number.isnumeric() == False or int(guess_number) < 1 or int(guess_number) > 10:
            guess_number = input("Error! Must be a number between 1 and 10!\nTry again: ")
        checkNumber(int(guess_number))

