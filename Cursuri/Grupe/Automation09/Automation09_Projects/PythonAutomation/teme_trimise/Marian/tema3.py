'''Exerciții obligatorii - grad de dificultate: Usor spre Mediu
Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
X este un int.'''

# x = int(input('Numarul ales este: '))

'''1. Declară o listă note_muzicale în care să pui do re mi etc până la do
Afișeaz-o:'''
note_muzicale = ['do','re', 'mi', 'fa', 'so', 'la', 'si', 'do']
print(note_muzicale)

'''● Inversează ordinea folosind slicing și suprascrie această listă.'''
note_muzicale = note_muzicale[::-1]

'''● Printează varianta actuală (inversată).'''
print(note_muzicale)

'''● Pe această listă aplică o metodă care bănuiești că face același lucru,
adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
deoarece metoda face asta automat.'''
note_muzicale.reverse()

'''● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta
inițială.'''
print(note_muzicale)

'''Concluzii: slicing e temporar, dacă vrei să păstrezi noua variantă va trebui să
suprascrii lista sau să o salvezi într-o listă nouă. Metoda găsită de tine face
suprascrierea automat și permanentizează aceste modificări. Ambele variante
își găsesc utilitatea în funcție de ce ne dorim în acel moment.'''

'''2. De câte ori apare ‘do’?'''
nota_do = note_muzicale.count('do')
print(f'Nota do apare de {nota_do} ori in note muzicale')

'''3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
Găseste 2 variante să le unești într-o singură listă.'''
lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]
print(lista1 + lista2)

for i in lista2 :
    lista1.append(i)

# alta varianta ar fi lista1.extend(lista2)

'''4.
● Sortează și afișază lista generată la exercițiul anterior.'''
print(lista1)

# '''● Sortează numărul 0 folosind o funcție.''' -> Aici a fost o greseala, trebuia sa scrie sa fie eliminat nr 0
lista1.sort()

'''● Afișaza iar lista.'''
print(lista1)

'''5. Folosind un if verifică lista generată la exercițiul 3 și afișază:'''
'''● Lista este goală.'''
if lista1 == []:
    print('Lista este goala')

'''● Lista nu este goală.'''
if lista1 == [0, 1, 2, 3, 4, 5, 6]:
    print('Lista nu este goala')

# Aici hardcodezi valoarea listei si nu prea e ok.
# O varianta mai eficienta care sa se aplice pe orice lista ar fi una care sa porneasca de la prima varianta a ta:

if lista1 == []:
    print('Lista este goala')
else:
    print('Lista nu este goala')

'''6. Folosește o funcție care să șteargă lista de la exercițiul 3.'''
del lista1[0::]


# Alta varianta ar fi lista1.clear()
print(lista1)

'''7. Copy paste la exercițiul 5. Verifică încă o dată.
Acum ar trebui să se afișeze că lista e goală.'''
if lista1 == []:
    print('Lista este goala')
if lista1 == [0, 1, 2, 3, 4, 5, 6]:
    print('Lista nu este goala')

'''8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
Folosește o funcție că să afișezi Elevii (cheile)'''
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}

print(dict1.keys())

'''9. Printează cei 3 elevi și notele lor
Ex: ‘Ana a luat nota {x}’
Doar nota o vei lua folosindu-te de cheie'''

'''varianta 1'''
print('Ana a luat nota: ' + str(dict1['Ana']))
print('Gigel a luat nota: ' + str(dict1['Gigel']))
print('Dorel a luat nota: ' + str(dict1['Dorel']))

'''varianta 2'''
for key, value in dict1.items():
     print('{} a luat nota  : {}'.format(key, value))

'''10. Dorel a făcut contestație și a primit 6'''

'''● Modifică nota lui Dorel în 6'''
dict1.update({'Dorel' : 6})

'''● Printează nota după modificare'''
print('Dupa contestatie Dorel a luat nota: ' + str(dict1['Dorel']))

'''11. Gigel se transferă din clasă'''
'''● Căuta o funcție care să îl șteargă'''
dict1.pop('Gigel')
print(f'Elevi ramasi: {dict1}')

'''● Vine un coleg nou. Adaugă Ionică, cu nota 9'''
dict1['Ionica'] = 9


'''● Printează noii elevi'''
print(f'Elevi dupa modificari {dict1}')

'''12.
Set'''
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}

'''● Adaugă în zilele_sapt ‘luni’'''
before = zile_sapt
zile_sapt.add('luni')
after = zile_sapt

'''● Afișeaza zile_sapt'''
print(before, after)

if before == after:
    print('Ai adaugat un duplicat')

'''13.Folosește un if și verifică dacă:'''
'''● Weekend este un subset al zilelor din săptămânii.'''
'''● Weekend nu este un subset al zilelor din săptămânii.'''
if weekend.issubset(zile_sapt):
    print('Weekend este un subset al zilelor din săptămânii')

else:
    print('Weekend nu este un subset al zilelor din săptămânii')

'''14. Afișează diferențele dintre aceste 2 seturi.'''
diferente = zile_sapt.difference(weekend)
if diferente == zile_sapt.difference(weekend):
    print(diferente)

'''15. Afișază intersecția elementelor din aceste 2 seturi.'''
intersectie = zile_sapt.intersection(weekend)
if intersectie == zile_sapt.intersection(weekend):
    print(intersectie)

'''Exerciții Opționale - grad de dificultate: Mediu spre greu(may need google) .'''

'''1. Ne imaginăm o echipă de fotbal pt teren sintetic.
3 Schimbări maxime admise:'''
'''● Declară o Listă cu 5 jucători'''
'''● Schimbari_efectuate = te joci tu cu valori diferite'''
'''● Schimbari_max = 3
Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
- Efectuează schimbarea'''
lista_jucatori = ['Ronaldo','Messi', 'Ibrahimovic','Di Maria', 'Buffon']
print(f'Jucatori in teren: {lista_jucatori}')
schimbari_max = 3
schimbariMaximAdmise = 3
schimbari_efectuate = 0
if (schimbari_efectuate < 0 or schimbari_efectuate >= schimbari_max):
    schimbariMaximAdmise -= 1
    schimbari_efectuate = schimbariMaximAdmise
    print('Nu sunt schimbari disponibile')
else:
    print('Jucatorul scos este:')
    iesire = input()
    print('Jucatorul introdus este:')
    intrare = input()
    if ('Ronaldo'in iesire or 'Messi' in iesire or 'Ibrahimovic' in iesire or 'Di Maria' in iesire or 'Buffon' in iesire):
        schimbariMaximAdmise -= 1
        schimbari_efectuate = schimbariMaximAdmise
        lista_jucatori.remove(iesire)
        lista_jucatori.append(intrare)
        print(f'A intrat {intrare} a ieșit {iesire} mai ai {schimbari_efectuate} schimbări')
        print(f'Noua lista de jucatori: {lista_jucatori}')
    else:
        schimbariMaximAdmise -= 1
        schimbari_efectuate = schimbariMaximAdmise
        print(f'Nu se poate efectua schimbarea deoarece jucătorul {iesire} nu e în teren')
        print(f'Mai ai {schimbari_efectuate} schimbari')