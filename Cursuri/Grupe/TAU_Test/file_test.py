"""todo sortati lista 2 dupa penultimul element (ultima litera din fiecare string)
            expected result = [mac, ipad, apple, iphone]"""

lista_2 = ["apple", "mac", "iphone", "ipad", "apple"]

sorted_list = sorted(lista_2)[::-1]
print(sorted_list)