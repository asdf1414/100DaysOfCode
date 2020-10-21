################################################################################
# Suppose you are given two lists of n points, one list p1, p2, ..., pn on 
# the line y = 0 and the other list q1, q2, ..., qn on the line y = 1. 
# Imagine a set of n line segments connecting each point pi to qi. 
# Write an algorithm to determine how many pairs of the line segments intersect.
################################################################################
# this solution should have a time complexity of O(n^2)

import random

def count_intersections(lst1, lst2):
    # initialize variables
    intersections = 0
    # create list-pairs [[p1,q1], [p2,q2], ..., [pn,qn]]
    pairs = [[lst1[idx], lst2[idx]] for idx in range(0, len(lst1))]

    # take a pair and iterate over whole list
    for pair_1 in pairs:
        for pair_2 in pairs:
            # check if the two pairs intersect
            if pair_2[0] > pair_1[0] and pair_2[1] < pair_1[1] or \
               pair_2[0] < pair_1[0] and pair_2[1] > pair_1[1]:
                intersections += 1
            else: pass

    return int(intersections / 2)

# generates random lists for testing
lst1 = [random.randrange(0,100) for i in range(0,1000)]
lst2 = [random.randrange(0,100) for i in range(0,1000)]

print(count_intersections(lst1, lst2))