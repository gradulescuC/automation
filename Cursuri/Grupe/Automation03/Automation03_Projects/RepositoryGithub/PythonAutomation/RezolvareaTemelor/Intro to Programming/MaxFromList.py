# Fara nested functions
def maxList():
    list = []
    element = int(input("Enter number of list elements: "))
    for i in range(1, element + 1):
        elem = int(input(f"Enter element {i}: "))
        list.append(elem)
    print("The list is: ", list)
    maxNum = list[0]
    for i in list:
        if maxNum < i:
            maxNum = i
    print(f"The biggest number is: {maxNum}")

maxList()

print("--------------------------------")

# Cu nested functions

def inputList():
    list = []
    element = int(input("Enter number of list elements: "))
    for i in range(1, element + 1):
        elem = int(input(f"Enter element {i}: "))
        list.append(elem)
    print(f"The list is: {list}")
    def maxList():
        maxNum = list[0]
        for i in list:
            if maxNum < i:
                maxNum = i
        print(f"The biggest number is: {maxNum}")
        return maxNum
    return maxList()

inputList()

