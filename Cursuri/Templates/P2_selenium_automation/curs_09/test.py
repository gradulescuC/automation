b = input('What fruits do you like?')
z = b[0]
v = z + b[1:len(b)-1].replace(z,z.upper()) + b[len(b)-1]
print(v)