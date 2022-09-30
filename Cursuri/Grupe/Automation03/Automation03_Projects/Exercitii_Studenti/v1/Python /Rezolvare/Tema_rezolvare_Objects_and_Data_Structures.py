#!/usr/bin/env python
# coding: utf-8

# ## Temă

# Scrieți o scurtă descriere/definiție pentru următoarele noțiuni:

# Double Click aici pentru a scrie răspunsurile:
# 
# (Numere)Numbers: Variabilele numerice sunt de 2 tipuri: integer (int) care reprezinta numere intregi pozitive sau negative si float care reprezinta numere pozitive sau negative cu una sau mai multe zecimale.
# 
# (Șiruri)Strings: Sirurile reprezinta orice tip de text care este inclus intre ghilimele simple, ' ', duble, " ", sau triple, ''' ''', """ """. Ghilimelele triple se folosesc pentru a reprezenta sirurile de caractere pe mai multe linii.
# 
# (Liste)Lists: Listele reprezinta o insiruire de elemente despartite prin virgula, ",", in interiorul unor paranteze patrate, "[]". Elementele dintr-o lista sunt ordonate, se pot schimba, sunt indexate si pot fi duplicate. 
# 
# Tuples: Tuples reprezinta o insiruire de elemente despartite prin virgula, ",", in interiorul unor paranteze rotunde, "()". Elementele dintr-un tuple au o ordine definita care nu poate fi schimbata, NU se pot schimba (introduce sau sterge elemente), sunt indexate si pot fi duplicate.
# 
# (Dicționare)Dictionaries: Dictionarele reprezinta o insiruire de elemente compuse din pereche "cheie:valoare" separate prin virgula, ",", in interiorul unor acolade, "{}". Elementele dintr-un dictionar sunt ordonate, se pot schimba, sunt indexate prin "cheie" si nu pot fi duplicate, "keys" sunt unice. Elementele unui dictionar pot fi de orice tip (string, int, float, boolean and tipuri de liste)

# ## Numere
# Scrieți o ecuație în care să folosiți înmulțirea, împărțirea, ridicarea la putere, adunarea și scăderea care să fie egală cu 100.25.

# In[17]:


6 * 8 + 24 / 6 + 3 ** 4 - 32.75


# Răspundeți la următoarele 3 întrebări fără a scrie cod. Scrieți apoi codul corespunzător pentru a vă verifica răspunsul.
# 
#     Care este valoarea expresiei 4 * (6 + 5) 
#     
#     Care este valoarea expresiei 4 * 6 + 5 
#     
#     Care este valoarea expresiei 4 + 6 * 5 

# In[ ]:


44


# In[ ]:


29


# In[ ]:


34


# Care este *tipul* (*type*) rezultatului expresiei 3 + 1.5 + 4?<br><br>

# In[ ]:


float


# Ce folosiți pentru a găsi radicalul și pătratul unui număr? Dați exemple.

# In[1]:


# Square root: folosim metoda sqrt(parametru) dupa ce am importat-o initial. Ex: print(sqrt(36)) = 6


# In[2]:


# Square:
1. Putem inmulti numarul cu el insusi: 6 * 6
2. Putem folosi metoda pow(parametru, exponent): print(pow(6, 2))
3. Putem folosi operatorul "**" care ridica valoarea la puterea a doua: 6 ** 2


# ## Strings

# Având string-ul 'hello' folosiți o comandă care returnează litera 'e' (folosind indexul).

# In[1]:


print(("hello")[1])


# Faceți reverse la string-ul 'hello' folosind slicing:

# In[2]:


print(("hello")[::-1])


# Având string-ul 'hello' oferiți două metode pentru a produce litera 'o' folosind index-ul (indexing).

# In[3]:


# Method 1:
print(('hello')[4])


# In[4]:


# Method 2:
print(('hello')[-1])


# ## Liste

# Construiți lista [0,0,0] în două moduri diferite.

# In[7]:


# Method 1:
list1 = [0, 0, 0]
print(list1)


# In[8]:


# Method 2:
list2 = []
list2.extend([0, 0, 0])
print(list2)

# sau

list3 = list4 = list5 = [0]
print(list3 + list4 + list5)


