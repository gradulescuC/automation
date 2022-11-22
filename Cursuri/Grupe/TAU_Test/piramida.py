# x = 7
# for i in range(x):
# 		print(f"{i}"*i) # i + i -> ii
# 										# i + i + i -> iii
# 										# i + i + i + i -> iiii
randuri = int(input('Introdu un numar de randuri: '))
for x in range(randuri):
    for y in range(x+1): # capatul de de interval nu se in considerare (x + 1 pentru x = 2 => valorile de iteratie 1,2)
        print(x+1,end='')
    print()
"""
x = 0
	y = 1 (valori de iteratie: 0)
	print(x+1,end='') -> 1
x = 1
	y = 2 (valori de iteratie: 0,1)
	print(x+1,end='') -> 22
x = 2
	y = 3 (valori de iteratie: 0,1,2)
	print(x+1,end='') -> 333
x = 3
	y = 4 (valori de iteratie: 0,1,2,3)
	print(x+1,end='') -> 4444
x = 4
	y = 5 (valori de iteratie: 0,1,2,3,4)
	print(x+1,end='') -> 55555
x = 5
	y = 4 (valori de iteratie: 0,1,2,3,4,5)
	print(x+1,end='') -> 666666
x = 6
	y = 7 (valori de iteratie: 0,1,2,3,4,5,6)
	print(x+1,end='') -> 7777777
"""