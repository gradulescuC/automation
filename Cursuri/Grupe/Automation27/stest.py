def player1():
    p1 = input("Jucatorul 1 alege randul si coloana: ")
    rand = int(p1[0]) - 1
    coloana = int(p1[1]) - 1
    i = 0
    j = 0
    for i in range(3):
        if i == rand:
            for j in range(3):
                if j == coloana:
                    tabla[i][j] = "X"
    print(*tabla, sep="\n")
def player2():
    p1 = input("Jucatorul 2 alege randul si coloana: ")
    rand = int(p1[0]) - 1
    coloana = int(p1[1]) - 1
    i = 0
    j = 0
    for i in range(3):
        if i == rand:
            for j in range(3):
                if j == coloana:
                    tabla[i][j] = "0"
    print(*tabla, sep="\n")

def check():
    win = False
    if tabla[0][0] == tabla[0][1] == tabla[0][2] or tabla[1][0] == tabla[1][1] == tabla[1][2] or tabla[2][0] == \
            tabla[2][1] == tabla[2][2]:
        win = True
    if tabla[0][0] == tabla[1][0] == tabla[2][0] or tabla[0][1] == tabla[1][1] == tabla[2][1] or tabla[0][2] == \
            tabla[1][2] == tabla[2][2]:
        win = True
    if tabla[0][0] == tabla[1][1] == tabla[2][2] or tabla[0][2] == tabla[1][1] == tabla[2][0]:
        win = True
    return win

tabla = [["R1c1", "R1c2", "R1c3 "], ["R2c1", "R2c2", "R2c3"], ["R3c1", "R3c2", "R3c3"]]
print(*tabla, sep = "\n")
i=1
while i<=4:
    win = False
    player1()
    check()
    if check():
        print("Player 1 (X)  WINS !!!")
        break
    player2()
    check()
    if check():
        print("Player 2 (0)  WINS !!!")
        break
    i+=1
if check()==False:
    print("Jocul s-a incheiat la egalitate")