# În lista de mai jos înlocuiți 'hello' cu 'goodbye':

# In[17]:


list3 = [1,2,[3,4,'hello']]


# In[18]:


list3[2][2] = 'goodbye'


# In[19]:


print(list3)


# Sortați lista de mai jos:

# In[25]:


list4 = [5,3,4,6,1]


# In[22]:


# Method 1:
list4.sort()
print(list4)


# In[26]:


# Method 2:
print(sorted(list4))


# ## Dicționare

# Folosind keys și indexing, extrageți 'hello' din următoarele dicționare: 

# In[9]:


d = {'simple_key':'hello'}
# Grab 'hello'
print(d['simple_key'])


# In[6]:


d = {'k1':{'k2':'hello'}}
# Grab 'hello'
print(d['k1']['k2'])


# In[10]:


# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
#Grab hello
print(d['k1'][0]['nest_key'][1][0])


# In[11]:


# This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
#Grab hello
print(d['k1'][2]['k2'][1]['tough'][2][0])


# Putem sorta un dicționar? De ce sau de ce nu?
# Dictionarele nu le putem sorta, nu exista o metoda de sortare specifica dictionarelor.
# Ceea ce putem face, este sa sortam elementele unui dictionar dupa items, keys sau values intr-o lista pe care apoi o putem transforma intr-un dictionar.
# 
# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 5}
# s = sorted(d.items())
# print(dict(s))

# ## Tuples

# Care este diferența majoră dintre tuples și liste?<br><br>
# Diferenta dintre liste si tuples este ca listele sunt mutabile iar tuples sunt imutabile.

# Cum creați un tuple? Dați exemplu.

# In[20]:


tup = (4, 'text', 7, 8.45, 4, True)
print(tup)
print(type(tup))


# ## Mulțimi 

# Ce este unic pentru o mulțime?<br><br>
# Multimea reprezinta o colectie neordonata de elemente unice, care nu permit duplicate.

# Folosiți set pentru a găsi valorile unice pentru lista de mai jos:

# In[13]:


list5 = [1,2,2,33,4,4,11,22,3,3,2]


# In[14]:


print(set(list5))


# ## Booleans

# Pentru următorul quiz, avem un preview al operatorilor de comparație. În tabelul de mai jos a=3 și b=4. 
# 
# <table class="table table-bordered">
# <tr>
# <th style="width:10%">Operator</th><th style="width:45%">Description</th><th>Example</th>
# </tr>
# <tr>
# <td>==</td>
# <td>If the values of two operands are equal, then the condition becomes true.</td>
# <td> (a == b) is not true.</td>
# </tr>
# <tr>
# <td>!=</td>
# <td>If values of two operands are not equal, then condition becomes true.</td>
# <td> (a != b) is true.</td>
# </tr>
# <tr>
# <td>&gt;</td>
# <td>If the value of left operand is greater than the value of right operand, then condition becomes true.</td>
# <td> (a &gt; b) is not true.</td>
# </tr>
# <tr>
# <td>&lt;</td>
# <td>If the value of left operand is less than the value of right operand, then condition becomes true.</td>
# <td> (a &lt; b) is true.</td>
# </tr>
# <tr>
# <td>&gt;=</td>
# <td>If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.</td>
# <td> (a &gt;= b) is not true. </td>
# </tr>
# <tr>
# <td>&lt;=</td>
# <td>If the value of left operand is less than or equal to the value of right operand, then condition becomes true.</td>
# <td> (a &lt;= b) is true. </td>
# </tr>
# </table>

# Care va fi rezultatul Boolean pentru următoarele linii de cod? Răspundeți mai întâi și apoi verificați.

# In[15]:


# Answer before running cell
2 > 3
False


# In[16]:


# Answer before running cell
3 <= 2
False


# In[17]:


# Answer before running cell
3 == 2.0
False


# In[18]:


# Answer before running cell
3.0 == 3
True


# In[19]:


# Answer before running cell
4**0.5 != 2
False


# Ultima întrebare: Care este rezultatul boolean pentru următoarea celulă de cod? 

# In[20]:


# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
l_one[2][0] >= l_two[2]['k1']

False


# ## Great Job ! :) 

# In[ ]:




