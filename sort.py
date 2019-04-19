# sort.py
# Sorting algorithms

from random import randint

# Checks if a list is sorted
def isSorted(list):
    for i in range(1, len(list)):
        if(list[i - 1] > list[i]):
            return False
    return True
# End of isSorted function

# Bubble sort
def bubble(inputList):
    sortList = list(inputList)
    while not isSorted(sortList):
        for j in range(len(sortList) - 1):
            if sortList[j] > sortList[j + 1]:
                swap = sortList[j + 1]
                sortList[j + 1] = sortList[j]
                sortList[j] = swap
    return sortList
# End of bubble function

# Selection sort
def selection(inputList):
    sortList = list(inputList)
    for i in range (len(sortList) - 1):
        smallest = i
        for j in range (i + 1, len(sortList)):
            if sortList[smallest] > sortList[j]:
                smallest = j
        swap = sortList[smallest]
        sortList[smallest] = sortList[i]
        sortList[i] = swap
    return sortList
# End of selection function

# Bogosort
def bogo(inputList):
    sortList = list(inputList)
    while not isSorted(sortList):
        rand1 = randint(0, len(sortList) - 1)
        rand2 = randint(0, len(sortList) - 1)
        swap = sortList[rand1]
        sortList[rand1] = sortList[rand2]
        sortList[rand2] = swap
    return sortList
# End of bogo function
