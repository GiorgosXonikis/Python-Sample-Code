
# 4.Find Certain Numbers
# Write a function find_numbers(min, max) that will find all numbers that
# are a multiple of 7 but not a multiple of 5.
# First, try getting it right with an explicit for loop. If you have it up
# and running, write a second version that avoids explicit for loops and
# uses filter and lambda only!


def find_numbers(min , max):
    # store the range of the given numbers
    numbers = list(range(min, max + 1))

    # double filter the array
    output_list = list(filter(lambda x: x % 7 == 0, filter(lambda x: x % 5 == 0, numbers)))

    return output_list


print(find_numbers(5, 700))
