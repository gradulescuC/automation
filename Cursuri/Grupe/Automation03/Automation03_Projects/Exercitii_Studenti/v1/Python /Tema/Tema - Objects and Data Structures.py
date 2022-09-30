#!/usr/bin/env python
# coding: utf-8

# ## Temă

# Scrieți o scurtă descriere/definiție pentru următoarele noțiuni:

# Double Click aici pentru a scrie răspunsurile:
# 
# (Numere)Numbers: 
# 
# (Șiruri)Strings:
# 
# (Liste)Lists:
# 
# Tuples:
# 
# (Dicționare)Dictionaries:
# 

# ## Numere
# Scrieți o ecuație în care să folosiți înmulțirea, împărțirea, ridicarea la putere, adunarea și scăderea care să fie egală cu 100.25.

# In[2]:





# Răspundeți la următoarele 3 întrebări fără a scrie cod. Scrieți apoi codul corespunzător pentru a vă verifica răspunsul.
# 
#     Care este valoarea expresiei 4 * (6 + 5) 
#     
#     Care este valoarea expresiei 4 * 6 + 5 
#     
#     Care este valoarea expresiei 4 + 6 * 5 

# In[ ]:





# In[ ]:





# In[ ]:





# Care este *tipul* (*type*) rezultatului expresiei 3 + 1.5 + 4?<br><br>

# In[ ]:





# Ce folosiți pentru a găsi radicalul și pătratul unui număr? Dați exemple.

# In[1]:


# Square root:


# In[2]:


# Square:


# ## Strings

# Având string-ul 'hello' folosiți o comandă care returnează litera 'e' (folosind indexul).

# In[ ]:





# Faceți reverse la string-ul 'hello' folosind slicing:

# In[ ]:





# Având string-ul 'hello' oferiți două metode pentru a produce litera 'o' folosind index-ul (indexing).

# In[4]:


# Method 1:


# In[5]:


# Method 2:


# ## Liste

# Construiți lista [0,0,0] în două moduri diferite.

# In[6]:


# Method 1:


# In[7]:


# Method 2:


# În lista de mai jos înlocuiți 'hello' cu 'goodbye':

# In[8]:


list3 = [1,2,[3,4,'hello']]


# In[ ]:





# In[ ]:





# Sortați lista de mai jos:

# In[20]:


list4 = [5,3,4,6,1]


# In[9]:


# Method 1:


# In[10]:


# Method 2:


# ## Dicționare

# Folosind keys și indexing, extrageți 'hello' din următoarele dicționare: 

# In[11]:


d = {'simple_key':'hello'}
# Grab 'hello'


# In[12]:


d = {'k1':{'k2':'hello'}}
# Grab 'hello'


# In[13]:


# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
#Grab hello


# In[14]:


# This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
#Grab hello


# Putem sorta un dicționar? De ce sau de ce nu?
# 
# 

# ## Tuples

# Care este diferența majoră dintre tuples și liste?<br><br>
# 

# Cum creați un tuple? Dați exemplu.

# In[ ]:





# ## Mulțimi 

# Ce este unic pentru o mulțime?<br><br>
# 

# Folosiți set pentru a găsi valorile unice pentru lista de mai jos:

# In[38]:


list5 = [1,2,2,33,4,4,11,22,3,3,2]


# In[ ]:





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


# In[16]:


# Answer before running cell
3 <= 2


# In[17]:


# Answer before running cell
3 == 2.0


# In[18]:


# Answer before running cell
3.0 == 3


# In[19]:


# Answer before running cell
4**0.5 != 2


# Ultima întrebare: Care este rezultatul boolean pentru următoarea celulă de cod? 

# In[20]:


# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
l_one[2][0] >= l_two[2]['k1']


# ## Great Job ! :) 

# In[ ]:




