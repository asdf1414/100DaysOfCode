################################################################################
# Given a collection of intervals, find the minimum number of intervals you 
# need to remove to make the rest of the intervals non-overlapping. Intervals 
# can "touch", such as [0, 1] and [1, 2], but they won't be considered 
# overlapping. For example, given the intervals (7, 9), (2, 4), (5, 8), 
# return 1 as the last interval can be removed and the first two won't overlap.
# The intervals are not necessarily sorted in any order.
################################################################################
# this algorithm has a time complexity of O(n)

def search_overlap(lst):
    # initialize variables
    overview = []
    amount_to_delete = 0
    # sort intervals
    lst = sorted(lst)
    
    # create overview list looking like this:
    # for each interval in the main list I generate a list [0,0].
    # The following for loop changes the first index to a 1 if the
    # left interval neighbour overlaps with the current interval
    # and the second index into a 1 if the right neighbour interval
    # overlaps with the current.
    for idx, interval in enumerate(lst):
        left = 0
        right = 0

        #if idx > 0 and interval[0] < lst[idx-1][1]:
        if idx > 0 and overview[idx-1][1] == 1:
            left = 1
        if idx < len(lst)-1 and interval[1] > lst[idx+1][0]:
            right = 1

        overview.append([left, right])
    
    # following for loop deletes all [1,1] pairs and sets 
    # the left neighbour to [x,0] and the right to [0,x]
    # at the end it increments the final counter.
    filter_idx = 0
    for val in overview:
        if val[0] + val[1] == 2:
            overview[filter_idx-1][1] = 0
            overview[filter_idx+1][0] = 0

            del lst[filter_idx]
            del overview[filter_idx]

            amount_to_delete += 1
        else:
            filter_idx += 1
    
    # following for loop now iterates over the list and checks
    # if the right neighbour has a 1 at the first index. if true:
    # delete the current interval and increases the final counter
    # else: move onto next interval and check again.
    filter_idx = 0
    for val in overview:
        if filter_idx < len(lst)-1 and overview[filter_idx+1][0] == 1:
            del lst[filter_idx]
            del overview[filter_idx]

            amount_to_delete += 1
        else:
            filter_idx += 1
    
    return amount_to_delete


intervals = [[1,5], [7,11], [10,13], [4,6], [13,15], [15,16]]
print("Min. intervals to remove: " + str(search_overlap(intervals)))