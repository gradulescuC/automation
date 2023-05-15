# Comparatia pentru password si sold de la tastatura prin consola

expectedUsr = 'Gabriela'
expectedPass = 'abcd'
expectedSold = 1000
user = input("Enter User ")
password = input("Enter Password ")
sold = int(input("Enter Sold "))
assert user==expectedUsr
assert password == expectedPass
assert sold == expectedSold