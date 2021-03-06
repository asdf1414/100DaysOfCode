################################################################################
# Given a string with repeated characters, rearrange the string so that no 
# two adjacent characters are the same. If this is not possible, return None. 
# For example, given "aaabbc", you could return "ababac". Given "aaab", 
# return None.
################################################################################

import string, random, time, xlsxwriter


def search_duplicates(lst):
    # declare variables
    dupl = []
    index = 0
    neighbour = 1
    count = 0
    do_check = True

    # returns None if one character appears more than
    # half of the length of the list
    if initial_check(lst) and do_check:
        return None
    else:
        do_check = False

    while True:
        # break if index exceeds length of list
        if index >= len(input_list) - 1: break
        # check if next char in list is the same
        elif lst[index] == lst[neighbour]:
            # if true: remove char from list and move it to list,
            # that stores duplicates then repeat for next char
            dupl.append(lst[neighbour])
            del lst[neighbour]
            count += 1
        else:
            # else: go to next char and repeat
            count = 0; index += 1; neighbour += 1
    
    # return finished main list if duplicate list is empty
    if not dupl: 
        return lst
    # if all duplicates in the dupl list are the same, this algorithm
    # will stop and pass the dupl and main list to search_empty_slot
    if all(dupl):
        return (search_empty_slots(dupl, lst))
    # elif the last item in the duplicate list is the same as the
    # first in the main list
    elif dupl[-1] != lst[0]:
        # if true: add duplicate list in front of main list
        lst = dupl + lst
    else:
        # else: add duplicate list behind main list
        lst += dupl
    
    # recurse function with the new main list
    return(search_duplicates(lst))


# this algorithm uses nested loops, therefore It only gets used if nescessary
def search_empty_slots(dupl, lst):
    # init index
    index = 0
    for char in dupl:
        while True:
            # if the first duplicate from the dupl list is not the same as the
            # left or right neighbour, insert it at the given index
            if dupl[0] != lst[index] and dupl[0] != lst[index - 1]:
                lst.insert(index, dupl[0])
                dupl.pop()
                break
            else:
                # else: move onto the next index and redo loop
                index += 1

    return lst

# this small algorithm checks if there is a character more than 
# len(list)/2 times in the main list. If this is the case, the list
# can't be arranged and it returns True
def initial_check(lst):
    # generate string with all characters in the ascii alphabet
    alphabet = string.ascii_lowercase
    for char in alphabet:
        # count how many times each character is in the main list
        indices = [i for i, x in enumerate(lst) if x == char]
        # return True if a character is more than len(list) / 2 in the main list
        if len(indices) > len(lst) / 2:
            return True

# this is a debug function. It's used to check if the output list
# is correct and not two same characters are adjacent
def check_assignments(output):
    # init variables
    check_num = 0
    error = False
    for i in output:
        # break if check_num exceeded length of output list
        if check_num == len(output) - 1: break
        # print an error if two same characters are adjacent
        if i == output[check_num - 1] or \
        i == output[check_num + 1]:
            error = True
            print("set error to true at: " + str(check_num))
        # increment index checker
        check_num += 1
        
    if error:
        print("wrong list assignment found!")
    else:
        print("list correctly assigned")


# below here is just data collection for 
# the time analysis of this algorithm above
inc_list = []
dur_list = []
incrementor = 0

for i in range(0,500):
    incrementor += 1000
    input_list = []
    # generates a list of randomly placed characters from a-z
    # within the given range (e.g. 100'000)
    for i in range(0, incrementor):
        alphabet = string.ascii_lowercase
        rdm_index = random.randrange(0, 25)
        input_list.append(alphabet[rdm_index])

    start_time = time.time()
    output = search_duplicates(input_list)
    end_time = time.time()

    duration = end_time - start_time
    inc_list.append(incrementor)
    dur_list.append(duration)
    
xlsx_list = [inc_list, dur_list]

with xlsxwriter.Workbook('problem_005-time-analysis.xlsx') as workbook:
    worksheet = workbook.add_worksheet()

    for row_num, data in enumerate(xlsx_list):
        worksheet.write_row(row_num, 0, data)