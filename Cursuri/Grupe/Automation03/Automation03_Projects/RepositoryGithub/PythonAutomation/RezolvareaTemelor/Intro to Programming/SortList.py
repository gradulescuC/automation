def inputList():
    list = []
    element = int(input("Enter number of list elements: "))
    for i in range(1, element + 1):
        elem = int(input(f"Enter element {i}: "))
        list.append(elem)
    print(f"The list is: {list}")
    def orderList():
        for i in range(len(list)):
            for j in range(i + 1, len(list)):
                if list[i] > list[j]:
                    minimum = list[i]
                    list[i] = list[j]
                    list[j] = minimum
        print(f"The ordered list is: {list}")
    return orderList()

inputList()