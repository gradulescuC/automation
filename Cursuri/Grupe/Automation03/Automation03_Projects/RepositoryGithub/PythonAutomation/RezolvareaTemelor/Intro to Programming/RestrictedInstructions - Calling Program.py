import RestrictedInstructions_CalledProgram

if RestrictedInstructions_CalledProgram.authorized == 1:
    print("You are authenticated")
else:
    print("Please try again")
    RestrictedInstructions_CalledProgram.username = input("Enter username: ")
    RestrictedInstructions_CalledProgram.password = input("Enter password: ")
