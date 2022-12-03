text = input('String: ')
a = text[0]
replace = text.replace(a, a.upper())
rez = text[0] + text[1:- 1].replace(text[0],text[0].upper()) + text[-1]
print(rez)
