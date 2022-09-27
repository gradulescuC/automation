"""
exceptie = o eroare in Python, care apare atunci cand Python nu poate sa execute codul
            si opreste executia tuturor instructiunilor care urmeaza
# se poate trata / aborda cu ceea ce se numese try -  except
try = incearca sa executi o bucata de cod
except = in cazul in care bucata de cod returneaza eroare, vreau sa mi se execute o alta linie de cod
            care sa permita executarea restului de teste
Exista o serie de exceptii care sunt predefinite cum ar fi IndexError, ZeroDivisionError, IndentationError
In cazul in care nu stim la ce sa ne asteptam, putem sa folosim exceptia generala Exception
\n = escape character care inseamna new line
        in general atunci cand vrem sa schimbam semnificatia unui caracter
                ne putem folosi de caracterul escape "\"
        ex: \n inseamna new line
            \" inseamna afisarea unei ghilimele pe ecran, in loc de interpretarea ei ca inceput sau sfarsit de string
Mai multe exemple de exceptii: https://docs.python.org/3/library/exceptions.html
"""

# number = 0
# number2 = 10/number
#
# print("Impartirea la 0 nu este posibila")


try: #in try punem codul despre care presupunem ca ar putea genera o exceptie
    number = 0
    number2 = 10/number
except Exception as e: #in except tratam orice exceptie (salvam mesajul ei in variabila e)
    print("Test impartirea la 0: Impartirea la 0 nu este posibila")

try:
    varsta = 30
    print("Varsta ta este de 30 de ani")
except Exception as e:
    print("Ceva nu a mers bine, te rog sa verifici")

try: # in try punem codul 'periculos'
    lista = [1, 2, 3]
    lista[6]
except IndexError as e: #tratam IndexError exception
    print("Test accesare elemente lista: List out of bound exception")
    print(f"Eroarea primita a fost: {e}")
    print(f"Eroarea primita a fost: \n {e}")