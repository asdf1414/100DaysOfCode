################################################################################
# Suppose an array sorted in ascending order is rotated at some pivot unknown 
# to you beforehand. Find the minimum element in O(log N) time. You may 
# assume the array does not contain duplicates. For example, 
# given [5, 7, 10, 3, 4], return 3.
################################################################################

def search_pivot(lst):
    # return element if list has only one element
    if len(lst) == 1:
        return lst[0]
    # initial mid, start definement
    start = 0
    end = len(lst) - 1

    while True:
        # define middle element of current list part
        mid = int(start + (end - start) / 2)

        # check if current mid-num is smaller than start or bigger
        # than end neighbour
        # if true: return current mid or mid+1 (found smallest)
        if lst[mid] < lst[mid - 1]:
            return lst[mid]
        if lst[mid] > lst[mid + 1]:
            return lst[mid + 1]

        # main algorithm logic. This comparsion checks if it should 
        # search in the start or end half of the list
        if lst[mid] > lst[0]:
            start = mid + 1
        else:
            end = mid - 1

# Driver code
lst = [6,7,8,9,10,4]
print(search_pivot(lst))