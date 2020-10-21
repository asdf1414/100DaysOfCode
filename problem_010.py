# problem: https://mailchi.mp/59f844f71f1c/problem-10?e=6de8a670d8
# approach: binary search since the list is sorted ascending

import random

def search_pivot(lst):
    # return if list has only one element
    if len(lst) == 1:
        return lst[0]
    # initial mid, start definement
    end = len(lst) - 1
    start = 0

    while True:
        # define middle element of current list part
        mid = int((start + (end - start)) / 2)

        # check if current mid is bigger than the right neighbour
        # if true: retunr current mid (found smallest)
        if lst[mid] > lst[mid + 1]:
            return lst[mid + 1]

        # check if current mind is smaller than left neighbour
        # if true: return current mid (found smallest)
        if lst[mid] < lst[mid - 1]:
            return lst[mid]
        
        # main algorithm logic. This comparsion checks if it should 
        # search in the left or right half of the list
        if lst[mid] > lst[0]:
            start = mid + 1
        else:
            end = mid - 1

    return lst[mid]


# Driver code
lst = [5,7,10,3,4]

print(search_pivot(lst))