grocery_list =[]
dict_grocery = {}

while True:
 item = input().upper()
 if item not in grocery_list:
      grocery_list.append(item)