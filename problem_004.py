################################################################################
# There are N couples sitting in a row of length 2 * N. They are currently 
# ordered randomly, but would like to rearrange themselves so that each 
# couple's partners can sit side by side.
################################################################################

import random

# style 1: one list for all persons, sort inside the list itself
def sort_couples_1(n):
    # initialize counter variables
    first = 0
    swaps = 0
    # declare neighbour indices relative to first
    neighbour_l = first - 1
    neighbour_r = first + 1
    # generate couples list and randomize it
    couples = 2 * list(range(1, n+1))
    random.shuffle(couples)

    while True:
        # break loop if first is >= length-2 of couples list
        if first >= len(couples) - 2: break
        # search for the partner (same variable)
        partner = couples.index(couples[first])

        # if the left or right neighbour is already the partner
        # move onto the next person and redo loop
        if couples[neighbour_r] == couples[first]: first += 2
        elif couples[neighbour_l] == couples[first]: first += 1

        else:
            # if no neighbour is the partner, switch the the current number with
            # the spot from the required partner
            couples[neighbour_r] = couples[partner]
            first = partner
            couples[partner] = couples[neighbour_r]
            swaps += 1

    return swaps



# style 2: one reference list and one list that needs to be 
# sorted according to the reference list
def sort_couples_2(n):
    # generate reference list, assign ref_list to 
    # sort_list and randomize it
    ref_list = [i for i in range(1, n+1)]
    sort_list = ref_list[:]
    random.shuffle(sort_list)

    # initialize counter variables
    swaps = 0
    first = 0

    while True:
        # break loop if first is >= length-1 of ref_list
        if first >= len(ref_list) - 1: break
        # check if the current number in sort_list already located at 
        # the same index as in the ref_list
        elif sort_list[first] == ref_list[first]:
            first += 1

        # if the current number is not at the right index, switch
        # with the required number for the current index
        else:
            # search for the number that needs to be switched
            to_switch = sort_list.index(ref_list[first])
            # save the index from this number
            saved_val = sort_list[first]

            # switch both numbers
            sort_list[first] = sort_list[to_switch]
            sort_list[to_switch] = saved_val
            # increment counter variables
            first += 1; swaps += 1
    
    return swaps

    
# n = amount of couples
print(sort_couples_1(10))
print(sort_couples_2(10))