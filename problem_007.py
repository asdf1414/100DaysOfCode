# problem: https://mailchi.mp/bcd73dca2f47/problem-6?e=6de8a670d8
# this solution should have a time complexity of O(n^2)

import random

def count_intersections(lst1, lst2):
    # initialize variables
    intersections = 0
    # create list-pairs [[p1,q1], [p2,q2], ..., [pn,qn]]
    pairs = [[lst1[idx], lst2[idx]] for idx in range(0, len(lst1))]

    for pair_1 in pairs:
        for pair_2 in pairs:
            if pair_2[0] > pair_1[0] and pair_2[1] < pair_1[1] or \
               pair_2[0] < pair_1[0] and pair_2[1] > pair_1[1]:
                # print("intersection: " + str(pair_1) + " " +  str(pair_2) + "\n")
                intersections += 1
            else: pass

    return int(intersections / 2)

# generates random lists for testing
lst1 = [random.randrange(0,100) for i in range(0,100)]
lst2 = [random.randrange(0,100) for i in range(0,100)]

print(count_intersections(lst1, lst2))