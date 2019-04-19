# sort.py
# Sorting algorithms

# Checks if a list is sorted
def isSorted(list):
    for i in range(1, len(list)):
        if(list[i - 1] > list[i]):
            return False
    return True
# End of isSorted function

# Bubble sort
def bubble(list):
    while not isSorted(list):
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                swap = list[j + 1]
                list[j + 1] = list[j]
                list[j] = swap
    return list
# End of bubble function

# Selection sort
def selection(list):
    for i in range (len(list) - 1):
        smallest = i
        for j in range (i + 1, len(list)):
            if list[smallest] > list[j]:
                smallest = j
        swap = list[smallest]
        list[smallest] = list[i]
        list[i] = swap
    return list
# End of selection function
