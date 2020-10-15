def check(num_list, k):
    # create new list without numbers > k
    reduced_nums = [num for num in num_list if num <= k]

    # sort numbers ascending
    sorted_nums = sorted(reduced_nums)

    while True:
        # end function if list is empty
        if not sorted_nums: return False
        
        # take last number from list
        last = sorted_nums[-1]

        # search for remaining amount from (k - last) in list
        if (k - last) in sorted_nums:
            return True
        else:
            # remove last integer and redo loop
            sorted_nums = sorted_nums[:-1]


numbers_input = [10, 15, 3, 7]
k = 17

if (check(numbers_input, k)):
    print("match found!")