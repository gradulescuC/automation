def highest_even(my_list):
    n = 0
    for i in my_list:
        if i%2 == 0 and i > n:
            n = i
    return n

print(highest_even([13,9,23,11,66,3,22,10]))
